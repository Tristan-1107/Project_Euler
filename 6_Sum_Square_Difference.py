def square(n):
    return n*n

def main():
    sum1 = 1
    sum2 = 0
    for i in range(1,100, 1):
        sum1 = sum1 + square(i+1)
    
    for j in range(1,101,1):
        sum2 += j
    sum2 = square(sum2)

    print(sum2 - sum1)

if __name__ == "__main__":
    main()