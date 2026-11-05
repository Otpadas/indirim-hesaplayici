price = float(input("Sepetinizin toplam fiyatını giriniz: "))
vip_durum = str(input("VIP misiniz? (Evet/Hayır): ")).lower()
if vip_durum == "evet":
    if price >= 1000:
        discount = price * 0.25
        remaining_price = price - discount
        print(f"Sepetinizin indirim ile toplam fiyatı: {remaining_price} TL")
    elif price < 1000:
        discount = price * 0.15
        remaining_price = price - discount
        print(f"Sepetinizin indirim ile toplam fiyatı: {remaining_price} TL")
else:
    if price >= 1000:
        discount = price * 0.10
        remaining_price = price - discount
        print(f"Sepetinizin indirim ile toplam fiyatı: {remaining_price} TL")
    elif price < 1000:
        print(f"Sepetinizin toplam fiyatı: {price} TL")
