def main():
    sum = 0

    for i in range(1000):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i

    print(sum)

if __name__ == "__main__":
    main()