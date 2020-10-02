i = 8
while i >= 5: 
	j = i 
	while j >=5: 
		print("  ",end = " ") 
		j-=1 
	j = 8
	while j >= i : 
		print("* ",end=" ") 
		j-=1 
	print("\n") 
	i-=1
else :
	i = 5
	while i >= 1 : 
		j = 5
		while j > i : 
			print("  ",end = " ") 
			j-=1 
		while j != 0 : 
			print("* ", end = " ") 
			j-=1 
		print("\n")
		i-=1