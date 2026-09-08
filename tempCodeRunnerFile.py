cubes = [1, 8, 27, 65, 125] # Note that 4**3 is 64, not 65
cubes[3] = 64  # Replace the wrong value
print(cubes) # Output: [1, 8, 27, 64, 125]

cubes.append(216) # thêm lập phương của 6
cubes.append(7**3) # thêm lập phương của 7
print(cubes) # Output: [1, 8, 27, 64, 125, 216, 343]