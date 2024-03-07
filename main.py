# pip install pillow

import os
import tkinter.font as tkFont
import csv

# importando Tkinter

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog

#  Importando pillow

from PIL import Image, ImageTk
from matplotlib.pyplot import text




# cores

cor0 = "#f0f3f5" # preto
cor1 = "#feffff" # branco
cor2 = "#3fb5a3" # verde
cor3 = "#fc766d" # vermelho
cor4 = "#403d3d" # letra
cor5 = "#4a88e8" # azul


# criando a janela

janela = Tk ()
janela.title ("")
janela.geometry('390x350')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)


# frames

frame_logo = Frame(janela, width=400, height=60, bg=cor1, relief="flat")
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=400, height=400, bg=cor1, relief="flat")
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#  Configurando frame logo

# imagem = Image.open('icon.png')
imagem = Image.open(os.path.join(r'E:\Curso\Projetos\website_block\icon.png')) # caminho da imagem.
imagem = imagem.resize((45, 45))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_logo, height=60, image=imagem, background=cor1)
l_imagem.place(x=20, y=3)

l_logo = Label(frame_logo, text='Bloqueador de Sites', height=1, anchor=NE, font=('Ivy 25'),  background=cor1, fg=cor4)
l_logo.place(x=70, y=10)

l_linha = Label(frame_logo, text='', width=445, height=1, anchor=NW, font=('Ivy 1'),  background=cor3)
l_linha.place(x=0, y=57)

# Criando funções

global iniciar
global websites

iniciar = BooleanVar()

# Função ver_site

def ver_site():
    listabox.delete(0,END)
    
    # acessando arquivo csv
    with open('sites.csv') as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            listabox.insert(END, row)

# Função salvar_site

def salvar_site(i):
    # acessando arquivo csv
    with open('sites.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i])
        messagebox.showinfo('Site', 'O Site foi adicionado!')
        
    ver_site()

# Função deletar site

def deletar_site(i):
    
    def adicionar(i):
        # acessando arquivo csv
        with open('sites.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(i)
            messagebox.showinfo('Site', 'O Site foi removido!')
            
        ver_site()
    
    nova_lista = []
    with open('sites.csv', 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            nova_lista.append(row)
            for campo in row:
                if campo == i:
                    print(campo)
                    nova_lista.remove(row)
                    
    adicionar(nova_lista)
                    
                    
# Função Adicionar

def adicionar_site():
    site = e_site.get()
    if site == '':
        pass
    else:
        listabox.insert(END,site)
        e_site.delete(0,END)
        salvar_site(site)
        
# Função remover

def remover_site():
    site = listabox.get(ACTIVE)
    sites = []
    for i in site:
        sites.append(i)
    deletar_site(sites[0])
        
        
def desbloquear_sites():
    iniciar.set(False)
    messagebox.showinfo('Site', 'Os sites foram desbloqueados')
    bloqueador_site()        

def bloquear_sites():
    iniciar.set(True)
    messagebox.showinfo('Site', 'Os sites foram bloqueados')
    bloqueador_site()

# Função bloqueador sites

def bloqueador_site():
    
    # caminho do arquivo host do windows
    local_do_host = r"C:\Windows\System32\drivers\etc\hosts"
    redicionar = '127.0.0.1'
    
    websites = []
    
    # acessando o ficheiro CSV
    
    with open('sites.csv') as file:
        ler_csv = csv.reader(file)
        for row in ler_csv:
            websites.append(row[0]) 
    
    if iniciar.get()==True:
        with open(local_do_host,'r+') as arquivo:
            conteudo=arquivo.read()
            for site in websites:
                if site in conteudo:
                    pass
                else:
                    arquivo.write(redicionar+" "+site+"\n")
    else:
        with open(local_do_host,'r+') as arquivo:
            conteudo=arquivo.readlines()
            arquivo.seek(0)
            for line in conteudo:
                if not any(site in line for site in websites):
                    arquivo.write(line)
            arquivo.truncate()
    
    
    
    

# Configurando frame corpo

l_site = Label(frame_corpo, text='Digite o site que deseja bloquear no campo abaixo *', height=1, anchor=NE, font=('Ivy 10 bold'),  background=cor1, fg=cor4)
l_site.place(x=20, y=20)

e_site = Entry(frame_corpo, width=21, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
e_site.place(x=23, y=50)

b_add = Button(frame_corpo, command=adicionar_site, text='Adicionar', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor5, fg=cor1)
b_add.place(x=267, y=50)

b_remv = Button(frame_corpo, command=remover_site, text='Remover', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor5, fg=cor1)
b_remv.place(x=267, y=100)


b_desbloquear = Button(frame_corpo, command=desbloquear_sites, text='Desbloquear', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor3, fg=cor1)
b_desbloquear.place(x=267, y=150)

b_bloquear = Button(frame_corpo, command=bloquear_sites, text='Bloquear', width=10, height=1, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, background=cor2, fg=cor1)
b_bloquear.place(x=267, y=200)


listabox = Listbox(frame_corpo, font=('Aria 9 bold'), width=33, height=10)
listabox.place(x=23, y=100)

ver_site()

janela.mainloop ()

