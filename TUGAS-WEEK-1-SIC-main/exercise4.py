# Tugas 4: Operasi pada String

# input nama pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")

# bikin pesan terima kasih
pesan_terima_kasih = "Terima kasih, " + nama_pelanggan + " sudah berbelanja di Coffee Shop Bahagia!"

# bikin garis pemisah
garis = "*" * 25

# data produk (misalnya dari tugas sebelumnya)
nama_produk1 = "Kopi Pagi"
total_kopi = 36001.0   # contoh hasil hitung dari Tugas 3

# cetak struk
print(garis)
print(pesan_terima_kasih)
print(f"Total harga {nama_produk1} adalah Rp{total_kopi}")
print(garis)

'''
*************************
Terima kasih, Natasyah sudah berbelanja di Coffee Shop Bahagia!
Total harga Kopi Pagi adalah Rp36001.0
*************************
'''