def Pascal(n):
    for i in range(n + 1):
        print(f"n={i}", end=" ")
        he_so= 1
        for j in range(1, i + 2):
            print(he_so, end=" ")
            he_so = he_so * (i - j + 1) // j
        print()

n = int(input("Nhập số nguyên dương n : "))
if n < 0:
    print("n phải là số nguyên dương ")
else:
    print("Tam giác Pascal ứng với bậc", n, "là:")
    Pascal(n)
