import random

def dice():
    print('What is your name?')
    name = input()
    print(f'Hello, {name}!')
    print('Rolling dice...')
    l = [1, 2, 3, 4, 5, 6]
    sum = 0
    for i in range(2):
        r = random.choice(l)
        print(f'Die {i}: {r}')
        sum+=r
    print(f'Total value: {sum}')

if __name__ == '__main__':
    dice()