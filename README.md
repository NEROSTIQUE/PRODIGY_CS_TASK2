🔐 Image Encryption and Decryption Tool
A lightweight and user-friendly Image Encryption Tool built using Python, Tkinter, and Pillow (PIL). This application allows users to securely encrypt and decrypt images using simple pixel manipulation techniques and a secret key. Ideal for educational purposes, lightweight image protection, or just exploring how pixel-level image processing works.

🚀 Features
✅ Encrypt any image using a numeric key.

🔄 Decrypt images encrypted with the tool using the same key.

🔢 Uses custom pixel manipulation and row-swapping for encryption.

💾 Save the encrypted or decrypted image locally.

🖼️ View images in the application before and after processing.

🧪 Lightweight and beginner-friendly code structure for learning purposes.

🛠️ How It Works
Pixel Manipulation: Each pixel’s RGB values are altered mathematically using the encryption key.

Row Swapping: Half of the image’s rows are flipped vertically to add a layer of confusion.

Decryption: The process is reversed using the same key to retrieve the original image.

🧑‍💻 Requirements
Python 3.7+

Pillow

Install dependencies using:


🔐 Example
Original Image → Encrypt with key 123 → Encrypted Image

Encrypted Image → Decrypt with same key 123 → Original Image


This tool is intended for learning and experimentation in:

Image processing

Cryptography basics

GUI development with Tkinter

⚠️ Note: This is not a secure encryption for production or sensitive data. For secure encryption, consider using cryptographic libraries like PyCryptodome.

📃 License
This project is licensed under the MIT License.

❤️ Contribute
Pull requests, suggestions, and improvements are welcome!
If you find this project helpful, feel free to ⭐️ star it and share it with others.
