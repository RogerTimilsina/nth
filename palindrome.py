# code to check palindrome

def check(num: int) -> bool:
    n: int = num
    rev: int = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    if rev == num:
        return True
    return False


x = int(input("Enter a number"))
if check(x):
    print("Palindrome")
else:
    print("Not palindrome")
