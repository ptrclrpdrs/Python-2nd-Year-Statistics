user = eval(input('Enter hour: '))
day = input('Enter am (1) or pm (2): ')
hour = eval(input('How many hours ahead?: '))
hour += user
if hour > 24:
    print('Cannot convert that time.')
elif hour >= 1 and hour <= 12 and day == '1':
    print(f'New hour: {hour}', 'am')
    print()
elif hour >= 12 and hour <= 24 and day == '1':
    hour = hour - 12
    print(f'New hour: {hour}', 'pm')
    print()
elif hour >= 1 and hour <= 12 and day == '2':
    print(f'New hour: {hour}', 'am')
    print()
elif hour >= 12 and hour <= 24 and day == '2':
    hour = hour - 12
    print(f'New hour: {hour}', 'pm')
    print()