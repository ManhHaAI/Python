# %%
# Nếu là số dương ta sẽ in một thông điệp thích hợp
num = 3
if num > 0:
    print(num, "là số dương.")
print("Thông điệp này luôn được in.")

num = -1
if num > 0:
    print(num, "là số dương.")
print("Thông điệp này cũng luôn được in.")

# %%
# Chuong trinh kiem tra xem so am hay duong
# Va hien thi thong bao phu hop

num = 0

# Hay thu chuong trinh voi 2 gia tri sau:
# num = -5
# num = 0

if num >= 0:
    print("So duong hoac bang 0")
else:
    print("So am")

# %%
x = int(input("Nhap mot so: "))
if x < 0:
    print("So am")
elif x == 0:
    print("So 0")
elif x == 1:
    print("So 1")
else:
    print("So duong")

# %%
# Trong code này, nhập vào một số
# Kiểm tra xem số âm hay dương
# hay bằng không và hiển thị
# thông báo thích hợp
# Sử dụng hàm if lồng nhau

num = float(input("Nhập một số: "))
if num >= 0:
    if num == 0:
        print("Số Không")
    else:
        print("Số dương")
else:
    print("Số âm")

# %%
x = 11

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# %%
a = 33
b = 200

if b > a:
    pass

# %%
x = 0
a = 5
b = 5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

# %%
