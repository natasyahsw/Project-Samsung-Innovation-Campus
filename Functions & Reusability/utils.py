def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid. Gunakan C/F/K."

    # Konversi ke Celsius dulu
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        if nilai < 0:
            return "Error: Kelvin tidak boleh negatif."
        c = nilai - 273.15

    # Dari Celsius ke tujuan
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    elif ke == "k":
        k = c + 273.15
        if k < 0:
            return "Error: Hasil konversi ke Kelvin tidak boleh negatif."
        return k
