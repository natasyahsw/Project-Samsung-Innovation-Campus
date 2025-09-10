# Buat list nama siswa
siswa = ['Natasyah', 'Fanni', 'Reza', 'Deny']

# Buat dictionary nilai siswa
nilai_siswa = {
    'Natasyah': 90,
    'Fanni': 85,
    'Reza': 88,
    'Deny': 80
}

print("List awal siswa:", siswa)
print("Dictionary nilai awal:", nilai_siswa)

# Tambahkan satu nama siswa baru ke akhir list siswa
siswa.append('Andi')
print("\nSetelah menambah 'Andi':", siswa)

# Hapus satu siswa tertentu dari list (misal 'Reza')
siswa.remove('Reza')
print("Setelah menghapus 'Reza':", siswa)

# Cetak nama siswa pertama dan terakhir
print("Siswa pertama:", siswa[0])
print("Siswa terakhir:", siswa[-1])

# Cetak 3 siswa terakhir dengan slicing
print("3 siswa terakhir:", siswa[-3:])

# Cetak index dan nama siswa
print("\nIndex dan nama siswa:")
for idx, nama in enumerate(siswa):
    print(f"{idx}. {nama}")

# Ubah nilai ujian salah satu siswa di dictionary (misal Fanni → 90)
nilai_siswa['Fanni'] = 90
print("\nSetelah mengubah nilai Fanni jadi 90:", nilai_siswa)

# Hapus data nilai siswa lain menggunakan pop() (misal Reza)
nilai_siswa.pop('Reza', None)
print("Setelah mem-pop 'Reza':", nilai_siswa)

# Ganti key nama siswa tertentu jadi nama baru (misal Deny → Deny Pratama)
if 'Deny' in nilai_siswa:
    nilai_siswa['Deny Pratama'] = nilai_siswa.pop('Deny')
print("Setelah mengganti key 'Deny' jadi 'Deny Pratama':", nilai_siswa)
