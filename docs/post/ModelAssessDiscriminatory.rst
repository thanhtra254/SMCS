.. _post-model_assess-disc:

================================
Model Assessment: Discriminatory
================================


Kiểm định tính phân biệt
========================

Kiểm định tính phân biệt được sử dụng ở hầu hết các mô hình dự báo. Một mô hình là tốt nếu quan sát A "xấu" hơn quan sát B thì mô hình phải dự báo được rằng A "xấu" hơn B. Mục đích của kiểm định tính phân biệt là kiểm tra điều này. Một số kiểm định sau đây thường được áp dụng để kiếm tra tính phân biệt của mô hình.

Đánh giá thứ tự bad rate 
------------------------

Kiểm định này thường được thực hiện như sau:

- Chia các dữ liệu thành các nhóm dựa trên kết quả đầu ra của mô hình. Cách chia thường dùng là đảm bảo số quan sát ở mỗi nhóm bằng nhau (`quatile binning <https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=prochp&docsetTarget=prochp_hpbin_overview03.htm&locale=en>`_).
- Sắp xếp theo thứ tự các nhóm từ xấu đến tốt theo kết quả đầu ra và tính số lượng good, bad trong mỗi nhóm. Từ đó tính được bad rate của mỗi nhóm.
- Vẽ đồ thị thể hiện Bad rate trong từng nhóm.

Ví dụ được cho trong hình sau:

.. image:: ./images/ModeAssessment/BadRate.png
  :align: center
  :alt: Bad Rate
  :height: 162px

Đường cong ROC và hệ số Gini 
----------------------------

Hệ số K-S
---------
