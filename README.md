# Học Liệu Chuyển Tiếp (HocLieuChuyenTiep)

Giải pháp phân phối học liệu vi mô theo bài học qua mã QR nhằm hỗ trợ học sinh duy trì việc học trong giai đoạn chờ cung ứng sách giáo khoa chính thức.

---

## 1. Bối cảnh & Bài toán đặt ra

Trong những tuần đầu năm học, việc điều chỉnh và phân phối sách giáo khoa có thể gặp độ trễ cục bộ tại một số địa phương, khiến học sinh chưa có đủ tài liệu học tập. Phản ứng tự phát phổ biến là photocopy nguyên cuốn sách vừa gây tốn kém chi phí, vừa tiềm ẩn nguy cơ vi phạm quyền tác giả theo Luật Sở hữu trí tuệ.

**Học liệu chuyển tiếp** được thiết kế như một công cụ đệm ngắn hạn: thay vì nhân bản cả cuốn sách, giáo viên chỉ trích xuất đúng số trang cần thiết cho từng buổi học cụ thể và chia sẻ nhanh qua mã QR.

---

## 2. Quy trình vận hành

1. **Trích xuất vi mô:** Giáo viên tải tệp tài liệu PDF lên trình duyệt và chọn đúng khoảng trang cho tiết học ngày hôm đó (khoảng 2 – 4 trang).
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

## 4. Công nghệ sử dụng

* **Giao diện:** HTML5, CSS3 theo phong cách tối giản (Minimalism), thiết kế tối ưu cho màn hình TV và điện thoại.
* **Kết xuất PDF:** `PDF.js` (Mozilla) xử lý trực tiếp tệp PDF trên trình duyệt.
* **Mã QR:** `QRCode.js` sinh mã ma trận động theo từng buổi học.
* **Triển khai:** Tương thích với nền tảng máy chủ cục bộ hoặc lưu trữ đám mây tĩnh trên Vercel / GitHub Pages.

---

## 5. Hướng dẫn chạy thử nghiệm

### Chạy cục bộ trên máy tính:
Yêu cầu máy đã cài sẵn Python 3:

```bash
# 1. Di chuyển vào thư mục dự án
cd sachdung

# 2. Khởi chạy máy chủ cục bộ
python server.py

# 3. Mở trình duyệt truy cập: http://localhost:8080
```

