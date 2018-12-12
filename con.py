name = input('Hello, Whats your name? \n')
print(name, "Feel free to tell me what you would like converted")
print('Please be advised these are rough approximations')

convert = input('We can do pounds, ounces, kilograms, grams, stones, and tons \n')
while (convert != 'kilograms') and (convert != 'grams') and (convert != 'stones') and (convert != 'tons') and (convert != 'ounces') and (convert != 'pounds'):
        print('Please Give me a Valid Unit')
        convert = input()

if convert == ("pounds"):
    print('How Many Pounds')
    try:
        pounds = float(input())
    except:
        print('Please Give me a Valid Number')
        pounds = float(input())

    unit1 = input('Into What Unit Would you like to convert into \n')

    while (unit1 != 'kilograms') and (unit1 != 'grams') and (unit1 != 'stones') and (unit1 != 'tons') and (unit1 != 'ounces'):
        print('Please Give me a Valid Unit')
        unit1 = input()

    if unit1 == ('kilograms'):
        kilograms = pounds / 2.2
        print('The amount of pounds you entered is {}. \n'
              'This is {:.2f} kilograms'.format(pounds, kilograms))
    elif unit1 == ('grams'):
        grams= pounds * 453.592
        print('The amount of pounds you entered is {}. \n'
              'This is {:.2f} grams'.format(pounds, grams))
    elif unit1 == ('ounces'):
        ounces = pounds * 16
        print('The amount of pounds you entered is {}. \n'
              'This is {:.2f} ounces'.format(pounds, ounces))
    elif unit1 == ('stones'):
        stones = pounds / 14
        print('The amount of pounds you entered is {}. \n'
        'This is {:.2f} stones'.format(pounds, stones))
    elif unit1 == ('tons'):
        tons = pounds / 2000
        print('The amount of pounds you entered is {}. \n'
        'This is {:.2f} tons'.format(pounds, tons))

# Below I continue this method of creating a converter
# Now that initial setup has been done

elif convert == ("ounces"):
    print('How Many Ounces')
    try:
        ounces = float(input())
    except:
        print('Please Give me a Valid Number')
        ounces = float(input())

    unit1 = input('Into What Unit Would you like to convert into \n')

    while (unit1 != 'kilograms') and (unit1 != 'grams') and (unit1 != 'stones') and (unit1 != 'tons') and (unit1 != 'pounds'):
        print('Please Give me a Valid Unit')
        unit1 = input()

    if unit1 == ('kilograms'):
        kilograms = ounces / 35.274
        print('The amount of ounces you entered is {}. \n'
              'This is {:.2f} kilograms'.format(ounces, kilograms))
    elif unit1 == ('grams'):
        grams = ounces * 28.35
        print('The amount of ounces you entered is {}. \n'
              'This is {:.2f} grams'.format(ounces, grams))
    elif unit1 == ('pounds'):
        pounds = ounces / 16
        print('The amount of ounces you entered is {}. \n'
              'This is {:.2f} pounds'.format(ounces, pounds))
    elif unit1 == ('stones'):
        stones = ounces / 224
        print('The amount of ounces you entered is {}. \n'
        'This is {:.2f} stones'.format(ounces, stones))
    elif unit1 == ('tons'):
        tons = ounces / 32000
        print('The amount of ounces you entered is {}. \n'
        'This is {:.2f} tons'.format(ounces, tons))

elif convert == ("kilograms"):
    print('How Many Kilograms')
    try:
        kilograms = float(input())
    except:
        print('Please Give me a Valid Number')
        kilograms = float(input())

    unit1 = input('Into What Unit Would you like to convert into \n')

    while (unit1 != 'ounces') and (unit1 != 'grams') and (unit1 != 'stones') and (unit1 != 'tons') and (unit1 != 'pounds'):
        print('Please Give me a Valid Unit')
        unit1 = input()

    if unit1 == ('ounces'):
        ounces = kilograms * 35.274
        print('The amount of kilograms you entered is {}. \n'
              'This is {:.2f} ounces'.format(kilograms, ounces))
    elif unit1 == ('grams'):
        grams = kilograms * 1000
        print('The amount of kilograms you entered is {}. \n'
              'This is {:.2f} grams'.format(kilograms, grams))
    elif unit1 == ('pounds'):
        pounds = kilograms * 2.205
        print('The amount of kilograms you entered is {}. \n'
              'This is {:.2f} pounds'.format(kilograms, pounds))
    elif unit1 == ('stones'):
        stones = kilograms / 6.35
        print('The amount of kilograms you entered is {}. \n'
        'This is {:.2f} stones'.format(kilograms, stones))
    elif unit1 == ('tons'):
        tons = kilograms / 907.185
        print('The amount of kilograms you entered is {}. \n'
        'This is {:.2f} tons'.format(kilograms, tons))

