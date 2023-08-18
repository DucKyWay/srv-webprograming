transfer = float(input("จำนวนเงิน: "))
fee = 0
if transfer <= 10000:
    fee = 50
elif transfer >= 10000 and transfer <= 20000:
    fee = 60
elif transfer >= 20001 and transfer <= 30000:
    fee = 70
elif transfer >= 30001 and transfer <= 40000:
    fee = 80
elif transfer >= 40001 and transfer <= 50000:
    fee = 90
elif transfer >= 50001 and transfer <= 65000:
    fee = 100
elif transfer >= 65001 and transfer <= 80000:
    fee = 110
elif transfer >= 80001 and transfer <= 100000:
    fee = 120
else:
    print("เกิดข้อผิดพลาด")

if fee <= 120 and fee != 0:
    print("ค่าธรรมเนียม", fee, "บาท")
else:
    print("ไม่สามารถทำรายการที่มีค่ามากกว่า 100,000 บาทได้")
