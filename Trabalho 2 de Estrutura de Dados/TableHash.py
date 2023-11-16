class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [['L', None] for _ in range(tamanho)]

    def funcao_hash(self, nome):
        soma_ascii = sum(ord(char) for char in nome)
        return soma_ascii % self.tamanho

    def tentativa_quadratica(self, indice, tentativa):
        return (indice + tentativa ** 2) % self.tamanho

    def inserir(self, nome):
        indice = self.funcao_hash(nome)
        tentativa = 1

        while self.tabela[indice][0] == 'O':
            # Se a posição está ocupada, ajuste o índice usando a tentativa quadrática
            indice = self.tentativa_quadratica(indice, tentativa)
            tentativa += 1

        # Insira o elemento na posição encontrada
        self.tabela[indice] = ['O', nome]

    def buscar(self, chave):
        indice = hash(chave) % self.tamanho
        tentativa = 1

        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                return f"'{chave}' encontrado no índice {indice}"
            else:
                indice = (indice + tentativa) % self.tamanho
                tentativa += 1

            if tentativa > self.tamanho:
                return f"Tabela cheia. '{chave}' não encontrado na tabela."

        return f"'{chave}' não encontrado na tabela"

    def deletar(self, nome):
        indice = self.funcao_hash(nome)
        tentativa = 1

        while self.tabela[indice][0] != 'L':
            if self.tabela[indice][0] == 'O' and self.tabela[indice][1] == nome:
                # Se a posição está ocupada e a chave corresponde, marque como deletado
                self.tabela[indice] = ['R', None]
                return
            # Ajuste o índice usando a tentativa quadrática
            indice = self.tentativa_quadratica(indice, tentativa)
            tentativa += 1

    def imprimir_tabela(self):
        for i, (estado, elemento) in enumerate(self.tabela):
            print(f"{i}: Estado: {estado}, Elemento: {elemento}")