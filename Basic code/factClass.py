class Factorial:
    def Fact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f
n = 50

ob = Factorial()
print("\nFactorial of", n, "=", ob.Fact(n))
