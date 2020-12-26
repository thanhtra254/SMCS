.. _post-moni-accuracy:

===========================
Monitoring Report: Accuracy
===========================

Kiểm định tính chính xác
========================

Kiểm định sự chính xác chỉ xuất hiện ở các mô hình phải dự đoán chính xác biến đầu ra (khác với mô hình xếp hạng chỉ quan tâm tới thứ tự giữa các quan sát). Ví dụ phổ biến về mô hình dạng này là mô hình PD. Trong trường hợp này, chất lượng của mô hình phụ thuộc vào việc dự đoán chính xác khả năng vỡ nợ (PD) của từng nhóm xếp hạng. Kiểm định sự chính xác là việc so sánh giữa kết quả đã ước lượng (PD predicted) và kết quả thực tế (PD actual). Một số kiểm định thường được sử dụng như sau:

Two side nominal test
---------------------

Kiểm định p-value của two side nominal test (cho nhóm i) được tính như sau:

.. math::
  p_i=\phi\left(\frac{d_i/n_i-PD_i}{\sqrt{\frac{PD_i(1-PD_i)}{n_i}}}\right)


Trong đó:

- :math:`n_i` là số lượng quan sát trong nhóm i.
- :math:`d_i` là số lượng default thực tế trong nhóm i.
- :math:`PD_i` là xác xuất vỡ nợ ước lượng của nhóm i.



Walk-through of an example spider
=================================

In order to show you what Scrapy brings to the table, we'll walk you through an
example of a Scrapy Spider using the simplest way to run a spider.
