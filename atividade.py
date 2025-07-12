import pandas as pd
import sqlite3 as sqlite 


data = pd.Series([1, 3, 5, 7, 9])
print(data)

# Criar um DataFrame
data = {'Nome': ['Ana', 'Bob', 'Catarina', 'Daniel'],
        'Idade': [23, 35, 45, 27],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}
df = pd.DataFrame(data)
print(df)







# data=pd.Series([1,2,35,7,9])
# print(data)
# conn=sqlite.connect('Atividade.db')
# cursor=conn.cursor()


# def tabela():
#     cursor.execute(''' 
    
#     CREATE TABLE IF NOT EXISTS dados (
#     nome TEXT NOT NULL,
#     idade INTEGER NOT NULL,
#     cidade TEXT NOT NULL
#                                       )'''
#                                       )

#     conn.commit()

# def dados():
#     cursor.execute(''' INSERT INTO dados (nome,idade,cidade) VALUES (?,?,?)   ''')
#     conn.commit()





# tabela()
# dados()



# 2 leitura de Dados de Arquivos
# 3 Visualização de Dados
# 4 seleção e Indexação
# 5 Filtragem de Dados
# 6. Manipulação de Dados










