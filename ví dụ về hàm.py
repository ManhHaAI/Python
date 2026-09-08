qtm_str = 'Python'

# enumerate()
qtm_enum = list(enumerate(qtm_str))

# Output: list(enumerate(qtm_str) = [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
print('list(enumerate(qtm_str) = ', qtm_enum)

# default(implicit) order
thu_tu_mac_dinh = "{}, {} và {}".format('Quản','Trị','Mạng')
print('\n--- Thứ tự mặc định ---')
print(thu_tu_mac_dinh)

# sử dụng đối số vị trí để sắp xếp thứ tự
vi_tri_thu_tu= "{1}, {0} và {2}".format('Quản','Trị','Mạng')
print('\n--- Thứ tự theo vị trí ---')
print(vi_tri_thu_tu)

# sử dụng từ khóa để sắp xếp thứ tự
tu_khoa_thu_tu = "{s}, {b} và {j}".format(j='Quản',b='Trị',s='Mạng')
print('\n--- Thứ tự theo từ khóa ---')
print(tu_khoa_thu_tu)