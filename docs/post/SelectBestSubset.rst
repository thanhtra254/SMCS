
.. _post-select_bestsubset:

=========================================
Variable Selection: Best Subset Selection
=========================================

Tổng quan
=========

Best Subset Selection là thuật toán lựa chọn biến bằng cách thử tất cả các tập con của tập hợp biến. Với :math:`n` biến ban đầu, về lý thuyết sẽ có :math:`2^n-1` tập hợp con.
Với mỗi tập con, ta tiến hành hồi quy mô hình với các biến trong tập con này và tính toán các chỉ số như sau:

- Metric: Tiêu chí để đánh giá mô hình. Vì các mô hình Credit Scoring hay sử dụng Gini là chỉ số đánh giá nên các metric sau đây thường được sử dụng:

  - Gini của dữ liệu train/ validation.
  - Gini của Cross validation (xem thêm `Cross Validation <https://smcs.readthedocs.io/vi/latest/post/ModelCrossValidation.html>`_).
  - Gini của K-fold validation (xem thêm `K-fold Validation <https://smcs.readthedocs.io/vi/latest/post/ModelCrossValidation.html>`_).
  
- Số lượng các biến có hệ số ước lượng là âm: về tiêu chí chọn biến thì các hệ số ước lượng không được là số âm (xem thêm `variable selection <https://smcs.readthedocs.io/vi/latest/post/SelectOverview.html>`_.

Do số lượng các trường hợp cần thử là rất lớn (:math:`2^n-1` trường hợp) nên thuật toán chỉ thích hợp với các dữ liệu có số lượng biến ít (nhỏ hơn 20 biến).

Sử dụng Macro
=============

Để thực hiện chọn biến bằng phương pháp best subset, ta sử dụng Macro VARSELECT_ALL_COMBINE;

Syntax
------

Cú pháp của macro như sau:

.. code:: sh

  VARSELECT_ALL_COMBINE(DATA=, VARLIST=, PERCENT=0.7, BATCH_SIZE=1000, NUM=50, METRIC=GINI_CROSS);
  
Trong đó:

- **DATA** là dữ liệu train. Dữ liệu cần có biến BAD và các biến trong **VARLIST**.
- **VALID** là dữ liệu validate (nếu có). Dữ liệu validate có cấu trúc tương tự train.
- **VARLIST** danh sách các biến được đưa vào thử.
- **PERCENT** tỉ lệ phần trăm quan sát ở dữ liệu train/ toàn bộ quan sát trong trường hợp **METRIC** là *GINI_CROSS*.
- **BATCH_SIZE** là số lượt thử mỗi "lần". Nguyên nhân là SAS không thể thử cùng lúc :math:`2^n-1` trường hợp (do giới hạn về RAM, dung lượng ổ cứng). Số lần thử sẽ là :math:`\frac{2^n-1}{BATCH\_SIZE}` (tổng số step).
- **NUM** là số lượng các lần chia trong trường hợp **METRIC** là *GINI_CROSS* hoặc *GINI_KFOLD*.
- **METRIC** là tiêu chí để lựa chọn mô hình. Các giá trị có thể là:

  - *GINI_CROSS* Gini của dữ liệu validate khi thực hiện Cross Validation.
  - *GINI_KFOLD* Gini của dữ liệu validate khi thực hiện KFold Validation.
  - *GINI_VALID* Gini của dữ liệu validate (dữ liệu **VALID**).
  - *GINI_TRAIN* Gini của dữ liệu train (dữ liệu **DATA**).
  
  
Detail
------

Chú ý rằng, trong trường hợp không sử dụng WOE Transform thì hệ số của các biến không ràng buộc phải là số dương. Tuy nhiên để tiện cho việc thống kê, ta cần đổi dấu của biến để các hệ số  trước khi các biến trong varlist 

Output
------

Kết quả đầu ra của Macro là bảng *RESULT* với mỗi dòng là thông tin một lần thử. Dữ liệu có các biến như sau:

- ID: định danh của lần thử.
- MEAN_TRAIN_GINI: Giá trị trung bình của Gini trong mẫu train.
- NUM_VAR: Số lượng biến của lần thử.
- SELECT_VAR: Mã hóa các biến được chọn vào mô hình dưới dạng 0-1. Số 1 ở vị trí thứ i nghĩa là biến thứ i trong **VARLIST** được chọn vào trong lần thử.
- MEAN_VALID_GINI: Giá trị trung bình của Gini trong mẫu validate. Cột này chính là thông tin của tham số **METRIC**.
- NUM_NEG: Số lượng các biến có hệ số ước lượng là số âm.

.. csv-table:: Example of dataset RESULT
	:header: ID,MEAN_TRAIN_GINI,NUM_VAR,SELECT_VAR,	MEAN_VALID_GINI,NUM_NEG
	:align: center
	:widths: 15, 30, 20, 30, 30, 15
	
	 1,	20.37%,	1,	000000001,	16.47%,	0
	 2,	38.41%,	1,	000000010,	33.04%,	0
	 3,	46.44%,	2,	000000011,	41.18%,	0
	 4,	44.77%,	1,	000000100,	43.63%,	0
	 5,	50.64%,	2,	000000101,	47.49%,	0
	 ...,	...,	...,	...,	...,	...

  
  
Example
-------

Ví dụ chọn biến với metric là Gini của Kfold validation:

.. code:: sh

  %VARSELECT_ALL_COMBINE(DATA=DATA.TRAIN, VARLIST=X1 X2 X3 X4 X5 X6 X7 X8 X9 X10);

Ví dụ chọn biến với metric là Gini của Cross validation:

.. code:: sh

  %VARSELECT_ALL_COMBINE(DATA=DATA.TRAIN, VARLIST=X1 X2 X3 X4 X5 X6 X7 X8 X9 X10, METRIC=GINI_CROSS);

Ví dụ chọn biến với BATCH_SIZE=500

.. code:: sh

  %VARSELECT_ALL_COMBINE(DATA=DATA.TRAIN, VARLIST=X1 X2 X3 X4 X5 X6 X7 X8 X9 X10, METRIC=GINI_CROSS, BATCH_SIZE=500);
