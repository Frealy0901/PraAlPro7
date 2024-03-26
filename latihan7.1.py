# Soal 1 #
def anagram():                                              # Mendefinisikan 
    x = sorted(input1)                                      # Mensorted x,y
    y = sorted(input2)
    
    if x == y or y == x:                                    # Jika x sama dengan y atau y sama dengan x maka akan di print kata adaalah anagram
        print("Kata tersebut anagram")
    else:                                                   # jika tidak maka kata itu bukan anagram
        print("Kata itu bukanlah anagram")              

input1 = input("Masukkan kata pertama: ").lower()           # Inputan dari user
input2 = input("Masukkan kata kedua: ").lower()
anagram()