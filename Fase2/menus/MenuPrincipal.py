from menu import Menu

from base_conhecimento.baseConhecimento import entregas, encomendas


def menu_principal():
    optionss = [
                ("Mostrar encomendas", lambda: print(encomendas)),
                ("Mostrar entregas", lambda: print(entregas)),
                ("Voltar", Menu.CLOSE)
                ]
    menu = Menu(title="Green Distribution Management", options=optionss)  # customize the options

    menu.open()
    menu.set_prompt(">")


if __name__ == "__main__":
    menu_principal()
