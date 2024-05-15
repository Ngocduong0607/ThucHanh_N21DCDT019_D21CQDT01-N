def fibonacci(n): 
    assert n >= 0 and int(n) == n
    fib_de_quy = []
    for i in range(n+1):
        if i in [0, 1]:
            fib_de_quy.append(i)
        else:
            fib_de_quy.append(fib_de_quy[-1] + fib_de_quy[-2])
    return fib_de_quy
def fibonacci_ko_de_quy(n):
    assert n >= 0 and int(n) == n, 'The number must be a non-negative integer only!'
    if n in [0, 1]:
        return n

    a, b, c = 0, 1, 0
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c
n = int(input("Nhập số nguyên dương n = "))   
print("{Đệ Quy} Dãy Fibonacci cho đến số thứ", n, "là:")
print(fibonacci(n))
print("{không đệ quy}Dãy Fibonacci cho đến số thứ", n, "là:")
x= [fibonacci_ko_de_quy(i) for i in range(n+1)]
print(x)