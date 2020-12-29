.. _post-data_reducesize:

================
Data Reduce Size
================

Overview
========

Data xây dựng mô hình được import từ nhiều nguồn khác nhau (SQL, Excel, Csv). Trong nhiều trường hợp, định dạng dữ liệu trong các file này không đúng. Một số ví dụ phổ biến như sau:

- Độ dài các biến chữ quá lớn: SQL thường sử dụng NVARCHAR(MAX), khi import dữ liệu này vào SAS, độ dài của biến chữ quá lớn dẫn đến kích thước dữ liệu quá nặng không cần thiết.
- Các biến ngày tháng được hiểu không đúng định dạng: Các biến ngày tháng khi import từ dữ liệu SQL thường có định dạng text (ví dụ '2020-01-08'). Việc convert các biến này thành đúng định dạng đôi khi tốn nhiều thời gian.

Macro DATA_REDUCE_SIZE với mục đích xử lý hai vấn đề trên:

- Với biến chữ có độ dài lớn, macro giảm thiểu độ dài xuống ngắn nhất có thể (và vẫn dữ nguyên thông tin của dữ liệu).
- Với các biến ngày tháng định dạng sai, macro chuyển các biến này thành đúng định dạng  là format YYMMDD10. của SAS (dữ liệu sẽ hiển thị là 2020-01-08)

Sử dụng Macro
=============

Syntax
------

Cú pháp của macro như sau:

.. code:: sh   
    
    %DATA_REDUCE_SIZE(INPUT, OUTPUT, DATE_VARLIST)

Trong đó:

- **INPUT** là data đầu vào.
- **OUTPUT** là data đầu ra.
- **DATE_VARLIST** là danh sách các biến ngày tháng bị sai định dạng.

Detail
------

Output
------

Kết quả đầu ra của Macro là dữ liệu **OUTPUT** với các biến định dạng ký tự (biến character) đã được rút gọn độ dài tối thiểu và các biến dạng date time đã được chuyển về đúng định dạng YYYY-MM-DD.

Example
-------

.. code:: sas    
    
    %REDUCE_SIZE(DATA.IMPORT, DATA.IMPORT1, 
        DATE_VARLIST=
            CREATION_DATE
            MIN_VALUE_DATE
            DATE_OF_ISSUE
            CUR_START_LIVING_DATE
            EMP_START_WORK_DATE
            CUS_OPEN
            MIN_BD_COLL);




