import time

t = int(input('Enter time in seconds: '))
for x in reversed(range(1, t+1)):
    sec_ = x % 60
    min_ = int(x / 60) % 60
    hours_ = int(x / 3600)
    print(f'{hours_:02}:{min_:02}:{sec_:02}')
    time.sleep(1)

print('Time\'s up!')
