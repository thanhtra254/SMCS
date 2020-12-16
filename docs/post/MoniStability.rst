.. _post-moni-stability:

============================
Monitoring Report: Stability
============================

Đánh giá sự ổn định được chia thành hai loại: Đánh giá trên toàn dữ liệu và đánh giá theo từng biến.

Đánh giá sự ổn định trên toàn bộ dữ liệu
========================================

Ý nghĩa sự ổn định của toàn dữ liệu:

-	Đánh giá sự ổn định của mô hình nhằm mục đích đảm bảo tương lai sẽ giống với quá khứ.
-	Đánh giá độ ổn định nhằm đảm bảo các chỉ số cut-off vẫn giữa nguyên ý nghĩa với mẫu development.
-	Đánh giá sự ổn định của từng biến để lựa chọn biến.

Để đánh giá sự ổn định ta cần dữ liệu train và out of time. Sau khi xây dựng xong mô hình, ta sẽ tiến hành chấm điểm cho hai dữ liệu này. Sau khi có điểm, ta chia điểm chấm này thành 20 khoảng vào tính số lượng và phần trăm quan sát trong mỗi khoảng. Hình sau đây minh họa sự so sánh phân phối giữa dữ liệu train và out of time:

Trong đó :math:`\%Dev,\%Rec` là phần trăm quan sát trong mỗi khoảng của mẫu train (DEV-development) và out of time (REC- recent).

Để có một đánh giá định lượng, ta sử dụng chỉ số PSI (population stability index)

.. math::
  PSI=\sum_{i=1}^n\left(\%Dev_i-\%Rec_i\right)\times \ln\left(\frac{\%Dev_i}{\%Rec_i}\right)
  
Trong đó:

- :math:`\%Rec_i`: Tỉ lệ quan sát ở khoảng thứ i so với toàn mẫu ở mẫu kiểm định (out of time).
- :math:`\%Dev_i`: Tỉ lệ quan sát ở khoảng thứ i so với toàn mẫu ở mẫu phát triển (train).

Thang đánh giá cho chỉ số PSI được cho dưới đây:

- :math:`PSI \le 10`: Mô hình là ổn định.
- :math:`10 \le PSI \le 20`: Mô hình tương đối ổn định.
- :math:`20 < PSI`: Mô hình không ổn định.

Đánh giá sự ổn định của từng biến
=================================

Ý nghĩa sự ổn định của từng biến:

- Tìm ra nguyên nhân mất ổn định của mô hình.
- Đánh giá sự biến động của mỗi biến qua thời gian.
- Tìm ra các sai sót trong hệ thống.

Để đánh giá sự ổn định cho từng biến, ta thực hiện tương tự đánh giá sự ổn định cho toàn mẫu. Chỉ số sử dụng là CSI (characteristic stability index). 

.. math::
  CSI=\sum_{i=1}^n\left(\%Dev_i-\%Rec_i\right)\times \ln\left(\frac{\%Dev_i}{\%Rec_i}\right)
  
Trong đó:

- :math:`\%Rec_i`: Tỉ lệ quan sát ở nhóm thứ i so với toàn mẫu ở mẫu kiểm định (out of time).
- :math:`\%Dev_i`: Tỉ lệ quan sát ở nhóm thứ i so với toàn mẫu ở mẫu phát triển (train).
