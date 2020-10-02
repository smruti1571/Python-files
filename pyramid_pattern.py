i = 1
while i <= 8: 
	j = i 
	while j < 8 : 
		print("  " , end = " ") 
		j+=1 
	j = 1 
	while j <= i: 
		print("* ", end = " ") 
		print("  " , end = " ") 
		j+=1 
	print("\n")
	i+=1
i = 1
while i <= 7:
	j = 1
	while j <= i: 
		print("  " , end = " ") 
		j+=1 
	j = 7
	while j >= i: 
		print("* ", end = " ") 
		print("  " , end = " ") 
		j-=1 
	print("\n")
	i+=1
