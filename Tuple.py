# %%
t = (10, "quan tri mang", 2j)
#t[0:2] = (10, 'quan tri mang')
print("t[0:2] = ", t[0:2])


# %%
t = (10, "quan tri mang", 2j)
#t[0:2] = (10, 'quan tri mang')
t[0:2] 

# %%
# Tuple rỗng
# Output: ()
my_tuple = ()
print(my_tuple)

# tuple số nguyên
# Output: (2, 4, 16, 256)
my_tuple = (2, 4, 16, 256)
print(my_tuple)

# tuple có nhiều kiểu dữ liệu
# Output: (10, "Quantrimang.com", 3.5)
my_tuple = (10, "Quantrimang.com", 3.5)
print(my_tuple)

# tuple lồng nhau
# Output: ("QTM", [2, 4, 6], (3, 5, 7))
my_tuple = ("QTM", [2, 4, 6], (3, 5, 7))
print(my_tuple)

# tuple có thể được tạo mà không cần dấu ()
# còn gọi là đóng gói tuple
# Output: (10, "Quantrimang.com", 3.5)

my_tuple = 10, "Quantrimang.com", 3.5
print(my_tuple)

# mở gói (unpacking) tuple cũng có thể làm được
# Output:
# 10
# Quantrimang.com
# 3.5
a, b, c = my_tuple
print(a)
print(b)
print(c) 

# %%
# tạo tuple chỉ với ()
# Output: <class 'str'>
my_tuple = ("Quantrimang.com")
print(type(my_tuple))

# khi thêm dấu phẩy vào cuối
# Output: <class 'tuple'>
my_tuple = ("Quantrimang.com",) 
print(type(my_tuple))

# dấu () là tùy chọn, bạn có thể bỏ nếu thích
# Output: <class 'tuple'>
my_tuple = "Quantrimang.com",
print(type(my_tuple))


# %%
# tuple lồng nhau
n_tuple = ("Quantrimang.com", [2, 6, 8], (1, 2, 3))

# index lồng nhau
# Output: 'r'
print(n_tuple[0][5])

# index lồng nhau
# Output: 8
print(n_tuple[1][2])

# %%
my_tuple = (1, 3, 5, [7, 9])

# không thể thay đổi phần tử của tuple
# Nếu bạn bỏ dấu # ở dòng 8
# Bạn sẽ nhận được lỗi:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# Nhưng phần tử có index 3 trong tuple là list
# list có thể thay đổi, nên phần tử đó có thể thay đổi
# Output: (1, 3, 5, [8, 9])
my_tuple[3][0] = 8
print(my_tuple)

# Nếu cần thay đổi tuple hãy gán lại giá trị cho nó
# Output: ('q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g')
my_tuple = ('q', 'u', 'a', 'n', 't', 'r', 'i', 'm', 'a', 'n', 'g')
print(my_tuple)

# %%
QTM = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']

# Count
# Output: 2
print(QTM.count('m'))

# Index
# Output: 3
print(QTM.index('n'))

# %%
for ngon_ngu in ('Python','C++','Web'):
    print("Tôi thích lập trình:",ngon_ngu)

# %%
