## miles and kilometers
def print_menu():
    print('1. Convert kilometers to miles')
    print('2. Convert miles to kilometers')

def km_2_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_2_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = int(input('which conversion would you like to do?: '))
    if choice == 1:
        km_2_miles()
    
    if choice == 2:
        miles_2_km()
    