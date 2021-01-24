.. _post-model_assess-accuracy:

===============================
 Assessment: Accuracy
===============================

Kiểm định tính chính xác
========================

Kiểm định sự chính xác chỉ xuất hiện ở các mô hình phải dự đoán chính xác biến đầu ra (khác với mô hình xếp hạng chỉ quan tâm tới thứ tự giữa các quan sát). Ví dụ phổ biến về mô hình dạng này là mô hình PD. Trong trường hợp này, chất lượng của mô hình phụ thuộc vào việc dự đoán chính xác khả năng vỡ nợ (PD) của từng nhóm xếp hạng. Kiểm định sự chính xác là việc so sánh giữa kết quả đã ước lượng (PD predicted) và kết quả thực tế (PD actual). Một số kiểm định thường được sử dụng như sau:

Normal test
-----------

Kiểm định p-value của two side nominal test (cho nhóm i) được tính như sau:

.. math::
  p_i=\phi\left(\frac{d_i/n_i-PD_i}{\sqrt{\frac{PD_i(1-PD_i)}{n_i}}}\right)


Trong đó:

- :math:`n_i` là số lượng quan sát trong nhóm i.
- :math:`d_i` là số lượng default thực tế trong nhóm i.
- :math:`PD_i` là xác xuất vỡ nợ ước lượng của nhóm i.

Chi-square test
---------------

Kiểm định Chi-square test được tính như sau:

.. math::
  \chi^2=\sum_{i=1}^k \frac{(n_i PD_i -d_i)^2}{n_i PD_i(1-PD_i)}
  p=cdf('chisquare', \chi^2, k)

Trong đó:

- :math:`n_i` là số lượng quan sát trong nhóm i.
- :math:`d_i` là số lượng default thực tế trong nhóm i.
- :math:`PD_i` là xác xuất vỡ nợ ước lượng của nhóm i.
- :math:`k` là số lượng các nhóm.

Binomial Test
-------------

Kiểm định p-value của binomial test (cho nhóm i) được tính như sau:

.. math::
  p_i=\sum_{m=0}^{d_i-1}\binom{n_i}{m}PD_i^m\left(1-PD_i\right)^{n_i-m}
  
Trong đó:

- :math:`n_i` là số lượng quan sát trong nhóm i.
- :math:`d_i` là số lượng default thực tế trong nhóm i.
- :math:`PD_i` là xác xuất vỡ nợ ước lượng của nhóm i.

Kiểm định p-value của Poison binomial test (cho sample) được tính như sau:

.. math::
  p=\sum_{A \subseteq N, |A|<d}\prod_{a\in A}PD(a)\prod_{a\in N\ A}(1-PD(a))

Sử dụng macro
=============
