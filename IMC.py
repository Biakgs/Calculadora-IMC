from tkinter import *
from tkinter import ttk
from tkinter import messagebox

co0 = "#811c43"  
# Vinho
co1 = "#e1e0de"  
# Cinza
co2 = "#7cbfb6"  
# Verde 


janela = Tk()
janela.title('IMC')
janela.geometry('295x230')
janela.iconbitmap("xx.ico")


style = ttk.Style() 
style.theme_use("clam")

frame_cima = Frame(janela, width=295, height=50,bg=co1, pady=0, padx=0, relief="flat",)
frame_cima.grid(row=0, column=0, sticky=NSEW) 

frame_baixo = Frame(janela, width=295, height=200,bg=co1, pady=0, padx=0, relief="flat",)
frame_baixo.grid(row=1, column=0, sticky=NSEW) 


app_imc = Label(frame_cima, text="Calculadora de IMC", width=20, height=1, padx=0, relief="flat", anchor="center", font=('ariel 16 '), bg=co1, fg=co0)
app_imc.place(x=0, y=2) 

app_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

l_peso = Label(frame_baixo , text="Peso", height=1, padx=0, relief="flat", anchor="center", font=('ariel 10 '), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, columnspan=1,  sticky=NW, pady=10, padx=3)
l_peso1 = Label(frame_baixo , text="kg", height=1, padx=0, relief="flat", anchor="center", font=('ariel 10 '), bg=co1, fg=co0)
l_peso1.grid(row=0, column=2, columnspan=1,  sticky=NW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, font=('ariel 10 '),justify='center',relief=RIDGE, bd=2  )
e_peso.grid(row=0, column=1, columnspan=1,  sticky=NSEW, pady=10, padx=3) 

l_altura = Label(frame_baixo , text="Altura", height=1, padx=0, relief="flat", anchor="center", font=('ariel 10 '), bg=co1, fg=co0)
l_altura.grid(row=1, column=0, columnspan=1,  sticky=NW, pady=10, padx=3)
l_altura1 = Label(frame_baixo , text="m", height=1, padx=0, relief="flat", anchor="center", font=('ariel 10 '), bg=co1, fg=co0)
l_altura1.grid(row=1, column=2, columnspan=1,  sticky=NW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, font=('ariel 10 '), justify='center',relief=RIDGE, bd=2)
e_altura.grid(row=1, column=1, columnspan=1,  sticky=NSEW, pady=10, padx=3)  
l_resultado = Label(frame_baixo ,width=5, text="---", height=1, padx=6, pady=12, relief="groove", anchor="center", font=('ariel 24 bold'), bg=co2, fg="white")
l_resultado.place(x=175, y=10) 
l_resultado_texto = Label(frame_baixo , width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center", font=('ariel 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=85)  


b_calcular = Button(frame_baixo, text="Calcular",width=34, height=1, overrelief=SOLID,  bg=co2, fg="white", font=('ariel 10 bold'), anchor="center", relief=RAISED, bd=3 )
b_calcular.grid(row=4, column=0,  sticky=NSEW, pady=60, padx=5, columnspan=30)

def calcular():
  peso = float(e_peso.get())    
  altura = float(e_altura.get())**2    
  resultado = peso/altura        
  if resultado < 18.5:        
    l_resultado_texto['text'] = "Seu IMC ??: Abaixo do peso"
    l_resultado_texto['fg'] = "red"
    messagebox.showinfo(title="Dica", message="Voc?? est?? abaixo do peso ideal. Isso pode ser apenas uma caracter??stica pessoal, mas tamb??m pode ser um sinal de desnutri????o ou de algum problema de sa??de. Caso esteja perdendo peso sem motivo aparente, procure um m??dico.")
  elif resultado >= 18.5 and resultado <= 24.9:
    l_resultado_texto['text'] = "Seu IMC ??: Normal"
    l_resultado_texto['fg'] = "green"
    messagebox.showinfo(title="Dica", message="Parab??ns, voc?? est?? com o peso normal. Recomendamos que mantenha h??bitos saud??veis em seu dia a dia. Especialistas sugerem ingerir de 4 a 5 por????es di??rias de frutas, verduras e legumes, al??m da pr??tica de exerc??cios f??sicos - pelo menos 150 minutos semanais..")
  elif resultado >24.9 and resultado <= 29.9:
    l_resultado_texto['text'] ="Seu IMC ??: Sobrepeso"
    l_resultado_texto['fg'] = "orange"
    messagebox.showinfo(title="Dica", message="Aten????o! Alguns quilos a mais j?? s??o suficientes para que algumas pessoas desenvolvam doen??as associadas, como diabetes e hipertens??o. ?? importante rever seus h??bitos. Procure um m??dico.")
  elif resultado >29.9 and resultado <= 39.9:        
    l_resultado_texto['text'] = "Seu IMC ??: Obesidade"
    l_resultado_texto['fg'] = "red"
    messagebox.showinfo(title="Dica", message="Sinal de alerta! O excesso de peso ?? fator de risco para desenvolvimento de outros problemas de sa??de. A boa not??cia ?? que uma pequena perda de peso j?? traz benef??cios ?? sa??de. Procure um m??dico para definir o tratamento mais adequado para voc??.")
  else:   
    l_resultado_texto['text'] = "Seu IMC ??: Obesidade grave"
    l_resultado_texto['fg'] = "red"
    messagebox.showinfo(title="Dica", message="Sinal vermelho! Ao atingir este n??vel de IMC, o risco de doen??as associadas ?? muito alto. Busque ajuda de um profissional de sa??de; n??o perca tempo.")
     
    
  l_resultado['text'] = "{:.{}f}".format( resultado, 2 )  
  

b_calcular = Button(frame_baixo,command=calcular, text="Calcular",width=34, height=1, overrelief=SOLID,  bg=co2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED )
b_calcular.grid(row=4, column=0,  sticky=NSEW, pady=60, padx=5, columnspan=30)

janela.mainloop()