def Fibo(n):
    if n <= 1:
        return n
    else:
        return Fibo(n - 1) + Fibo(n - 2)


def Fibo2(n):
    print(f"func call param {n}")
    if n <= 1:
        return n
    else:
        return Fibo2(n - 1) + Fibo2(n - 2)


def main():
    for i in range(15):
        print(Fibo(i), end=' ')
    print()


if __name__ == "__main__":
    main()
    print()
    Fibo2(7)

