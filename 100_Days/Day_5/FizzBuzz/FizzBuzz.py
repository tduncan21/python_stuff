def fizz_buzz(num):
    div_by_three = "Fizz"
    div_by_five = "Buzz"
    div_by_both = div_by_three + div_by_five

    if num % 3 == 0 and num % 5 == 0:
        #output FizzBuzz
        output(div_by_both)
    elif num % 3 == 0:
        #output Fizz
        output(div_by_three)
    elif num % 5 == 0:
        #output Buzz
        output(div_by_five)
    else:
        #output number
        output(str(num))
    return


def output(text):
    print(text)
    return


for num in range(1, 101):
    fizz_buzz(num)