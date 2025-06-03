import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import random

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.image = None
        self.encrypted_image = None
        self.image_path = ""

        # GUI layout
        self.label = tk.Label(root, text="No image loaded.")
        self.label.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=5)

        self.key_entry = tk.Entry(root, width=30)
        self.key_entry.insert(0, "Enter encryption key (number)")
        self.key_entry.pack(pady=5)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_image)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_image)
        self.decrypt_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=5)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.bmp")])
        if path:
            self.image_path = path
            self.image = Image.open(path).convert("RGB")
            self.display_image(self.image)
            self.label.config(text=os.path.basename(path))

    def display_image(self, img):
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.imgtk = img_tk
        self.canvas.configure(image=img_tk)

    def get_key(self):
        try:
            return int(self.key_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Key", "Please enter a numeric key.")
            return None

    def encrypt_image(self):
        key = self.get_key()
        if key is None or self.image is None:
            return

        img = self.image.copy()
        pixels = img.load()

        width, height = img.size
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                # Simple pixel manipulation
                pixels[i, j] = (
                    (r + key) % 256,
                    (g + key * 2) % 256,
                    (b + key * 3) % 256,
                )

        # Swapping rows based on key
        for j in range(height // 2):
            for i in range(width):
                p1 = pixels[i, j]
                p2 = pixels[i, height - j - 1]
                pixels[i, j], pixels[i, height - j - 1] = p2, p1

        self.encrypted_image = img
        self.display_image(img)
        self.label.config(text="Encrypted")

    def decrypt_image(self):
        key = self.get_key()
        if key is None or self.encrypted_image is None:
            return

        img = self.encrypted_image.copy()
        pixels = img.load()

        width, height = img.size
        # Re-swap the rows
        for j in range(height // 2):
            for i in range(width):
                p1 = pixels[i, j]
                p2 = pixels[i, height - j - 1]
                pixels[i, j], pixels[i, height - j - 1] = p2, p1

        # Reverse pixel manipulation
        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (
                    (r - key) % 256,
                    (g - key * 2) % 256,
                    (b - key * 3) % 256,
                )

        self.encrypted_image = img
        self.display_image(img)
        self.label.config(text="Decrypted")

    def save_image(self):
        if self.encrypted_image:
            path = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png")])
            if path:
                self.encrypted_image.save(path)
                messagebox.showinfo("Saved", "Image saved successfully!")
        else:
            messagebox.showwarning("No image", "No image to save!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
