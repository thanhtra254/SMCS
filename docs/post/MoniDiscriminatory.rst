.. _post-moni-discriminatory:

=================================
Monitoring Report: Discriminatory
=================================

Đánh giá sự phân biệt được chia thành hai loại: Đánh giá trên toàn dữ liệu và đánh giá theo từng biến.

Đánh giá sự phân biệt trên toàn bộ dữ liệu
==========================================

Đánh giá sự phân biệt của từng biến
===================================

Sử dụng Macro
=============

Syntax
------

Cú pháp chạy macro để output ra báo cáo ổn định của mô hình như sau:

.. code:: sh

  %LET DATA_GB=
  %LET VARLIST=	
  %LET DEVDAY=
  PROC FORMAT;
    /* SCORE */
    VALUE SCOREF 
  RUN;
  %MONI_DCRM;

Trong đó:

- **DATA_GB** (data): Dữ liệu để kiểm định cần chứa tất cả các thông tin như sau:
  - Dữ liệu bao gồm thông tin train và outtime. Phân biệt bởi biến **YEARMONTH** có định dạng YYYYMM.
  - Dữ liệu phải chứa các biến trong **VARLIST** dưới dạng WOE_ và GRP_. Ví dụ **VARLIST=X1 X2** thì dữ liệu phải chứa **WOE_X1 WOE_X2 GRP_X1 GRP_X2**
  - **SCORE** là output từ mô hình.
  - Dữ liệu phải chứa biến **Good/Bad** ở dạng 0/1 là outcome của mô hình.

- **VARLIST (variable list)**: Các biến này sẽ được đưa vào báo cáo tính ổn định.
- **FORMAT (proc format)**: Các điểm cắt của SCORE được lưu dưới dạng PROC FORMAT.
- **DEVDAY(YYYYMM)**: thể hiện cách phân tách dữ liệu train và outtime. Macro hiểu rằng nếu YEARMONTH <= DEVDAY thì dữ liệu và Development, còn lại là out of time.

Detail
------

Kết quả
-------

Ví dụ
-----

**Ví dụ 1:** Chạy báo cáo monitoring discriminatory với dữ liệu DATA.GINI bao gồm cả train và out of time (các dữ liệu phải có biến Good Bad). Các biến thuộc mô hình *X1 X2 X3 X4 X5 X6 X7 X8 X9 10*.

.. code:: sh


  %LET DATA_GB= DATA.ALL;
  %LET VARLIST= X1 X2 X3 X4 X5 X6 X7 X8 X9 10;
  %LET DEVDAY=201703;

  PROC FORMAT;
    /* SCORE */
    VALUE SCOREF
      -9999997< - 0.022 = '.< - 0.022'
      0.022< - 0.028 = '0.022< - 0.028'
      0.028< - 0.035 = '0.028< - 0.035'
      0.035< - 0.043 = '0.035< - 0.043'
      0.043< - 0.051 = '0.043< - 0.051'
      0.051< - 0.06 = '0.051< - 0.06'
      0.06< - 0.071 = '0.06< - 0.071'
      0.071< - 0.086 = '0.071< - 0.086'
      0.086< - 0.102 = '0.086< - 0.102'
      0.102< - 0.122 = '0.102< - 0.122'
      0.122< - 0.143 = '0.122< - 0.143'
      0.143< - 0.178 = '0.143< - 0.178'
      0.178< - 0.251 = '0.178< - 0.251'
      0.251< - HIGH = '0.251< - HIGH';
  RUN;


  %MONI_DCRM;
