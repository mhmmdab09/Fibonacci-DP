def fibonacciCal(num):
    fib= [0,1,1]
    if num < 0:
        return "wrong input"
    elif num < 3:
        return fib[num]
    else:
        place = 2
        while num > place:
            fib.append(fib[place - 1] + fib[place])
            place = place + 1
        return fib[num]




number = int(input("which number do you want ? : "))
print(fibonacciCal(number))