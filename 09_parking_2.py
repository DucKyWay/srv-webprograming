in_time = input("in:(XX : XX)")
out_time = input("out:(XX : XX)")

def price(in_time, out_time):
    in_hr = int(in_time[0:2])
    in_mn = int(in_time[3:5])
    out_hr = int(out_time[0:2])
    out_mn = int(out_time[3:5]) 

    total = (out_hr * 60 + out_mn) - (in_hr * 60 + in_mn)

    if total % 60 == 0:
        hr = total // 60
    else:
        hr = total // 60 + 1
        
    if 8 <= in_hr <= 20 and 8 <= out_hr <= 20 and 0 <= in_mn < 60 and 0 <= out_mn < 60:
        if hr <= 1 and in_mn == out_mn:
            print("Total price: 0")
        if total < 60:
            print("Total price: 0")
        if in_mn == out_mn:
            hr = hr + 1
            if 1 < hr <= 6:
                price = (hr - 1) * 30 
                print(f"Total price: {abs(price)}")
            if hr > 6:
                price = 150 + (hr - 6) * 50
                print(f"Total price: {price}")
    else:
        print("-- ไม่สามารถจอดเวลานี้ได้ --")
        print("__________")

price(in_time, out_time)
