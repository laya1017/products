#讀取舊檔案
products = []
with open('products.csv', 'r',encoding='utf-8') as f:
	for line in f:
		#print(str(line))
		name, price = line.strip().split(',')
		if [name, price] == ['商品', '價格']:
			continue
		products.append([name, price])
print(products)
#讓使用者輸入
while True:
	name = input('輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	products.append([name, price])
print(products)
for p in products:
	print(p[0], '的價格是', p[1])
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
