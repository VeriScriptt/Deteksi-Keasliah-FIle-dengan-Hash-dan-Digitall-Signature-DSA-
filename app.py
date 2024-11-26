import hashlib
import argparse
import os
from cryptography.hazmat.primitives import hashes # type: ignore
from cryptography.hazmat.primitives.asymmetric import padding # type: ignore
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key # type: ignore
from cryptography.hazmat.backends import default_backend # type: ignore

# Fungsi untuk membuat hash dari file
def generate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):  # Membaca file dalam chunk
                sha256_hash.update(chunk)  # Update hash dengan setiap chunk
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Fungsi untuk membuat digital signature
def create_signature(file_path, private_key_path):
    file_hash = generate_file_hash(file_path)
    if file_hash is None:
        return None

    file_hash = file_hash.encode()
    try:
        with open(private_key_path, "rb") as key_file:
            private_key = load_pem_private_key(key_file.read(), password=None, backend=default_backend())
    except FileNotFoundError:
        print(f"Error: Private key '{private_key_path}' not found.")
        return None

    signature = private_key.sign(
        file_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Fungsi untuk verifikasi digital signature
def verify_signature(file_path, signature, public_key_path):
    file_hash = generate_file_hash(file_path)
    if file_hash is None:
        return None

    file_hash = file_hash.encode()
    try:
        with open(public_key_path, "rb") as key_file:
            public_key = load_pem_public_key(key_file.read(), backend=default_backend())
    except FileNotFoundError:
        print(f"Error: Public key '{public_key_path}' not found.")
        return None

    try:
        public_key.verify(
            signature,
            file_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# Fungsi utama
def main():
    # Menggunakan argparse untuk mengambil argumen dari baris perintah
    parser = argparse.ArgumentParser(description="File Authenticity Detection using Hash and Digital Signature")
    parser.add_argument("--mode", choices=["sender", "receiver"], required=True, help="Mode: sender or receiver")
    parser.add_argument("--file", required=True, help="Path to the file to process")
    parser.add_argument("--private-key", help="Path to the private key (required for sender)")
    parser.add_argument("--public-key", help="Path to the public key (required for receiver)")
    parser.add_argument("--signature", help="Path to save/load the signature")

    args = parser.parse_args()

    # Mengecek mode dan menjalankan sesuai mode
    if args.mode == "sender":
        # Mode pengirim: Generate signature
        if not args.private_key or not args.signature:
            print("Error: Private key and signature file path are required for sender mode.")
            return

        signature = create_signature(args.file, args.private_key)
        if signature is not None:
            with open(args.signature, "wb") as sig_file:
                sig_file.write(signature)
            print(f"Signature generated and saved to {args.signature}")
    
    elif args.mode == "receiver":
        # Mode penerima: Verify signature
        if not args.public_key or not args.signature:
            print("Error: Public key and signature file path are required for receiver mode.")
            return
        
        try:
            with open(args.signature, "rb") as sig_file:
                signature = sig_file.read()
        except FileNotFoundError:
            print(f"Error: Signature file '{args.signature}' not found.")
            return

        is_valid = verify_signature(args.file, signature, args.public_key)
        if is_valid is None:
            print("Verification failed due to missing file or key.")
        elif is_valid:
            print("Signature is valid. The file is authentic.")
        else:
            print("Signature is invalid. The file may have been tampered with.")

if __name__ == "__main__":
    main()
