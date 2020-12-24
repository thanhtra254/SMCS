.. _intro-examples:

========
Examples
========

Tạo dữ liệu Dummy
=================

Để tạo dữ liệu Dummy, ta sử dụng Macro:

.. code:: sh

  %DATA_DUMMY(NOBS=1000000);


Với *NOBS* là tham số để macro sinh ra dữ liệu gồm *NOBS* quan sát. Có thể điều chỉnh *NOBS* để phù hợp với cấu hình máy tính. Kết quả của macro là ba dữ liệu: 

- Dữ liệu TRAIN minh họa cho dữ liệu được dùng để xây dựng mô hình (có YEARMONTH nằm trong đoạn 201901 đến 201903).
- Dữ liệu OUTTIME minh họa cho dữ liệu Out of time (có YEARMONTH nằm trong đoạn 201904 đến 201912).
- Dữ liệu VARIABLE_SQL minh họa cho dữ liệu import từ SQL. 

Các biến trong dữ liệu TRAIN và OUTTIME như sau:

- Biến ID minh họa cho Key của dữ liệu.
- Biến Y là biến liên tục trong khoảng (0,1) được tạo ra theo phân phối Beta(0.2, 0.2).
- Biến Good, Bad được định nghĩa dựa trên biến Y.
- Các biến X1-X13 được tạo ra ngẫu nhiên (có thể phụ thuộc hoặc không phụ thuộc Y). Trong đó hai biến X5 và X13 là biến chữ có độ dài lớn (255) và còn lại là các biến số.
- Biến OBS_DATE minh họa cho observationn date và đang có định dạng sai (định dạng chữ thay vì datetime).

Các biến trong dữ liệu VARIABLE_SQL như sau:

- Biến ID minh họa cho key của dữ liệu, được dùng để map với bảng TRAIN và OUTTIME.
- Biến ID_MONTH minh họa cho khoảng thời gian lấy dữ liệu của biến (xem thêm tại `Data Aggregation <https://smcs.readthedocs.io/vi/latest/post/DataAggregation.html>`_).
- Biến Z1-Z4 là các biến số được sinh ra phụ thuộc vào biến Y và ID_MONTH.

Data Preparation
================

Data Aggregation
----------------

Để tạo các biến từ dữ liệu SQL, ta sử dụng Macro:

.. code:: sh
  
  %DATA_AGGREGATION(DSIN=VARIABLE_SQL, 
                    DSOUT=VARIABLE, 
                    MAX_MONTH=12, 
                    ID=ID, 
                    VARLIST= Z1 Z2 Z3);

Kết quả nhận được là dữ liệu VARIABLE chứa các biến ba chiều. 

Giảm kích thước dữ liệu
-----------------------

Dữ liệu TRAIN và OUTTIME có kích thước là 207MB và 622MB tương ứng. Biến OBS_DATE trong hai dữ liệu đang có định dạng sai. Ta thu gọn dữ liệu như sau:

.. code:: sh

  %DATA_REDUCE_SIZE(TRAIN, DATA.IMPORT, OBS_DATE);
  %DATA_REDUCE_SIZE(OUTTIME, DATA.OUTTIME, OBS_DATE);

Kết quả nhận được là hai dữ  liệu DATA.IMPORT và DATA.OUTTIME với kích thước 37MB và  112MB. Ta tiến hành JOIN các biến vào dữ liệu TRAIN và VALIDATE:

.. code:: sh

  DATA DATA.IMPORT;
    MERGE DATA.IMPORT(IN= DATA) VARIABLE (IN= VAR);
    BY ID;
    IF DATA;
  RUN;

  DATA DATA.OUTTIME;
    MERGE DATA.OUTTIME(IN= DATA) VARIABLE (IN= VAR);
    BY ID;
    IF DATA;
  RUN;


Chia thành train/ Validate 
--------------------------

Ta chia dữ liệu thành hai phần, 70% quan sát cho dữ liệu train và 30% quan sát cho dữ liệu validate. Cách làm như sau:

.. code:: sh

  %DATA_PARTITION(DATA.IMPORT, DATA.TRAIN, DATA.VALIDATE, 70, GOOD);

Chương trình SAS hiện thông báo như sau:

======== ================ =====================
One Target Stratified Sampling Frequency Table
-----------------------------------------------
  Target    Number of Obs    Number of Samples
-------- ---------------- ---------------------
 0          1249504          874776
 1          1248420          874000
-------- ---------------- ---------------------



  
