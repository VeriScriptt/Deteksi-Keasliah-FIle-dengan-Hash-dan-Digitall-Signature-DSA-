Alur Penggunaan Hash dan DSA dalam Proyek:
Pada Pengirim (Sender Mode):

Pengirim pertama kali menghasilkan hash dari file menggunakan fungsi generate_file_hash().
Kemudian, pengirim menandatangani hash tersebut menggunakan private key dengan fungsi sign_file().
Tanda tangan digital (signature) disimpan dalam file dan dikirimkan bersama file asli kepada penerima.

Pada Penerima (Receiver Mode):

Penerima pertama kali menghitung hash dari file yang diterima menggunakan fungsi generate_file_hash().
Penerima kemudian memverifikasi tanda tangan digital menggunakan public key dengan fungsi verify_signature().
Penerima membandingkan hash yang dihitung dengan yang ada pada tanda tangan. Jika tanda tangan dan hash cocok, maka file diterima sebagai asli.
Hubungan Antara Hash dan DSA:
Hashing memastikan bahwa file yang diterima adalah salinan yang tepat dari file yang dikirim, tanpa perubahan apapun. Setiap perubahan dalam file akan menghasilkan hash yang berbeda, yang memungkinkan penerima untuk mendeteksi perubahan tersebut.
Digital Signature (DSA) memberikan jaminan keaslian bahwa file tersebut benar-benar berasal dari pengirim yang sah dan tidak dimodifikasi selama pengiriman.

kesimpulan
Hashing adalah teknik untuk mendeteksi integritas file. Dengan hashing, kita dapat dengan cepat memeriksa apakah file yang diterima sama persis dengan file yang dikirim.
Digital Signature (DSA) adalah metode untuk memverifikasi keaslian dan asal-usul file, memastikan bahwa file benar-benar dikirim oleh pengirim yang sah dan tidak telah diubah oleh pihak lain selama pengiriman.

Sebelum menggunakan program pastikan sudah menginstal openssl, pada linux biasanya sudah ada openssl secara default

Cara menggunakan Program
1.	Buka linux
2.	Generate private key : openssl genrsa -out private_key.pem 2048 
3.	Generate Public key : openssl rsa -in private_key.pem -pubout -out public_key.pem
4.	Simpan keys itu dalam folder keys
5.	Simpan file yang akan di beri signature dan di cek keasliannya di folder file
6.	Simpan signature di folder signature, seperti folder pada repositori ini
7.	Menjalankan mode pengirim (sender)

python app.py --mode sender --file path/to/your/file.txt --private-key path/to/private_key.pem --signature path/to/signature.sig

8.	Menjalankan mode penerima (receiver)

python app.py --mode receiver --file path/to/your/file.txt --public-key path/to/public_key.pem --signature path/to/signature.sig

9. Anda dapat meniru struktur folder dari repo ini

Penjelasan:
--mode receiver: Menentukan mode untuk penerima yang akan memverifikasi signature.
--file file/test.txt: Menunjukkan file yang akan diverifikasi.
--public-key keys/public_key.pem: Menunjukkan path ke public key untuk verifikasi.
--signature signature/signature.sig: Menunjukkan path ke file signature yang dihasilkan oleh pengirim.
Catatan:
Pada mode receiver, tidak perlu argumen private-key. Yang diperlukan adalah public-key untuk verifikasi signature.
Pastikan file file/test.txt dan file signature/signature.sig ada dan dapat diakses oleh program.

