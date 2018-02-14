import timeit


sepnums = "-".join(str(n) for n in range(100))
print(sepnums)

timeit.timeit(' "-".join(str(n) for n in range(100))', number=10000)
