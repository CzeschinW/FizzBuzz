#Runs while loop until changes
check = True

#index number to increment that is printed and used to chaeck for divisors
i = 0

#While loop for code that will run until "check" is made false
while(check == True):
    #increment "i" by one each time the loop is run
    i = i + 1

    # checks to see if i ÷ 15 = 0, if true then prints FizzBuzz
    if(i % 15 == 0):
        print('FizzBuzz\n')

    #checks to see if i ÷ 5 = 0, if true then prints FizzBuzz
    elif(i % 5 == 0):
        print('Buzz\n')

    #checks to see if i ÷ 3 = 0, if true then prints FizzBuzz
    elif(i % 3 == 0):
        print('Fizz\n')

    #if i ÷ 15, 5, or 3 does not = 0 then it will print i
    else:
        print(f"{i}\n")

    #checks to see if i = 100, if not it continues the loop, once i = 100 "check" becomes false which will end the loop
    if(i == 100):
        check = False
