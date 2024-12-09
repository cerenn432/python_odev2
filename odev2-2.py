# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC


vize1=67
vize2=85
final=92

ortalama=vize1*30/100+vize2*30/100+final*40/100
print(ortalama)
if 90<=ortalama<=100:
    print("AA")
elif 80<=ortalama<=89:
    print("BA")   
elif 70<=ortalama<=79:
    print("BB")
elif 60<=ortalama<=69:
    print("CB")
elif 50<=ortalama<=59:
    print("CC")
elif 40<=ortalama<=49:
    print("DC")