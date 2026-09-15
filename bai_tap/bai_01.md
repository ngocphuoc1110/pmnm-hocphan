# BÀI TẬP 1: TỔNG QUAN PHẦN MỀM TỰ DO VÀ MÃ NGUỒN MỞ

- **Họ và tên:** Hồ Ngọc Phước
- **Mã sinh viên:** 23T1020405
- **Lớp:** Phần mềm mã nguồn mở - Nhóm 1
- **Kho lưu trữ:** `pmnm-hocphan`
- **Đường dẫn file:** `bai_tap/bai_01.md`

---

## BÀI 1.1 — BẮT BUỘC

> *Lưu ý: Nội dung Bài 1.1 được cập nhật trực tiếp tại file `README.md` ở thư mục gốc của kho lưu trữ `pmnm-hocphan`.*

---

## BÀI 1.2 — BẮT BUỘC: PHÂN TÍCH DỰ ÁN RẼ NHÁNH DO MÂU THUẪN CỘNG ĐỒNG — OPENOFFICE VÀ LIBREOFFICE

### 1. Bối cảnh lịch sử và nguyên nhân mâu thuẫn
StarOffice ban đầu được phát triển bởi Sun Microsystems và sau đó được chuyển đổi thành dự án mã nguồn mở OpenOffice.org vào năm 2000. Dự án nhanh chóng trở thành bộ ứng dụng văn phòng mã nguồn mở phổ biến nhất, cung cấp giải pháp thay thế hoàn hảo cho Microsoft Office. Tuy nhiên, sự phụ thuộc quá lớn vào Sun Microsystems đã tạo ra tâm lý lo ngại trong cộng đồng nhà phát triển. Sun nắm giữ quyền quyết định tối cao về định hướng kỹ thuật, duy trì quy trình đóng góp mã nguồn phức tạp và yêu cầu thỏa thuận chuyển nhượng bản quyền (Copyright Assignment Agreement).

Bước ngoặt xảy ra vào năm 2010 khi Oracle Corporation thâu tóm Sun Microsystems. Trái ngược với kỳ vọng về sự hợp tác, Oracle thể hiện thái độ thờ ơ với cộng đồng, áp đặt cơ chế quản trị độc đoán và chậm trễ trong việc tiếp thu các đóng góp từ bên ngoài. Lo ngại về tương lai của OpenOffice.org và sự thương mại hóa thái quá từ phía Oracle, các thành viên chủ chốt trong cộng đồng phát triển cùng các tổ chức hỗ trợ đã quyết định tách ra để thành lập The Document Foundation (TDF) vào tháng 9 năm 2010.

### 2. Quá trình rẽ nhánh (Forking) và sự ra đời của LibreOffice
Nhận thấy Oracle không đồng ý chuyển giao thương hiệu "OpenOffice" cho một tổ chức độc lập, cộng đồng đã thực hiện rẽ nhánh (fork) mã nguồn OpenOffice.org để tạo ra một dự án mới mang tên LibreOffice. Mục tiêu chính của TDF là tạo ra một bộ ứng dụng văn phòng độc lập với nhà cung cấp (vendor-neutral), được quản trị bởi cộng đồng và hoàn toàn tự do.

Sau khi LibreOffice ra đời, Oracle quyết định ngừng phát triển OpenOffice.org thương mại và trao tặng mã nguồn cùng thương hiệu cho Apache Software Foundation (ASF) vào năm 2011, trở thành Apache OpenOffice. Tuy nhiên, do sự khác biệt về giấy phép sử dụng (Apache License 2.0 của ASF là giấy phép permissive, trong khi LibreOffice sử dụng LGPLv3/MPL mang tính copyleft bảo hộ), LibreOffice có thể tiếp thu mã nguồn từ Apache OpenOffice, nhưng chiều ngược lại thì không thể.

