# Hệ thống hỗ trợ quyết định bất động sản TP.HCM

Ứng dụng Streamlit này hỗ trợ người dùng chọn căn nhà phù hợp tại TP.HCM bằng cách kết hợp dữ liệu bất động sản, luật chuyên gia và độ ưu tiên AHP.

## Nội dung chính

- `app.py`: ứng dụng chính Streamlit.
- `Database/danh_sach_nha.csv`: dữ liệu danh sách nhà.
- `Database/database_backup.sql`: sao lưu cơ sở dữ liệu.

## Yêu cầu

- Python 3.10+
- streamlit
- pandas
- numpy
- plotly
- psycopg2

## Cài đặt

1. Tạo môi trường ảo:

```bash
python -m venv venv
```

2. Kích hoạt môi trường:

- Windows:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

3. Cài đặt phụ thuộc:

```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
streamlit run app.py
```

## Cấu hình cơ sở dữ liệu

Ứng dụng kết nối PostgreSQL với cấu hình mặc định:

- host: `localhost`
- database: `HeHoTroQuyetDinh`
- user: `postgres`
- password: `admin`
- port: `5432`

Bạn nên thay đổi thông tin này trong `app.py` nếu cần.

## GitHub

Repo này đã khởi tạo git. Để đẩy lên GitHub, chạy:

```bash
git remote add origin <URL-repo>
git branch -M main
git push -u origin main
```
