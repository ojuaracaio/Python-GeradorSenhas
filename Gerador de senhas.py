from tkinter import *
import random

root=Tk()
root.title('Gerador de Senhas')

dicionario=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','&','*']

def gerar():
	senha=random.choices(dicionario,k=slider.get())
	resultado.delete(0,END)
	resultado.insert(0,''.join(senha))
	

dificuldade = LabelFrame(root, text='Dificuldade')
saída=LabelFrame(root, text='Resultado')
botao=Button(root, text='Gerar Senha', command=gerar)
slider=Scale(dificuldade, from_=5, to=20, orient=HORIZONTAL)
resultado=Entry(saída)

dificuldade.pack()
slider.pack()
botao.pack()
saída.pack()
resultado.pack()



root.mainloop()