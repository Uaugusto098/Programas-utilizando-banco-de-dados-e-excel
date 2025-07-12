import pandas as pd 
import statistics as st
caminho='tabelaalunos.xlsx'
ex=pd.read_excel('tabelaalunos.xlsx')
tabelas=[ex['Matematica'],ex['Fisica'],ex['Portugues'],ex['Biologia']]
inicio=True
# tbmat=(ex['Matematica'])
# tbfis=(ex['Fisica'])
# tbpt=(ex['Portugues'])
# tbbio=(ex['Biologia'])
print("                    Tabela de Notas ")
print("\n",ex.head())

while inicio==True:
    print('''
    1-Matematica
    2-Fisica
    3-Portugues
    4-Biologia
    5-Média de todas as notas
    0-Sair
            ''')
    escolha=input("Qual materia deseja saber a média ?: ")
    match escolha:

        case "1":
            print("Média Matematica: ",st.mean(tabelas[0]))
            
        case "2":
            print("Média Fisica: ",st.mean(tabelas[1]))
            
        case "3":
            print("Média Portugues: ",st.mean(tabelas[2]))
            
        case "4":
            print("Média Biologia: ",st.mean(tabelas[3])) 
        case "5":
            print("Matematica: ",st.mean(tabelas[0]))
            print("Fisica: ",st.mean(tabelas[1]))
            print("Portugues: ",st.mean(tabelas[2]))
            print("Biologia: ",st.mean(tabelas[3])) 
            inicio=False


        case "0":
            inicio=False  
            


    
    































