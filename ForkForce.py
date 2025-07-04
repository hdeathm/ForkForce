# اگر این کامنت رو میبینی یعنی ریپازیتوری رو کلون کردی روی ادیتورت. 
#  n حالا این زیر 👇🏻 یک تابع بنویس که یک عدد ورودی 
#  بگیره و یک عملیات ریاضی به دلخواه روش انجام بده و مقدار نهایی رو برگردونه.

    
# Defined by Asle Falah
def power_if_prime(n):
  
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return n ** 2  
    else:
        return n

      
def exp(x):
    f = 1
    if x < 0:
        x = (-1) * x
        f = -1
    xs = 1
    nm = 1
    ex = 1
    for i in range(1 , x * 18):
        xs *= x
        nm *= i
        ex += (xs / nm)
    if f == -1:
        ex = 1 / ex
    return ex




# defined by Abolfazl 
def powerOfTwo(n):
    return 2**n


    
# defined by ali,kamalpour
def logarithm(n, base=10):
    if n <= 0:
        return None
    result = 0
    current = n
    while current >= base:
        current /= base
        result += 1
    return result

