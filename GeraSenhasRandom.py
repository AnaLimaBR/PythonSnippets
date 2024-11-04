import random
import string

def gerar_senha(tamanho=12):
    """
    Gera uma senha aleatória com o tamanho especificado.

    Parâmetros:
    tamanho (int): comprimento da senha. Padrão é 12 caracteres.

    Retorna:
    str: senha gerada aleatoriamente.

    Exemplo:
    senha = gerar_senha(16)
    print(senha)  # Saída pode ser algo como: 'aB1!@9Fd3*Ke7X'
    """
    # Definindo o conjunto de caracteres: letras maiúsculas, minúsculas, números e caracteres especiais.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Cria a senha misturando aleatoriamente os caracteres até o tamanho especificado.
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
if __name__ == "__main__":
    print("Sua nova senha é:", gerar_senha(16))
