.. _intro-overview:

==========
Giới thiệu
==========

Tổng quan
=========
Mô hình chấm điểm rủi ro tín dụng (Credit Risk Scoring, Credit risk scorecard) là công cụ được sử dụng từ rất lâu trong ngân hàng nhằm mục đích phân loại khác hàng tốt hay xấu. Ví dụ một  thẻ điểm hay được sử dụng là FICO score. Các ngân hàng cũng xây thẻ điểm tín dụng cho riêng ngân hàng mình. Với các khách hàng có điểm tín dụng cao, khách hàng sẽ được chấp nhận cấp khoản vay. Đối với các khác hàng có điểm tín dụng thấp, khách hàng sẽ bị từ chối cấp khoản vay.
Bảng sau đây minh hoa cho một một thẻ điểm tín dụng:

.. list-table:: Title
   :widths: 25 50 10
   :header-rows: 1
   
   * - Attribute
     - Range
     - Score
   * - Age
     - Age < 25
     - 17
   * - 
     - 25 <= Age < 30
     - 20
   * - 
     - 30 <= Age < 35
     - 25
   * - 
     - 35 <= Age < 40
     - 31
   * - 
     - 40 <= Age
     - 33
   * - Income
     - Income < 5,000,000
     - 30
   * - 
     - 5,000,000 <= Income < 10,000,000
     - 5
   * - 
     - 10,000,000 <= Income < 20,000,000
     - 20
   * - 
     - 20,000,000 <= Income < 35,000,000
     - 40
   * - 
     - 35,000,000 <= Income
     - 60   
   * - Gender
     - Male
     - 25
   * - 
     - Female
     - 30
     
Ví dụ một khách hàng có thông tin như sau:

- Tuổi:
- Thu nhập.
- Loan to value
- Hạn mức thẻ tín dụng (Total_lim_cc):

Giả sử chính sách của ngân hàng chỉ cho vay với khách hàng có 500 điểm trở lên thì khách hàng trong ví dụ sẽ bị từ chối cấp khoản vay. 
Cấu trúc của thẻ điểm tín dụng như sau:  Điểm tín dụng của khác hàng là tổng điểm của các yếu tố. Trong từng yếu tố lại chia ra thành các nhóm nhỏ (attribute). Cấu trúc này rất dễ hiểu và dễ sử dụng đối với đơn vị kinh doanh. Ví dụ từ bảng minh họa ta thấy:

- Với yếu tố tuổi, tuổi càng cao thì khách hàng có điểm tín dụng càng tốt.
- Khi so sánh giữa yếu tố tuổi và thu nhập. Có thể thấy rằng thu nhập có ảnh hưởng nhiều hơn tới điểm tín dụng của khách hàng.


Quy trình xây dựng Credit Scoring
=================================

In order to show you what Scrapy brings to the table, we'll walk you through an
example of a Scrapy Spider using the simplest way to run a spider.

