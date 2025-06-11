import pandas as pd
import matplotlib.pyplot as plt
import os

# Definir o caminho da pasta csv
pasta_csv = 'csv'

# Lista com os nomes dos 7 arquivos CSV
arquivos = ['resultados1.csv', 'resultados2.csv', 'resultados3.csv', 
           'resultados4.csv', 'resultados5.csv', 'resultados6.csv', 'resultados7.csv']

# Criar caminhos completos para os arquivos na pasta csv
caminhos_arquivos = [os.path.join(pasta_csv, arquivo) for arquivo in arquivos]

# Verificar se a pasta csv existe
if not os.path.exists(pasta_csv):
    print(f"✗ Erro: A pasta '{pasta_csv}' não foi encontrada!")
    print(f"Certifique-se de que a pasta '{pasta_csv}' existe no diretório atual.")
    exit(1)

# Ler todos os arquivos e armazenar em uma lista
print(f"Lendo arquivos CSV da pasta '{pasta_csv}'...")
dfs = []
for i, (arquivo, caminho) in enumerate(zip(arquivos, caminhos_arquivos), 1):
    try:
        df = pd.read_csv(caminho)
        dfs.append(df)
        print(f"✓ {arquivo} carregado com sucesso")
    except FileNotFoundError:
        print(f"✗ Erro: {arquivo} não encontrado na pasta '{pasta_csv}'")
        exit(1)

print(f"\nTotal de {len(dfs)} arquivos carregados com sucesso!")

# Calcular média apenas do tempo (N e contador são constantes)
print("\nCalculando média dos tempos de execução...")
dados_media = pd.concat(dfs).groupby('N').agg({
    'Contador': 'first',  # Pega o primeiro valor (são todos iguais)
    'Tempo de execucao': 'mean'  # Calcula a média apenas do tempo
}).reset_index()

# Mostrar os dados com média
print("\nDados com tempo médio calculado:")
print(dados_media)
print(f"\nObservação: N e Contador são constantes entre execuções.")
print(f"Apenas o tempo de execução varia e teve sua média calculada de {len(arquivos)} execuções.")

# Gráfico 1: Tempo médio de execução
plt.figure(figsize=(12, 6))
plt.plot(dados_media['N'], dados_media['Tempo de execucao'], 'b-o', linewidth=2, markersize=8)
plt.xlabel('N', fontsize=12)
plt.ylabel('Tempo Médio de Execução (segundos)', fontsize=12)
plt.title(f'Tempo Médio de Execução vs Tamanho de Entrada (Média de {len(arquivos)} execuções)', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.7)
plt.yscale('log')
plt.tight_layout()
plt.show()

# Gráfico 2: Contador (valores constantes)
plt.figure(figsize=(12, 6))
plt.plot(dados_media['N'], dados_media['Contador'], 'r-o', linewidth=2, markersize=8)
plt.xlabel('N', fontsize=12)
plt.ylabel('Contador (operações)', fontsize=12)
plt.title('Número de Operações vs Tamanho de Entrada', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.7)
plt.yscale('log')
plt.tight_layout()
plt.show()

# Salvar os gráficos
salvar = input("\nDeseja salvar os gráficos? (s/n): ").lower()
if salvar == 's':
    # Recriar e salvar o primeiro gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(dados_media['N'], dados_media['Tempo de execucao'], 'b-o', linewidth=2, markersize=8)
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Tempo Médio de Execução (segundos)', fontsize=12)
    plt.title(f'Tempo Médio de Execução vs Tamanho de Entrada (Média de {len(arquivos)} execuções)', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.7)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('tempo_medio_7execucoes.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Recriar e salvar o segundo gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(dados_media['N'], dados_media['Contador'], 'r-o', linewidth=2, markersize=8)
    plt.xlabel('N', fontsize=12)
    plt.ylabel('Contador (operações)', fontsize=12)
    plt.title('Número de Operações vs Tamanho de Entrada', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.7)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('contador_7execucoes.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Gráficos salvos como 'tempo_medio_7execucoes.png' e 'contador_7execucoes.png'")

# Salvar dados médios em CSV na pasta csv
salvar_csv = input("Deseja salvar os dados médios em CSV? (s/n): ").lower()
if salvar_csv == 's':
    caminho_resultado = os.path.join(pasta_csv, 'resultados_media_7execucoes.csv')
    dados_media.to_csv(caminho_resultado, index=False)
    print(f"✓ Dados médios salvos em '{caminho_resultado}'")

print("\nAnálise concluída!")
print(f"Média calculada com base em {len(arquivos)} execuções para maior precisão estatística.")
