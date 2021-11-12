a1= float(input("Masukkan alas atap :"))
a2= float(input("Masukkan tinggi atap :"))
a3= float(input("Masukkan tinggi tembok:"))

luas = 0.5 * (a1 * a2)
persegi = a3 * a3

print("rumah tersebut membutuhkan" ,str((luas + persegi) / 5), "sak semen")

