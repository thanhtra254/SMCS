.. _topics-index:

.. image:: ./logo/SMCS_Logo_Big.png
   :align: center
   :width: 600
   



===========================================
SAS Macros for Credit Scoring documentation
===========================================

**SAS Macros for Credit Scoring (SMCS)** là tập hợp các `Macro`_ được viết trên chương trình `SAS`_ với mục đích phục vụ việc xây dựng mô hình `Credit Scorecard <https://en.wikipedia.org/wiki/Credit_scorecards>`_. Các Macro được viết cho các bước sau đây trong quá trình xây dựng mô hình:

* Chuẩn bị dữ liệu.
* Làm sạch dữ liệu & phân tích biến.
* Lựa chọn biến & hồi quy mô hình.
* Trình bày kết quả.

.. _SAS: https://www.sas.com/en_us/home.html
.. _Macro: https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=mcrolref&docsetTarget=p1nypovnwon4uyn159rst8pgzqrl.htm&locale=en

Getting help
============

Xử lý các vấn đề với macro:

* Liên hệ với tác giả qua email công việc: trant6@vpbank.com.vn.
* Liên hệ với tác giả qua email cá nhân: thanhtra254@gmail.com
* Đặt câu hỏi trên trang web `SAS Communities`_.
* Phản hồi các lỗi lên trang `issue tracker`_.

.. _SAS Communities: https://communities.sas.com/
.. _issue tracker: https://github.com/thanhtra254/SMCS/issues
 
Một số mẹo sử dụng:

* Dùng công cụ search để tìm các nội dung.

.. image:: ./logo/Search.png
   :align: center
   :width: 300
   
* Export tài liệu thành văn bản PDF/Html/Epub: Click vào cuối trang và chọn nội dung tương ứng.
.. image:: ./logo/Export.png
   :align: center
   :width: 300


First steps
===========

.. toctree::
   :caption: First steps
   :hidden:

   intro/overview
   intro/install
   intro/examples

:doc:`intro/overview`
    Giới thiệu về Credit Scoring và các bước xây dựng mô hình Credit Scoring.

:doc:`intro/install`
    Cài đặt các macro SAS trên máy tính để xây dựng mô hình.

:doc:`intro/examples`
    Học cách sử dụng Macro và xây dựng mô hình với dữ liệu đơn giản.
	
	
Data preparation
================
.. toctree::
   :caption: Data preparation
   :hidden:
   
   post/DataAggregation
   post/DataPartition
   post/DataReduceSize
   
:doc:`post/DataAggregation`
    Các kỹ thuật cho việc trích xuất biến.

:doc:`post/DataPartition`
    Kỹ thuật chia dữ liệu thành train và validate theo phương pháp stratify sampling.

:doc:`post/DataReduceSize`
    Giảm kích thước của dữ liệu để hiệu năng tính toán trên file cao hơn.
    
    
Variable Analysis
=================
.. toctree::
   :caption: Variable Analysis
   :hidden:
   
   post/VariableReview
   post/VariableAnalysis
   post/VariableInteaction
   post/VariableTransformation

:doc:`post/VariableReview`
    Tính toán các chỉ số thống kê (Max, mean, std, ...) và chỉ số dự báo (IV, Gini, ...) của biến để đưa ra cái nhìn tổng quan về dữ liệu
    
:doc:`post/VariableAnalysis`
    Binning và group các biến, sau đó tính toán chỉ số WoE.
   
:doc:`post/VariableInteaction`
    Variable Interaction: Các phát hiện và phân tích interactive giữa các biến.
    
:doc:`post/VariableTransformation`
   Transform các biến ban đầu thành dạng WoE.   


Variable Selection
==================
.. toctree::
   :caption: Variable Selection
   :hidden:
   
   post/SelectOverview
   post/SelectFoward
   post/SelectMarIV
   post/SelectBestSubset
   
   
:doc:`post/SelectOverview`
    Tổng quan về lựa chọn biến và các phương pháp lựa chọn biến.
    
:doc:`post/SelectFoward`
    Lựa chọn các biến sử dụng phương pháp Forward Selection. Các biến được lựa chọn tại mỗi bước được dựa trên hệ số Gini.
    
:doc:`post/SelectMarIV`
    Lựa chọn các biến sử dụng phương pháp Marginal Information Value.
    
:doc:`post/SelectBestSubset`
    Lựa chọn các biến bằng cách thử tất cả các tổ hợp biến.

Model Assessment
================
.. toctree::
   :caption: Model Assessment
   :hidden:
   
   post/ModelAssess
   post/ModelCrossValidation
   
:doc:`post/ModelAssess`
    Tính toán các chỉ số đánh giá mô hình.
:doc:`post/ModelCrossValidation`
    Đánh giá mô hình bằng các phương pháp: cross validation, f-fold validation và boostraping validation.
   
Report Scorecard
================
.. toctree::
   :caption: Report Scorecard
   :hidden:
   
   post/ReportVariable
   post/ReportScorecard
   
:doc:`post/ReportVariable`
    Trình bày kết quả binning các biến.

:doc:`post/ReportScorecard`
    Trình bày kết quả mô hình và định dạng Scorecard.
    
    
Monitoring
==========
.. toctree::
   :caption: Monitoring
   :hidden:
   
   post/MoniStability
   post/MoniDiscriminatory
   post/MoniAccuracy
   
:doc:`post/MoniStability`
    Các hậu kiểm về tính ổn định của mô hình.

:doc:`post/MoniDiscriminatory`
    Các kết quả hậu kiểm về tính phân biệt của mô hình. Nội dung bao gồm Gini, KS của score và Gini, IV của từng biến.
    
:doc:`post/MoniAccuracy`
    Các kết quả hậu kiểm về tính chính xác của mô hình.
