import sys
arg1 = float(sys.argv[1])
arithmatic = sys.argv[2]
arg3 = float(sys.argv[3])

if arithmatic == '+' or arithmatic == 'plus' or arithmatic == 'add':
	math = arg1 + arg3
	print(math)
elif arithmatic == '-' or arithmatic == 'minus' or arithmatic == 'subtract':
	math = arg1 - arg3
	print(math)
elif arithmatic == '*' or arithmatic == 'times' or arithmatic == 'multiply':
	math = arg1 * arg3
	print(math)
elif arithmatic == '/' or arithmatic == 'divide' or arithmatic == '%':
	math = arg1 / arg3
	print(math)
else:
	print('Examples:\npython3 simple-calculator.py 10 + 10\npython3 simple-calculator.py 10 - 10\npython3 simple-calculator.py 10 * 10\npython3 simple-calculator.py 10 / 10')
