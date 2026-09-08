# %%
# Một ví dụ về for loop đơn giản

fruits = ["apple", "orange", "kiwi"]

for fruit in fruits:

    print(fruit)

# %%
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x, end="  ")

# %%
# Lặp chữ cái trong quantrimang
for chu in "quantrimang":
    print("Chữ cái hiện tại:", chu)

# Lặp từ trong chuỗi
chuoi = ["bố", "mẹ", "em"]
for tu in chuoi:
    print("Anh yêu", tu)

# %%
# Tính tổng tất cả các số trong danh sách A
# Danh sách A
A = [1, 3, 5, 9, 11, 2, 6, 8, 10]
# Biến để lưu trữ tổng các số là tong, gán giá trị ban đầu bằng 0
tong = 0
# Vòng lặp for, a là biến lặp
for a in A:
    tong = tong + a
# Đầu ra: Tổng các số là 55
print("Tổng các số là:", tong)

# %%
# Lặp chữ cái có break:

a = ["quan", "tri", "mang", ".", "com"]
for chu in a:
    if chu == ".":
        break
    print(chu)
print("Nội dung ngoài vòng lặp for")

# %%
# Lặp chữ cái có continue:

a = ["quan", "tri", "mang", ".", "com"]
for chu in a:
    if chu == ".":
        continue
    print(chu)
print("Nội dung ngoài vòng lặp for")

# %%
for i in range(100):
    print("Anh xin lỗi")
print("Em ơi, anh chép xong ồi nè!")

# %%
# Lệnh 1
print(range(9))
# Lệnh 2
print(list(range(9)))
# Lệnh 3
print(list(range(2, 5)))
# Lệnh 4
print(list(range(0, 15, 5)))

# %%
chuoi = ["bố", "mẹ", "em"]

for tu in range(len(chuoi)):
    print("Anh yêu", chuoi[tu])


# %%
for num in range(-2, -5, -1):
    print(num, end=", ")

# %%
# Ví dụ về vòng lặp lồng nhau trên QuanTriMang

tinhtu = ["đỏ", "to", "ngon"]
qua = ["táo", "chuối", "cherry"]

for x in qua:
    for y in tinhtu:
        print(x, y)

# %%
B = [0, 2, 4, 5]

for b in B:
    print(b)
else:
    print("Đã hết số.")

# %%
# Lặp dãy từ 0 đến 10
for num in range(0, 10):
    # Lặp trên các thừa số của một số trong dãy
    for i in range(2, num):
        # Xác định thừa số đầu tiên (phép chia có số dư bằng 0)
        if num % i == 0:
            j = num / i  # Ước lượng thừa số thứ 2
            print("%d bằng %d * %d" % (num, i, j))
            break  # Dừng vòng for hiện tại, chuyển đến số tiếp theo trong vòng for đầu tiên
    else:  # Phần else trong vòng lặp
        print(num, "là số nguyên tố")

# %%
x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)

# %%
for num in range(10, 14):
    for i in range(2, num):
        if num % i == 1:
            print(num)
            break

# %%
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var += 1
else:
    var += 1
print(var)

# %%
