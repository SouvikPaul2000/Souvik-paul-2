class Palindrome:
    def Pal(self, n):
        l=n[::-1]
        if n==l:
           return print("yes its a palindrome")
        else:
           return print("no its not a palindrome")
        
n = "malayalam"

ob = Palindrome()
print(ob.Pal(n))
