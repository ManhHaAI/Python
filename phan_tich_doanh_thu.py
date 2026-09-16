import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# BƯỚC 1: DÙNG NUMPY TẠO DỮ LIỆU
# ==========================================
# Tạo mảng các tháng từ 1 đến 12
thang = np.arange(1, 13)

# Giả lập doanh thu: Mức cơ bản là 50 triệu, cộng thêm biến động ngẫu nhiên từ -10 đến 30 triệu
np.random.seed(42)  # Cố định seed để random ra kết quả giống nhau mỗi lần chạy
doanh_thu = 50 + np.random.randint(-10, 30, size=12)

# ==========================================
# BƯỚC 2: DÙNG PANDAS XỬ LÝ DỮ LIỆU
# ==========================================
# Đưa mảng NumPy vào DataFrame (bảng dữ liệu) của Pandas
df = pd.DataFrame({"Tháng": thang, "Doanh thu": doanh_thu})

# Tính toán thêm cột "Lợi nhuận" (Giả sử biên lợi nhuận là 30% doanh thu)
df["Lợi nhuận"] = df["Doanh thu"] * 0.75

# Tính "Doanh thu lũy kế" (Cộng dồn doanh thu từ tháng 1 đến tháng hiện tại)
df["Lũy kế"] = df["Doanh thu"].cumsum()

print("--- BẢNG BÁO CÁO TÀI CHÍNH 12 THÁNG ---")
print(df)
print("-" * 40)

# ==========================================
# BƯỚC 3: DÙNG MATPLOTLIB VẼ BIỂU ĐỒ
# ==========================================
# Tạo một khung tranh với kích thước 10x6 inch
plt.figure(figsize=(10, 6))

# Vẽ biểu đồ CỘT thể hiện Doanh thu
plt.bar(df["Tháng"], df["Doanh thu"], color="skyblue", label="Doanh thu")

# Vẽ biểu đồ ĐƯỜNG thể hiện Lợi nhuận đè lên trên
plt.plot(
    df["Tháng"],
    df["Lợi nhuận"],
    color="red",
    marker="o",
    linewidth=2,
    label="Lợi nhuận (75%)",
)

# Trang trí cho biểu đồ đẹp và chuyên nghiệp hơn
plt.title("BÁO CÁO DOANH THU VÀ LỢI NHUẬN NĂM 2026", fontsize=14, fontweight="bold")
plt.xlabel("Tháng", fontsize=12)
plt.ylabel("Triệu VNĐ", fontsize=12)

# Đảm bảo trục X hiển thị đủ từ 1 đến 12
plt.xticks(df["Tháng"])

# Thêm lưới mờ nằm ngang cho dễ nhìn số liệu
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Hiển thị chú thích (Legend)
plt.legend()

# Show biểu đồ ra cửa sổ
print("Đang mở biểu đồ trực quan...")
plt.show()
