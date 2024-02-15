import tkinter as tk

def btc_cli():
    label.config(text="c, " + entry.get())

# Utwórz główne okno
root = tk.Tk()
root.title("b")

# Dodaj etykietę
label = tk.Label(root, text="a")
label.pack(pady=10)

# Dodaj pole do wprowadzania tekstu
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Dodaj przycisk
button = tk.Button(root, text="d", command=btc_cli)
button.pack(pady=10)

# Uruchom pętlę główną
root.mainloop()
