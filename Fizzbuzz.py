check = True
i = 0
while(check == True):
    i = i + 1
    if(i % 15 == 0):
        print('FizzBuzz')
    elif(i % 5 == 0):
        print('Buzz')
    elif(i % 3 == 0):
        print('Fizz')
    else:
        print(f"{i}")
    if(i == 100):
        check = False
