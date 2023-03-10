#Problem 3
def sum_n(n):
    while 1<=n:
        sum = 0
        total = 0
        sum += n
        n = n-1
        total = sum+n
        print(total)
        
sum_n(4)


#Problem 4
def fibonacci(n):
    if n>0:
        fibonacci(n)==fibonacci(n-1)+fibonacci(n-2)
        return fibonacci(n)
    else:
        print("That integer is not positive.")
print(fibonacci(10))
