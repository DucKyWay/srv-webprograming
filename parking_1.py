in_time = input("in:(XX : XX)")
out_time = input("out:(XX : XX)")

def price(in_time,out_time) :
    in_hr = int(in_time[0:2])
    in_mm = int(in_time[3:5])
    out_hr = int(out_time[0:2])
    out_mm = int(out_time[3:5])

    total = (out_hr * 60 + out_mm) - (in_hr * 60 + in_mm)


    if (total) % 60 == 0 :
        hr = total // 60
    else:
        hr = total // 60 + 1

    if 7 <= in_hr <= 24 and out_hr <= 24 and 0 <= in_mm <= 60 and 0 <= out_mm <= 60 :
        if hr <= 2 : 
            print("total price : 0")
        if 2 < hr <= 4 :
            price = hr - 2 * 20
            print(f'total price : {abs(price)}')
        if hr > 4 :
            price = (40 + (hr - 4) * 30)
            print(f'total price : {price}')
    else : 
        print("__________")

price(in_time,out_time)

in_time = input("in:(XX : XX)")
out_time = input("out:(XX : XX)")

def price(in_time,out_time) :
    in_hr = int(in_time[0:2])
    in_mm = int(in_time[3:5])
    out_hr = int(out_time[0:2])
    out_mm = int(out_time[3:5])

    total = (out_hr * 60 + out_mm) - (in_hr * 60 + in_mm)

    if (total) % 60 == 0 :
        hr = total // 60
    else:
        hr = total // 60 + 1

    if 7 <= in_hr <= 24 and out_hr <= 24 and 0 <= in_mm <= 60 and 0 <= out_mm <= 60 :
        if hr <= 2 : 
            print("total price : 0")
        if 2 < hr <= 4 :
            price = hr - 2 * 20    # ค่่าจอด 2 ชม แรก
            print(f'total price : {abs(price)}')
        if hr > 4 :
            price = (40 + (hr - 4) * 30) #ค่าจอด ตั่งแต่ 4 ชม. ขึ้นไป
            print(f'total price : {price}')
    else : 
        print("__________")

price(in_time,out_time)