products = []

while True:
    name = input('輸入商品名稱：')

    if name == 'q':
        break

    price = input('輸入商品價格：')

    p = []          
    p.append(name)
    p.append(price)     

    products.append(p)    # 這四行也可以寫成 products.append([name, price])


for p in products:
    print('商品名聲:',p[0],'商品價格:',p[1])


# 把記帳內容寫入csv檔案 (多用於Excel)

with open('products.csv','w') as f:
    for p in products:
        f.write(p[0]+','+p[1]+'\n')  # 寫入csv檔(Excel)建議用逗點做區隔
