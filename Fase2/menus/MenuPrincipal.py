from random import randint

import psutil
from menu import Menu

from algoritmos_procura.a_estrela import a_estrela
from algoritmos_procura.bfs import bfs
from algoritmos_procura.dfs import dfs
from algoritmos_procura.dfs_lim import dfs_limited
from algoritmos_procura.dijkstra import dijkstra
from algoritmos_procura.gulosa import resolve_gulosa
from base_conhecimento.Encomenda import Encomenda
from base_conhecimento.baseConhecimento import mapa
from base_conhecimento.circuitos import *
from base_conhecimento.geraGrafo import gera_grafo
from base_conhecimento.gera_atribuicoes import gera_atribuicoes
from base_conhecimento.gera_encomenda import gera_encomendas
from gera_encomendas import gera_circuitos
from gera_encomendas.gera_circuitos import *

algoritmos = {
    "dfs": dfs,
    "dfs_lim": dfs_limited,
    "bfs": bfs,
    "gulosa": resolve_gulosa,
    "a_estrela": a_estrela,
    "dijkstra": dijkstra
}


def print_lista(lista):
    for item in lista:
        print(item)


def gerar_grafo():
    nome_grafo = input("Insira o nome da cidade: ")
    num_nodos = int(input("Insira o número de nodos: "))
    prob_conexao = int(input("Insira a probabilidade de conexão: "))
    gera_grafo(nome_grafo, num_nodos, prob_conexao)
    print("Cidade criada com sucesso!")
    print(f"Cidade guardada com o nome \"{nome_grafo}.png\"\n")


def mostrar_encomendas():
    print("Encomendas: ")
    print_lista(encomendas.values())


def mostrar_entregas():
    print("Entregas: ")
    print_lista(entregas)


def gerar_encomendas():
    print("Lista dos grafos já gerados: ")
    print_lista(mapa["grafos"].keys())
    nome_grafo = input("Insira o nome do grafo: ")
    if nome_grafo not in mapa["grafos"].keys():
        print("Nome do grafo ainda não gerado.")
        return
    num_encomendas = int(input("Insira o número de encomendas: "))
    gera_encomendas(num_encomendas, nome_grafo)
    gera_atribuicoes()
    print("Encomendas geradas com sucesso.")


def gerar_circuitoss():

    crit = input("Pretende usar o critério ecológico? (S)im/(N)ão ")
    import gera_encomendas.gera_veiculos
    gera_encomendas.gera_veiculos.criterio_ecologico = crit.upper() == "S"

    print(f"Algoritmos implementados: {algoritmos.keys()}")
    alg = input("Nome do algoritmo a ser usado: ")
    executar_algoritmo(alg)

    gera_encomendas.gera_veiculos.criterio_ecologico = False


def executar_algoritmo(nome_algoritmo):
    if not Encomenda.encomendas_por_entregar():
        print("Não há encomendas para entregar!")
        return

    inicio_tempo = time.time()
    inicio_memoria = psutil.Process().memory_info().rss

    gerar_circuitos(algoritmos.get(nome_algoritmo))

    print(f"Memoria de execução do algoritmo: {(psutil.Process().memory_info().rss - inicio_memoria) / 1024 ** 2}MB")

    print(f"Tempo de execução do algoritmo: {time.time() - inicio_tempo}s")

    print("Circuito gerado com sucesso!")


def ha_circuitos():
    return len(circuitos_efetuados) > 0


def formata_caminho(caminho):
    str = ""
    locais = caminho.split(';')
    for i in range(len(locais) - 2):
        str += f"{locais[i]}->"
    str += f"{locais[len(locais)-2]}"
    return str


def circuitoss_mais_produtivos():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("Circuitos Mais Produtivos: ")
    for circuito, produtividade in circuitos_mais_produtivos():
        print(f"Circuito: {formata_caminho(circuito)}")
        print(f"    Entregas/percurso: {str(produtividade)}")
    print("\n")


def circuito_mais_usado_counterr():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("O circuito mais usado quanto ao número de vezes que foi percorrido é:")
    circuito, percursos = circuito_mais_usado_counter()
    print(f"Circuito: {formata_caminho(circuito)}")
    print(f"    Percursos: {str(percursos)}")
    print("\n")


def circuito_mais_usado_pesoo():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("O circuito mais usado com base no peso total das entregas do percurso é:")
    circuito, peso = circuito_mais_usado_peso()
    print(f"Circuito: {formata_caminho(circuito)}")
    print(f"    Peso total: {str(peso)}Kg")

    print("\n")


def circuito_mais_usado_volumee():
    if not ha_circuitos():
        print("Ainda não foram gerados circuitos.")
        return
    print("O circuito mais usado com base no volume total das entregas do percurso: ")
    #print(circuito_mais_usado_volume())
    circuito, volume = circuito_mais_usado_volume()
    print(f"Circuito: {formata_caminho(circuito)}")
    print(f"    Volume total: {volume}")


def mudar_modo_teste():
    gera_circuitos.modo_teste = not gera_circuitos.modo_teste
    string = "ativado" if (gera_circuitos.modo_teste is True) else "desativado"
    print(f"Modo de teste {string}!")


def gerar_encomendas_automaticamente():
    num_encomendas = 15

    grafo_int = randint(0, len(mapa["grafos"]) - 1)
    grafo = list(mapa["grafos"].keys())[grafo_int]
    print("Grafo selecionado aleatoriamente!")

    gera_encomendas(num_encomendas, grafo)
    print(f"Geração de {num_encomendas} encomendas com sucesso!")

    gera_atribuicoes()
    print("Geração das atribuições das encomendas aos estafetas com sucesso!")

    print("Encomendas geradas com sucesso.")


def correr_todos():
    if not Encomenda.encomendas_por_entregar():
        gerar_encomendas_automaticamente()

    m_teste = gera_circuitos.modo_teste
    print("De modo a correr todos os algoritmos nas mesmas condições o modo teste será ativado, caso não esteja!")
    gera_circuitos.modo_teste = True

    for nome in algoritmos.keys():
        print(f"Inicia-se a procura com o algoritmo {nome}!")
        executar_algoritmo(nome)

    print("A repor o modo de teste...")
    gera_circuitos.modo_teste = m_teste


def menu_principal():
    logging.basicConfig(
        filename='output.log',
        filemode='w',
        format='[%(levelname)s] %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
    )
    options = [
        ("Mostrar todas as encomendas", mostrar_encomendas),
        ("Mostrar todas as entregas", mostrar_entregas),
        ("Gerar encomendas", gerar_encomendas),
        ("Entregar encomendas", gerar_circuitoss),
        ("Criar cidade de entrega", gerar_grafo),
        ("Mostrar circuitos mais produtivos", circuitoss_mais_produtivos),
        ("Mostrar circuito mais usado", circuito_mais_usado_counterr),
        ("Mostrar circuito com maior número de entregas por peso", circuito_mais_usado_pesoo),
        ("Mostrar circuito com maior número de entregas por volume", circuito_mais_usado_volumee),
        ("Ativar/desativar modo de teste", mudar_modo_teste),
        ("Realizar testes para todos os algoritmos", correr_todos),
        ("Sair", Menu.CLOSE)
    ]
    menu = Menu(title="\n****Green Distribution Management****", options=options)
    menu.open()
    menu.set_prompt(">")


if __name__ == "__main__":
    menu_principal()
