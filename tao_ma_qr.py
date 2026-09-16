import qrcode

# 1. Dữ liệu cần mã hóa
data = "file:///C:/Users/admin/OneDrive/Desktop/VocabVN%20-%20T%E1%BB%AB%20v%E1%BB%B1ng%20ti%E1%BA%BFng%20Anh%20theo%20ch%E1%BB%A7%20%C4%91%E1%BB%81.html"

# 2. Cấu hình chi tiết cho mã QR
qr = qrcode.QRCode(
    version=1,  # Kích thước mã QR (từ 1 đến 40). Số càng lớn mã càng to và chứa được nhiều dữ liệu.
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mức độ sửa lỗi (L, M, Q, H). H là cao nhất (chịu được 30% lỗi).
    box_size=10,  # Kích thước của mỗi ô vuông nhỏ trong mã QR (pixel).
    border=4,  # Độ dày của viền trắng xung quanh mã QR (mặc định là 4).
)

# 3. Thêm dữ liệu vào đối tượng qr
qr.add_data(data)
qr.make(fit=True)

# 4. Tạo hình ảnh và tùy chỉnh màu sắc
# fill_color: màu của mã QR, back_color: màu nền
img = qr.make_image(fill_color="darkblue", back_color="lightyellow")

# 5. Lưu file
img.save("ma_qr_tuy_chinh.png")

print("Đã tạo mã QR tùy chỉnh thành công!")
img.show()
