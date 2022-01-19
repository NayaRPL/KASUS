print("contoh kasusu")
nama=input("masukkan nama:")
nim=input("masukkan nim:")
jml_mtkl=int(input("masukkan jumlah matkul:"))
for i in range (0,jml_mtkl):
     nama_matkul=input("masukkan nama matkul:")
     sks=int(input("masukkan sks:"))
     nilai=int(input("masukkan nilai:"))
     if nilai >= 80 and nilai <= 100 :
       bobot =4
       print("nilai anda di mata kuiah:",nama_matkul,"A")
     elif nilai >=65:
        bobot =3
        print("nilai anda di mata kuiah:",nama_matkul,"B")
     elif nIlai >=55:
        bobot =2
        print("nilai anda di mata kuiah:",nama_matkul,"C")
     else:
        bobot =0
        print("nilai anda di mata kuiah:",nama_matkul,"d")
total_bobot=bobot*sks
ipk=total_bobot/sks
if ipk >=3.5 and ipk<=4:
    print("PREDIKAT DENGAN SANGAT PUJIAN")
elif ipk >=3:
    print("PREDIKAT DENGAN SANGAT MEMUASKAN")
elif  ipk >= 2.5 and ipk <=2.99:
    print("PREDIKAT MEMUASKAN")
else :
    print("PREDIKAT LULUS")
print("total ipk:",ipk)
