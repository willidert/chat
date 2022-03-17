if __name__ == "__main__":
    with open('roteiro.txt', 'r') as file:
        roteiro = [frase.strip().lower() for frase in file.readlines()]
        a = input().lower()
        while a != 'sair':
            try:
                pos = roteiro.index(a)
                print(f'bot: {roteiro[pos+1]}')
            except Exception:
                print('Segue o roteiro P#$%@...')
            a = input().lower()