elif convert == ("grams"):
    print('How Many grams')
    try:
        grams = float(input())
    except:
        print('Please Give me a Valid Number')
        grams = float(input())

    unit1 = input('Into What Unit Would you like to convert into \n')

    while (unit1 != 'ounces') and (unit1 != 'kilograms') and (unit1 != 'stones') and (unit1 != 'tons') and (unit1 != 'pounds'):
        print('Please Give me a Valid Unit')
        unit1 = input()

    if unit1 == ('ounces'):
        ounces = grams / 28.35
        print('The amount of grams you entered is {}. \n'
              'This is {:.2f} ounces'.format(grams, ounces))
    elif unit1 == ('kilograms'):
        kilograms = grams / 1000
        print('The amount of grams you entered is {}. \n'
              'This is {:.2f} kilograms'.format(grams, kilograms))
    elif unit1 == ('pounds'):
        pounds = grams / 453.592
        print('The amount of grams you entered is {}. \n'
              'This is {:.2f} pounds'.format(grams, pounds))
    elif unit1 == ('stones'):
        stones = grams / 6350.293
        print('The amount of grams you entered is {}. \n'
        'This is {:.2f} stones'.format(grams, stones))
    elif unit1 == ('tons'):
        tons = grams / 907184.74
        print('The amount of grams you entered is {}. \n'
        'This is {:.2f} tons'.format(grams, tons))

elif convert == ("stones"):
    print('How Many stones')
    try:
        stones = float(input())
    except:
        print('Please Give me a Valid Number')
        stones = float(input())

    unit1 = input('Into What Unit Would you like to convert into \n')

    while (unit1 != 'ounces') and (unit1 != 'kilograms') and (unit1 != 'grams') and (unit1 != 'tons') and (unit1 != 'pounds'):
        print('Please Give me a Valid Unit')
        unit1 = input()

    if unit1 == ('ounces'):
        ounces = stones * 224
        print('The amount of stones you entered is {}. \n'
              'This is {:.2f} ounces'.format(stones, ounces))
    elif unit1 == ('kilograms'):
        kilograms = stones * 6.35
        print('The amount of stones you entered is {}. \n'
              'This is {:.2f} kilograms'.format(stones, kilograms))
    elif unit1 == ('pounds'):
        pounds = stones * 14
        print('The amount of stones you entered is {}. \n'
              'This is {:.2f} pounds'.format(stones, pounds))
    elif unit1 == ('grams'):
        grams = stones * 6350.293
        print('The amount of stones you entered is {}. \n'
        'This is {:.2f} grams'.format(stones, grams))
    elif unit1 == ('tons'):
        tons = stones / 142.857
        print('The amount of stones you entered is {}. \n'
        'This is {:.2f} tons'.format(stones, tons))

elif convert == ("tons"):
    print('How Many tons')
    try:
        tons = float(input())
    except:
        print('Please Give me a Valid Number')
        tons = float(input())

    unit1 = input('Into What Unit Would you like to convert into \n')

    while (unit1 != 'ounces') and (unit1 != 'kilograms') and (unit1 != 'grams') and (unit1 != 'stones') and (unit1 != 'pounds'):
        print('Please Give me a Valid Unit')
        unit1 = input()

    if unit1 == ('ounces'):
        ounces = tons * 32000
        print('The amount of tons you entered is {}. \n'
              'This is {:.2f} ounces'.format(tons, ounces))
    elif unit1 == ('kilograms'):
        kilograms = tons * 907.185
        print('The amount of tons you entered is {}. \n'
              'This is {:.2f} kilograms'.format(tons, kilograms))
    elif unit1 == ('pounds'):
        pounds = tons * 2000
        print('The amount of tons you entered is {}. \n'
              'This is {:.2f} pounds'.format(tons, pounds))
    elif unit1 == ('grams'):
        grams = tons * 907184.74
        print('The amount of tons you entered is {}. \n'
        'This is {:.2f} grams'.format(tons, grams))
    elif unit1 == ('stones'):
        stones = tons * 142.857
        print('The amount of tons you entered is {}. \n'
        'This is {:.2f} stones'.format(tons, stones))

print('Thank You and Have A Great Day!')
