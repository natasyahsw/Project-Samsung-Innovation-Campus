# Tugas 2: Konversi Tipe Data dan Input Pengguna

# input dari pengguna
jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")

# cek tipe data awal
print("Tipe data awal jumlah kopi:", type(jumlah_kopi_str))
print("Tipe data awal jumlah roti:", type(jumlah_roti_str))

# konversi ke integer
jumlah_kopi_int = int(jumlah_kopi_str)
jumlah_roti_int = int(jumlah_roti_str)

# cek tipe data setelah konversi (cukup sekali aja biar sama kayak contoh soal)
print("Tipe data setelah konversi:", type(jumlah_kopi_int))


'''
Masukkan jumlah pesanan kopi: 2
Masukkan jumlah pesanan roti: 3
Tipe data awal jumlah kopi: <class 'str'>
Tipe data awal jumlah roti: <class 'str'>
Tipe data setelah konversi: <class 'int'>
Tipe data setelah konversi: <class 'int'>
'''