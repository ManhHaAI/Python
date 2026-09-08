# %%
# In và đếm các số từ 0 tới 8:

count = 1
n = 0
while n < 8:
    print("Số thứ", count, " là:", n)
    n = n + 1
    count = count + 1
print("Hết rồi!")
# %%
n = int(input("Nhập n: "))  # Nhập số n tùy ý
tong = 0  # khai báo và gán giá trị cho tong
i = 1  # khai báo và gán giá trị cho biến đếm i

while i <= n:
    tong = tong + i
    i = i + 1  # cập nhật biến đếm

print("Tổng là", tong)

# %%
i = 1
while i < 6:
    print(i)
    if i == 3:  # kiểm tra điều kiện xem i bằng 3 hay chưa
        break
    i += 1  # cập nhật biến đếm

# %%
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# %%
dem = 0
while dem < 3:
    print("Đang ở trong vòng lặp while")
    dem = dem + 1
else:
    print("Đang ở trong else")

# %%
n = 0
while n < 2:
    print(n, "nhỏ hơn 2")
    n = n + 1
else:
    print(n, "không nhỏ hơn 2")
# %%
x = 0
while x < 100:
    x += 2
print(x)
# %%
a = ["vàng", "đỏ", "trắng", "xanh", "tím"]
while a:
    if len(a) < 3:
        break
    print(a.pop())
print("Màu sắc rực rỡ")
# %%
a = ["vàng", "đỏ", "trắng", "xanh", "tím"]
while a:
    if len(a) < 3:
        continue
    print(a.pop())
print("Màu sắc rực rỡ")

# %%
# ví dụ 1: viết chương trình tính tổng các số lẻ từ 1 đến 50
tong = 0
i = 1
while i <= 50:
    if i % 2 != 0:
        tong += i
    i += 1
print("Tổng các số lẻ từ 1 đến 50 là:", tong)

# %%
# vd2: viết chương trình cho phép nhập vào một chuỗi kí tự và
# in ra chuỗi viết hoa tất cả các kí tự trong chuỗi đó. Chương
# trình sẽ dừng khi người dùng nhập vào chuỗi "exit"

while True:
    chuoi = input("Nhập vào một chuỗi kí tự (hoặc 'exit' để thoát): ")
    if chuoi.lower() == "exit":
        print("Chương trình kết thúc.")
        break
    else:
        print("Chuỗi viết hoa:", chuoi.upper())
# %%
chuoi = None
while True:
    chuoi = input("Nhập vào một chuỗi kí tự : ")
    if chuoi != "exit":
        print("Chuỗi viết hoa:", chuoi.upper())
    else:
        print("Chương trình kết thúc.")
        break

# %%
for i in range(1, 11):
    print(i)

# %%
# Nhận đầu vào từ người dùng cho đến khi họ nhập một nguyên âm
nguyenAm = "aeiouAEIOU"

# vòng lặp vô hạn
while True:
    m = input("Nhập một nguyên âm: ")
    # Điều kiện ở giữa khối lệnh
    if m in nguyenAm:
        break
    print("Đây không phải là nguyên âm. Hãy thử lại!")

# Code by Quantrimang.com
print("Chuẩn rồi, cảm ơn bạn!")
# %%
# Tung xúc xắc cho đến khi người dùng chọn thoát:

import random

while True:
    input("Nhấn Enter để tung xúc xắc")

    # nhận số mặt xúc xắc bất kỳ từ 1 đến 6
    num = random.randint(1, 6)
    print("Bạn tung được mặt", num)
    option = input("Bạn có muốn tung lại không?(y/n) ")

    # điều kiện
    if option == "n":
        break

# %%
