ticket = 1 #1表示有车票
knifeLength = 50#cm
if ticket == 1:
	print("通过车票检查，进入车站，接下来安检")
	if knifeLength <=10:
		print("通过了安检，进入到候车亭")
	else:
		print("安检没通过")
else:
	print("没买票，不能进站")
