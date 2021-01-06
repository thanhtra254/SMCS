.. _post-var_transformation:

=======================
Variable Transformation
=======================

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

Chú ý rằng phiên bản mới nhất của macro `variable analysis <https://smcs.readthedocs.io/vi/latest/post/VariableAnalysis.html>`_ sử sẽ tự động output ra bảng chứa dữ liệu format. Để chạy các format này ta dùng lệnh:

.. code:: sh
  
  	PROC FORMAT CNTLIN=BIN_MAPPING;
	  RUN;
    
Trong đó *BIN_MAPPING* là dữ liệu chứa format. Các biến ban đầu sẽ được chuyển sang các giá trị WOE dựa trên các khoảng chia này. Để thực hiện việc biến đổi sang dạng WOE, ta dùng macro **DATA_ADD_WOE**.

Sử dụng Macro
=============

Syntax
------

Macro **VAR_ADD_WOE** là công cụ transform các biến từ dạng ban đầu sang dạng WOE và lưu sang một dữ liệu mới. Cú pháp của macro như sau:

.. code:: sh

  %DATA_ADD_WOE(DATA=, VALIDATE=, TEST=, KEEP=,VARLIST=);
  
Trong đó:

-	**DATA** (data): Dữ liệu train. Các giá trị WOE của từng nhóm sẽ được tính dựa  trên dữ liệu  DATA. Macro đẩy ra hai dữ liệu liên quan:

  -	*DATA_WOE* (output) chứa các biến đã được chuyển sang dạng WoE từ dữ liệu DATA. Các biến được đổi tên bắt đầu bằng WOE\_.
  -	*DATA_GRP* (output) chứa các biến đã được chuyển sang dạng group từ dữ liệu DATA. Các biến được đổi tên bắt đầu bằng GRP\_.
  
-	**VALIDATE** (data): Dữ liệu validate. Macro sử dụng WOE được tính từ **DATA** để transform các biến. Macro đẩy ra hai dữ liệu mới:
  -	*VALIDATE_WOE* (output) chứa các biến đã được chuyển sang dạng WoE từ dữ liệu **VALIDATE**. Các biến được đổi tên bắt đầu bằng WOE\_.
  -	*VALIDATE_GRP* (output) chứa các biến đã được chuyển sang dạng group từ dữ liệu **VALIDATE**. Các biến được đổi tên bắt đầu bằng GRP\_.
  
-	**TEST** (data): Tương tự dữ liệu **VALIDATE**.

-	**KEEP** (variable list): Các biến cần giữ lại (ví dụ customer_id, yearmonth, contract_no). Nguyên nhân vì mặc định macro ADD_WOE chỉ giữ lại các biến có dạng WOE\_, GRP\_, GOOD, BAD.

-	**VARLIST** (variable list): Các biến sẽ được transform thành dạng WoE và Group.

Detail
------

Các bước xử lý trong macro như sau:

- Bước 1: Transform các biến thành dạng Group (các biến có tiền tố GRP\_) và tạo bảng DATA_GRP (ví dụ tham số **DATA** là DATA.PD_RB thì dữ liệu sẽ có tên là DATA.PD_RB_GRP. Lưu ý rằng cách hiểu này được áp dụng cho các nội dung phía dưới trong bài viết này). Sử dụng `PROC FREQ <https://documentation.sas.com/?docsetId=procstat&docsetVersion=9.4&docsetTarget=procstat_freq_syntax01.htm&locale=en>`_ để tính WoE của các nhóm của các biến Group;
-	Bước 2: Tạo bảng DATA_WOEDATA chứa thông tin tổng hợp về nhóm và WoE của các biến thuộc **VARLIST**.
-	Bước 3: Chuyển các biến trong dữ liệu DATA thành dạng WoE và tạo ra bảng DATA_WOE.
-	Bước 4: Nếu dữ liệu **VALIDATE** tồn tại thì chuyển các biến trong dữ liệu **VALIDATE** thành dạng group và WoE. Đẩy ra hai bảng VALIDATE _WOE và VALIDATE _GRP.
-	Bước 5: Nếu dữ liệu **TEST** tồn tại thì chuyển các biến trong dữ liệu **TEST** thành dạng group và WoE. Đẩy ra hai bảng TEST _WOE và TEST_GRP.

Output
------

Đầu ra của Macro là các bảng sau đây:

- Các bảng chứa thông tin biến dưới dạng group: DATA_GRP, VALIDATE_GRP, TEST_GRP.
- Các bảng chứa thông tin biến dưới dạng WoE: DATA_WOE, VALIDATE_WOE, TEST_WOE.
- Bảng chứa thông tin các nhóm của biến: DATA_WOEDATA.
- Bảng chứa thông tin binning: DATA_MAPPING.

Example
-------

Ví dụ 1: Sử dụng proc format để lưu khoảng chia của biến:


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

  PROC FORMAT;
    /* X2 */
    VALUE X2F
      . = '[01] MISSING' 
      LOW - -0.9836932146 = '[02] X2 <= -0.9836932146' 
      -0.9836932146< - -0.9347724580 = '[03] -0.9836932146 < X2 <= -0.9347724580' 
      -0.9347724580< - -0.7442787976 = '[04] -0.9347724580 < X2 <= -0.7442787976' 
      -0.7442787976< - -0.5803201324 = '[05] -0.7442787976 < X2 <= -0.5803201324' 
      -0.5803201324< - -0.3848034212 = '[06] -0.5803201324 < X2 <= -0.3848034212' 
      -0.3848034212< - -0.0590991114 = '[07] -0.3848034212 < X2 <= -0.0590991114' 
      -0.0590991114< - 0.9552791091 = '[08] -0.0590991114 < X2 <= 0.9552791091' 
      0.9552791091< - HIGH = '[09] 0.9552791091 < X2';
  RUN;
  /*----More format here----*/
  
  PROC FORMAT;
    /* X12 */
    VALUE X12F


      . = '[01] MISSING' 
      LOW - -388973.67807 = '[02] X12 <= -388,973.67807' 
      -388973.67807< - -272177.72584 = '[03] -388,973.67807 < X12 <= -272,177.72584' 
      -272177.72584< - -166793.56727 = '[04] -272,177.72584 < X12 <= -166,793.56727' 
      -166793.56727< - -117865.48115 = '[05] -166,793.56727 < X12 <= -117,865.48115' 
      -117865.48115< - -16449.67509 = '[06] -117,865.48115 < X12 <= -16,449.67509' 
      -16449.67509< - HIGH = '[07] -16,449.67509 < X12';
  RUN;

  %VAR_ADD_WOE (DATA=DATA.TRAIN, VALIDATE= DATA.VALID, 
    KEEP=Y YEARMONTH,
    VARLIST=X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12);



Ví dụ 2: Sử dụng dataset để lưu khoảng chia của biến:

.. code:: sh

    PROC FORMAT CNTLIN=BIN_MAPPING;
	  RUN;
    
    %VAR_ADD_WOE (DATA=DATA.TRAIN, VALIDATE= DATA.VALID, 
      KEEP=Y YEARMONTH,
      VARLIST=X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12);


