# Soal 2 
def frekuensi_kata(input1, input2):                 # Mendefinisikan
    kalimat_murni = input1.replace(".", "").replace("!", "").replace(",", "").replace("?", "").replace(":", "").replace(";", "")  # Merubah 
    kalimat_new = kalimat_murni.lower()             # Merubah inputan user menjadi kecil
    input2 = input2.lower()
    input1 = input1.strip('.,!?')                   # Membuat hilangkan titik dll dalam inputan
    input2 = input2.strip('.,!?')
    kata1 = kalimat_new.split()                     # Memisahkan dan memecahkan kalimat

    frekuensi = 0                                   # membuat variabel                                                          
    for kata2 in kata1:                             # pada kata2 di kata1 jika kata2 sama dengan inputan2 maka frekuensi ditambah sama dengan satu atau variabel tadi diisikan atau di tambah 1
        if kata2 == input2:
            frekuensi += 1
    return frekuensi

input1 = input("Masukkan kalimat: ")                        # Inputan dari User
input2 = input("Kata yang dicari: ")
frekuensi = frekuensi_kata(input1, input2)                  # Didalam frekuensi terdapat def frekuensi_kata()
print(f"{input2} ada {frekuensi} pada kalimat tersebut")    # Memunculkan hasil
