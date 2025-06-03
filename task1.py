import tkinter as tk
from tkinter import messagebox

def caesar_shift(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def encrypt():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")
        return
    text = input_text.get("1.0", "end").strip()
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", caesar_shift(text, shift))
    output_text.config(state="disabled")

def decrypt():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer.")
        return
    text = input_text.get("1.0", "end").strip()
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", caesar_shift(text, -shift))
    output_text.config(state="disabled")

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("600x600")
root.config(bg="#1e1f29")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Caesar Cipher Tool", font=("Segoe UI", 22, "bold"), bg="#1e1f29", fg="#6c63ff")
title.pack(pady=20)

# Frame
frame = tk.Frame(root, bg="#292b3e", padx=20, pady=20)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Input label and text
input_label = tk.Label(frame, text="Enter your message:", font=("Segoe UI", 12, "bold"), bg="#292b3e", fg="#ecf0f1")
input_label.pack(anchor="w")
input_text = tk.Text(frame, height=5, font=("Segoe UI", 12), bg="#3c3f58", fg="#ecf0f1", insertbackground="#ecf0f1", bd=0, relief="flat")
input_text.pack(fill="x", pady=(5, 15))

# Shift label and entry
shift_label = tk.Label(frame, text="Enter shift value (integer):", font=("Segoe UI", 12, "bold"), bg="#292b3e", fg="#ecf0f1")
shift_label.pack(anchor="w")
shift_entry = tk.Entry(frame, font=("Segoe UI", 12), bg="#3c3f58", fg="#ecf0f1", insertbackground="#ecf0f1", bd=0, relief="flat")
shift_entry.pack(fill="x", pady=(5, 15))

# Buttons frame
btn_frame = tk.Frame(frame, bg="#292b3e")
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt ??", font=("Segoe UI", 14, "bold"), bg="#48c774", fg="white",
                        activebackground="#3abd63", activeforeground="white", relief="flat", padx=20, pady=8,
                        cursor="hand2", command=encrypt)
encrypt_btn.grid(row=0, column=0, padx=15)

decrypt_btn = tk.Button(btn_frame, text="Decrypt ??", font=("Segoe UI", 14, "bold"), bg="#c0392b", fg="white",
                        activebackground="#e74c3c", activeforeground="white", relief="flat", padx=20, pady=8,
                        cursor="hand2", command=decrypt)
decrypt_btn.grid(row=0, column=1, padx=15)

# Output label and text
output_label = tk.Label(root, text="Result:", font=("Segoe UI", 16, "bold"), bg="#1e1f29", fg="#6c63ff", pady=10)
output_label.pack(anchor="w", padx=40)

output_text = tk.Text(root, height=6, font=("Segoe UI", 13), bg="#3c3f58", fg="#ecf0f1", wrap="word", bd=0, relief="flat", padx=15, pady=15)
output_text.pack(padx=20, pady=(0, 20), fill="both")
output_text.config(state="disabled")

root.mainloop()

