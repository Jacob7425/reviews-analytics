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

# 篩選
new = []  # 建立新的清單
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[5]) # new 出來的都是長度小於100

# 篩選_2
good = []
for d in data:
	if 'good' in d:  # 如果d裡面有'good'
		good.append(d)  # 就把d裝進good清單
print('一共有', len(good), '筆留言提到good')

# 進階清單快寫法 
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')

# bad = ['bad' in d for d in data]
# print(bad)

# 文字記數
wc = {}
for d in data:
	words = d.split() #split() 預設值為空白 所以可不寫
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過')

print('感謝使用本查詢功能')



