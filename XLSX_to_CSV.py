from tkinter import *
from tkinter import filedialog
import pandas as pd

def conversao():
    fileNames = filedialog.askopenfilename()
    print(fileNames)
    newfileNames = fileNames.replace(".xlsx",".csv")
    wb = pd.read_excel(fileNames,engine='openpyxl')
    df=pd.DataFrame(wb)
    df.to_csv(newfileNames,sep=';', index=False, encoding='utf-8')
    resultado["text"]="Concluído!\n Arquivo disponivel em: \n"+newfileNames

#---------------------------------------------------------------------------------------------------------------------

janela=Tk()
janela.title("Conversor xlsx para csv")
#janela.geometry("400x400")

instruction = Label(janela,text="Selecione o arquivo que deve ser convertido clicando no botão abaixo")
instruction.grid(column=0,row=0,padx=50,pady=20)

botao= Button(janela,text="clique aqui",command=conversao)
botao.grid(column=0,row=1,padx=20,pady=20)

resultado=Label(janela,text=" ")
resultado.grid(column=0,row=2,padx=20,pady=20)

janela.mainloop()

#abaixo codigo para transformar um arquivo py em exe
#python -m PyInstaller --onefile --windowed --name="fileName" Homework.py
