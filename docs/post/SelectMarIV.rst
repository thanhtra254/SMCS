.. _post-select_mariv:

=========================================
Variable Selection: Marginal IV Selection
=========================================

Marginal IV
===========
Ta định nghĩa mô hình M_kvới kết quả đầu ra: :math:`P(Good)_i=(y_(k,i))`. Xét biến X được chia thành các nhóm 1,2,…,n. Với mỗi nhóm, ta định nghĩa ΔWoE như sau:

.. math::
    \Delta WoE=WoE_obs-WoE_Exp=\ln\left(\\frac{G_obs/TotalG_obs}{B_obs/TotalB_obs}\\right)-\\ln\\left(\\frac{G_exp/TotalG_exp}{B_exp/TotalB_exp}\\right)

Trong đó:
- G_obs,B_obs là số lượng quan sát good, số lượng quan sát bad trong nhóm.
- G_exp,B_exp là tổng xác xuất dự báo good, tổng xác suất dự báo bad trong nhóm.

Công thức tính Marginal IV của biến được cho như sau:

.. math::
	MIV=\\sum_{i=1}^n \\left(%G_obs-%B_obs \\right)
Minh họa công thức tính được cho trong bảng dưới đây:

Lưu ý rằng, với model chỉ có intercept thì công thức Marginal IV cho kết quả trùng với IV.

Thuật toán lựa chọn biến dựa trên MIV
=====================================

Dựa trên khái niệm Marginal IV, thuật toán chọn biến dựa trên Marginal IV được đề xuất như sau:

#. Xếp các biến theo thứ tự marginal IV giảm dần.
#. Chọn biến có Marginal IV lớn nhất vào mô hình và ước tính hệ số. Từ đó tính ra các kết quả dự báo của mô hình.
#. Tính lại Marginal IV của các biến (chú ý rằng, Marginal IV của biến đã vào mô hình bằng 0).
#. Tiếp tục các bước từ 1 đến 3 cho đến khi không còn biến nào có Marginal IV đủ lớn (có thể chọn điểm cắt MIV>0.01)

Minh họa cho kết quả chọn biến sử dụng Marginal IV được cho trong bảng dưới đây:

