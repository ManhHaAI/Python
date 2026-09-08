a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print (x) # Output: [['a', 'b', 'c'], [1, 2, 3]]
print (x[0]) # Output: ['a', 'b', 'c']
print(x[0][1]) # Output: b

squares = [1, 4, 9, 16, 25]
print(squares) # Output: [1, 4, 9, 16, 25]  

qtm_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
# Output: q
print(qtm_list[0])

# Output: a
print(qtm_list[2])

# Output: t
print(qtm_list[4])

# List lồng nhau
ln_list = ["Happy", [1,3,5,9]]

# Index lồng nhau

# Output: a
print(ln_list[0][1])

# Output: 9
print(ln_list[1][3])

qtm_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']

# Code by Quantrimang.com
# Output: m
print(qtm_list[-1])
# Output: i
print(qtm_list[-9])

#%%
cubes = [1, 8, 27, 65, 125] # Note that 4**3 is 64, not 65
cubes[3] = 64  # Replace the wrong value
print(cubes) # Output: [1, 8, 27, 64, 125]

cubes.append(216) # thêm lập phương của 6
cubes.append(7**3) # thêm lập phương của 7
print(cubes) # Output: [1, 8, 27, 64, 125, 216, 343]


# %%
a = 2
b = 3
sum = a + b
print(sum) # Output: 5

# %%
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Output: ['c', 'd', 'e']
print(letters[2:5]) 

# %%
letters[2:5] = ['x', 'y', 'z']  
# thay thế vài giá trị
print(letters) # Output: ['a', 'b', 'x', 'y', 'z', 'f', 'g']

# %%
letters = ['a', 'b', 'c', 'd']
len(letters) # Output: 4

# %%
my_list = ['p','r','o','g','r','a','m','i','z']
del my_list[2] # xóa phần tử thứ 2
print(my_list) # Output: ['p', 'r', 'g', 'r', 'a', 'm', 'i', 'z']

# %%
my_list = ['p','r','o','g','r','a','m','i','z']
del my_list[5:7] # xóa phần tử từ 5 đến 6
print(my_list) # Output: ['p', 'r', 'o', 'g', 'r', 'i', 'z']

# %%
my_list = ['q','u','a','n','t','r','i','m','a','n','g','.','c','o','m']
# xóa phần tử có index từ 1 đến 6
del my_list[1:7]

# Output: ['q', 'm', 'a', 'n', 'g', '.', 'c', 'o', 'm']
print(my_list)

# %%
QTM = [9,8,7,6,8,5,8]

# Output: 2
print(QTM.index(7))

# Output: 3
print(QTM.count(8))

QTM.sort()

# Output: [5, 6, 7, 8, 8, 8, 9]
print(QTM)

QTM.reverse()

# Output: [9, 8, 8, 8, 7, 6, 5]
print(QTM)
# %%
cub3 = [3 ** x for x in range(9)]

# Output: [1, 3, 9, 27, 81, 243, 729, 2187, 6561]
print(cub3)
# %%
cub3 = []
for x in range (9):
    cub3.append(3**x)
print(cub3)

# %%
for ngon_ngu in ['Python', 'C', 'Java']:
    print('Tôi thích Ngôn ngữ lập trình:', ngon_ngu)

# %%
letters = ['a', 'b', 'c', 'd']
print(letters)

upper_letters = []
for letter in letters:
    result = letter.upper()
    upper_letters.append(result)

print(upper_letters)

# %%
letters = ['a', 'b', 'c', 'd']
print(letters)
# sử dụng List Comprehension
upper_letters = [x.upper() for x in letters]

print(upper_letters)


# %%
ages = [1, 34, 5, 7, 3, 57, 356]
print(ages)
# in danh sách các phần tử lớn hơn 50
old_ages = [x for x in ages if x > 50]
print(old_ages)

# %%
