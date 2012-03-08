#Problem 4: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99. Find the largest palindrome made from the product of two 3-digit numbers. 

# returns whether a number is palindromic or not
def isPalindrome(n):
            s = str(n)
            return s == s[::-1]

largest = 0
for a in range(100, 1000):
            for b in range(100,1000):
                        if isPalindrome(a * b) and (a*b) > largest:
                                    largest = a * b
print largest