def main():
    arr = [0 for _ in range(10)]
    readCount = 0

    while True:
        readData = int(input("자연수 입력 : "))
        if readData < 1:
            break

        arr[readCount] = readData
        readCount += 1

    for i in range(readCount):
        print(arr[i], end=' ')


if __name__ == '__main__':
    main()