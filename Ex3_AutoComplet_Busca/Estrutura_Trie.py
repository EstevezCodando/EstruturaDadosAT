class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False
class Trie:
    def __init__(self):
        self.raiz = NoTrie()
        self.palavras_inseridas = []

    def inserir_palavra(self, palavra: str):
        """
        Insere uma palavra na Trie.
        """
        no_atual = self.raiz
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoTrie()
            no_atual = no_atual.filhos[caractere]
        no_atual.fim_de_palavra = True
        
        # Se quisermos usar na correção aproximada
        self.palavras_inseridas.append(palavra)

    def buscar_no_prefixo(self, prefixo: str) -> NoTrie:
        """
        Percorre a Trie até o final do prefixo e retorna o nó correspondente.
        Se o prefixo não existir, retorna None.
        """
        no_atual = self.raiz
        for caractere in prefixo:
            if caractere not in no_atual.filhos:
                return None
            no_atual = no_atual.filhos[caractere]
        return no_atual

    def _coletar_palavras(self, no: NoTrie, prefixo: str, resultados: list):
        """
        Percorre recursivamente a Trie a partir de 'no', 
        coletando palavras que começam com 'prefixo' no array 'resultados'.
        """
        # Se este nó representa o final de uma palavra
        if no.fim_de_palavra:
            resultados.append(prefixo)

        # Para cada caractere filho, continuamos a busca
        for caractere, proximo_no in no.filhos.items():
            self._coletar_palavras(proximo_no, prefixo + caractere, resultados)

    def autocompletar(self, prefixo: str, limite_sugestoes: int = 5) -> list:
        """
        Retorna sugestões de palavras que iniciam com o 'prefixo'.
        O limite_sugestoes restringe quantas sugestões retornar (default=5).
        """
        no_prefixo = self.buscar_no_prefixo(prefixo)
        if not no_prefixo:
            return []
        
        resultados = []
        self._coletar_palavras(no_prefixo, prefixo, resultados)
        return resultados[:limite_sugestoes]  # Retorna somente até o limite

    def corrigir_palavra(self, palavra_digitada: str, limite_sugestoes: int = 5) -> list:
        """
        Retorna sugestões de palavras que tenham a menor distância de edição 
        (Levenshtein) em relação a 'palavra_digitada'.
        """
        # Opcional: Se o conjunto de palavras for muito grande, métodos mais eficientes seriam utilizados.
        distancias = []
        for palavra in self.palavras_inseridas:
            dist = distancia_levenshtein(palavra_digitada, palavra)
            distancias.append((palavra, dist))

        # Ordena pela distância (menor primeiro) e pega as primeiras
        distancias.sort(key=lambda x: x[1])
        
        # Se quiser só as que têm a menor distância absoluta, poderíamos filtrar, 
        # mas aqui pegaremos até 'limite_sugestoes'
        return [tupla[0] for tupla in distancias[:limite_sugestoes]]

def distancia_levenshtein(str1: str, str2: str) -> int:
    """
    Calcula a distância de Levenshtein entre 'str1' e 'str2'.
    Retorna o número mínimo de edições (inserção, remoção, substituição).
    """
    # Se uma das strings for vazia, a distância é o tamanho da outra
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    # Cria uma matriz (tabela) de distâncias
    # Tamanho: (len(str1)+1) x (len(str2)+1)
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializa primeira coluna e primeira linha
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Preenche a tabela
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            custo_substituicao = 0 if str1[i-1] == str2[j-1] else 1

            dp[i][j] = min(
                dp[i-1][j] + 1,           # Remoção
                dp[i][j-1] + 1,           # Inserção
                dp[i-1][j-1] + custo_substituicao  # Substituição (0 se iguais, 1 se diferente)
            )
    return dp[m][n]


def main():
    trie_livros = Trie()

    # Inserir alguns títulos ou palavras-chave
    lista_livros = [
        "harry potter",
        "haskell programming",
        "hunger games",
        "hamlet",
        "historias da mitologia",
        "python data science",
        "python para iniciantes",
        "programming in c",
        "projeto phoenix",
    ]

    for titulo in lista_livros:
        trie_livros.inserir_palavra(titulo)

    print("== AUTOCOMPLETAR ==")
    prefixo = "ha"
    sugestoes = trie_livros.autocompletar(prefixo, limite_sugestoes=3)
    print(f"Prefixo digitado: '{prefixo}' -> Sugestões: {sugestoes}")

    prefixo = "pyth"
    sugestoes = trie_livros.autocompletar(prefixo, limite_sugestoes=5)
    print(f"Prefixo digitado: '{prefixo}' -> Sugestões: {sugestoes}")

    print("\n== CORREÇÃO AUTOMÁTICA ==")
    palavra_incorreta = "haary potter"
    correcoes = trie_livros.corrigir_palavra(palavra_incorreta, limite_sugestoes=3)
    print(f"Palavra digitada incorretamente: '{palavra_incorreta}' -> Sugestões: {correcoes}")

    palavra_incorreta = "progrmming"
    correcoes = trie_livros.corrigir_palavra(palavra_incorreta, limite_sugestoes=5)
    print(f"Palavra digitada incorretamente: '{palavra_incorreta}' -> Sugestões: {correcoes}")

if __name__ == "__main__":
    main()
