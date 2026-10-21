# Selenium WebDriver Automation Testing – SauceDemo

## 1. Giới thiệu
Repo này là bài thực hành kiểm thử tự động giao diện website bằng Selenium WebDriver và Python. Website kiểm thử: https://www.saucedemo.com/

## 2. Mục tiêu
- Tìm hiểu cách Selenium điều khiển trình duyệt.
- Xây dựng và chạy tối thiểu 05 test case tự động.
- Kiểm tra kết quả thực tế bằng các assertion trong pytest.
- Lưu mã nguồn và báo cáo trong GitHub Repository.

## 3. Công cụ và môi trường
- Python 3.10 trở lên
- Google Chrome
- Selenium WebDriver 4
- pytest
- Visual Studio Code hoặc terminal
- Windows 10/11 (có thể điều chỉnh để chạy trên hệ điều hành khác)

Selenium Manager được Selenium 4 tích hợp hỗ trợ quản lý driver tự động trong nhiều trường hợp, vì vậy thường không cần tải ChromeDriver thủ công.

## 4. Danh sách test case

| ID | Tên test case | Dữ liệu kiểm thử | Kết quả mong đợi |
|---|---|---|---|
| TC01 | Đăng nhập hợp lệ | `standard_user` / `secret_sauce` | Chuyển tới trang Products và hiển thị danh sách sản phẩm |
| TC02 | Đăng nhập sai mật khẩu | `standard_user` / `wrong_password` | Hiển thị thông báo lỗi đăng nhập |
| TC03 | Kiểm tra danh sách sản phẩm | Tài khoản hợp lệ | Hiển thị 6 sản phẩm trên trang Products |
| TC04 | Thêm sản phẩm vào giỏ hàng | Sauce Labs Backpack | Huy hiệu giỏ hàng là 1 và sản phẩm xuất hiện trong giỏ |
| TC05 | Đăng xuất | Tài khoản hợp lệ | Quay lại trang đăng nhập |

## 5. Cấu trúc thư mục

```text
selenium-saucedemo/
├── README.md
├── requirements.txt
├── pytest.ini
├── tests/
│   └── test_saucedemo.py
└── screenshots/
```

## 6. Cài đặt và chạy kiểm thử trên Windows

Mở PowerShell hoặc terminal tại thư mục repo, chạy lần lượt:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest
```

Nếu PowerShell chặn kích hoạt môi trường ảo, có thể bỏ qua bước activate và chạy trực tiếp:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest
```

Chrome cần được cài đặt và máy tính cần có kết nối Internet khi chạy test lần đầu. Mỗi test sẽ mở một phiên trình duyệt riêng và tự đóng khi kết thúc.

## 7. Kết quả kiểm thử

Chạy lệnh `pytest` để xem kết quả trong terminal. Khi thành công, pytest sẽ hiển thị số test `passed`; nếu có test thất bại, xem phần thông báo lỗi để xác định nguyên nhân.

| ID | Kết quả thực tế | Trạng thái |
|---|---|---|
| TC01 | Điền sau khi chạy kiểm thử | Chưa chạy |
| TC02 | Điền sau khi chạy kiểm thử | Chưa chạy |
| TC03 | Điền sau khi chạy kiểm thử | Chưa chạy |
| TC04 | Điền sau khi chạy kiểm thử | Chưa chạy |
| TC05 | Điền sau khi chạy kiểm thử | Chưa chạy |

**Lưu ý:** Không ghi tất cả test là PASS trước khi thực sự chạy chương trình. Sau khi chạy, cập nhật bảng trên theo kết quả terminal và chụp ảnh màn hình kết quả để làm minh chứng. Có thể lưu ảnh vào thư mục `screenshots/`.

## 8. Kết luận
Bài thực hành minh họa cách sử dụng Selenium WebDriver để tự động hóa các thao tác trên website: đăng nhập, kiểm tra danh sách sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất. Các kiểm tra được thực hiện tự động bằng pytest assertion.

## 9. Tài liệu tham khảo
- Selenium documentation: https://www.selenium.dev/documentation/
- Selenium sample scripts của Sauce Labs: https://docs.saucelabs.com/web-apps/automated-testing/selenium/sample-scripts/
- Website thực hành: https://www.saucedemo.com/
