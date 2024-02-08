from utilities import input_
from decode import decode

def main():
    input_()
    date = input()
    print(decode(date))

if __name__ == "__main__":
    main()