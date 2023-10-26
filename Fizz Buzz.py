#Write a python program that prints the numbers from 1 to 100. But for multiples of seven, print "Fizz" instead of the number, 
#and for the multiples of three, print "Buzz". For numbers which are multiples of both three and seven, print "FizzBuzz".

for i in range(1,101):
    if i%3 ==0 and i%7==0:
        print("fizzbuzz")
    elif i%7==0:
        print("Fizz")
    elif i%3==0:
        print("Buzz")
    else:
        print(i)