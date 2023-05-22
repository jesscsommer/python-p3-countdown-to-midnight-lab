import time

def countdown(integer):
    while integer >= 1:
        print(f'{integer} SECOND(S)!')
        integer -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(integer):
    while integer >= 1:
        print(f'{integer} SECOND(S)!')
        time.sleep(1)
        integer -= 1
    print('HAPPY NEW YEAR!')

