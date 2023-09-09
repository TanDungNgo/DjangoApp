# Sử dụng image cơ sở có Python đã cài đặt (chọn phiên bản Python phù hợp)
FROM python:3.8

# Đặt biến môi trường để tránh thông báo Python được lưu đệm
ENV PYTHONUNBUFFERED 1

# Tạo thư mục /app trong container và đặt nó làm thư mục làm việc
RUN mkdir /app
WORKDIR /app

# Sao chép tệp requirements.txt từ máy tính vào /app trong container
COPY requirements.txt /app/

# Cài đặt các gói Python từ requirements.txt, bao gồm Django
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ dự án Django của bạn vào /app trong container
COPY . /app/

# Chạy các lệnh khởi tạo cơ sở dữ liệu hoặc các tác vụ khác ở đây (tuỳ thuộc vào dự án của bạn)

# Mở cổng 8000 để ứng dụng Django có thể truy cập từ bên ngoài (tùy thuộc vào cổng bạn đã cấu hình trong dự án Django)
EXPOSE 8000

# Khởi động ứng dụng Django bằng lệnh dưới đây (thay "yourprojectname" bằng tên dự án của bạn và "0.0.0.0:8000" bằng cổng và địa chỉ IP mà bạn muốn chạy)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