### 3. Hậu quả, bài học và tình trạng hiện tại
Sự rẽ nhánh này đã dẫn đến sự chuyển dịch hoàn toàn lực lượng phát triển và người dùng từ OpenOffice sang LibreOffice:
- **Sức sống kỹ thuật:** LibreOffice thu hút hàng trăm nhà phát triển tích cực, liên tục dọn dẹp mã nguồn cũ, tối ưu hóa hiệu năng, cải thiện khả năng tương thích với định dạng OOXML của Microsoft (.docx, .xlsx, .pptx) và duy trì chu kỳ phát hành định kỳ 6 tháng một lần.
- **Apache OpenOffice suy yếu:** Apache OpenOffice rơi vào tình trạng thiếu hụt nhân lực nghiêm trọng, việc sửa lỗi bảo mật diễn ra rất chậm và hầu như không có tính năng mới trong nhiều năm qua.

**Bài học rút ra:**
Một dự án mã nguồn mở thành công không chỉ dựa vào mã nguồn tốt mà còn phụ thuộc vào mô hình quản trị (governance model). Mâu thuẫn giữa lợi ích doanh nghiệp kiểm soát độc quyền và nguyện vọng đóng góp tự do của cộng đồng sẽ dẫn đến sự "rẽ nhánh" tự nhiên. LibreOffice là minh chứng điển hình cho sức mạnh của cộng đồng khi quyền tự quyết được trả về cho các nhà phát triển.

---

## BÀI 1.3 — TỰ CHỌN: "TRAGEDY OF THE COMMONS" TRONG PHẦN MỀM MÃ NGUỒN MỞ — NGHIÊN CỨU TRƯỜNG HỢP XZ-UTILS

### 1. Khái niệm "Tragedy of the Commons" trong bối cảnh Mã nguồn mở
Khái niệm "Bi kịch của tài sản chung" (Tragedy of the Commons) ban đầu mô tả hiện tượng kinh tế học khi một tài nguyên dùng chung bị khai thác quá mức bởi các cá nhân vì lợi ích riêng, dẫn đến sự sụp đổ của toàn hệ thống. Trong hệ sinh thái phần mềm mã nguồn mở (OSS), bi kịch này xuất hiện dưới hình thái: **sự mất cân bằng giữa mức độ tiêu thụ hạ tầng và mức độ đóng góp bảo trì.**

Hàng triệu doanh nghiệp và tập đoàn công nghệ toàn cầu xây dựng sản phẩm thương mại dựa trên hàng ngàn thư viện mã nguồn mở miễn phí. Các tổ chức này thu lợi nhuận lớn nhưng hầu như không tài trợ kinh phí hay nhân lực để duy trì các thành phần nền tảng đó. Hệ quả là công việc bảo trì các thư viện quan trọng bị đẩy lên vai một vài lập trình viên tình nguyện, làm việc không lương. Điều này dẫn đến tình trạng kiệt sức (burnout), thiếu hụt kiểm định an ninh và nguy cơ sụp đổ chuỗi cung ứng phần mềm.

---

### 2. Phân tích trường hợp cụ thể: Sự cố xz-utils (CVE-2024-3094)

#### Bối cảnh và thực trạng của dự án xz-utils
`xz-utils` (chứa thư viện cốt lõi `liblzma`) là bộ công cụ nén dữ liệu lossless được sử dụng trên hầu hết hệ điều hành Linux và Unix. Nó là thành phần phụ thuộc hạ tầng bắt buộc của nhiều gói phần mềm quan trọng, bao gồm dịch vụ OpenSSH (`sshd`) trên các bản phân phối như Debian, Ubuntu hay Fedora.

Dù giữ vai trò sống còn trong hạ tầng an ninh mạng, dự án `xz-utils` trong nhiều năm chỉ được bảo trì bởi một nhà phát triển duy nhất là Lasse Collin. Ông phải tự xử lý hàng ngàn báo cáo lỗi và yêu cầu tính năng mà không nhận được sự hỗ trợ tài chính hay nhân lực từ các tập đoàn lớn sử dụng phần mềm của mình.

