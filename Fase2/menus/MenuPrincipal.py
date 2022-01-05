import time
from time import sleep

from menu import Menu

from algoritmos_procura.a_estrela import a_estrela
from algoritmos_procura.bfs import bfs
from algoritmos_procura.dfs import dfs
from algoritmos_procura.dfs_lim import dfs_limited
from algoritmos_procura.gulosa import resolve_gulosa
from base_conhecimento.circuitos import *
from base_conhecimento.geraGrafo import gera_grafo
from gera_encomendas.gera_circuitos import *
import psutil

logging.basicConfig(level=logging.DEBUG)


def print_lista(lista):
    for item in lista:
        print(item)


def gerar_grafo():
    nome_grafo = input("Meta o nome do grafo: ")
    num_nodos = int(input("Meta número de nodos: "))
    prob_conexao = int(input("Meta probabilidade de conexão: "))
    gera_grafo(nome_grafo, num_nodos, prob_conexao)
    print("Grafo gerado com sucesso!")
    print(f"Grafo guardado com o nome \"{nome_grafo}.png\"\n")
    sleep(2)


def mostrar_encomendas():
    print("Encomendas: ")
    print_lista(encomendas.values())


def mostrar_entregas():
    print("Entregas: ")
    print_lista(entregas)


def circuitoss_mais_produtivos():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("Circuitos Mais Produtivos: ")
    print_lista(circuitos_mais_produtivos())
    print("\n")


def circuito_mais_usado_counterr():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("O circuito mais usado quanto ao número de vezes que foi percorrido é:")
    print(circuito_mais_usado_counter())
    print("\n")


def circuito_mais_usado_pesoo():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("O circuito mais usado com base no peso total das entregas do percurso é:")
    print(circuito_mais_usado_peso())
    print("\n")


def circuito_mais_usado_volumee():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("O circuito mais usado com base no volume total das entregas do percurso: ")
    print(circuito_mais_usado_volume())


def menu_principal():
    options = [
        ("Mostrar encomendas", mostrar_encomendas),
        ("Mostrar entregas", mostrar_entregas),
        ("Gerar circuitos", gerar_circuitoss),
        ("Gerar grafo", gerar_grafo),
        ("Mostrar circuitos mais produtivos", circuitoss_mais_produtivos),
        ("Mostrar circuito mais usado", circuito_mais_usado_counterr),
        ("Mostrar circuito com maior número de entregas por peso", circuito_mais_usado_pesoo),
        ("Mostrar circuito com maior número de entregas por volume", circuito_mais_usado_volumee),
        ("Sair", Menu.CLOSE)
    ]
    menu = Menu(title="\n****Green Distribution Management****", options=options)  # customize the options
    menu.open()
    menu.set_prompt(">")


if __name__ == "__main__":
    menu_principal()
