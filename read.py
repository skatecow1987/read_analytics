data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 5000 == 0: # %用來求餘數 此行表示如果為千的倍數才會印出
			print(len(data))  #此兩行可以看出讀取進度

print(len(data))
print(data[0])
print('--------------')
print(data[1])
