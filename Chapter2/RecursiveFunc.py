def Recursive(num):
    if num <= 0:
        return
    print(f"Recursive call! {num}")
    Recursive(num - 1)


def main():
    Recursive(3)


if __name__ == "__main__":
    main()