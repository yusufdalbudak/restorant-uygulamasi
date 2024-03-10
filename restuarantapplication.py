import tkinter as tk
from tkinter import messagebox, simpledialog


masalar = {a: 0 for a in range(20)}


def dosya_kontrolu(dosya_adi="bakiye.txt"):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            veri = dosya.read().split("\n")[:-1]
            for index, bakiye in enumerate(veri):
                masalar[index] = float(bakiye)
    except FileNotFoundError:
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            print("Kayıt dosyası oluşturuldu.")

def dosya_guncelle(dosya_adi="bakiye.txt"):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for bakiye in masalar.values():
            dosya.write(f"{bakiye}\n")


def hesap_ekle():
    masa_no = simpledialog.askinteger("Hesap Ekle", "Masa Numarası:")
    if masa_no is not None and 0 <= masa_no < 20:
        eklenecek_ücret = simpledialog.askfloat("Hesap Ekle", "Eklenecek Ücret:")
        if eklenecek_ücret is not None:
            masalar[masa_no] += eklenecek_ücret
            bilgi_guncelle()
    else:
        messagebox.showerror("Hata", "Geçersiz masa numarası!")


def hesap_odeme():
    masa_no = simpledialog.askinteger("Hesap Ödeme", "Masa Numarası:")
    if masa_no is not None and 0 <= masa_no < 20:
        masalar[masa_no] = 0
        bilgi_guncelle()
    else:
        messagebox.showerror("Hata", "Geçersiz masa numarası!")


def bilgi_guncelle():
    bilgi_alani.config(state=tk.NORMAL)
    bilgi_alani.delete('1.0', tk.END)
    for masa_no, bakiye in masalar.items():
        bilgi_alani.insert(tk.END, f"Masa {masa_no}: {bakiye} TL\n")
    bilgi_alani.config(state=tk.DISABLED)


root = tk.Tk()
root.title("DALBUDAK RESTAURANT UYGULAMASI")
root.geometry("400x600")


tk.Button(root, text="Masaları Görüntüle", command=bilgi_guncelle).pack(pady=10)
tk.Button(root, text="Hesap Ekle", command=hesap_ekle).pack(pady=10)
tk.Button(root, text="Hesap Ödeme", command=hesap_odeme).pack(pady=10)
tk.Button(root, text="Çıkış", command=lambda: (dosya_guncelle(), root.destroy())).pack(pady=10)


bilgi_alani = tk.Text(root, height=20, width=50, state=tk.DISABLED)
bilgi_alani.pack(pady=10)


dosya_kontrolu()
bilgi_guncelle()
root.mainloop()
