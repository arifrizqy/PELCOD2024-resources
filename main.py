# [FUNCTION]
# def
def sayHello(param_nama, param_umur):
   print(f"Hello {param_nama}, Umur: {param_umur}")
   print("selamat pagi")

nilai = int(input("Masukkan nilai: "))

nilai = nilai + 5

if (nilai > 90 and nilai <= 100):
   print("selamat anda lulus, dengan nilai yang memuaskan")
   nama = input("Masukkan nama: ")
   sayHello(nama, 19)
elif (nilai > 80):
   print("selamat anda lulus")
   nama = input("Masukkan nama: ")
   sayHello(nama, 20)
elif (nilai > 70):
   print("lulus tapi deket jurang")
   nama = input("Masukkan nama: ")
   sayHello(nama, 21)
else:
   print("anda masih belum lulus tes, semangat dan coba lagi")
   nama = input("Masukkan nama: ")
   sayHello(nama, 45)


# [LOOP]
# for loop
for i in range(10, 0, -2):
   print(i)
   print("Hello world")

# while loop
angka = 10

while (angka >= 1):
   print(angka)
   angka -= 1 # angka = angka - 1



sayHello()
sayHello()
sayHello()
sayHello()
sayHello()
sayHello()

# [ANONYMOUS FUNCTION: lambda]
fungsi_kurang4 = lambda param_angka : param_angka - 4

angka = 10
# 
print(fungsi_kurang4(angka))