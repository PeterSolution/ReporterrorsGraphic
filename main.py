import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Utwórz główne okno
root = tk.Tk()
root.title("Prosty interfejs graficzny")

# Dodaj etykietę
label = tk.Label(root, text="Witaj w moim interfejsie graficznym!")
label.pack(pady=10)

# Dodaj pole do wprowadzania tekstu
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Dodaj przycisk
button = tk.Button(root, text="Przywitaj się", command=on_button_click)
button.pack(pady=10)

# Uruchom pętlę główną
root.mainloop()