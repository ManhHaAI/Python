dict1 = {} #dictionary rỗng
#dict2 là dictionary với các khóa nguyên
dict2 = {1: 'Quantrimang.com',2: 'Công nghệ'}
#Tạo dictionary với khóa hỗn hợp
dict3 = {'tên': 'QTM', 1: [1, 3, 5]}
#Tạo dictionary bằng dict()
dict4 = dict({1:'apple', 2:'ball'})
#Tạo dictionary từ chuỗi với mỗi mục là một cặp
dict5 = dict([(1,'QTM'), (2,'CN')])
print("Kiểu của dict2:", type(dict2))
print("Kiểu của dict5:", type(dict5))
print("Kiểu của dict3:", type(dict3))
print("Kiểu của dict4:", type(dict4))
print("Kiểu của dict1:", type(dict1))

#%%
users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
print(users.keys())
# prints
['lastname', 'age', 'firstname']

# %%
#khai báo và gán giá trị dict2
dict2 = {1: 'Quantrimang.com','quantrimang': 'Công nghệ'} 
print(type(dict2)) #in kiểu dữ liệu của dict2
#trích xuất dữ liệu bằng khóa rồi in
print("dict2[1] = ", dict2[1]) 
print("dict2[quantrimang] = ",dict2['quantrimang'])

# %%
# Ví dụ lập trình Python minh họa cách truy cập một phần tử từ dictionary
 
# Tạo một Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
 
# Truy cập phần tử bằng key
print("Accessing a element using key:")
print(Dict['name'])
 
# Truy cập phần tử bằng get()
# Phương thức
print("Accessing a element using get:")
print(Dict.get(3))

# %%
dict2 = {1: 'Quantrimang.com','quantrimang': 'Công nghệ'}

#cập nhật giá trị
dict2['quantrimang'] = 'Quản trị mạng'

#output: {1: 'Quantrimang.com', 'quantrimang': 'Quản trị mạng'}
print(dict2)

#thêm phần tử mới
dict2[3] = 'Python'

#output: {1: 'Quantrimang.com', 'quantrimang': 'Quản trị mạng', 3: 'Python'}
print(dict2)

# %%
# tạo dictionary
binh_phuong = {1:1, 2:4, 3:9, 4:16, 5:25}

# xóa phần tử số 4
# Output: 16
print(binh_phuong.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(binh_phuong)

# xóa phần tử cụ thể
del binh_phuong[2]

# output: {1: 1, 3: 9, 5: 25}
print(binh_phuong)

# xóa phần tử bất kỳ
# Output: (5, 25)
print(binh_phuong.popitem())

# Output: {1: 1, 3: 9}
print(binh_phuong)

# xóa tất cả phần tử
binh_phuong.clear()

# output: {}
print(binh_phuong)

# xóa dictionary binh_phuong
del binh_phuong

# tạo lỗi nếu bỏ # ở lệnh sau
# print(squares)

# %%
lap_phuong = {x: x*x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
print(lap_phuong)

# %%
lap_phuong = {}
for x in range(6):
    lap_phuong[x] = x*x*x
print(lap_phuong)

# %%
lap_phuong_chan = {x: x*x*x for x in range (10) if x%2==0}
# output: {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
print(lap_phuong_chan)

# %%
lap_phuong_le = {x: x*x*x for x in range (10) if x%2==1}
# output: {1: 1, 3: 27, 5: 125, 7: 343, 9: 729}
print(lap_phuong_le)

# %%
lap_phuong = {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
for i in lap_phuong:
    print(lap_phuong[i])

# %%
