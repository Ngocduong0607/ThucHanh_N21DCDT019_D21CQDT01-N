def Phanloaiso(n):
    sum_of_divisors = 1 

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:  
                sum_of_divisors += n // i


    if sum_of_divisors < n:
        return "deficient"
    elif sum_of_divisors == n:
        return "perfect"
    else:
        return "abundant"

def number_classification(x, y):
    if x <= 0 or y <= 0 or x > y:
        print("Vui lòng nhập hai số nguyên dương x và y sao cho x ≤ y ")
        return

    print("Phân loại các số từ", x, "đến", y)
    for num in range(x, y + 1):
        classification = Phanloaiso(num)
        print(f"{num} là số {classification}")

x = int(input("Nhập vào số nguyên dương x : "))
y = int(input("Nhập vào số nguyên dương y (x ≤ y) : "))
number_classification(x, y)