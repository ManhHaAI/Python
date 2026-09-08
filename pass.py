# %%
# pass chỉ giữ chỗ các khối lệnh trong for:

sequence = {"p", "a", "s", "s"}
for val in sequence:
    pass

# %%
a = 50
b = 100

if b < a:
    pass
else:
    print("b lớn hơn a")

# %%
while True:
    num = int(input("Nhập một số: "))
    if num == 0:
        break
    print("Gấp ba của", num, "là", 3 * num)

# %%
a = 5
b = 7
sum = a + b
print("Tổng của", a, "và", b, "là", sum)

# %%
# tính tổng các số từ 1 đến n
n = int(input("Nhập n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Tổng các số từ 1 đến", n, "là", total)

# %%
# Thử những số khác nhau bằng cách gán số đó cho n
n = 15

# Dùng lệnh sau nếu muốn người dùng nhập số
# n = int(input("Nhập số n: "))

# Khởi tạo tổng tong và biến đếm i
tong = 0
i = 1

while i <= n:
    tong = tong + i
    i = i + 1  # cập nhật số đếm
# Code by Quantrimang.com
# in tổng
print("Tổng các số từ 1 đến ", n, " là", tong)

# %%
a = 5
b = 3
hiệu = a - b
print("Hiệu của", a, "và", b, "là", hiệu)

# %%
