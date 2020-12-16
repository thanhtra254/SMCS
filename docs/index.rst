.. _topics-index:

===========================================
SAS Macros for Credit Scoring documentation
===========================================

**SAS Macros for Credit Scoring (SMCS)** là tập hợp các `Macro`_ được viết trên chương trình `SAS`_ với mục đích phục vụ việc xây dựng mô hình `CreditScorecard`_. Các Macro được viết cho các bước sau đây trong quá trình xây dựng mô hình:

* Chuẩn bị dữ liệu.
* Làm sạch dữ liệu & phân tích biến.
* Lựa chọn biến & hồi quy mô hình.
* Trình bày kết quả.

.. _SAS: https://www.sas.com/en_us/home.html
.. _Macro: https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=mcrolref&docsetTarget=p1nypovnwon4uyn159rst8pgzqrl.htm&locale=en
.. _CreditScorecard: https://en.wikipedia.org/wiki/Credit_scorecards
Getting help
============

Xử lý các vấn đề với macro:

* Liên hệ với tác giả thông qua email công việc: trant6@vpbank.com.vn.
* Liên hệ với Email cá nhân: thanhtra254@gmail.com
* Đặt câu hỏi trên trang web `SAS Communities`_.
* Report bugs with Scrapy in our `issue tracker`_.

.. _SAS Communities: https://communities.sas.com/
.. _issue tracker: https://github.com/thanhtra254/SMCS/issues



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
   
:doc:`post/DataAggregation`
    Các kỹ thuật cho việc trích xuất biến.

:doc:`post/DataPartition`
    Kỹ thuật chia dữ liệu thành train và validate theo phương pháp stratify sampling.

Variable Analysis
=================
.. toctree::
   :caption: Variable Analysis
   :hidden:
   
   post/VariableReview
   post/VariableAnalysis

:doc:`post/VariableReview`
    Tính toán các chỉ số thống kê (Max, mean, std, ...) và chỉ số dự báo (IV, Gini, ...) của biến để đưa ra cái nhìn tổng quan về dữ liệu
    
:doc:`post/VariableAnalysis`
    Binning và group các biến, sau đó tính toán chỉ số WoE.
    
    
Data transformation
===================
.. toctree::
   :caption: Data transformation
   :hidden:
   
   post/DataTransformartion

:doc:`post/DataTransformartion`
    Transform các biến ban đầu thành dạng WoE.
   
Variable Selection
==================
.. toctree::
   :caption: Variable Selection
   :hidden:
   
   post/SelectFoward
   post/SelectMarIV

:doc:`post/SelectFoward`
    Lựa chọn các biến sử dụng phương pháp Forward Selection. Các biến được lựa chọn tại mỗi bước được dựa trên hệ số Gini.
    
:doc:`post/SelectMarIV`
    Lựa chọn các biến sử dụng phương pháp Marginal Information Value.

Model Assessment
================
.. toctree::
   :caption: Model Assessment
   :hidden:
   
   post/ModelAssess
   
:doc:`post/ModelAssess`
    Tính toán các chỉ số đánh giá mô hình.
   
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
