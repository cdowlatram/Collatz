def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

while True:
    print('Please enter a number.')
    try:
        userInt = int(input())
        while userInt != 1:
            userInt = collatz(userInt)
            print(userInt)
        if userInt == 1:
            break
    except:
        print('Error: Invalid Value. You did not enter an integer.')
