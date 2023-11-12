def kalkulator():
    while True:
        print("Pilih operasi.")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pemangkatan")

        #Meminta input dari user
        pilihan = input("Masukkan pilihan: ")
    
        if pilihan == "1":
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            print(f"{angka1} + {angka2} = {angka1 + angka2}")
            break

        elif pilihan == "2":
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            print(f"{angka1} - {angka2} = {angka1 - angka2}")
            break

        elif pilihan == "3":
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            print(f"{angka1} x {angka2} = ")
            break

        elif pilihan == "4":
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            print(f"{angka1} / {angka2} = {angka1 / angka2}")
            break

        elif pilihan == "5":
            basis = int(input("Masukkan bilangan basis: "))
            pangkat = int(input("Masukkan bilangan pangkatnya: "))
            print(f"{basis} ^ {pangkat} = {basis ** pangkat}")
            break
        
kalkulator()