#I use the bitwise calculation of the parity of the number, as it is faster than dividing with a remainder

def isEven(digit:int)->bool:
    return not digit&1

def main():
    for n in range(1_000_000):
        isEven(n)

if __name__ == '__main__':
    main()