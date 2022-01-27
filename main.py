'''
A recursive solution with complexity of:
O(Φ^n) where Φ = (√5 + 1)/2
fib(n) = {
    0                       n=0
    1                       n=1
    fib(n-2) + fib(n-1)     if n>1
}
'''
def fib_recursive(n:int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 2) + fib_recursive(n - 1)

'''
A dynamic programming approach.
'''
def fib_dynamic(n:int) -> int:
    if n <= 1:
        return n
    # populate indices 0 and 1
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i-2] + F[i-1])
    return F[n]

if __name__ == '__main__':
    print(fib_recursive(9))
    print(fib_dynamic(9))