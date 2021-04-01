def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)


def main():
    print(f"1! = {Factorial(1)}")
    print(f"2! = {Factorial(2)}")
    print(f"3! = {Factorial(3)}")
    print(f"4! = {Factorial(4)}")
    print(f"9! = {Factorial(9)}")


if __name__ == "__main__":
    main()