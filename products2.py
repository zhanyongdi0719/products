# 建立記帳程式(輸入商品名稱、價格)
# 如何同時印出名稱、價格？ 運用二維清單 (教學影片62)

products = []

while True:
    name = input('輸入商品名稱：')

    if name == 'q':
        break

    price = input('輸入商品價格：')

    p = []           # 先建立每個小清單p(包含商品名稱與價格)
    p.append(name)
    p.append(price)     # 這三行也可以寫成 p = [name, price]

    products.append(p)   # 再把每個小清單p加到大清單products裡


# 用for loop把商品名稱、價格完整印出來

for p in products:
    print('商品名聲:',p[0],'商品價格:',p[1])
