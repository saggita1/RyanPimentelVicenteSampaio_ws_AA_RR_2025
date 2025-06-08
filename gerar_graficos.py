import pandas as pd
import matplotlib.pyplot as plt

# ler o csv
dados = pd.read_csv('resultados.csv')

# ver os dados
print(dados)

# plotar
plt.figure(figsize=(10, 6))
plt.plot(dados['N'], dados['Tempo de execucao'], 'b-o')
plt.xlabel('N')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de execucao vs tamanho de entrada')
plt.grid(True)
#plt.yscale('log')  # escala log
plt.show()

#plotar segundo
plt.figure(figsize=(10, 6))
plt.plot(dados['N'], dados['Contador'], 'b-o')
plt.xlabel('N')
plt.ylabel('Contador')
plt.title('Contador vs tamanho de entrada')
plt.grid(True)
#plt.yscale('log')  # escala log
plt.show()