# Aula 09 - Fibonacci: recursivo (exponencial) x linear
import timeit

def fib(n):
    """A função Fibonacci recursiva. O(2^n)"""
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(N):
    """Fibonacci com laço. O(n)"""
    if N <= 0:
        return "O valor de N deve ser maior que 0"
    elif N == 1:
        return 1
    elif N == 2:
        return 1

    sum, first, second = 1, 1, 1
    count = 3

    while count <= N:
        sum = first + second
        first = second
        second = sum
        count += 1

    return sum

def fib2(n):
    # mostra os n primeiros números: O(n) * O(n) = O(n^2)
    for i in range(1, n + 1):
        fibonacci(i)
    return

if __name__ == "__main__":
    print([fib(i) for i in range(1, 11)])
    print([fibonacci(i) for i in range(1, 11)])

    # equivalente ao %timeit do notebook
    t1 = timeit.timeit(lambda: fib(20), number=100) / 100
    t2 = timeit.timeit(lambda: fib2(20), number=100) / 100
    print(f"fib(20)  recursivo : {t1*1e6:.1f} µs")
    print(f"fib2(20) linear    : {t2*1e6:.1f} µs")
