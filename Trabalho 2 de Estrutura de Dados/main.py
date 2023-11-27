# Função para ler nomes de um arquivo e inseri-los na tabela de hash
from TableHash import TabelaHash


def ler_nomes_e_inserir(tabela, arquivo):
    with open(arquivo, 'r') as file:
        nomes = file.read().splitlines()

    for nome in nomes:
        tabela.inserir(nome)


# Exemplo de uso
tamanho_tabela = 11
tabela_hash = TabelaHash(tamanho_tabela)

ler_nomes_e_inserir(tabela_hash, 'nomes.txt')

tabela_hash.imprimir_tabela()

print("=====================================================================")
# Testar as funções
print(tabela_hash.buscar('Joao'))  # Verificar se 'Joao' está na tabela
tabela_hash.deletar('Diana')  # Deletar 'Diana' da tabela

# Imprimir a tabela de hash para visualização
tabela_hash.imprimir_tabela()