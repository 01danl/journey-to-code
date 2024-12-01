a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
else:
    if a == 0:
        if b == pow(c,2):
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")

    else:
        if (pow(c,2) -b) % a == 0:
            x = (pow(c,2) - b) // a 
            if a * x + b >= 0:
                print(x)
            else:
                print("NO SOLUTION")

        else:
            print("NO SOLUTION")
