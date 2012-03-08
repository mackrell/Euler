# Problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def primesTo(n):
            p = []
            for i in range(1,n+1):
                        if isPrime(i):
                                    p.append(i)
            return p

def isPrime(n):
            if n == 1:
                        return False
            else:
                        for x in range(2,int(n**0.5)+1):
                                    if n%x == 0:
                                                return False
            return True
            
def product(p):
            if len(p) == 0:
                        return 0
            results = 1
            for e in p:
                        e = int(e)
                        results = results * e
            return results

p = primesTo(20)
p = p + [2, 2, 3, 2]
print product(p)