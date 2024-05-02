#Daftar barang beserta harganya
daftar_barang = {
    "beras":10000,
    "gula":8000,
    "telur":2000,
    "minyak goreng":15000,
    "garam":5000,
}

daftar_barang2 = {
    "Beras":10000,
    "Gula":8000,
    "Telur":2000,
    "Minyak goreng":15000,
    "Minyak Goreng":15000,
    "minyak Goreng":15000,
    "Garam":5000,
}

#menampilkan daftar barang
print("=====================================")
print("------------DAFTAR BARANG------------")
print("=====================================")
for barang, harga in daftar_barang.items():
    print(f"{barang}:Rp {harga}")
for barang, harga in daftar_barang2.items():
    f"{barang}:Rp {harga}"

#input jumlah barang yang dibeli
total_belanja=0
jumlah_barang = int(input("\nMasukkan jumlah barang yang di beli : "))
print("=====================================")
print("=====================================")
#menghitung total belanjaan
for i in range(jumlah_barang):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    if barang in daftar_barang:
        total_belanja +=daftar_barang[barang]
    elif barang in daftar_barang2:
        total_belanja +=daftar_barang2[barang]
    else:
        print(f"{barang} tidak ada dalam daftar barang, dan pastikan untuk masukkan nama barang yang sesuai dengan daftar")
       
#menampilkan total belanjaan
print(f"\nTotal belanjaan Anda : Rp {total_belanja}")
    
            
