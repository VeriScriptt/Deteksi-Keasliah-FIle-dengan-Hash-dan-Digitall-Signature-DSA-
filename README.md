Sebelum menggunakan program pastikan sudah menginstal openssl, pada linux biasanya sudah ada
Cara menggunakan Program
1.	Buka linux
2.	Generate private key : openssl genrsa -out private_key.pem 2048 
3.	Generate Public key : openssl rsa -in private_key.pem -pubout -out public_key.pem
4.	Simpan keys itu dalam folder keys
5.	Simpan file yang akan di beri signature dan di cek di folder file
6.	Simpan signature di folder signature, seperti folder pada repositori ini
7.	Menjalankan mode pengirim (sender)

python app.py --mode sender --file path/to/your/file.txt --private-key path/to/private_key.pem --signature path/to/signature.sig

8.	Menjalankan mode penerima (receiver)

python app.py --mode receiver --file path/to/your/file.txt --public-key path/to/public_key.pem --signature path/to/signature.sig



