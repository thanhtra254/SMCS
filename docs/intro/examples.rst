.. _intro-examples:

========
Examples
========

Tạo dữ liệu Dummy
=================

Để tạo dữ liệu Dummy, ta sử dụng Macro:

.. code:: sh

  %%DATA_DUMMY;

Kết quả của macro là hai dữ liệu: 

- Dữ liệu TRAIN minh họa cho dữ liệu được dùng để xây dựng mô hình (có YEARMONTH nằm trong đoạn 201901 đến 201903).
- Dữ liệu OUTTIME minh họa cho dữ liệu Out of time (có YEARMONTH nằm trong đoạn 201904 đến 201912)

Các biến trong dữ liệu như sau:

- Biến Y là biến liên tục trong khoảng (0,1) được tạo ra theo phân phối Beta.
- Biến Good, Bad được định nghĩa dựa trên biến Y.
- Các biến X1-X13 được tạo ra ngẫu nhiên (có thể phụ thuộc hoặc không phụ thuộc Y). Trong đó hai biến X5 và X13 là biến chữ và còn lại là các biến số.

Data Preparation
================

Do không có bước data mining nên ta bỏ ra bước Data Aggregation. Ta thực hiện các bước sau:

Giảm kích thước dữ liệu
-----------------------

.. code:: sh

  %DATA_REDUCE_SIZE(TRAIN, DATA.IMPORT, );
  %DATA_REDUCE_SIZE(OUTTIME, DATA.OUTTIME, );

Kết quả nhận được là hai dữ  liệu DATA.IMPORT và DATA.OUTTIME.

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



  
