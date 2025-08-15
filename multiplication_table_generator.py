def multiplication_printer(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = int(input('Enter a number to print its multiplication table: '))
    multiplication_printer(float(a))