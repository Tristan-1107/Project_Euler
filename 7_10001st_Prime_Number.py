n = 10001

prime_arr = [None]*n
prime_arr[0] = 2

p = 3
j = 1

while(prime_arr[n-1] == None):
    i = 0
    prime = 1
    while(prime_arr[i] is not None):
        if p % prime_arr[i] == 0:
            prime = 0
            break
        i += 1

    if prime == 1:
        prime_arr[j] = p
        j += 1
    p += 1

print(prime_arr[10000])
