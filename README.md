# Proyek Hash dan DSA: Verifikasi Keaslian File

## **Alur Penggunaan Hash dan DSA dalam Proyek**

### **1. Pengirim (Sender Mode)**

1. Pengirim pertama kali menghasilkan **hash** dari file menggunakan fungsi `generate_file_hash()`.
2. Kemudian, pengirim **menandatangani hash** tersebut menggunakan **private key** dengan fungsi `sign_file()`.
3. Tanda tangan digital (**signature**) disimpan dalam file dan dikirimkan bersama file asli kepada penerima.

### **2. Penerima (Receiver Mode)**

1. Penerima pertama kali menghitung **hash** dari file yang diterima menggunakan fungsi `generate_file_hash()`.
2. Penerima kemudian **memverifikasi tanda tangan digital** menggunakan **public key** dengan fungsi `verify_signature()`.
3. Penerima membandingkan **hash** yang dihitung dengan yang ada pada tanda tangan. Jika tanda tangan dan hash cocok, maka file diterima sebagai asli.

---

## **Hubungan Antara Hash dan DSA**

- **Hashing** memastikan bahwa file yang diterima adalah salinan yang tepat dari file yang dikirim, tanpa perubahan apapun. Setiap perubahan dalam file akan menghasilkan hash yang berbeda, yang memungkinkan penerima untuk mendeteksi perubahan tersebut.
  
- **Digital Signature (DSA)** memberikan jaminan keaslian bahwa file tersebut benar-benar berasal dari pengirim yang sah dan tidak dimodifikasi selama pengiriman.

---

## **Kesimpulan**

- **Hashing** adalah teknik untuk mendeteksi integritas file. Dengan hashing, kita dapat dengan cepat memeriksa apakah file yang diterima sama persis dengan file yang dikirim.
  
- **Digital Signature (DSA)** adalah metode untuk memverifikasi keaslian dan asal-usul file, memastikan bahwa file benar-benar dikirim oleh pengirim yang sah dan tidak telah diubah oleh pihak lain selama pengiriman.

---

## **Persyaratan Sistem**

Sebelum menggunakan program ini, pastikan Anda sudah menginstal **OpenSSL**. Biasanya, OpenSSL sudah terpasang secara default pada sistem Linux.

---

## **Cara Menggunakan Program**

### **Langkah-langkah untuk Menggunakan Program**

1. **Buka Terminal Linux.**

2. **Generate private key** dengan perintah:

   ```bash
   openssl genrsa -out private_key.pem 2048

3. **Generate public key** dengan perintah:
   ```bash
   openssl rsa -in private_key.pem -pubout -out public_key.pem
4. **Simpan keys tersebut dalam folder keys.**
5. Simpan file yang akan diberi signature dan diuji keasliannya dalam folder file.
6. Simpan signature di folder signature, seperti struktur folder pada repositori ini.

