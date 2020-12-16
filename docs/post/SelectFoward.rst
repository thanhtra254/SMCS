.. _post-select_foward:

====================================
Variable Selection: Foward Selection
====================================

Variable Selection
==================

Việc lựa chọn biến ở mô hình Credit Scoring có mục đích chọn số biến ít nhất sao cho mô hình là mạnh nhất. Đương nhiên việc chọn số biến ít nhất sẽ có lợi thế cho việc triển khai và hậu kiểm mô hình sau này. Mô hình Credit Scoring thường yêu cầu các ràng buộc như sau:

- Các biến không có tương quan đôi một lớn hơn 0.7: Thật ra điều này không hề có trong bất kỳ tài liệu chính thống nào. Nhiều nghiên cứu chỉ ra rằng với số lượng mẫu đủ lớn thì sự đa cộng tuyến giữa các biến không ảnh hưởng tới kết quả hồi quy mô hình. Ngưỡng 0.7 là tự quy định.
- Các hệ số phải là dương: Từ công thức tính :math:`WoE='\ln\left⁡(\frac{\%Good}{\%Bad}\right)` ta thấy rằng, khách hàng càng tốt thì WoE càng lớn. Điều đó nghĩa là các hệ số hồi quy :math:`\beta_1, \beta_2, \ldots, \beta_n` ứng với :math:`woeX1,woeX2,\ldots,woeXn` phải là các giá trị dương. 
- P-value của mỗi biến phải nhỏ hơn 0.05: Điều này để đảm bảo biến vào mô hình là có ý nghĩa. Tuy nhiên chỉ số này không đáng tin cậy và có thể fake dễ dàng.

Các phương pháp
===============
Các phương pháp chọn biến cho thuật toán GBT thường được dùng là Forward, Backward và Stepwise

Phương pháp forward
-------------------

Phương pháp forward được mô tả như sau:
-	Bước 0: Bắt đầu với mô hình có 0 biến. Chọn biến sao cho mô hình mạnh nhất (hệ số Gini là cao nhất). Đưa biến đó vào tập hợp biến đã vào mô hình.
-	Bước 1. Chọn biến từ tập hợp các biến chưa vào mô hình sao cho biến đó kết hợp với tập hợp biến đã vào mô hình để mô hình mạnh nhất. Thêm biến đó vào danh sách biến đã vào mô hình.
-	Bước 2. Tiếp tục các bước 1 cho đến khi việc thêm biến không ảnh hưởng khác biệt đến sức mạnh của mô hình
Minh họa cho phương pháp forward được cho như sau:

Phương pháp backward
--------------------

Phương pháp backward ngược lại với forward. Bắt đầu với việc cho tất cả các biến vào mô hình và loại dần các biến sao cho mô hình bị yếu đi ít nhất

Phương pháp stepwise
--------------------

Phương pháp stepwise là kết hợp của forward và backward. Các bước thực hiện được mô tả như sau:
-	Bước 0: Bắt đầu với mô hình có 0 biến. Chọn biến sao cho mô hình mạnh nhất. Đưa biến đó vào tập hợp biến đã vào mô hình
-	Bước 1.1. Chọn biến từ tập hợp các biến chưa vào mô hình sao cho biến đó kết hợp với tập hợp biến đã vào mô hình để mô hình mạnh nhất. Thêm biến đó vào danh sách biến đã vào mô hình.
-	Bước 1.2. Chọn biến từ tập hợp biến đã vào mô hình sao cho khi loại biến đó đi thì mô hình yếu đi ít nhất. Thêm biến đó vào tập hợp biến chưa vào mô hình.
-	Bước 2. Tiếp tục các bước 1.1 và 1.2 cho đến khi việc thêm biến/bỏ biến không ảnh hưởng khác biệt đến sức mạnh của mô hình
