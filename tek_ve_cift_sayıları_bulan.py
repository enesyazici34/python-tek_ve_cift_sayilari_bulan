sayi = int(input("Bir sayı girin: "))
tekToplam = 0
ciftToplam = 0

for i in range(1, sayi + 1):
    if i % 2 == 0:
        ciftToplam += i
    else:
        tekToplam += i

print("1'den", sayi, "kadar olan tek sayıların toplamı:", tekToplam)
print("1'den", sayi, "kadar olan çift sayıların toplamı:", ciftToplam)
