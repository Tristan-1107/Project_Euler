i = 2520
j = 1
divisible = 0
while(divisible == 0):
    for j in range(1,21, 1):
        if i % j != 0:
            break
        elif j == 20:
            divisible = 1
            print(i)
        else: 
            continue
    i += 20
