with open('console.txt', 'w') as file:
	file.write('')
file = open('console.txt', 'a')
a = '5'
print(b, file=file)

file.close()