from tkinter import *
from tkinter import messagebox
from elevate import elevate

elevate()

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirectIp = "127.0.0.1"

def bloquear_sites():
    sites = txt_sites.get("1.0", END).strip().split("\n")
    if not sites or sites == [""]:
        messagebox.showwarning("Aviso", "Nenhum site informado para bloquear.")
        return

    try:
        with open(hostsPath, "r+") as file:
            content = file.read()
            for site in sites:
                if site and site not in content:
                    file.write(f"{redirectIp} {site}\n")
        messagebox.showinfo("Sucesso", "Sites bloqueados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao bloquear sites: {e}")

def desbloquear_sites():
    sites = txt_sites.get("1.0", END).strip().split("\n")
    if not sites or sites == [""]:
        messagebox.showwarning("Aviso", "Nenhum site informado para desbloquear.")
        return

    try:
        with open(hostsPath, "r") as file:
            lines = file.readlines()

        with open(hostsPath, "w") as file:
            for line in lines:
                if not any(site in line for site in sites):
                    file.write(line)

        messagebox.showinfo("Sucesso", "Sites desbloqueados com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao desbloquear sites: {e}")

def ver_sites_bloqueados():
    try:
        with open(hostsPath, "r") as file:
            lines = file.readlines()
            bloqueados = [line.split()[1] for line in lines if line.startswith(redirectIp)]

        if bloqueados:
            sites_bloqueados_window = Toplevel(root)  #
            sites_bloqueados_window.title("Sites Bloqueados")
            sites_bloqueados_window.geometry("400x400")
            sites_bloqueados_window.configure(bg="#2C3E50")

            Label(sites_bloqueados_window, text="Sites Bloqueados:", font=("Poppins", 14, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

            txt_bloqueados = Text(sites_bloqueados_window, height=15, width=50, relief="flat", bd=1, highlightbackground="#7F8C8D", font=("Poppins", 12), fg="white", bg="#34495E")
            txt_bloqueados.insert(END, "\n".join(bloqueados))  
            txt_bloqueados.config(state=DISABLED) 
            txt_bloqueados.pack(padx=20, pady=10)

        else:
            messagebox.showinfo("Sem Sites Bloqueados", "Não há sites bloqueados no momento.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo de hosts: {e}")

# Interface Tkinter
root = Tk()
root.title("Bloqueador de Sites")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#2C3E50")  

title_frame = Frame(root, bg="#34495E", pady=10)
title_frame.pack(fill=X)
Label(title_frame, text="Bloqueador de Sites", font=("Poppins", 18, "bold"), bg="#34495E", fg="white").pack()

frame_entry = Frame(root, bg="#2C3E50")
frame_entry.pack(pady=20, fill=X)

Label(frame_entry, text="Digite o endereço do site: (ex: www.facebook.com)", font=("Poppins", 12), bg="#2C3E50", fg="white").pack(anchor="w", padx=20, pady=5)

txt_sites = Text(frame_entry, height=4, width=50, relief="flat", bd=1, highlightbackground="#7F8C8D", font=("Poppins", 12), wrap=WORD, fg="white", bg="#34495E")
txt_sites.pack(padx=20, pady=5)

frame_buttons = Frame(root, bg="#2C3E50")
frame_buttons.pack(pady=10)

btn_bloquear = Button(frame_buttons, text="Bloquear Site", bg="#E74C3C", fg="white", font=("Poppins", 10, "bold"), width=15, relief="flat", command=bloquear_sites)
btn_bloquear.grid(row=0, column=0, padx=10, pady=10, ipadx=8, ipady=8)

btn_desbloquear = Button(frame_buttons, text="Desbloquear Site", bg="#1ABC9C", fg="white", font=("Poppins", 10, "bold"), width=15, relief="flat", command=desbloquear_sites)
btn_desbloquear.grid(row=0, column=1, padx=10, pady=10, ipadx=8, ipady=8)

btn_ver_bloqueados = Button(frame_buttons, text="Ver Sites Bloqueados", bg="#9B59B6", fg="white", font=("Poppins", 10, "bold"), width=20, relief="flat", command=ver_sites_bloqueados)
btn_ver_bloqueados.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=8, ipady=8)


root.mainloop()
