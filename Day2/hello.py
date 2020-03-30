import time


def n_th_term_of_fibanocci(n):
    if n in (1, 2):
        return 1
    else:
        return n_th_term_of_fibanocci(n-1) + n_th_term_of_fibanocci(n-2)


# Added this comment
n = int(input("Enter number of lines: "))
if n > 0:
    for line in range(1, n+1):
        x = int((line-1)*line/2) + 1
        y = int((line+1)*line/2) + 1
        for z in range(x, y):
            print(n_th_term_of_fibanocci(z), end=" ")
        print("\n")
else:
    print("Please enter positive values")
