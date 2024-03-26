# Soal 3 #
def spasi_berlebih():                   # Mendefinisikan
    x = input.lower()
    x = input.split()                   # Memecahkan atau memisahkah
    kalimatnormal = " ".join(x)         
    return kalimatnormal
    
def spasi_berlebih():                   # Mendefinisikan
    x = input.lower()
    x = input.split()                   # Memecahkan dan memisahkan kalimat pada inputan 
    hasil = []                          # Menyediakan Hasil buat di isi nantinya
    for kata in x:                      # Perulangan 
        if kata[0] == " ":              # Jika kata dipanggil 0 sama dengan kosong / spasi
            continue                    # Continue atau lanjutkan
        else:                           # Jika tidak maka diisi ke hasil
            hasil.append(kata)
    return " ".join(hasil)
            

input = input("Masukkan kalimat yang mau diperbaiki: ")       # Meminta pengguna memasukan inputan
kalimatnormal = spasi_berlebih()               
print(f"Setelah diperbaiki : {kalimatnormal}")             # Memunculkan kalimatnormal yang sudah diisi dengan def spasi_berlebihan