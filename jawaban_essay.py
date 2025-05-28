from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=12)

# Judul
pdf.set_font("Times", "B", 16)
pdf.cell(200, 10, txt="UTS-STRUKTUR DATA", ln=True, align="C")
pdf.ln(10)

# Isi
pdf.set_font("Times", size=12)

isi = [
    "1. Pengertian Sturktur Data:",
    "Struktur data ialah suatu teknik tertentu untuk menyimpan dan mengatur data di komputer sehingga",
    "dapat diproses atau digunakan lebih efisien.",
    "",

    "2. Kegunaan struktur data:",
    "- Semakin teratur bikin data. Dengan struktur data, kita bisa menyimpan dan mengatur data dengan",
    "baik, sehingga tidak berantakan dan mudah dicari.",
    "- Membuat proses pengolahan lebih cepat. Kalau data sudah tertata, program bisa lebih cepat",
    "melaksanakan tugasnya, seperti mencari data atau mengubah isi data.",
    "- Menghemat penggunaan memori. Struktur data yang tepat bisa membantu program menggunakan memori",
    "secukupnya, sehingga tidak boros.",
    "- Memudahkan kita ngoding. Karena udah sudah terdapat pola dan aturan tertentu, maka kita menjadi",
    "lebih mudah menulis kode efisien dan rapi.",
    "- Membantu algoritma agar lancar berjalan. Banyak algoritma yang membutuhkan struktur data tertentu "
    "sehingga dapat dijalankan dengan maksimal, misalnya seperti mencari atau mengurutkan data.",
    "",

    "3. Jenis-jenis struktur data beserta penjelasan:",
    "- Array: Menyimpan banyak data yang sejenis dalam satu wadah. Setiap elemen punya posisi (indeks).",
    "- Linked List: Kumpulan elemen yang terhubung satu sama lain, cocok buat data yang sering ditambah",
    "atau dihapus.",
    "- Stack: adalah data yang terlama masuk akan jadi yang pertama keluar.",
    "- Queue: ialah siapa yang masuk lebih awal keluar lebih dahulu.",
    "- Tree: Mirip struktur pohon, digunakan untuk menggambarkan data yang bertingkat.",
    "- Graph: Cocok untuk menunjukkan hubungan antar objek, contohnya dalam peta atau jaringan sosial.",
    "",

    "4. Apa itu Array dan Kegunaan:",
    "Array adalah wadah yang bisa menampung banyak nilai dengan jenis yang sama, dan tiap nilainya bisa",
    "diakses lewat nomor urut (indeks). Array terkadang digunakan saat menyimpan data dalam jumlah banyak",
    "dan ingin mengaksesnya dengan cepat.",
    "",

    "5. Contoh Array:",
    "- Dalam menyimpan daftar kontak.",
    "- Daftar atau playlist mp3 atau mp4.",
    "- Menyimpan data nilai",
    "",

    "6. Array dengan python:",
    'husbu_rina = ["Misaki", "Chifuyu", "Kazutora"]',
    "",
    "# Tampilkan semua husbu",
    'print("Daftar Husbu Rina:")',
    "for husbu in husbu_rina:",
    '    print("-", husbu)',
    "",
    "# Contoh akses satu-satu",
    'print("\\nHusbu favorit pertama:", husbu_rina[0])',
]

for baris in isi:
    pdf.cell(200, 10, txt=baris, ln=True)

# Simpan PDF
pdf.output("Jawaban_UTS_Essay-Sabrina_Azahra.pdf")

print("Jawaban_UTS_Essay-Sabrina_Azahra.pdf")
