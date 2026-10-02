# 📚 SachDung — Giải pháp Tiếp cận Sách Giáo Khoa Hợp Pháp

> **Giải pháp sáng tạo, hợp pháp và có khả năng áp dụng thực tế** nhằm hỗ trợ học sinh duy trì việc học trong thời gian chưa được cung ứng đầy đủ sách giáo khoa.

🌐 **Demo:** [sachdung.github.io](https://sachdung.github.io) *(cập nhật sau khi deploy)*

---

## 🔍 Bối cảnh & Vấn đề

Trong quá trình triển khai thống nhất hệ thống sách giáo khoa, nguồn cung chưa đáp ứng kịp nhu cầu tại nhiều địa phương. Học sinh bị gián đoạn học tập, phụ huynh lúng túng — và giải pháp "photocopy sách" tuy nhanh nhưng vi phạm Luật Sở hữu trí tuệ.

**SachDung** đề xuất hệ thống ba tầng giải pháp — phủ toàn bộ từ thành thị đến vùng không có điện, không có mạng.

---

## 💡 Giải pháp: Hệ thống Ba Tầng

### 🟢 Tầng 1 — Giải pháp Online
*Dành cho vùng có điện + Internet ổn định (thành thị)*

| Yếu tố | Chi tiết |
|---|---|
| Chi phí | **0đ / học sinh** |
| Triển khai | **24 giờ** |
| Cơ sở pháp lý | Bản quyền NXB GDVN, CC BY-NC-SA |

**Cách hoạt động:**
- Nhà trường đăng ký **mã truy cập tập thể** miễn phí với NXB Giáo dục VN
- Học sinh truy cập sách điện tử chính thức tại `hanhtrangso.nxbgd.vn`
- Bổ sung: VioEdu, Khan Academy tiếng Việt, kênh YouTube Bộ GD&ĐT
- Chia sẻ qua Zalo/nhóm lớp — không cần hạ tầng bổ sung

---

### 🟡 Tầng 2 — Thư viện bỏ túi (Offline)
*Dành cho vùng có điện, mạng yếu hoặc không có*

| Yếu tố | Chi tiết |
|---|---|
| Chi phí | **~40.000đ/USB** hoặc 800.000đ/trường (Raspberry Pi) |
| Triển khai | **3–5 ngày** |
| Cơ sở pháp lý | Giấy phép Creative Commons |

**Hai phương án:**

**A. USB Thư viện bỏ túi**
- USB 8GB (~40.000đ) chứa đủ tài liệu cả năm học
- Nội dung: CK-12, Wikipedia for Schools, PhET Simulations — tất cả CC
- Không cần internet sau khi tải; dùng được trên điện thoại/laptop cũ

**B. Mini Server Kolibri**
- Raspberry Pi (~800.000đ/trường) cài phần mềm Kolibri (mã nguồn mở)
- Tạo WiFi nội bộ bán kính 50m — học sinh kết nối bằng điện thoại cũ
- Không cần internet; chứa toàn bộ nội dung Creative Commons

---

### 🔴 Tầng 3 — Phi công nghệ
*Dành cho vùng không có điện, không có thiết bị số*

| Yếu tố | Chi tiết |
|---|---|
| Chi phí | **0đ** |
| Triển khai | **Ngay lập tức** |
| Cơ sở pháp lý | Điều 25 Luật SHTT VN + Quyền giảng dạy |

**Ba phương pháp:**

1. **Luân chuyển sách có kiểm soát**
   - 1 bộ sách gốc → lịch mượn theo ca trong lớp
   - Giáo viên soạn "Phiếu học tập bộ xương" — tóm tắt kiến thức trọng tâm mỗi bài
   - Học sinh không cần có sách liên tục

2. **Sơ đồ tư duy — Diễn giải lại kiến thức**
   - GV vẽ sơ đồ tư duy bài học lên bảng
   - HS chép sơ đồ (không sao chép nguyên văn) → tạo tài liệu cá nhân mới
   - Là sản phẩm sáng tạo mới — không vi phạm bản quyền

3. **Học nhóm tổng hợp**
   - Nhóm 4–6 học sinh dùng chung 1 cuốn sách
   - Mỗi em tóm tắt 1 chương bằng lời của mình → tập tài liệu cộng đồng
   - GV kiểm duyệt và nhân rộng trong lớp

---

## ⚖️ Cơ sở Pháp lý

| Hoạt động | Cơ sở pháp lý |
|---|---|
| Truy cập sách điện tử NXB | NXB GDVN cung cấp bản quyền truy cập miễn phí |
| Kolibri + Khan Academy + CK-12 | Giấy phép Creative Commons CC BY-NC-SA |
| Tóm tắt bài giảng bởi GV | Quyền sử dụng trong giảng dạy (Luật GD, Luật SHTT) |
| Sao chép 1 bản cá nhân | **Điều 25 Luật SHTT VN 2005 (sửa đổi 2022)** |
| Sơ đồ tư duy | Tác phẩm phái sinh — sản phẩm sáng tạo mới |

---

## 📊 So sánh với phương án Photocopy không phép

| Tiêu chí | SachDung | Photocopy không phép |
|---|---|---|
| Tuân thủ bản quyền | ✅ Hoàn toàn hợp pháp | ❌ Vi phạm Luật SHTT |
| Chi phí học sinh | ✅ 0đ (Tầng 1 & 3) | Phí in ấn mỗi học kỳ |
| Vùng không điện/mạng | ✅ Tầng 3 phủ sóng | ❌ Cần máy in, điện |
| Tốc độ triển khai | ✅ 24–48 giờ | Vài ngày |
| Rủi ro pháp lý | ✅ Không có | ❌ Có thể bị xử phạt |

---

## 🚀 Lộ trình Triển khai

```
Tuần 1:   Kích hoạt Tầng 1 + Tầng 3 trong 24–48 giờ
           → Đăng ký mã truy cập sách số với NXB
           → GV soạn Phiếu học tập bộ xương

Tuần 2:   Triển khai Tầng 2 cho vùng nông thôn
           → Sở GD cấp USB / cài Kolibri cho trường

Tuần 3–4: Đánh giá, thu thập phản hồi, điều chỉnh

Kết thúc: Khi sách chính thức về đầy đủ → dừng hệ thống tạm thời
           Lưu lại kinh nghiệm triển khai cho tương lai
```

---

## 🌟 Điểm nổi bật

- **Không ai bị bỏ lại**: 3 tầng phủ 100% học sinh — từ thành thị đến vùng không điện
- **Zero vi phạm bản quyền**: Mỗi phương án có cơ sở pháp lý cụ thể
- **Chi phí gần bằng 0**: Tận dụng tài nguyên sẵn có và mã nguồn mở
- **Triển khai trong 24–48 giờ**: Không cần đầu tư hạ tầng lớn
- **Giá trị lâu dài**: Thư viện USB và học nhóm tiếp tục hữu ích sau khủng hoảng

---

## 📁 Cấu trúc Repository

```
sachdung/
├── index.html        # Landing page giải pháp
└── README.md         # Tài liệu này
```

---

## 📬 Liên hệ

- **Email:** [Email của bạn]
- **GitHub:** [GitHub của bạn]

---

*SachDung — Giải pháp chuyển tiếp hợp pháp. Tuân thủ Luật SHTT VN 2005 (sửa đổi 2022) · Creative Commons.*
