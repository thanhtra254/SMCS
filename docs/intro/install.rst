.. _intro-install:

=======
Cài đặt
=======

Tải các macros
==============

Cài đặt tự động
---------------

Để cài đặt SMCS, tạo Project SAS Enterprise Guide (file .EGP) và tạo một program, sau đó gõ lệnh như sau:

.. code:: sh

  DATA _NULL_;
    LOCATION=DEQUOTE("&_CLIENTPROJECTPATH");
    CALL SYMPUTX("LOCATION", SUBSTR(LOCATION, 1, FINDC(LOCATION, "\", -255)-1));
  RUN;

  X 'FCOPY 
    "\\10.39.133.225\Document\RMD\RCC(GSRR)\Modeling\05 TRAINEE\4. DATABASE VM\MACROS\*" 
    "&LOCATION\MACROS"';

Các macro sẽ được cài đặt trong thư mục 

  ``&LOCATION\MACROS`` 
  
Trong đó &LOCATION là vị trí lưu file SAS. Ví dụ file .EGP được lưu tại thư mục 

  ``E:\THANHTRA254\2. PROJECT\84. Sas macros for Credit Scoring``
  
thì các Macro sẽ được lưu tại 

  ``E:\THANHTRA254\2. PROJECT\84. Sas macros for Credit Scoring\MACROS`` 

Để load các macro ta dùng lệnh:

.. code:: sh

  LIBNAME MACRO "&LOCATION\MACROS";
  OPTIONS MSTORED SASMSTORE=MACRO;
  
  
Cài đặt thủ công
----------------

Để cài đặt thủ công ta làm các bước như sau:

- Tạo thư mục MACROS trong nơi chứa Project.
- Copy toàn bộ các file trong thư mục ``\\10.39.133.225\Document\RMD\RCC(GSRR)\Modeling\05 TRAINEE\4. DATABASE VM\MACROS\`` vào thư mục vừa tạo.
- Tạo library Macro bằng cách gõ lệnh:

.. code:: sh

  LIBNAME MACRO "&PATHNAME\MACROS";
  OPTIONS MSTORED SASMSTORE=MACRO;

Trong đó **&PATHNAME** là nơi chứa Project.
  

Kiểm tra thông tin Macros
=========================

Để kiểm tra thông tin của các macro, ta sử dụng lệnh sau:

.. code:: sh

  PROC SQL NOPRINT;
    CREATE TABLE MACRO_LIST AS
      SELECT OBJNAME AS MACRO_NAME,OBJDESC AS MACRO_DESC,CREATED,MODIFIED
        FROM DICTIONARY.CATALOGS
          WHERE OBJTYPE='MACRO' 
            AND LIBNAME NOT IN ("WORK", "SASHELP", "SASUSER");
  QUIT;

Kết quả nhận được như sau:

.. list-table:: Macro Information
   :widths: 35 60 25 25
   :header-rows: 1
   
   * - MACRO_NAME
     - MACRO_DESC
     - CREATED
     - MODIFIED
   * - DATA_ADD_WOE	
     - Transform to WOE and GRP datas. For detail: https://smcs.readthedocs.io/vi/latest/post/DataTransformartion.html
     - 22DEC20:09:45:14	
     - 22DEC20:09:45:14
   * - DATA_AGGREGATION	
     - Aggregate data. For detail: https://smcs.readthedocs.io/vi/latest/post/DataAggregation.html	
     - 22DEC20:10:03:51	
     - 22DEC20:10:03:51
   * - DATA_DUMMY	
     - (NOBS(Number of observation)) | Create dummy datasets with 'nobs' observation	
     - 22DEC20:09:41:41	
     - 22DEC20:09:41:41
   * - ...
     - ...
     - ...
     - ...
     
Trong đó  MACRO_NAME là tên của Macro, MACRO_DESC là mô tả về Macro. CREATED và MODIFIED là ngày tạo và ngày cuối cùng thay đổi nội dung Macro.
