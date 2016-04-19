def power(base,exponent):
	
	if exponent == 0:
		return 1
	else:
		return base * power(base, exponent -1 )
			
	return power

print("The answer is: {}." .format(power(4, 4)))	
print("The answer is: {}." .format(power(7, 7)))	
print("The answer is: {}." .format(power(1, 1)))	
print("The answer is: {}." .format(power(3, 13)))	
print("The answer is: {}." .format(power(71, 2)))	
print("The answer is: {}." .format(power(4, 2)))	