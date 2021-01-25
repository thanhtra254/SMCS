.. _post-model_assess-accuracy:

===============================
Model Scoring
===============================

Model scoring là công việc chấm điểm (tính toán output) cho dữ liệu liệu mới sử dụng kết quả của mô hình đã xây dựng. Các bước tính toán khi chấm điểm như sau:

#. Dữ liệu đầu vào (data score) cần chứa đầy đủ các biến của mô hình.
#. Từ kết quả binning từ trước (kết quả mapping), tính toán các biến dưới dạng group và woe tương ứng với mỗi biến.
#. Tính score bằng công thức 

.. math::
  IV=\sum_{i=0}^n WoeX_i \times \beta_i

trong đó :math:`\WoeX_0 =1` và  :math:`\beta_i` là hệ số chặn (intercept). Các biến dưới dạng WOE :math:`WoeX_1, WoeX_2, ..., WoeX_n` và hệ số tương ứng :math:`\beta_1, \beta_2, ..., \beta_n`.

Sử dụng Macro
=============


Cú pháp
-------

Cú pháp của Macro như sau:

.. code:: sas
  
  %MODEL_SCORING(DS_SCORE, DS_OUT, DS_MAPPING, DS_PARAM, VARLIST);

Trong đó:

- **DS_SCORE (dataset)** là dữ liệu cần chấm điểm.

- **DS_OUT (dataset)** là dữ liệu đầu ra. Dữ liệu đầu ra sẽ chứa các biến trong **VARLIST**, các biến dạng Group, WOE và Score. 

- **DS_MAPPING (dataset)** là dữ liệu lưu thông tin mapping của cả dạng Group và WoE. Dữ liệu là kết quả đầu ra của Macro `Variable Transformation <https://smcs.readthedocs.io/vi/latest/post/VariableTransformation.html>`_.

.. csv-table:: Example of dataset DS_MAPPING
	:header: FMTNAME, START, END, LABEL, TYPE, SEXCL, EEXCL, HLO
	:align: center
	
	X2F,	.,	        .,		"[01] MISSING",			N,	N,	N,	
	X2F,	LOW,	        -0.9841,	"[02] (-INF, -0.9841]",		N,	N,	N,	L
	X2F,	-0.9841,        -0.8588,	"[03] (-0.9841, -0.8588]",	N,	Y,	N,	
	X2F,	-0.8588,        -0.5849,	"[04] (-0.8588, -0.5849]",	N,	Y,	N,	
	X2F,	-0.5849,        -0.0563,	"[05] (-0.5849, -0.0563]",	N,	Y,	N,	
	X2F,	-0.0563,	0.9544,		"[06] (-0.0563, 0.9544]",	N,	Y,	N,	
	X2F,	0.9544,		HIGH,		"[07] (0.9544 , +INF)",		N,	Y,	N,	H
  
- **DS_PARAM (dataset)** là dữ liệu lưu thông tin các hệ số. Dữ liệu là kết quả đầu ra của Macro Dữ liệu là kết quả đầu ra của Macro `Model Regression <https://smcs.readthedocs.io/vi/latest/post/ModelRegression.html>`_. Ví dụ về dữ liệu như dưới đây:

.. csv-table:: Example of dataset DS_PARAM
	:header: "_NAME_",	"_TYPE_",	"Intercept", 	WOE_X1,	WOE_X2,	WOE_X3,	WOE_X4,	WOE_X5,	WOE_X6,	WOE_X8
	:align: center
	
	Estimate,	PARMS,	0.01675,	0.9202,	0.7971,	0.8608,	0.8727,	0.9028,	0.1408,	0.06968,

- **VARLIST (danh sách biến)** là danh sách các biến trong mô hình.

Detail
------

Output
------

Kết quả đầu ra của macro là **DS_OUT (dataset)** chứa các biến trong **VARLIST**, các biến dạng Group, WOE và Score. 

Example
-------

Ví dụ về cách sử dụng Macro

.. code:: sas

  %MODEL_SCORING(DS_MAPPING=DATA.TRAIN_MAPPING,
    DS_PARAM=DATA.MODEL_REG_PARAM,
    DS_SCORE=DATA.OUTTIME,
    DS_OUT=DS_OUT,
    VARLIST=X1 X2 X3 X4 X5  X6 X8)
