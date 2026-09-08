# %%
def chao(ten):
    """Hàm này dùng để chào một người,
    tên được truyền vào như một tham số"""
    print("Chào bạn " + ten + ". Chúc một ngày vui vẻ!")


chao("ruby")


# %%
def QtmHello():
    print("QuanTriMang xin chào các bạn!")
    return


QtmHello()


# %%
def QtmHello():
    print("QuanTriMang xin chào các bạn!")
    return


QtmHello()
print("Bạn đang học về Python trên QuanTriMang.com")
QtmHello()


# %%
def QtmHello():
    print("QuanTriMang xin chào các bạn!")
    HomNayTotNgay()
    return


def HomNayTotNgay():
    print("Hôm nay là một ngày tốt, đúng không nhỉ!")
    return


QtmHello()


# %%
def XinChao(Name):
    print("Xin chào " + Name)
    return


XinChao("QuanTriMang")


# %%
def XinChao(Name):
    print("Xin chào " + Name)
    return


Name = input("Nhập tên của bạn: ")
XinChao(Name)


# %%
def PhepNhan(Number):
    return Number * 10


print(PhepNhan(5))


# %%
def DemTen(Name):
    return len(Name)


DienTen = "QuanTriMang.com"

print(DemTen(DienTen))


# %%
def chao(ten):
    """Hàm này dùng để chào một người,
    tên được truyền vào như một tham số"""
    print("Chào bạn " + ten + ". Chúc một ngày vui vẻ!")


print(chao.__doc__)


# %%
def gia_tri_tuyet_doi(so):
    """Hàm này trả về giá trị tuyệt đối
    của một số nhập vào"""
    if so >= 0:
        return so
    else:
        return -so


# Đầu ra: 5
print(gia_tri_tuyet_doi(5))

# Đầu ra: 8
print(gia_tri_tuyet_doi(-8))

# Đầu ra: Giá trị tuyệt đối của số nhập vào
num = int(input("Nhập số cần lấy giá trị tuyệt đối: "))
print(gia_tri_tuyet_doi(num))

# %%
x = 30


def ham_in():
    x = 15
    print("Giá trị bên trong hàm:", x)


ham_in()


print("Giá trị bên ngoài hàm:", x)

# %%
from functools import reduce


def add_num(a, b):
    return a + b


a = [1, 2, 3, 10]
print(reduce(add_num, a))
# kết quả:  16

# %%
from functools import reduce


def add_str(a, b):
    return a + " " + b


a = ["Quantrimang", "là", "1", "web", "thương mại điện tử"]
print(reduce(add_str, a))

# Quantrimang là một một web thương mại điện tử
# %%
words = "column1 column2 column3"
words = words.split(" ")
print(words)
# ['column1', 'column2', 'column3']

# %%
fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):
    print(i, j)

# 0 grape, 1 apple, 2 mango
# %%
fruits = ["táo", "cam", "xoài"]
for index, fruit in enumerate(fruits, start=1):
    print("Vị trí của", fruit, "là:", index)

# %%
tasks = ["Đi chợ", "Nấu cơm", "Rửa bát"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# %%
g = "(4 * 5)/4"
d = eval(g)
print(d)
# <strong>Output:</strong> 5.0
# %%
a = 10
b = 20
print(eval("a + b"))

# %%
expression = "60000000*(6/100)*(6/12)"
print(eval(expression))

# %%
b = [1, 3, 4, 6]
a = [1, 65, 7, 9]


def add(a, b):
    return a + b


b = sum(map(add, b, a))
print(b)  # 96


# %%
def add(a, b):
    return a + b


b = [1, 3, 4, 6]
a = [1, 65, 7, 9]

result = map(add, b, a)
print(list(result))


# %%
def square(number):
    return number**2


numbers = [1, 2, 3, 4]
print(list(map(square, numbers)))

# %%
numbers = [1, 2, 3, 4]
result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number * 2)

print(result)

# %%
