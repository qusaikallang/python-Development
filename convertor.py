from string_format import make
def convert():
    s = int(input("Enter the number to convert \n >>"))
    rem = []
    q = int(s/2)
    rem.append(s%2)
    while q > 0:
        rem.append(q % 2)
        q = int(q/2)
    rem.reverse()
    print(make.BOLD,make.RED,rem,make.END)

convert()