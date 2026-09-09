# %%
def tinh_tong(a, b):
    tong = a + b
    return tong  # trả giá trị của tổng về nơi gọi hàm


# gọi hàm
so1 = 5
so2 = 6
# a = 5
# b = 6
# tong = 5 + 6
# return 11
# kết quả in ra màn hình
print("Tổng hai số đầu là: ", tinh_tong(so1, so2))

# nhập từ bàn phím
so3 = int(input("Nhập một số: "))
so4 = int(input("Nhập một số nữa: "))
# input() nhận dữ liệu từ người dùng dưới dạng chuỗi.
# int() chuyển chuỗi đó thành số nguyên.

print("Tổng của hai số sau là: ", tinh_tong(so3, so4))

# %%
