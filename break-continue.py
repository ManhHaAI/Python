# %%
# Sử dụng break trong for

for val in "quantrimang":
    if val == "m":
        break
    print(val)

print("Kết thúc!")

# %%
# Ví dụ sử dụng break trong while trên QuanTriMang:

bien = 10
while bien > 0:
    print("Giá trị biến hiện tại là: ", bien)
    bien = bien - 1
    if bien == 5:
        break

print("OK!")

# %%
# Sử dụng continue trong for

for val in "quantrimang":
    if val == "m":
        continue
    print(val)

print("Kết thúc!")

# %%
# Ví dụ sử dụng continue trong while trên QuanTriMang:
bien = 10
while bien > 0:
    bien = bien - 1
    if bien == 5:
        continue
    print("Giá trị biến hiện tại là: ", bien)
print("OK!")

# %%
