# %%
a = {5,2,3,1,4}
print("a=", a) # Output: a= {1, 2, 3, 4, 5}

# %%
my_set = {1.0, "Xin chào", (1, 2, 3)}

#Output: QTM_Set= {'Xin chào', 1.0, (1, 2, 3)}
print("QTM_Set=",my_set)
# %%
# Khởi tạo my_set
my_set = {1,3}
print(my_set)

# Nếu bỏ dấu # ở dòng 9,
# Bạn sẽ nhận được lỗi
# TypeError: 'set' object does not support indexing

#my_set[0]

# Thêm phần tử
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# Thêm nhiều phần tử vào set
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# Thêm list và set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)

# %%
# Khởi tạo my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# Xóa phần tử bằng discard()
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# Xóa bằng remove()
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# Xóa phần tử không có 
# trong set bằng discard()
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# Xóa phần tử không có 
# trong set bằng remove()
# Nếu bạn bỏ dấu # ở dòng 27,
# bạn sẽ nhận được lỗi.
# Output: KeyError: 2

#my_set.remove(2)

# %%
# Khởi tạo my_set
# Output: set of unique elements
my_set = set("Quantrimang.com")
print(my_set)

# xóa phần tử bằng pop()
# Output: phần tử bị xóa ngẫu nhiên
print(my_set.pop())

# xóa phần tử khác bằng pop()
# Output: phần tử bị xóa ngẫu nhiên
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)

# %%
# Khởi tạo A và B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# sử dụng toán tử | 
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# sử dụng hàm union()
# Output: Như trên
print(A.union(B))
print(B.union(A))


# %%
# khởi tạo A và B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# sử dụng & 
# Output: {4, 5}
print("Giao của 2 tập hợp:", A & B)

# sử dụng intersection()
# Output: {4, 5}
print("Giao của 2 tập hợp:", A.intersection(B))
print("Giao của 2 tập hợp:", B.intersection(A))

# %%
# Khởi tạo A và B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Sử dụng toán tử - trên A
# Output: {1, 2, 3}
print("Hiệu của 2 tập hợp:", A - B)
# Sử dụng hàm difference() trên A
# Output: {1, 2, 3}
print("Hiệu của 2 tập hợp:", A.difference(B))

# Sử dụng toán tử - trên B
# Output: {8, 6, 7}
print("Hiệu của 2 tập hợp:", B - A)

# Sử dụng difference() trên B
# Output: {8, 6, 7}
print("Hiệu của 2 tập hợp:", B.difference(A))

# %%
# Khởi tạo A và B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Sử dụng toán tử ^
# Output: {1, 2, 3, 6, 7, 8}
print("Bù giữa 2 tập hợp:", A ^ B)
# Sử dụng symmetric_difference() trên A
# Output: {1, 2, 3, 6, 7, 8}
print("Bù giữa 2 tập hợp:", A.symmetric_difference(B))

# %%
# Khởi tạo my_set
my_set = set("Quantrimang.com")

# Kiểm tra xem Q có trong my_set không
# Output: True
print("Q có trong my_set không:", 'Q' in my_set)

# Kiểm tra xem q có trong my_set không
# Output: False
print("q có trong my_set không:", 'q' in my_set)

# %%
for letter in set("Python"):
    print("Ký tự:", letter)
    

# %%
