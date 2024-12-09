# 1) Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

benzin_fiyat = 39.35
dizel_fiyat = 41.71
lpg_fiyat = 20.28

mesafe=int(input("Gidilen Yol: "))

benzin_masrafı= (benzin_fiyat*mesafe)
print(benzin_masrafı)

dizel_masrafı= (dizel_fiyat*mesafe)
print(dizel_masrafı)

lpg_masrafı= (lpg_fiyat*mesafe)
print(lpg_masrafı)