.. _post-data_transformation:

===================
Data Transformation
===================

WOE Tranformation
=================

Sau khi phân tích biến, ta có được kết quả binning của các biến. Kết quả này được trình này dưới dạng `PROC FORMAT <https://documentation.sas.com/?docsetId=proc&docsetTarget=p1upn25lbfo6mkn1wncu4dyh9q91.htm&docsetVersion=9.4&locale=en>`_. Kết quả ví dụ như sau:

.. code:: sh

  PROC FORMAT;
    /* X1 */
    VALUE X1F
      .='[01] X1 <= -0.628623236 OR MISSING' 
      LOW - -0.628623236 = '[01] X1 <= -0.628623236 OR MISSING' 
      -0.628623236< - -0.544671434 = '[02] -0.628623236 < X1 <= -0.544671434' 
      -0.544671434< - -0.280795118 = '[03] -0.544671434 < X1 <= -0.280795118' 
      -0.280795118< - HIGH = '[04] -0.280795118 < X1';
  RUN;
  
Các biến ban đầu sẽ được chuyển sang các giá trị WOE dựa trên các khoảng chia này. Để thực hiện việc biến đổi sang dạng WOE, ta dùng macro **DATA_ADD_WOE**.

Sử dụng Macro
=============

Macro **DATA_ADD_WOE** là công cụ transform các biến từ dạng ban đầu sang dạng WOE và lưu sang một dữ liệu mới. Cú pháp của macro như sau:

.. code:: sh

  %DATA_ADD_WOE(DATA=, VALIDATE=, TEST=, KEEP=,VARLIST=);
  
Trong đó:

-	DATA (data): Dữ liệu train. Các giá trị WOE của từng nhóm sẽ được tính dựa  trên dữ liệu  DATA. Macro đẩy ra hai dữ liệu liên quan:

  -	DATA_WOE (output) chứa các biến đã được chuyển sang dạng WoE từ dữ liệu DATA. Các biến được đổi tên bắt đầu bằng WOE_.
  -	DATA_GRP (output) chứa các biến đã được chuyển sang dạng group từ dữ liệu DATA. Các biến được đổi tên bắt đầu bằng GRP_.
  
-	VALIDATE (data): Dữ liệu validate. Macro sử dụng WOE được tính từ DATA để transform các biến. Macro đẩy ra hai dữ liệu mới:
  -	VALIDATE _WOE (output) chứa các biến đã được chuyển sang dạng WoE từ dữ liệu VALIDATE. Các biến được đổi tên bắt đầu bằng WOE_.
  -	VALIDATE _GRP (output) chứa các biến đã được chuyển sang dạng group từ dữ liệu VALIDATE. Các biến được đổi tên bắt đầu bằng GRP_.
  
-	TEST (data): Tương tự dữ liệu VALIDATE.

-	KEEP (variable list): Các biến cần giữ lại (ví dụ customer_id, yearmonth, contract_no). Nguyên nhân vì mặc định macro ADD_WOE chỉ giữ lại các biến có dạng WOE_, GRP_, GOOD, BAD.

-	VARLIST (variable list): Các biến sẽ được transform thành dạng WoE và Group.
