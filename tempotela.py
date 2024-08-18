"""
// Disciplina: Algoritmos e Estrutura de dados
// Professor: Miguel Gabriel Prazeres de Carvalho
// Descrição: Séries Temporais.
// Autor: Lucas de Souza Lima

Séries Temporais: Tempo de Tela smartphone
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tempo_tela.csv') #carrega o dataframe em csv
df.Dia = pd.to_datetime(df.Dia) #converte a coluna 'Dia' para datetime
df.set_index('Dia', inplace=True)   #define a coluna 'Dia' como índice
#calcula a média móvel dos últimos 5 dias
df['Média Móvel dos últimos 5 Dias'] = df['Tempo de Tela(min)'].rolling(window=27).mean() 
df.plot(figsize=(9,4))  #plota o gráfico
plt.title('Tempo de Tela Diário no Mês de Agosto e Média Móvel dos Últimos 5 dias')  #título do gráfico
plt.ylabel('Tempo de Tela(min)')    #rótulo do eixo y
plt.xlabel('Dia')   #rótulo do eixo x
plt.grid()  #mostra a grade
plt.legend()    #mostra a legenda
plt.show()  #mostra o gráfico