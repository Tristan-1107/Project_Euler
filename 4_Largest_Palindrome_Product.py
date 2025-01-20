def EstPalindrome(n):
    n_str = str(n)
    i = 0
    j = len(n_str)-1
    while(i<=j):
        if n_str[i] == n_str[j]:
            i += 1
            j -= 1
        else:
            return 0
    return 1

def main():
    b = 0
    max_a = 0
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            if EstPalindrome(i*j) == 1:
                max_a = max(max_a, i*j)
    
    print(max_a)

if __name__ == "__main__":
    main()





    
