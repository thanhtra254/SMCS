.. _post-data_aggregation:

================
Data Aggregation
================



Dữ liệu SQL
===========

Khi xây dựng Credit Scoring, ta thường sử dụng công cụ SQL để tạo các biến. Dữ liệu thường được lấy theo cách sau đây để tăng tính hiệu quả:

.. image::  post/images/DataPreparation/DataSQL.png
  :height: 108
  :alt: Variable Extraction

Các biến sẽ được lấy tại từng khung thời gian (theo tháng, tuần, năm) trước ngày quan sát. Ví dụ về dữ liệu được cho như sau:

.. image::  post/images/DataPreparation/DataBefore.png
  :height: 262
  :alt: Example of data
  
Trong đó:

- ID là key của dữ liệu. Ví dụ customer\_id.
- ID\_month là số chỉ các frame. Ví dụ ID_month=3 nghĩa là thông tin được lấy tại tháng thứ 3 trước ngày quan sát.
- Var là các biến được lấy tại khoảng thời gian ID\_month tương ứng.

Từ dữ liệu này, ta tính các hàm tổng hợp:

- Num,Sum, Min, max, avg, std: Số lượng, tổng, giá trị nhỏ nhất, giá trị lớn nhất, giá trị trung bình, độ lệch chuẩn.
- Rng (range): giá trị lớn nhất – giá trị nhỏ nhất.
- Crr (Correlation): tương quan giữa biến và time step.
- Slp (Slope): hệ số góc giữa biến và time step.

.. image::  post/images/DataPreparation/DataAgg.png
  :height: 249
  :alt: Data from SQL

Kết quả của Data Aggregation là các biến mới được đặt tên theo quy tắc như sau:

``Varname_agg1_agg2_c/m(i)``

Trong đó:

- Varname là tên của biến:
- Agg1, agg2 là các hàm aggregation dữ liệu, đặt tên theo 3 ký tự (num, min, avg, max, sum, std (standard deviation), crr (correlation), slp (slope), rng(range)). Agg1 được lấy từ từng snapshot, agg2 được lấy theo cumulative.
- c/m(i): c(i) là trong i tháng trước ngày quan sát (cumulative), m(i) là trong tháng I trước ngày quan sát (marginal).

**Ví dụ:** DPD_max_max_c12: Giá trị DPD lớn nhất của các giá trị lớn nhất trong vòng 12 tháng trước ngày quan sát. Có thể hiểu đơn giản là DPD lớn nhất trong 12 tháng trước ngày quan sát. Chú ý rằng có thể có những biến vô nghĩa (ví dụ DPD_max_min_12m). Cần lưu ý điều này khi phân tích biến. Minh họa về dữ liệu sau bước Data Aggregation được cho như sau:

.. image::  post/images/DataPreparation/DataBefore.png
  :height: 283
  :alt: Data from SQL

Sử dụng Macro
=============

Syntax
------

Để thực hiện Data Aggregation, ta sử dụng Macro DATA_AGGREGATION. Cú pháp của Macro như sau:

.. code:: sh
  
  %Data_Aggregation (Dsin, Dsout, max_month, id, varlist)
  
Trong đó:

- **Dsin:** data đầu vào chính là data dạng multiple từ SQL.
- **Dsout:** data đầu ra. Mỗi biến cơ sở sẽ tạo ra max 𝑚𝑜𝑛𝑡ℎ×10  biến mới
- **Max_month:** Là số tháng lớn nhất trước ngày quan sát (12,6) của cột id_month.
- **Id:** Primary key của bảng. Ví dụ business_date customer_id.
- **Varlist:** Danh sách các biến.