#### Diễn biến bi kịch và đòn tấn công chuỗi cung ứng
Đến năm 2021, Lasse Collin rơi vào tình trạng kiệt sức do áp lực công việc và sức khỏe. Nhận thấy điểm yếu này, một tài khoản ẩn danh tên "Jia Tan" bắt đầu xuất hiện, tích cực đóng góp các bản sửa lỗi. Đồng thời, nhiều tài khoản ảo (sockpuppets) liên tục gửi email gây áp lực hối thúc Lasse Collin bàn giao quyền quản trị dự án cho người khác với lý do dự án cập nhật quá chậm.

Do quá mệt mỏi và thiếu người hỗ trợ, Lasse Collin đã cấp quyền commit và quản lý kho chứa cho Jia Tan. Sau khi giành được sự tin tưởng trong hai năm, vào đầu năm 2024, Jia Tan đã cài một mã độc cửa sau (backdoor) tinh vi vào các bản phát hành release tarball của `xz-utils` (phiên bản 5.6.0 và 5.6.1). Mã độc này can thiệp vào tiến trình xác thực của `sshd`, cho phép kẻ tấn công thực thi mã từ xa trên máy chủ Linux mà không cần mật khẩu.

Lỗ hổng nghiêm trọng CVE-2024-3094 được phát hiện kịp thời bởi kỹ sư Andres Freund nhờ nhận thấy sự sụt giảm hiệu năng bất thường (độ trễ 500ms), tránh được một thảm họa an ninh mạng toàn cầu.

---

### 3. Đề xuất cơ chế khắc phục và giải pháp bền vững

Sự cố `xz-utils` là hồi chuông cảnh báo đắt giá. Để khắc phục bi kịch này, cộng đồng công nghệ cần triển khai các giải pháp đồng bộ:

#### a. Cơ chế tài chính và tài trợ doanh nghiệp
Các doanh nghiệp thụ hưởng từ mã nguồn mở phải coi việc đóng góp tài chính cho các thư viện phụ thuộc là trách nhiệm bắt buộc.
- **Quỹ tài trợ tập trung:** Mở rộng đóng góp vào các quỹ như Sovereign Tech Fund, Open Source Security Foundation (OpenSSF) hoặc GitHub Sponsors để trả lương cho nhà bảo trì dự án hạ tầng.
- **Phân bổ theo SBOM:** Trích tỷ lệ phần trăm ngân sách CNTT của doanh nghiệp phân bổ cho các dự án nguồn mở dựa trên danh mục phụ thuộc (Software Bill of Materials).

#### b. Mô hình Quản trị và Xây dựng Đội ngũ
- **Cơ chế đồng quản trị (Co-maintainership):** Loại bỏ rủi ro nhà bảo trì duy nhất. Các tổ chức như Linux Foundation nên phân công kỹ sư toàn thời gian hỗ trợ kiểm duyệt mã (code review) và quản lý phát hành cho các dự án cốt lõi.
- **Xác minh danh tính:** Thiết lập quy trình kiểm tra danh tính (KYC) cho các nhà bảo trì mới trước khi cấp quyền commit nhạy cảm.

#### c. Tự động hóa và Đảm bảo An ninh chuỗi cung ứng
- **Xác thực xây dựng nguồn mở (SLSA & Reproducible Builds):** Đảm bảo mã nguồn phát hành khớp chính xác với kho mã nguồn công khai, ngăn chặn việc chèn mã độc vào file nén release.
- **Giám sát sức khỏe dự án:** Sử dụng công cụ theo dõi tự động để cảnh báo các dự án hạ tầng chỉ có 1 maintainer hoặc có dấu hiệu quá tải.

---

### 4. Kết luận
Bi kịch của tài sản chung trong mã nguồn mở không thể giải quyết bằng thiện chí đơn thuần. Nó đòi hỏi sự thay đổi tư duy toàn diện từ các tập đoàn công nghệ: chuyển từ "khai thác miễn phí" sang "trách nhiệm đồng sở hữu", đảm bảo một hệ sinh thái an toàn và bền vững.
