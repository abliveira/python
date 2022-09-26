"""
Referências:
    https://docs.python.org/3/library/argparse.html

Os argumentos da linha de comando são os valores transmitidos durante a chamada do programa
junto com a instrução de chamada. O Módulo Argparse ajuda a criar um programa em um ambiente
de linha de comando de uma forma que parece não apenas fácil de codificar, mas também melhora
a interação

Instalação
Como o argparse faz parte da biblioteca padrão do Python, ele já deve estar instalado.
No entanto, se não for, pode-se instalá-lo usando o seguinte comando:

pip install argparse

Execução
Para rodar este programa, deve se usar "python Argparse.py --port <algumacoisa>",
Sendo <algumacoisa> sendo completamente substituído por algum valor para entrada.

"""

# Import the library
import argparse
# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--name', type=str, required=True)
# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument
print('Hello,', args.name)