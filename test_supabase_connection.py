import pathlib
import sys

try:
    import tomllib
except ModuleNotFoundError:
    print("Python 3.11+ is required to run this test script because it uses tomllib.")
    sys.exit(1)

try:
    import psycopg2
    from psycopg2 import OperationalError
except ImportError:
    print("psycopg2 is not installed in this environment. Install it with 'pip install psycopg2-binary' before testing.")
    sys.exit(1)


def load_secrets():
    secret_path = pathlib.Path(".streamlit/secrets.toml")
    if not secret_path.exists():
        print("Không tìm thấy file .streamlit/secrets.toml.")
        print("Hãy tạo file này với nội dung Supabase của bạn.")
        return None
    with secret_path.open("rb") as f:
        data = tomllib.load(f)
    return data.get("postgres")


def connect_test(secret):
    if not secret:
        print("Không có thông tin database trong st.secrets.")
        return False

    required = ["host", "port", "database", "user", "password", "sslmode"]
    missing = [k for k in required if k not in secret]
    if missing:
        print("Thiếu khóa trong secrets:", ", ".join(missing))
        return False

    print("Sử dụng cấu hình Supabase sau:")
    for k in required:
        if k != "password":
            print(f"  {k}: {secret[k]}")
        else:
            print("  password: <hidden>")

    try:
        conn = psycopg2.connect(
            host=secret["host"],
            port=secret["port"],
            database=secret["database"],
            user=secret["user"],
            password=secret["password"],
            sslmode=secret["sslmode"],
        )
        conn.close()
        print("✅ Kết nối tới Supabase thành công!")
        return True
    except OperationalError as e:
        print("❌ Kết nối thất bại:")
        print(str(e))
        return False


def main():
    secret = load_secrets()
    if not secret:
        print("Hãy điền thông tin Supabase vào .streamlit/secrets.toml và thử lại.")
        sys.exit(1)

    success = connect_test(secret)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
