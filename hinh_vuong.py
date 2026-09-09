import turtle

# turtle là một thư viện trong Python dùng để vẽ đồ họa, đặc biệt là các hình học cơ bản như hình vuông, hình tròn, v.v.
# Tạo một cây bút vẽ
pen = turtle.Turtle()

# Tùy chỉnh (không bắt buộc)
pen.shape("turtle")  # Đổi hình dáng bút thành con rùa
pen.color("blue")  # Đổi màu nét vẽ thành màu xanh
pen.pensize(3)  # Độ dày của nét vẽ

# Vòng lặp để vẽ 4 cạnh của hình vuông
for i in range(4):
    pen.forward(100)  # Đi thẳng 100 pixel (chiều dài cạnh)
    pen.right(90)  # Xoay phải 90 độ (góc vuông)

# Giữ cửa sổ không bị tắt ngay sau khi vẽ xong
turtle.done()

# %%
import turtle

pen = turtle.Turtle()
pen.color("red")
pen.pensize(4)

canh = int(input("Nhập độ dài cạnh hình vuông: "))

for i in range(4):
    pen.forward(canh)
    pen.right(90)

turtle.done()
# %%
n = 5  # Kích thước cạnh của hình vuông (số lượng dấu sao)

# Vòng lặp in ra n hàng
for i in range(n):
    # Vòng lặp in ra n dấu sao trên mỗi hàng
    for j in range(n):
        print("* ", end="")  # In dấu sao và giữ con trỏ ở cùng một dòng
    print()  # Xuống dòng khi in hết 1 hàng

# %%
