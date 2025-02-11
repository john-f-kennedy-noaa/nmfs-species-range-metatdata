#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     16/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def myfunc(n):
      return abs(10-n)

    a = (5, 3, 1, 11, 2, 12, 17)
    x = sorted(a, key=myfunc)
    print(a)
    print(x)
    for n in a:
        print(f"{n}, {myfunc(n)}")

    a = ("Jenifer", "Sally", "Jane")
    x = sorted(a, key=len)
    print(x)

##    (5, 3, 1, 11, 2, 12, 17)
##    [11, 12, 5, 3, 17,  2,  1]
##      1,  2, 3, 5, 11, 12, 17

if __name__ == '__main__':
    main()
