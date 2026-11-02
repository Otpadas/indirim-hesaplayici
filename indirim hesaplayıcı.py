item_price = float(input("Ürünün fiyatını giriniz: "))
discount_percentage = int(input("İndirim yüzdesini giriniz: "))

new_price = item_price - (item_price * discount_percentage / 100)
how_cheap = item_price - new_price

print(f"--- FATURA ---\nİndirim:\t{how_cheap:.2f} TL\nYeni Fiyat:\t{new_price:.2f} TL")
