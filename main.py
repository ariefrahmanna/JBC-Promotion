from send import automateWA


# Sesuaikan path dari file anda
WA_path = r"C:\Users\ipung\Downloads\JBC_Promotion\JBC_Promotion\WA.txt"
caption_path = r"C:\Users\ipung\Downloads\JBC_Promotion\JBC_Promotion\caption.txt"
image_path = r"C:\Users\ipung\Downloads\JBC_Promotion\JBC_Promotion\image.png"

# Sesuaikan jumlah nomor yang ingin anda kirim terlebih dahulu
# Jika ingin mengirim semua sekaligus di isikan dengan "ALL"
# Jika ingin beberapa saja isikan dengan angka, dengan contoh seperti dibawah ini
# start = 0
# end = 10

start = 0
end = 2

automateWA(start, end, image_path, caption_path, WA_path)