
from math import sqrt

print('Solve a quadratic equations')

def find_roots(a,b,c):
    
    D = sqrt(b**2-4*a*c)
    x_1 = (-b+D)/(2*a)
    x_2 = (-b-D)/(2*a)

    print('The roots of the quadratic equation are X1= {0} and X2= {1}'.format(x_1, x_2))

if __name__ == '__main__':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    find_roots(float(a), float(b), float(c))