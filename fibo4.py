def fib(n):
    """ Calculates the n-th Fibonacci number iteratively """
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print("Test for the fib function was successful!")
    else:
        print("The fib function is returning wrong values!")