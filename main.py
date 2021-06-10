# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Enter your name:')
    name = input()
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Do you want to play a game?')
    answer = input()
    if answer == 'yes' or 'y' or 'ye' :
        print("ok, let's go...")
        print('please enter range, (two numbers)')
        print('the second number must be greater than the first')
        num1 = int
        num2 = int
        while True:
            try:
                num1 = int(input())
                num2 = int(input())
                break
            except Exception:
                print('you must enter integer')
        print('loading...')
        num = randint(num1, num2)
        print('can you guess the number')
        nu = int
        while nu != num:
            while True:
                try:
                    nu = int(input())
                    break
                except Exception:
                    print('you must enter integer')
            if nu == num:
                print('Yes, you win!!')
            elif nu > num:
                print('the number you are looking for is less than the number you entered')
            elif nu < num:
                print('the number you are looking for is greater than the number you entered')

    elif answer == 'no' or 'No' or 'NO' or 'nO':
        print(f'By, by , {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('name')

