
.. _post-select_overview:

==================
Variable Selection
==================

Tổng quan
=========

Việc lựa chọn biến ở mô hình Credit Scoring có mục đích chọn số biến ít nhất sao cho mô hình là mạnh nhất. Việc chọn số biến ít nhất sẽ có lợi thế cho việc triển khai và hậu kiểm mô hình sau này. Mô hình Credit Scoring thường yêu cầu các ràng buộc như sau:

- Các biến không có tương quan đôi một lớn hơn 0.7: Thật ra điều này không hề có trong bất kỳ tài liệu chính thống nào. Nhiều nghiên cứu chỉ ra rằng với số lượng mẫu đủ lớn thì sự đa cộng tuyến giữa các biến không ảnh hưởng tới kết quả hồi quy mô hình. Ngưỡng 0.7 là tự quy định.
- Các hệ số phải là dương: Từ công thức tính :math:`WoE=\ln\left(\frac{\%Good}{\%Bad}\right)` ta thấy rằng, khách hàng càng tốt thì WoE càng lớn. Điều đó nghĩa là các hệ số hồi quy :math:`\beta_1, \beta_2, \ldots, \beta_n` ứng với :math:`woeX1,woeX2,\ldots,woeXn` phải là các giá trị dương. 
- P-value của mỗi biến phải nhỏ hơn 0.05: Điều này để đảm bảo biến vào mô hình là có ý nghĩa. Tuy nhiên chỉ số này không đáng tin cậy và có thể fake dễ dàng.
- Tối đa hóa sức mạnh của mô hình: Các tài liệu và các tổ chức tín dụng hay sử dụng chỉ số Gini (một số dạng khác là AR, AUC) để đánh giá sức mạnh của mô hình.

Phương pháp lựa chọn biến
=========================

Thử tất các các trường hợp
--------------------------

Thuật toán Greedy
-----------------

Thuật toán LASSO
----------------
    
