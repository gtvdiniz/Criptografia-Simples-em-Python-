class Criptografia:
    def criptografiaa(self):
        mensagem = input("Escreva aqui uma mensagem:\n")

        #Passo 1
        novamsg = "".join(reversed(mensagem))
        print(f'\nMensagem recebida: {mensagem}\nMensagem invertida: {novamsg}')

        #Passo 2
        numeros = "1234567890"
        letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
        letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Cria as versões "deslocadas" das strings
        letrasmini_cifrados = letras_minusculas[2:] + letras_minusculas[:2]
        numeros_cifrados = numeros[2:] + numeros[:2]
        letrasmega_cifrados = letras_maiusculas[2:] + letras_maiusculas[:2]

        # Cria a tabela de tradução usando str.maketrans
        tabela_ciframento = str.maketrans(letras_minusculas + numeros + letras_maiusculas,
                                          letrasmini_cifrados + numeros_cifrados + letrasmega_cifrados)

        # Aplica a tabela de tradução à mensagem invertida
        mensagem_cifrada = novamsg.translate(tabela_ciframento)
        print(f'Mensagem cifrada por deslocamento: {mensagem_cifrada}')

        #Passo 3
        cifragem_aleatoria = {
            "A": "X", "B": "M", "C": "Q", "D": "J", "E": "O", "F": "Z", "G": "P", "H": "T", "I": "L",
            "J": "Y", "K": "S", "L": "N", "M": "B", "N": "C", "O": "D", "P": "R", "Q": "V", "R": "F",
            "S": "K", "T": "E", "U": "G", "V": "W", "W": "A", "X": "U", "Y": "H", "Z": "I",


            "a": "x", "b": "m", "c": "q", "d": "j", "e": "o", "f": "z", "g": "p", "h": "t", "i": "l",
            "j": "y", "k": "s", "l": "n", "m": "b", "n": "c", "o": "d", "p": "r", "q": "v", "r": "f",
            "s": "k", "t": "e", "u": "g", "v": "w", "w": "a", "x": "u", "y": "h", "z": "i"
        }

        # Cria uma nova tabela de tradução a partir do dicionário
        ultima_mensagem = mensagem_cifrada.translate(str.maketrans(cifragem_aleatoria))

        print(f'Mensagem cifrada por substituição: {ultima_mensagem}')



crip = Criptografia()
crip.criptografiaa()
