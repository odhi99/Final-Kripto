# Final-Kripto
212227 Kristian Yodi Keupung | 212105 John Pedro
Mohon Maaf Jika Vidionya Kadang Suaranya Tidak Muncul, Disini saya akan menjelaskan sedikit penjelasan program tersebut
Program yang dibuat adalah tanda tangan digital menggunakan Digital Signature Algorithm dengan bahasa pemrograman Python
Pertama Import Modul, Modul cryptography digunakan untuk menyediakan algoritma dan fungsi yang diperlukan untuk kriptografi, termasuk DSA.
Kemudian saya membuat fungsi dengan nama fungsinya generate_key_pair Fungsi ini menghasilkan pasangan kunci privat dan publik DSA. Kunci privat digunakan untuk membuat tanda tangan, sementara kunci publik digunakan untuk memverifikasi tanda tangan.
Kemudian saya membuat fungsi dengan nama fungsi sign_message Fungsi ini menerima kunci privat dan pesan sebagai argumen, dan mengembalikan tanda tangan digital dari pesan tersebut.
Lalu  saya membuat fungsi lagi dengan nama fungsi verify_signature Fungsi ini memeriksa keaslian tanda tangan digital dengan menggunakan kunci publik DSA.
Lalu ada contoh penggunaan Contoh ini menciptakan pasangan kunci DSA, menandatangani pesan "Hello, World!" menggunakan kunci privat, dan kemudian memverifikasi tanda tangan menggunakan kunci publik. Hasilnya dicetak ke konsol. Anda dapat mengganti pesan atau mengubah input sesuai kebutuhan.
Tampilan ada di demo sekali lagi maaf jika suaranya tidak karena bug
