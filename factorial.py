def fact(num):
	if num == 1:
		return 1
	else:
		return fact(num-1) * num

num = 10

print(fact(num))
