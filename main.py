import os
from send import automateWA


START = 0
END = 2
# Sesuaikan jumlah nomor yang ingin anda kirim terlebih dahulu
# Jika ingin mengirim semua sekaligus di isikan dengan "ALL"
# Jika ingin beberapa saja isikan dengan angka, dengan contoh seperti dibawah ini

# Sesuaikan path dari file anda
caption_path = os.path.join(os.getcwd(), "caption.txt")
image_path = os.path.join(os.getcwd(), "image.png")
WA_path = os.path.join(os.getcwd(), "WA.txt")

automateWA(START, END, image_path, caption_path, WA_path)
