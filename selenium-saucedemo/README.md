# Selenium SauceDemo Testing

## 1. Giới thiệu dự án

Dự án **Selenium SauceDemo Testing** được xây dựng nhằm thực hành kiểm thử tự động giao diện website bằng Python, Selenium WebDriver và Pytest.

Website được sử dụng để kiểm thử là [SauceDemo](https://www.saucedemo.com/), một website mẫu hỗ trợ thực hành kiểm thử phần mềm.

Dự án tập trung kiểm tra các chức năng cơ bản như đăng nhập, hiển thị danh sách sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất.

- **Tên dự án:** Selenium SauceDemo Testing
- **Ngôn ngữ lập trình:** Python
- **Công cụ tự động hóa:** Selenium WebDriver
- **Framework kiểm thử:** Pytest
- **Website kiểm thử:** https://www.saucedemo.com/
- **Repository GitHub:** https://github.com/Duong465fds/selenium-saucedemo-testing

## 2. Mục tiêu

- Tìm hiểu quy trình kiểm thử tự động giao diện website.
- Sử dụng Selenium WebDriver để tự động hóa các thao tác trên trình duyệt.
- Sử dụng Pytest để tổ chức và thực thi các test case.
- Kiểm tra kết quả thực tế với kết quả mong đợi.
- Ghi nhận kết quả kiểm thử và chuẩn bị minh chứng phục vụ báo cáo.

## 3. Công nghệ sử dụng

| Công nghệ | Mục đích |
|---|---|
| Python 3.11 | Ngôn ngữ viết kịch bản kiểm thử |
| Selenium WebDriver | Tự động hóa thao tác trên trình duyệt |
| Pytest | Thực thi và quản lý các test case |
| Google Chrome | Trình duyệt kiểm thử |
| pip | Cài đặt các thư viện Python |
| GitHub | Lưu trữ mã nguồn và báo cáo dự án |

## 4. Các chức năng được kiểm thử

Dự án bao gồm 5 test case chính.

| STT | Mã test case | Chức năng | Kết quả mong đợi |
|---|---|---|---|
| 1 | TC01 | Đăng nhập bằng thông tin hợp lệ | Đăng nhập thành công và chuyển đến trang sản phẩm |
| 2 | TC02 | Đăng nhập bằng mật khẩu không hợp lệ | Hệ thống từ chối đăng nhập và hiển thị thông báo lỗi |
| 3 | TC03 | Hiển thị danh sách sản phẩm | Danh sách sản phẩm được hiển thị |
| 4 | TC04 | Thêm sản phẩm vào giỏ hàng | Sản phẩm được thêm vào giỏ hàng |
| 5 | TC05 | Đăng xuất tài khoản | Người dùng được chuyển về trang đăng nhập |

**Lưu ý:** Kết quả mong đợi được mô tả theo mục tiêu của từng test case. Kết quả thực tế được xác định thông qua các assertion trong mã kiểm thử.

## 5. Cấu trúc thư mục

Cấu trúc chính của dự án:

```text
selenium-saucedemo/
├── .venv/
├── tests/
│   └── test_saucedemo.py
├── requirements.txt
├── pytest.ini
└── README.md
```

Giải thích:

- `tests/test_saucedemo.py`: Chứa các test case Selenium.
- `requirements.txt`: Danh sách thư viện cần cài đặt.
- `pytest.ini`: Cấu hình thực thi Pytest.
- `README.md`: Tài liệu hướng dẫn sử dụng dự án.
- `.venv/`: Môi trường Python ảo trên máy cá nhân, không cần đưa lên GitHub.

## 6. Yêu cầu môi trường

Để chạy dự án, cần chuẩn bị:

- Windows 10 hoặc Windows 11.
- Python 3.11 hoặc phiên bản tương thích.
- Google Chrome.
- Git nếu muốn tải dự án bằng lệnh clone.
- Kết nối Internet để tải thư viện và truy cập website kiểm thử.

Kiểm tra phiên bản Python:

```powershell
python --version
```

Kiểm tra phiên bản Git:

```powershell
git --version
```

## 7. Hướng dẫn cài đặt

### Bước 1: Tải dự án

Mở PowerShell và chạy:

```powershell
git clone https://github.com/Duong465fds/selenium-saucedemo-testing.git
```

Di chuyển vào thư mục dự án:

```powershell
cd selenium-saucedemo-testing/selenium-saucedemo
```

Nếu đã tải dự án về máy, chỉ cần mở PowerShell tại thư mục `selenium-saucedemo`.

### Bước 2: Tạo môi trường ảo

```powershell
python -m venv .venv
```

Môi trường ảo giúp tách biệt các thư viện của dự án với môi trường Python chung trên máy tính.

### Bước 3: Cài đặt thư viện

Chạy lệnh:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
```

Sau đó cài đặt các thư viện trong `requirements.txt`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Các thư viện chính bao gồm Selenium và Pytest. Những thư viện phụ thuộc sẽ được pip tự động cài đặt.

### Bước 4: Chạy kiểm thử

Thực thi toàn bộ test case bằng lệnh:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Trong đó:

- `python.exe`: Sử dụng Python trong môi trường ảo của dự án.
- `-m pytest`: Chạy Pytest.
- `-v`: Hiển thị chi tiết từng test case.

## 8. Kết quả kiểm thử

Sau khi cài đặt thư viện thành công, dự án đã được chạy kiểm thử bằng Pytest.

Kết quả ghi nhận ở lần chạy gần nhất:

```text
tests/test_saucedemo.py::test_tc01_login_with_valid_credentials PASSED
tests/test_saucedemo.py::test_tc02_login_with_invalid_password PASSED
tests/test_saucedemo.py::test_tc03_products_list_is_displayed PASSED
tests/test_saucedemo.py::test_tc04_add_product_to_cart PASSED
tests/test_saucedemo.py::test_tc05_logout PASSED

========================= 5 passed in 23.07s =========================
```

### Bảng tổng hợp kết quả

| Chỉ số | Kết quả |
|---|---:|
| Tổng số test case | 5 |
| Số test case thành công | 5 |
| Số test case thất bại | 0 |
| Tỷ lệ thành công | 100% |
| Thời gian chạy lần gần nhất | 23,07 giây |

### Đánh giá kết quả

Tất cả 5 test case đều đạt trạng thái `PASSED` trong lần chạy gần nhất.

Điều này cho thấy các kiểm tra và assertion được thực hiện trong bộ test đều đạt yêu cầu ở lần chạy đó.

Đối với TC02, trạng thái `PASSED` có nghĩa là chương trình xác nhận đúng hành vi mong đợi khi đăng nhập bằng mật khẩu không hợp lệ, không có nghĩa là đăng nhập bằng mật khẩu sai thành công.

Kết quả này xác nhận bộ kiểm thử cơ bản hoạt động thành công. Tuy nhiên, vẫn cần bổ sung thêm test case nếu muốn đánh giá toàn diện hơn các chức năng của website.

## 9. Ảnh minh chứng

Để hoàn thiện báo cáo, nên bổ sung ảnh chụp màn hình kết quả thực tế sau khi chạy lệnh:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Có thể tạo thư mục lưu ảnh như sau:

```text
selenium-saucedemo/
└── screenshots/
    └── pytest-results.png
```

Sau khi chụp ảnh và tải tệp `pytest-results.png` lên GitHub tại đúng đường dẫn, thêm đoạn Markdown sau vào README:

```markdown
![Kết quả chạy kiểm thử Selenium và Pytest](screenshots/pytest-results.png)
```

**Lưu ý:** Chỉ thêm đường dẫn ảnh sau khi ảnh đã được tải lên repository. Ảnh minh chứng phải là ảnh chụp kết quả thực tế từ terminal.

## 10. Xử lý một số vấn đề thường gặp

### 10.1. Không tìm thấy Python

Kiểm tra Python đã được cài đặt và thêm vào PATH chưa:

```powershell
python --version
```

Nếu lệnh không hoạt động, hãy kiểm tra lại quá trình cài đặt Python.

### 10.2. Không cài đặt được thư viện

Chạy lại lệnh cài đặt:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Nếu gặp lỗi, hãy kiểm tra thông báo lỗi cuối cùng trong terminal và kết nối Internet.

### 10.3. Xuất hiện cảnh báo cache của pip

Một số cảnh báo như `Cache entry deserialization failed` có thể liên quan đến dữ liệu cache của pip.

Trong lần chạy dự án này, các thư viện đã được cài đặt thành công và Pytest thực thi bình thường. Vì vậy, không cần xử lý cảnh báo này nếu không phát sinh lỗi cài đặt thực tế.

### 10.4. Selenium không mở được trình duyệt

- Kiểm tra Google Chrome đã được cài đặt.
- Kiểm tra kết nối Internet.
- Kiểm tra thông báo lỗi Selenium để xác định nguyên nhân.
- Chạy lại test case sau khi khắc phục vấn đề.

## 11. Hướng phát triển

Trong tương lai, dự án có thể được mở rộng với các nội dung:

- Kiểm thử xóa sản phẩm khỏi giỏ hàng.
- Kiểm thử sắp xếp sản phẩm theo giá hoặc tên.
- Kiểm thử quy trình thanh toán.
- Kiểm thử dữ liệu đầu vào không hợp lệ.
- Bổ sung ảnh chụp màn hình khi test thành công hoặc thất bại.
- Tạo báo cáo HTML bằng Pytest.
- Tích hợp GitHub Actions để tự động chạy test khi có thay đổi mã nguồn.

## 12. Kết luận

Dự án Selenium SauceDemo Testing đã xây dựng và thực thi thành công bộ kiểm thử tự động cơ bản bằng Python, Selenium WebDriver và Pytest.

Bộ kiểm thử bao gồm 5 trường hợp: đăng nhập hợp lệ, đăng nhập không hợp lệ, hiển thị danh sách sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất.

Theo kết quả ghi nhận ở lần chạy gần nhất, **5/5 test case đều PASSED, đạt tỷ lệ thành công 100% trong lần chạy đó**.

Dự án giúp củng cố kiến thức về kiểm thử tự động giao diện web, xây dựng test case và sử dụng Pytest để xác nhận hành vi của hệ thống.

## 13. Tài liệu tham khảo

- SauceDemo: https://www.saucedemo.com/
- Selenium Documentation: https://www.selenium.dev/documentation/
- Pytest Documentation: https://docs.pytest.org/
- Repository dự án: https://github.com/Duong465fds/selenium-saucedemo-testing
