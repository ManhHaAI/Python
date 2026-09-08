#%%
import array as arr
a = arr.array('f',[1, 3, 4]) 
print(a)

# %%
# Tạo một "mảng" bằng List chứa các loại trái cây
trai_cay = ["Táo", "Chuối", "Cam"]

# Truy cập phần tử đầu tiên (vị trí số 0)
print(trai_cay[0])  # Kết quả: Táo

# Thêm phần tử mới
trai_cay.append("Xoài")
print(trai_cay)     # Kết quả: ['Táo', 'Chuối', 'Cam', 'Xoài']

# %%
import array

# Tạo một mảng chỉ chứa số nguyên (mã 'i' đại diện cho integer)
mang_so_nguyen = array.array('i', [1, 2, 3, 4, 5])

print(mang_so_nguyen[1])  # Kết quả: 2

# Nếu bạn cố thêm một chuỗi vào mảng này, Python sẽ báo lỗi
# mang_so_nguyen.append("Hello") -> Lỗi TypeError

# %%
import array as arr 
a = arr.array('i', [2, 4, 6, 8]) 

print("Phần tử đầu tiên:", a[0]) 
print("Phần tử thứ 2:", a[1]) 
print("Phần tử cuối cùng:", a[-1])
# %%
import array as arr 

numbers_list = [5, 85, 65, 15, 95, 52, 36, 25] 
numbers_array = arr.array('i', numbers_list) 

print(numbers_array[2:5]) # Phần tử thứ 3 đến 5 
print(numbers_array[:-5]) # Phần tử đầu tiên đến 4 
print(numbers_array[5:]) # Phần tử thứ 6 đến hết 
print(numbers_array[:]) # Phần tử đầu tiên đến cuối cùng

# %%
import array as arr 
numbers = arr.array('i', [1, 1, 2, 5, 7, 9]) 

# thay đổi phần tử đầu tiên 
numbers[0] = 0 
print(numbers) 
# Output: array('i', [0, 1, 2, 5, 7, 9]) 

# thay phần tử thứ 3 đến thứ 5 
numbers[2:5] = arr.array('i', [4, 6, 8]) 
print(numbers) 
# Output: array('i', [0, 1, 4, 6, 8, 9])

# %%
import array as arr
numbers = arr.array('i', [3, 5, 7])
print(numbers)
# thêm 4 vào cuối mảng
numbers.append(4)
print(numbers)
# nối vào cuối mảng
numbers.extend([5, 6, 7])
print(numbers)

# %%
import array as arr 

mang_le = arr.array('i', [3, 5, 7]) 
mang_chan = arr.array('i', [2, 6, 8]) 

numbers = arr.array('i') # tạo mảng trống 
numbers = mang_le + mang_chan 
# Code by quantrimang.com 
print(numbers) 
# Output: array('i', [3, 5, 7, 2, 6, 8])

# %%
import array as arr 

numbers = arr.array('i', [1, 1, 3, 5, 9]) 

numbers.remove(1) 
print(numbers) # Output: array('i', [1, 3, 5, 9]) 
print(numbers.pop(2)) # Output: 5 
print(numbers) # Output: array('i', [1, 3, 9])

# %%
# Ví dụ chứng minh độ phức tạp khi xóa phần tử trong mảng 
# Chia tách phần tử trong mảng
 
# Nhập mô đun mảng
import array as arr
 
# Tạo danh sách
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
 
# In các nhân tố của một mảng
# Dùng toán tử Slice 
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
 
# In các nhân tố từ điểm xác định trước tới cuối
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)
 
# In các nhân tố từ điểm bắt đầu tới cuối
Sliced_array = a[:]
print("Printing all elements using slice operation: ")
print(Sliced_array)

# %%
