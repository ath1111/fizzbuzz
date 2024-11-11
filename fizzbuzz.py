print("fizzbuzz!")
print("~~~~~~~~~~~~~~~~~~~")
x = 1
while x < 1000:
    if (x % 3) == 0:
        if (x % 5) ==0:
            print("fizzbuzz" , x)
        else:
            print("fizz" , x)
    elif (x % 5) == 0:
        print("buzz" , x)
        
    x = x + 1
