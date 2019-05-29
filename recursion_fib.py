def getFibNumber(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return getFibNumber(number-1) + getFibNumber(number-2)
i = 1
while i  < 10:
	print getFibNumber(i)
	i = i + 1

