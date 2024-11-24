from tkinter import *
from tkinter import messagebox
from elevate import elevate

# Elevar privilégios para administrador
elevate()

# Arquivo hosts
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

# Função para bloquear sites
def bloquear_sites():
    sites = txt_sites.get("1.0", END).strip().split("\n")
    if not sites or sites == [""]:
        messagebox.showwarning("Aviso", "Nenhum site informado para bloquear.")
        return

    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in sites:
                if site and site not in content:
                    file.write(f"{redirect_ip} {site}\n")
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Sites bloqueados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao bloquear sites: {e}")

# Função para desbloquear sites
def desbloquear_sites():
    sites = txt_sites.get("1.0", END).strip().split("\n")
    if not sites or sites == [""]:
        messagebox.showwarning("Aviso", "Nenhum site informado para desbloquear.")
        return

    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()

        with open(hosts_path, "w") as file:
            for line in lines:
                if not any(site in line for site in sites):
                    file.write(line)



                    

        atualizar_lista()
        messagebox.showinfo("Sucesso", "Sites desbloqueados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao desbloquear sites: {e}")

# Função para atualizar a lista de sites bloqueados
def atualizar_lista():
    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()
            bloqueados = [line.split()[1] for line in lines if line.startswith(redirect_ip)]
        txt_bloqueados.delete("1.0", END)
        txt_bloqueados.insert("1.0", "\n".join(bloqueados))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar lista: {e}")

# Interface Tkinter
root = Tk()
root.title("Bloqueador de Sites")
root.geometry("600x700")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Título
title_frame = Frame(root, bg="#f4f4f4", pady=10)
title_frame.pack(fill=X)
Label(title_frame, text="Bloqueador de Sites", font=("Arial", 24, "bold"), bg="#f4f4f4", fg="#333").pack()

# Frame para entrada de sites
frame_entry = Frame(root, bg="#f4f4f4")
frame_entry.pack(pady=15, fill=X)

Label(frame_entry, text="Digite o endereço do site (ex: www.facebook.com):", font=("Arial", 12), bg="#f4f4f4").pack(anchor="w", padx=20, pady=5)

txt_sites = Text(frame_entry, height=5, width=60, relief="solid", bd=1, highlightbackground="#ddd", font=("Arial", 10))
txt_sites.pack(padx=20, pady=5)

# Botões
frame_buttons = Frame(root, bg="#f4f4f4")
frame_buttons.pack(pady=10)

btn_bloquear = Button(frame_buttons, text="Bloquear Site", bg="#ff6b6b", fg="white", font=("Arial", 10, "bold"),
                      width=15, relief="groove", command=bloquear_sites)
btn_bloquear.grid(row=0, column=0, padx=20, pady=10)

btn_desbloquear = Button(frame_buttons, text="Desbloquear Site", bg="#2ecc71", fg="white", font=("Arial", 10, "bold"),
                         width=15, relief="groove", command=desbloquear_sites)
btn_desbloquear.grid(row=0, column=1, padx=20, pady=10)

# Lista de sites bloqueados
frame_bloqueados = Frame(root, bg="#f4f4f4")
frame_bloqueados.pack(pady=20, fill=X)

Label(frame_bloqueados, text="Sites Bloqueados:", font=("Arial", 12, "bold"), bg="#f4f4f4").pack(anchor="w", padx=20, pady=5)

txt_bloqueados = Text(frame_bloqueados, height=15, width=60, relief="solid", bd=1, highlightbackground="#ddd", font=("Arial", 10))
txt_bloqueados.pack(padx=20, pady=5)

# Atualizar lista ao iniciar
atualizar_lista()

# Iniciar o loop da interface
root.mainloop()
