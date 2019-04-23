import datetime
print('\033[93m'+'Choose the mode 1 for inserting text and 2 for appending text and mode 3 for searching'+'\033[0m')
choice =  input()

if choice == 1:
	r = open('r.txt','w')
	print('input the text to be inserted')
	r.write(str(datetime.datetime.now())+str(input()))
	r.close()
if choice == 3:
	t = open('r.txt','r')
	print('Input date to be searched[single number only]')
	search_con = str(input())
	for line in t.readlines():
		if search_con in line[0:25]:
			print(line)
	t.close()
if choice == 2:
	b = open('r.txt','a')
	print('Input text to be appended')
	b.write('\n'+str(datetime.datetime.now())+str(input()))
	b.close()