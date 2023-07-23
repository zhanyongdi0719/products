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


# 把記帳內容寫入txt檔案 (課程影片63)

with open('products.txt','w') as f:
    for p in products:
        f.write('商品名聲:'+p[0]+' 商品價格:'+p[1]+'\n') 

        # 在結尾的地方記事本不會幫你換行要自己補\n

