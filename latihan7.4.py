def terpendek_terpanjang():                                             # Mendefinisikan          
    x = input1.split()                                                  # Memecahkan dan memisahkan kalimat
    pendek = x[0]                                               
    panjang = x[0]
    for kata in x:                                                       # Untuk kata di dalam x akan di ulang jika kat lebih kecil dari pendek 
        if len(kata) < len(pendek):
            pendek = kata                                                # Maka pendek diisi dengan kata
        elif len(kata) > len(panjang):                                   # Dan jika kata lebih besar dari panjang 
            panjang = kata                                               # Maka panjang diisi dengan kata 
    return pendek, panjang

input1 = input("Masukkan kalimat anda: ")                                # Inputan dari user
pendek, panjang = terpendek_terpanjang()                                 # pendek dan panjang diisi def terpendek_panjang
print(f"Terpendek adalah : {pendek} dan Terpanjang adalah : {panjang}")  # Mumunculkan hasil 
