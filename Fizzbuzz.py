check = True
i = 0
while(check == True):
    i = i + 1
    if(i % 15 == 0):
        print('FizzBuzz\n')
    elif(i % 5 == 0):
        print('Buzz\n')
    elif(i % 3 == 0):
        print('Fizz\n')
    else:
        print(f"{i}\n")
    if(i == 100):
        check = False
