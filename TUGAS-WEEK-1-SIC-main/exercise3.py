# Tugas 3: Operasi pada Angka

# variabel dari Tugas 1
harga_kopi = 18000.5
harga_roti = 10000

# variabel dari Tugas 2 (anggap sudah diinput & dikonversi)
jumlah_kopi_int = 2
jumlah_roti_int = 3

# hitung total harga masing-masing
total_kopi = harga_kopi * jumlah_kopi_int
total_roti = harga_roti * jumlah_roti_int

# hitung total belanja
total_belanja = total_kopi + total_roti

# uang bayar
uang_bayar = 50000
kembalian = uang_bayar - total_belanja

# cetak hasil
print("Total harga kopi:", total_kopi)
print("Total harga roti:", total_roti)
print("Total belanja keseluruhan:", total_belanja)
print("Uang yang dibayarkan:", uang_bayar)
print("Kembalian:", kembalian)


'''
Total harga kopi: 36001.0
Total harga roti: 30000
Total belanja keseluruhan: 66001.0
Uang yang dibayarkan: 50000
Kembalian: -16001.0
'''