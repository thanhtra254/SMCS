.. _intro-install:

=======
Cài đặt
=======

Tải các macros
==============

Để cài đặt online, tạo Project SAS Enterprise Guide (file .EGP) và gõ lệnh như sau:

.. code:: sh

  DATA _NULL_;
    LOCATION=DEQUOTE("&_CLIENTPROJECTPATH");
    CALL SYMPUTX("LOCATION", SUBSTR(LOCATION, 1, FINDC(LOCATION, "\", -255)-1));
  RUN;

  X 'FCOPY 
    "\\10.39.133.225\Document\RMD\RCC(GSRR)\Modeling\05 TRAINEE\4. DATABASE VM\MACROS\*" 
    "&LOCATION\MACROS"';

Các macro sẽ được cài đặt trong thư mục **&LOCATION\MACROS** trong đó &LOCATION là vị trí lưu file SAS. Ví dụ file .EGP được lưu tại thư mục *E:\\THANHTRA254\\2. PROJECT\\84. Sas macros for Credit Scoring"* thì các Macro sẽ được lưu tại *E:\\THANHTRA254\\2. PROJECT\84. Sas macros for Credit Scoring\MACROS*. Để load các macro ta dùng lệnh:

.. code:: sh

  LIBNAME MACRO "&LOCATION\MACROS";
  OPTIONS MSTORED SASMSTORE=MACRO;
  
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
   :widths: 25 100 10 10
   :header-rows: 1
   
   * - MACRO_NAME
     - DATA_ADD_WOE
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
