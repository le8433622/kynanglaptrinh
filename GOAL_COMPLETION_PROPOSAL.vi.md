# Đề xuất để hoàn thành mục tiêu

Tài liệu này trả lời trực tiếp câu hỏi: **"bạn đề xuất điều gì để hoàn thành mục tiêu"** cho bộ khung *Fullstack Engineer Skill Builder*.


## 0) Mục tiêu chiến lược (theo yêu cầu mới)

Skill này được thiết kế cho **lập trình viên dùng AI** và team product nhỏ/vừa.

Mục tiêu là:
- Giảm tối đa giới hạn thường gặp của AI khi lập trình (đoán sai yêu cầu, bịa dependency, thiếu test, bỏ qua bảo mật).
- Biến quy trình làm việc thành chuẩn giống một **công ty phần mềm chuyên nghiệp**.
- Có thể dùng framework này để triển khai đa dạng sản phẩm thương mại (SaaS, internal tools, marketplace, e-commerce, CRM...).

Nguyên tắc thực thi để “fix giới hạn AI”:
1. AI chỉ là người soạn thảo đầu tiên, không phải nguồn sự thật cuối cùng.
2. Mọi quyết định kỹ thuật phải đi qua gate: business rule → contract → test → review.
3. Không có test thì không merge; không có rollback plan thì không deploy.

## 1) Mục tiêu cần chốt lại (đầu vào bắt buộc)
Trước khi code, cần điền đủ 4 thông tin sau:

- **Current task**: xây tính năng gì (kết quả kinh doanh cụ thể).
- **Current skill level**: Beginner / Intermediate / Advanced.
- **Stack preference**: đã có stack hay để hệ thống đề xuất.
- **Constraint**: thời gian, ngân sách, quy mô team, môi trường deploy.

> Nếu thiếu 1 trong 4 mục trên, dừng và làm rõ trước.

## 2) Đề xuất thực thi theo 2 nhịp

### Nhịp A — Foundation (1-2 ngày)
Mục tiêu: khóa phạm vi, không cho phép “code trước, nghĩ sau”.

1. Chốt **business rules** (ai được làm gì, bị cấm gì, điều kiện thành công/thất bại).
2. Chốt **kiến trúc tối thiểu có ích** (frontend/backend/db/auth/deploy).
3. Chốt **schema + API contract + shared types**.
4. Tạo skeleton repo: lint, formatter, test runner, CI cơ bản.

**Definition of Done (Nhịp A)**
- Có tài liệu business rules + API contract + auth flow.
- Có test scaffold chạy được trong CI.
- Không có dependency “mơ hồ” (phải pin version).

### Nhịp B — Delivery theo layer (3-5 ngày cho MVP nhỏ)
Mục tiêu: build theo thứ tự bắt buộc, mỗi layer phải chạy được trước khi qua layer kế tiếp.

1. **Layer 1**: DB + migration.
2. **Layer 2**: business logic thuần (pure function).
3. **Layer 3**: API mỏng (translate HTTP ↔ logic).
4. **Layer 4**: Frontend gọi API thật (không mock).
5. **Layer 5**: loading/error/edge case.

**Definition of Done (Nhịp B)**
- Mỗi feature có: 1 happy path + 2 edge cases + 1 security test.
- Có phân trang cho endpoint list.
- Không nuốt exception, không log dữ liệu nhạy cảm.

## 3) Bộ câu hỏi cần bạn trả lời ngay để bắt đầu
Để vào Phase 1 đúng chuẩn, vui lòng trả lời ngắn gọn:

1. Mục tiêu kinh doanh của feature đầu tiên là gì?
2. User chính là ai? Họ bị cấm thao tác nào?
3. Nếu hệ thống fail, tác động tệ nhất là gì?
4. Hệ thống hiện tại cần tích hợp gồm những gì?
5. Deadline MVP chính xác theo ngày nào?

## 4) Rủi ro lớn nhất và cách chặn

- **Rủi ro 1: Trôi phạm vi** → chặn bằng business rules + acceptance criteria đóng băng theo sprint.
- **Rủi ro 2: Build sai thứ tự** → chặn bằng gate theo layer, chưa pass test không qua layer mới.
- **Rủi ro 3: Thiếu bảo mật** → bắt buộc security test cho từng feature ngay từ đầu.
- **Rủi ro 4: Nợ kỹ thuật sớm** → bắt buộc review checklist (security/correctness/performance/maintainability).
- **Rủi ro 5: AI bịa thông tin kỹ thuật** → buộc verify package/docs chính thức trước khi dùng.
- **Rủi ro 6: AI bỏ sót yêu cầu nghiệp vụ** → review business rules với stakeholder trước khi code.

## 5) Đề xuất “minimum useful version”
MVP nên chỉ gồm:

- 1 luồng nghiệp vụ cốt lõi end-to-end.
- 1 role người dùng.
- 1 dashboard/1 màn hình chính.
- logging + health check + rollback notes.

Không thêm tính năng ngoài luồng cốt lõi trước khi đạt **Level 2 (Structural)**.

## 6) Cách chúng ta làm việc tiếp theo

- Bạn gửi 4 đầu vào ở mục (1).
- Tôi sẽ trả lại ngay **Phase 1 hoàn chỉnh** + đề xuất kiến trúc cụ thể.
- Sau đó mới bước sang Phase 2 và bắt đầu xây layer 1.


## 7) Thu thập ý kiến cộng đồng theo quy trình chuẩn

Để tiệm cận mục tiêu “hoàn hảo”, cần thu thập ý kiến theo vòng lặp thay vì cảm tính:

1. Thu thập từ nhiều kênh: GitHub/Reddit/Hacker News/Discord + retrospective nội bộ.
2. Chuẩn hóa dữ liệu theo mẫu `feedback/FEEDBACK_LOG_TEMPLATE.md`.
3. Ưu tiên bằng công thức điểm (severity x frequency x impact) / effort.
4. Chỉ nhận thay đổi khi có bằng chứng tái hiện được và test đi kèm.
5. Phát hành bản cập nhật định kỳ + changelog + metric trước/sau.

Chi tiết xem `COMMUNITY_PERFECTING_LOOP.md`.


## 8) Kết luận thiếu sót sau mỗi task (bắt buộc)

Sau mỗi task, phải có block kết luận thiếu sót với 6 trường:
- Missing
- Root cause
- Risk
- Action
- Owner
- Deadline

Không có block này thì task chưa được coi là hoàn tất.
