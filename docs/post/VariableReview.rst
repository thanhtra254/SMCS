.. _post-variable_review:

===============
Variable Review
===============

Lý thuyết
=========
Số lượng biến ban đầu của mô hình có thể từ hàng trăm đến hàng nghìn biến. Việc phân tích (`binning <https://smcs.readthedocs.io/vi/latest/post/VariableAnalysis.html>`_) từng biến tốn rất nhiều thời gian. Do đó cần có các công cụ để:  

- Tính toán các chỉ số thống kê của biến để từ đó đưa ra kết luận về chất lượng dữ liệu.
- Tính toán sơ bộ các chỉ số về tính dự báo của biến để có thể loại các biến có tính dự báo yếu, tránh trường hợp phải đưa nhiều biến vào phân tích.
- Tính toán sự tương quan và phân cụm các biến để có thể chọn ra biến tốt nhất trong từng cụm.

Chi tiết các phần như sau:

Tính toán các chỉ số thống kê
-----------------------------

Các chỉ số về tính dự báo
-------------------------


Phân cụm biến
-------------

Sử dụng Macro
=============

Cú pháp
-------

Cú pháp của Macro như sau:

.. code:: sh
  
  %Var_Review(train, outtime, numbin, exclude_varlist);
  
Trong đó:

- **train (dataset)** là dữ liệu dùng để review các biến. Dữ liệu bắt buộc phải có hai biến good và bad là target của mô hình.
- **outtime (dataset)** là dữ liệu out of time. Tham số này có thể không bắt buộc. Dữ liệu **outtime** phải có các biến tương tự như dữ liệu **train** ngoại trừ sự khác biệt như sau:
  
  - Có thể không có hai biến good, bad.
  - Bắt buộc phải có biến *YEARMONTH* chỉ time id của dữ liệu.
- **numbin (int)** chỉ số lượng các nhóm sẽ chia theo quantile binning. 
- **exclude_varlist** là các biến sẽ được bỏ ra khỏi phân tích. Trong dữ liệu thì các biến loại ra không phân tích sẽ ít hơn nhiều so với các biến sẽ đưa vào phân tích. Do đó chúng tôi sử dụng tham số này.

Detail
------

Macro sẽ xử lý theo hai loại biến là interval và categorical.

**Với biến interval**, công cụ sẽ chia biến thành các khoảng (số lượng khoảng bằng **numbin**) bằng công cụ `PROC HPBIN <https://documentation.sas.com/?docsetId=prochp&docsetTarget=prochp_hpbin_syntax01.htm&docsetVersion=9.4&locale=en>`_ đồng thời tính toán các chỉ số như sau:

- Các chỉ số thống kê: min, max, mean, median, std, non-missing, missing, số lượng các nhóm (là số thực tế so với **numbin** là số kỳ vọng).
- Số lượng good, bad, WoE, Bad rate trong các khoảng.
- Các chỉ số dự báo IV,
- Các chỉ số khác: max_badrate là tỷ lệ bad với nhất trong các nhóm tương tứng với mỗi biến.

**Với biến categorical**, macro chia biến thành các nhóm theo các giá trị khác nhau của biến. Các chỉ số sau đây được tính toán:

- Các chí số thống kê: non-missing, missing, số lượng các nhóm, mode.
- Các chỉ số dự báo: IV, max_badrate.

Nếu có tham số **outtime** thì macro sẽ sử dụng cách chia biến interval trong dữ liệu **train** để áp dụng vào dữ liệu **outtime**. Các biến categorical được xử lý tương tự như dữ liệu **train**. Macro sẽ tính toán chỉ số PSI cho các biến. 

Output
------

Kết quả của macro là các dữ liệu như sau: 

Các bảng liên quan đến các chỉ số thống kê * dự báo

- *MAPPING* là dữ liệu ghi lại cách binning các biến. Có thể sử dụng bảng này cùng với `PROC HPBIN <https://documentation.sas.com/?docsetId=prochp&docsetTarget=prochp_hpbin_syntax01.htm&docsetVersion=9.4&locale=en>`_ để binning các biến.

.. csv-table:: Example of dataset MAPPING
	:header: Variable, BinnedVariable, LB, UB, Range, Bin, Frequency, Proportion
	:align: center
	:widths: 10, 20, 20, 20, 30, 10, 10, 10
	
	X1,	BIN_X1,	.,    	-0.997,	X1 < -0.997,           	1,	8761,	0.05000029
  X1,	BIN_X1,	-0.997,	-0.992,	-0.997 <= X1 < -0.992,	2,	8761,	0.05000029
  X1,	BIN_X1,	-0.992,	-0.983,	-0.992 <= X1 < -0.983,	3,	8761,	0.05000029
  X1,	BIN_X1,	-0.983,	-0.971,	-0.983 <= X1 < -0.971,	4,	8761,	0.05000029
  X1,	BIN_X1,	-0.971,	-0.956,	-0.971 <= X1 < -0.956,	5,	8761,	0.05000029
	...,	...,	...,	...,	...,	..., ..., ...

- **

Các bảng liên quan đến độ ổn định (các bảng này chỉ xuất hiện nếu có dữ liệu **outtime**)


Example
-------
