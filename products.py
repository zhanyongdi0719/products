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
    p.append(price)

    products.append(p)   # 再把每個小清單p加到大清單products裡

print(products)     # 最後印出大清單

