title='''
██████╗░░█████╗░████████╗███████╗  ██████╗░███████╗████████╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔════╝  ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║░░██║███████║░░░██║░░░█████╗░░  ██║░░██║█████╗░░░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
██║░░██║██╔══██║░░░██║░░░██╔══╝░░  ██║░░██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██████╔╝██║░░██║░░░██║░░░███████╗  ██████╔╝███████╗░░░██║░░░███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
By Adithya Manjunath (github.com/Cr4zySh4rk/DateDetection'''
import datetime
import re
print(title)
now = datetime.datetime.now()
current_year = now.year
months = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September',
    '10': 'October', '11': 'November', '12': 'December', '1': 'January',
    '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
    '7': 'July', '8': 'August', '9': 'September'
}
invalid_dates = {}
missing_zero = {}
def detect_date(text):
    with open(f'{text}') as file_obj:
        content = file_obj.read()
        date_regex = re.compile(r'[\d]{1,2}/[\d]{1,2}/[\d]{2,4}')
        dates = date_regex.findall(content)
    return dates
def validate_date(list_of_dates):
    """Check if the dates in list are valid which means:
        example: ==> February has 29 or 28 days depending on the year, etc
    """
    if len(list_of_dates) == 0:
        print('There is no date detected!')
    else:
        for _ in list_of_dates:
            day, month, year = _.split('/')

            if int(day) in range(1, 10) and len(day) == 1:
                missing_zero[_] = (
                    f'0{day}/0{month}/{year}'
                    if int(month) in range(1, 10) and len(month) == 1
                    else f'0{_}'
                )

            elif int(month) in range(1, 10) and len(month) == 1:
                missing_zero[_] = f'{day}/0{month}/{year}'

            if month not in months.keys():
                invalid_dates[_] = f'The month {month} doesn\'t exist'

            elif month in ['01', '03', '05', '07', '08', '10', '12']:
                if int(day) > 31:
                    invalid_dates[_] = f'{months[month]} can\'t have more' \
                                       f' than 31 days'

            elif month in ['04', '06', '09', '11']:
                if int(day) > 30:
                    invalid_dates[_] = f'{months[month]} can\'t have more' \
                                       f' than 31 days'

            elif month == '02':
                if int(year) % 4 == 0:
                    if int(day) > 29:
                        invalid_dates[_] = f'{months[month]} can\'t have ' \
                                           f' more than 29 days' \
                                           f' when it is a leap year'
                elif int(day) > 28:
                    invalid_dates[_] = f'{months[month]} can\'t have ' \
                                       f'more than 29 days ' \
                                       f'when it is not a leap year'

            if int(year) < 1000 or int(year) > 2999:
                invalid_dates[_] = f'The year {year} is invalid' \
                                   f'(it is between 1000 - 2999)'

    for _ in invalid_dates.keys():
        if _ in list_of_dates:
            list_of_dates.remove(_)

    for _, value in missing_zero.items():
        if _ in list_of_dates:
            list_of_dates.remove(_)
    for value in missing_zero.values():
        list_of_dates.append(value)

file = input('Enter a .txt file to detect dates inside it: ')
dates_list = detect_date(file)
validate_date(dates_list)
if len(invalid_dates) > 0:
    print('WARNING'.center(13, '!'))
    print('Some dates detected are invalid..')
    print('\nInvalid dates : \n')
    for _, reason in invalid_dates.items():
        print(_, '==>', reason)
    print('\nValid dates detected : \n')
    for _ in dates_list:
        print(_, sep=', ')
else:
    print('List of the dates detected are : ')
    for _ in dates_list:
        print(_)