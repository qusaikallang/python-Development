# string to morse
s = input('Enter the String to be converted to morse code\n>>')
p = s.lower()
#s = input('enter the string to be convrted').split()
morse_table = {'a':'.-','b':'-...','c':'-.-.',
               'd':'-..','e':'-','f':'..-.','g':'--.'
    ,'h':'....','i':'..','j':'.---','k':'-.-',
               'l':'..','m':'--','n':'-.','o':'---',
               'p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--',
               'x':'-..-','y':'-.--','z':'--',
               '1':'.---','2':'..---','3':'...--','4':'....-','5':'......','6':'-....','7':'--...','8':'---..','9':'----.','0':'----',' ':''}
for i in p:
    #if i in morse_table.keys() :
    print(i+" is converted to "+ morse_table[i])

