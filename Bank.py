totalamount=0
while True:
	a=input("Type D or d for deposit and  enter amount for withdrawal type W or w and enter amount---")
	b=a.split(" ")
	c=b[0]
	d=int(b[1])
	if((c=='D') or (c=='d')):
		totalamount=totalamount +d
	elif((c=='W') or (c=='w')):
		if(totalamount<d):
			print("You dont have sufficient fund")
		else:
			totalamount=totalamount-d
	else:
		pass
	e=input("Want to continue (y) or (n)---")
	if not (e=='y'):
		break
print("Current Funds---",totalamount)
		
		