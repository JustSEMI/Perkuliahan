import os
import tkinter as tk
from tkinter import ttk, messagebox

BG_COLOR    = "#1e1e1e"
FG_COLOR    = "#dcdcdc"
BTN_COLOR   = "#2d2d2d"
BTN_HOVER   = "#3c3c3c"
ACCENT      = "#007acc"
DATA_FILE   = "crud.txt"

data = []

def load_data():
    """Baca data dari file .txt"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if "," in line:
                    nama, alamat = line.strip().split(",", 1)
                    data.append({"nama": nama, "alamat": alamat})
    update_table()

def save_data():
    """Simpan data ke file .txt"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for d in data:
            f.write(f"{d['nama']},{d['alamat']}\n")

def update_table():
    tree.delete(*tree.get_children())
    for i, item in enumerate(data, start=1):
        tree.insert("", "end", values=(i, item["nama"], item["alamat"]))

def tambah_data():
    nama = entry_nama.get().strip()
    alamat = entry_alamat.get().strip()
    if nama and alamat:
        data.append({"nama": nama, "alamat": alamat})
        save_data()
        update_table()
        entry_nama.delete(0, tk.END)
        entry_alamat.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Data berhasil ditambahkan!")
    else:
        messagebox.showwarning("Peringatan", "Nama dan alamat tidak boleh kosong!")

def ubah_data():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin diubah!")
        return

    nama_baru = entry_nama.get().strip()
    alamat_baru = entry_alamat.get().strip()

    if not (nama_baru and alamat_baru):
        messagebox.showwarning("Peringatan", "Nama dan alamat tidak boleh kosong!")
        return

    idx = int(tree.item(selected, "values")[0]) - 1
    data[idx]["nama"] = nama_baru
    data[idx]["alamat"] = alamat_baru
    save_data()
    update_table()
    messagebox.showinfo("Sukses", "Data berhasil diubah!")

def hapus_data():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
        return

    idx = int(tree.item(selected, "values")[0]) - 1
    konfirmasi = messagebox.askyesno("Konfirmasi", f"Hapus data '{data[idx]['nama']}'?")
    if konfirmasi:
        data.pop(idx)
        save_data()
        update_table()
        entry_nama.delete(0, tk.END)
        entry_alamat.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Data berhasil dihapus!")

def pilih_data(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_nama.delete(0, tk.END)
        entry_alamat.delete(0, tk.END)
        entry_nama.insert(0, values[1])
        entry_alamat.insert(0, values[2])

root = tk.Tk()
root.title("CRUDUI")
root.geometry("600x400")
root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background=BG_COLOR,
                fieldbackground=BG_COLOR,
                foreground=FG_COLOR,
                rowheight=25,
                font=("Consolas", 10))
style.configure("Treeview.Heading",
                background=BTN_COLOR,
                foreground=FG_COLOR,
                font=("Consolas", 10, "bold"))
style.map("Treeview",
          background=[("selected", ACCENT)],
          foreground=[("selected", "white")])

frame_input = tk.Frame(root, bg=BG_COLOR)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Nama:", fg=FG_COLOR, bg=BG_COLOR, font=("Consolas", 10)).grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(frame_input, bg=BTN_COLOR, fg=FG_COLOR, insertbackground="white", width=40, relief="flat")
entry_nama.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Alamat:", fg=FG_COLOR, bg=BG_COLOR, font=("Consolas", 10)).grid(row=1, column=0, padx=5, pady=5)
entry_alamat = tk.Entry(frame_input, bg=BTN_COLOR, fg=FG_COLOR, insertbackground="white", width=40, relief="flat")
entry_alamat.grid(row=1, column=1, padx=5, pady=5)

frame_btn = tk.Frame(root, bg=BG_COLOR)
frame_btn.pack(pady=10)

def hover_in(e): e.widget.config(bg=BTN_HOVER)
def hover_out(e): e.widget.config(bg=BTN_COLOR)

for text, cmd in [("Tambah", tambah_data), ("Ubah", ubah_data), ("Hapus", hapus_data)]:
    btn = tk.Button(frame_btn, text=text, command=cmd,
                    bg=BTN_COLOR, fg=FG_COLOR, activebackground=ACCENT,
                    relief="flat", padx=10, pady=5, font=("Consolas", 10))
    btn.pack(side="left", padx=5)
    btn.bind("<Enter>", hover_in)
    btn.bind("<Leave>", hover_out)

columns = ("No", "Nama", "Alamat")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("No", text="No")
tree.heading("Nama", text="Nama")
tree.heading("Alamat", text="Alamat")
tree.column("No", width=40, anchor="center")
tree.column("Nama", width=150)
tree.column("Alamat", width=300)
tree.bind("<ButtonRelease-1>", pilih_data)
tree.pack(padx=10, pady=10, fill="both", expand=True)

load_data()

root.mainloop()