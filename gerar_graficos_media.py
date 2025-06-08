import pandas as pd
import matplotlib.pyplot as plt

# Lista com os nomes dos arquivos CSV
arquivos = ['resultados1.csv', 'resultados2.csv', 'resultados3.csv']

# Ler todos os arquivos e armazenar em uma lista
print("Lendo arquivos CSV...")
dfs = []
for i, arquivo in enumerate(arquivos, 1):
    try:
        df = pd.read_csv(arquivo)
        dfs.append(df)
        print(f"✓ {arquivo} carregado com sucesso")
    except FileNotFoundError:
        print(f"✗ Erro: {arquivo} não encontrado")
        exit(1)

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
print(f"Apenas o tempo de execução varia e teve sua média calculada.")

# Gráfico 1: Tempo médio de execução
plt.figure(figsize=(12, 6))
plt.plot(dados_media['N'], dados_media['Tempo de execucao'], 'b-o', linewidth=2, markersize=8)
plt.xlabel('N', fontsize=12)
plt.ylabel('Tempo Médio de Execução (segundos)', fontsize=12)
plt.title('Tempo Médio de Execução vs Tamanho de Entrada', fontsize=14, fontweight='bold')
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
    plt.title('Tempo Médio de Execução vs Tamanho de Entrada', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.7)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('tempo_medio.png', dpi=300, bbox_inches='tight')
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
    plt.savefig('contador.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Gráficos salvos como 'tempo_medio.png' e 'contador.png'")

# Salvar dados médios em CSV
salvar_csv = input("Deseja salvar os dados médios em CSV? (s/n): ").lower()
if salvar_csv == 's':
    dados_media.to_csv('resultados_media.csv', index=False)
    print("✓ Dados médios salvos em 'resultados_media.csv'")

print("\nAnálise concluída!")