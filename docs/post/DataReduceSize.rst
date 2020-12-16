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

Syntax
======

Detail
======




