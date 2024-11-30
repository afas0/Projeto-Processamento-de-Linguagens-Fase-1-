# Parte 1 - Gerar automato gráficamente usando a biblioteca graphviz

import json
from graphviz import Digraph
import argparse


## Exemplo de argparser

def argumentos(args):
    
    automato : dict = {}
    nome_ficheiro = args.ficheiro
    #Ler ficheiro e criar automato
    with open(nome_ficheiro, "r", encoding="utf-8") as f:
        automato = json.load(f)
    if args.graphviz:      
        gerarGrafo(automato)
    elif args.rec :
        if args.palavra is None:
            print("Falta escrever a palavra pretendida quando -rec selecionado") 
        else:
            palavra = args.palavra
            testar(automato,palavra)     
    else:
        print("Usar opcao -h ou --help para ajuda nos argumentos.")

def gerarGrafo(automato):

    # Criar o diagrama de grafos do automato
    ponto = Digraph(comment='Automato')

    # 'none' para um node invisível
    ponto.node('start', shape='none', label='') 
    # criar transcição incial
    ponto.edge('start', automato["q0"], label='')

    # Criar os estados
    for estado in automato["delta"].keys():

        # caso o estado seja final
        if estado in automato["F"]:
            ponto.node(estado, estado, shape="doublecircle")

        else:
            ponto.node(estado, estado, shape="circle")

    # Criar as transições
    for estado_inicial, transicoes in automato["delta"].items():
        for simbolo, estado_final in transicoes.items():
            ponto.edge(estado_inicial, estado_final, label = simbolo)


            

    # Visualização
    ponto.render('automaton_graph', view=True, format='png')

    # Imprimir no terminal 
    print(ponto.source)

# Parte 2 - Gerar o código de funcionamento do automato
def verificacao(entrada : str, estado_inicial : str, transicoes : dict, estados_finais : list) -> bool:

    entrada : str = entrada.replace("ε", "")
    estado_atual : str = estado_inicial
    print(f"[caminho {estado_atual}", end="" )
    for simbolo in entrada:
        print(f"-{simbolo}>", end="")
        # caso haja uma transição
        if simbolo in transicoes[estado_atual]:
            estado_atual = transicoes[estado_atual][simbolo]
            print(f" {estado_atual}", end="" )
        else:
            # se não houver transição definida para este caracter de entrada, a palavra não é aceite
            print(f" Símbolo {simbolo} não pertence ao alfabeto ou está na ordem errada]")
            return False
            
    # Caso nao esteja no estado final
    if estado_atual not in estados_finais:
        print(f", {estado_atual} não é final]")
    else:
        print("]")
    return estado_atual in estados_finais

def testar(automato,palavra):   

    estado_inicial : str = automato["q0"]
    estados_finais : list = automato["F"]
    transicoes : dict = automato["delta"]
    resultado : bool = verificacao(palavra, estado_inicial, transicoes, estados_finais)
    
    if resultado:
        print(f"A palavra '{palavra}' é aceite pelo automato.")
    else:
        print(f"A palavra '{palavra}' não é aceite pelo automato.")

def main():
    # Argumentos de entrada para o programa
    parser = argparse.ArgumentParser(description='Algoritmo para testar AFD')
    parser.add_argument('ficheiro', type=str, help='Escolher ficheiro .json pretendido')
    parser.add_argument('-graphviz', action='store_true', help='Criação de grafo', required=False)
    parser.add_argument('-rec', action='store_true', help='Testar palavra', required=False)
    # nargs='?' Coloca em null a palavra caso nao seja escrita
    parser.add_argument('palavra', type=str, nargs='?', help='Palavra a verificar')
    args = parser.parse_args()
    
    argumentos(args)

if __name__ == "__main__":
    main()
