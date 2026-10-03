# Học Liệu Chuyển Tiếp

Giải pháp phân phối học liệu vi mô theo bài học qua mã QR nhằm hỗ trợ học sinh duy trì việc học trong giai đoạn chờ cung ứng sách giáo khoa chính thức.

---

## 1. Bối cảnh & Vấn đề đặt ra

Trong những tuần đầu năm học, việc điều chỉnh và phân phối sách giáo khoa có thể gặp độ trễ cục bộ tại một số địa phương, khiến học sinh chưa có đủ tài liệu học tập. Phản ứng tự phát phổ biến là photocopy nguyên cuốn sách vừa gây tốn kém chi phí, vừa tiềm ẩn nguy cơ vi phạm quyền tác giả theo Luật Sở hữu trí tuệ.

**Học liệu chuyển tiếp** được thiết kế như một công cụ đệm ngắn hạn: thay vì nhân bản cả cuốn sách, giáo viên chỉ trích xuất đúng số trang cần thiết cho từng buổi học cụ thể và chia sẻ nhanh qua mã QR.

---

## 2. Quy trình vận hành

1. **Trích xuất học liệu:** Giáo viên tải tệp tài liệu PDF lên trình duyệt và chọn đúng khoảng trang cho tiết học ngày hôm đó (khoảng 4 - 6 trang).
2. **Sinh mã QR trình chiếu:** Hệ thống tự động lưu các trang đã chọn và sinh mã QR độ nét cao để giáo viên chiếu lên màn hình TV hoặc máy chiếu của lớp.
3. **Tiếp cận bình đẳng:**
   - **Học sinh có thiết bị:** Bật camera quét mã QR để mở trực tiếp nội dung bài học trên trình duyệt di động mà không cần đăng ký tài khoản hay cài đặt phần mềm.
   - **Học sinh không có thiết bị:** Nhận bản in A4 của các trang trích xuất (hệ thống tích hợp sẵn nút in chuẩn A4) hoặc dùng chung sách tại tủ sách lớp học.
4. **Kết thúc chuyển tiếp:** Khi sách giáo khoa chính thức được phát về tay học sinh, lớp học quay lại sử dụng sách giấy bình thường.

---

## 3. Cơ sở pháp lý

Dự án vận dụng đúng quy định tại **Khoản 1 Điều 25 Luật Sở hữu trí tuệ Việt Nam (sửa đổi, bổ sung 2022)** về các trường hợp ngoại lệ không xâm phạm quyền tác giả:
* Chỉ trích dẫn một phần nhỏ tác phẩm (thường dưới 3% dung lượng sách) phục vụ trực tiếp cho mục đích giảng dạy trong lớp học.
* Hoàn toàn phi thương mại, không thu phí học sinh và phụ huynh.
* Không làm phương hại đến việc khai thác bình thường hay quyền lợi kinh tế của Nhà xuất bản.

---

## 4. Hướng dẫn chạy thử nghiệm

### a) Chạy cục bộ trên máy tính:
Yêu cầu máy đã cài sẵn Python 3:

```bash
# 1. Di chuyển vào thư mục dự án
cd sachdung

# 2. Khởi chạy máy chủ cục bộ
python server.py

# 3. Mở trình duyệt truy cập: http://localhost:8080
```
### b) Truy cập vào web [hoclieuchuyentiep.vercel.app](https://hoclieuchuyentiep.vercel.app) để sử dụng

## ⚠️ Hạn chế Kỹ thuật & Lưu ý quan trọng (Disclaimer)

Sản phẩm hiện đang ở giai đoạn **Prototype** nhằm mục đích kiểm chứng giải pháp chuyển tiếp học liệu. Dưới đây là các hạn chế kỹ thuật và lưu ý cần cân nhắc trước khi vận hành thực tế:

### a) Hạn chế về mặt Kỹ thuật & Hiệu năng
* **Giới hạn dung lượng file PDF:** Việc xử lý và trích xuất trang từ các file PDF sách giáo khoa dung lượng lớn (trên 100MB) có thể bị chậm, giật/lag hoặc chạm ngưỡng timeout/memory limit của Vercel Serverless Functions.
* **Lưu trữ dữ liệu có thời hạn:** Các liên kết tài liệu/mã QR tạo ra từ bản Demo hiện chỉ đóng vai trò truy xuất tạm thời, chưa được tích hợp hệ thống lưu trữ đám mây (Cloud Storage) và cơ sở dữ liệu chuyên dụng để đảm bảo duy trì liên kết lâu dài.
* **Độ tương thích thiết bị:** Trải nghiệm xem file và quét mã QR có thể gặp một số lỗi hiển thị nhỏ khi mở bằng các trình duyệt tích hợp (In-app Browser) như Zalo, Facebook, Messenger trên các thiết bị di động đời cũ.

### b) Trách nhiệm Pháp lý & Bản quyền
* **Phạm vi công cụ:** Ứng dụng chỉ đóng vai trò là công cụ kỹ thuật hỗ trợ giáo viên trích xuất nhanh tài liệu. Người sử dụng công cụ chịu trách nhiệm tự bảo đảm nội dung file PDF tải lên tuân thủ đúng giới hạn cho phép của **Luật Sở hữu trí tuệ** (ví dụ: chỉ trích xuất trọn vẹn 4 - 6 trang/tiết học phục vụ giảng dạy nội bộ phi thương mại theo Khoản 1 Điều 25).
* **Mục đích sử dụng:** Mọi mã QR và học liệu sinh ra từ hệ thống chỉ phục vụ mục đích học tập chuyển tiếp trong thời gian chờ sách giáo khoa chính thức, không lưu hành vì mục đích thương mại hay chia sẻ công khai quy mô lớn.

### c) Trạng thái Sản phẩm
* **Chưa phải bản chính thức:** Website [hoclieuchuyentiep.vercel.app](https://hoclieuchuyentiep.vercel.app) chưa cam kết về độ sẵn sàng, khả năng chịu tải đồng thời lớn cũng như các tiêu chuẩn bảo mật chuyên sâu.
