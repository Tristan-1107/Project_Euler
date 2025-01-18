def main():
    a, b = 0, 1  # Les deux premiers nombres de Fibonacci
    sum = 0 

    while b <= 4000000:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b  # Calcul des deux prochains nombres de Fibonacci

    print(sum)

if __name__ == "__main__":
    main()
