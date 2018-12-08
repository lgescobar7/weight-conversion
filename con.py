
name = input('Hello, Whats your name? \n')
print( name, "Feel free to tell me what you would like converted ")
print('Please be advised these are rough approximations')
convert = input('We can do pounds, ounces, kilograms, grams, stones, and tons \n')

if convert == ("pounds"):
    print('How Many Pounds')
    pounds = int(input())
    kilograms = pounds / 2.2
    grams = kilograms * 1000
    ounces = pounds * 16
    stones = pounds / 14
    tons = pounds / 2000
    print('The amount of pounds you entered is {}. \n'\
          'This is {} kilograms \n{} grams \n{} ounces \n{} stones \n{} tons'.format(pounds, kilograms, grams, ounces, stones, tons))

if convert == ("ounces"):
    print('How Many Ounces')
    ounces = int(input())
    kilograms = ounces / 35.274
    grams = ounces * 28.35
    pounds = ounces / 16
    stones = ounces / 224
    tons = ounces / 32000
    print('The amount of Ounces you entered is {}. \n'\
          'This is {} kilograms \n{} grams \n{} pounds \n{} stones \n{} tons'.format(ounces, kilograms, grams, pounds, stones, tons))

if convert == ("kilograms"):
    print('How Many Kilograms')
    kilograms = int(input())
    ounces = kilograms * 35.274
    grams = kilograms * 1000
    pounds = kilograms * 2.205
    stones = kilograms / 6.35
    tons = kilograms / 907.185
    print('The amount of Kilograms you entered is {}. \n'\
          'This is {} ounces \n{} grams \n{} pounds \n{} stones \n{} tons'.format(kilograms, ounces, grams, pounds, stones, tons))



if convert == ("grams"):
    print('How Many Grams')
    grams = int(input())
    ounces = grams / 28.35
    kilograms = grams / 1000
    pounds = grams / 453.592
    stones = grams / 6350.293
    tons = grams /  907184.74
    print('The amount of Grams you entered is {}. \n'\
          'This is {} ounces \n{} kilograms \n{} pounds \n{} stones, \n{} tons'.format(grams, ounces, kilograms, pounds, stones, tons))



if convert == ("stones"):
    print('How Many Stones')
    stones = int(input())
    ounces = stones * 224
    kilograms = stones * 6.35
    pounds = stones * 14
    grams = stones * 6350.293
    tons = stones / 142.857
    print('The amount of Stones you entered is {}. \n'\
          'This is {} ounces \n{} kilograms \n{} pounds \n{} grams \n{} tons'.format(stones, ounces, kilograms, pounds, stones, tons))


if convert == ("tons"):
    print('How Many Tons')
    tons = int(input())
    ounces = tons * 32000
    kilograms = tons * 907.185
    pounds = tons * 2000
    grams = tons * 907184.74
    stones = tons * 142.857
    print('The amount of Tons you entered is {}. \n'\
          'This is {} ounces \n{} kilograms \n{} pounds \n{} grams \n{} stones'.format(tons, ounces, kilograms, pounds, grams, stones))
