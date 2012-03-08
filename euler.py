#Functions for prime numbers

# returns whether n is prime or not
def isPrime(n):
            if n == 1:
                        return False
            else:
                        for x in range(2,int(n**0.5)+1):
                                    if n%x == 0:
                                                return False
            return True
            
# returns the first n prime numbers
def primes(n):
            primes = []
            count = 0
            i = 1
            while count < n:
                        if isPrime(i):
                                    primes.append(i)
                                    count = count +1
                        i = i + 1
            return primes
            
# return prime numbers up to n
def primesTo(n):
            p = []
            for i in range(1,n+1):
                        if isPrime(i):
                                    p.append(i)
            return p

# return the nth prime number
def prime(n):
            return primes(n)[-1]


# returns the first n numbers of the Fibonacci sequence
def fib(n):
            a, b = 1, 2
            i = 0
            results = []
            while i < n:
                        a, b = b, a + b
                        results.append(b)
                        i += 1                       
            return results


# return the factors of a number
def factorize(n):
            factors = []
            if n <= 1:
                        return factors
            else:
                        for x in range(1,int(n**0.5)+1):
                                    if n % x == 0:
                                                factors.append(x)
                                    for e in factors[1:]:
                                                if n % e == 0 and n/e not in factors:
                                                            factors.append(n/e)
            return factors

# returns whether a number is perfect or not
def isPerfect(n):
    return n == sum(factorize(n))
    
# returns whether a number is deficient or not
def isDeficient(n):
    return n > sum(factorize(n))
    
# returns whether a number is abundant or not
def isAbundant(n):
    return n < sum(factorize(n))
            
# return the prime factors of a number
def primeFactorize(n):
            factors = []
            if n == 1:
                        return
            else:
                        for x in range(2,int(n**0.5)+1):
                                    if n%x == 0 and isPrime(x):
                                                factors.append(x)
                     
            return factors
            
            
# returns whether a number is palindromic or not
def isPalindrome(n):
            s = str(n)
            return s == s[::-1]
            
# returns the product of items in a list
def product(p):
            if len(p) == 0:
                        return 0
            results = 1
            for e in p:
                        e = int(e)
                        results = results * e
            return results
            
# converts a string to a list
def string_to_list(s):
            p = []
            i = 0
            while i < len(s):
                        p.append(s[i])
                        i = i + 1
            return p
            