def fibo_recursive(n:int) -> int:
    """На вход подаётся целое число. Функиця рекурсивно вычисляет число Фиббоначи для данного числа и возвращает его"""
    if n in (1,2):
        return 1
    return fibo_recursive(n-1)+fibo_recursive(n-2)

def fibo(n:int)->int:
    """На вход подаётся целое число. Функиця вычисляет число Фиббоначи для данного числа и возвращает его"""
    n1=1
    n2=1
    fib3=0
    if n in (1,2):
        return 1
    else:
        for i in range(n-2):
            fib3 = n1 + n2
            n1 = n2
            n2 = fib3
        return fib3
def factorial(n:int) -> int:
    """На вход подаётся целое число. Функция возвращает факториал данного числа"""
    k=1
    for i in range(1,n+1):
        k=k*i
    return k

def factorial_recursive(n:int) -> int:
    """На вход подаётся целое число. Функция возвращает факториал данного числа. Вычисления производятся за счёт рекурсии"""
    if n==1:
        return 1
    else:
        return factorial_recursive(n-1)*n

