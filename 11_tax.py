def Tax(price):
    vat = 7

    price_vat = price * vat / 100
    total_tax = price + price_vat

    print("ภาษีมูลค่าเพิ่ม: ", price_vat)
    print("ราคาก่อนลด: ", total_tax)

def sale(total_tax):
    discount = float(input("ส่วนลด (%): "))
    total = total_tax * (1 - discount / 100)
    print("ราคาหลังหักส่วนลด: ", total)

price = float(input("ราคา: "))
Tax(price)
sale(price)
