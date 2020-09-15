data = []
count = 0  # 記數 for 6 and 7
with open('reviews.txt','r')as f:
	for line in f:
		data.append(line)
		count += 1  # count = count + 1
		if count % 1000 == 0:  # 每讀一千筆印一次  % = 求餘數
			print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

sum_len = 0  # sum = 加總
for d in data:
	sum_len += len(d)

print('留言的平均長度為', sum_len/len(data)) # len(data) = 留言數

#篩選
new = []  # 建立新的清單
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[5]) # new 出來的都是長度小於100