.. _post-select_mariv:

=========================================
Variable Selection: Marginal IV Selection
=========================================

Marginal IV
===========
Ta định nghĩa mô hình M_kvới kết quả đầu ra: P(Good)_i=(y_(k,i)  ) ̂. Xét biến X được chia thành các nhóm 1,2,…,n. Với mỗi nhóm, ta định nghĩa ΔWoE như sau:

.. math::
    \\Delta WoE=WoE_obs-WoE_Exp=ln((G_obs/TotalG_obs)/(B_obs/TotalB_obs ))-ln((G_exp/TotalG_exp)/(B_exp/TotalB_exp ))

Trong đó:
	G_obs,B_obs là số lượng quan sát good, số lượng quan sát bad trong nhóm.
	G_exp,B_exp là tổng xác xuất dự báo good, tổng xác suất dự báo bad trong nhóm.
Công thức tính Marginal IV của biến được cho như sau:
MIV=∑_(i=1)^n▒〖(%G_obs-%B_obs)〗×ΔWoE
Minh họa công thức tính được cho trong bảng dưới đây:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2
