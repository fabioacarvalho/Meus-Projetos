import flet
from flet import Column, ElevatedButton, Text, TextField


def main(page):

    login = TextField(label="Login", keyboard_type="email", autofocus=True, border_radius=10)
    senha = TextField(label="Senha", password=True, border_radius=10 )
    
    infos = Column()

    dados = []

    def btn_click(e):
        dados.insert(0, login.value)
        dados.insert(1, senha.value)
        infos.controls.append(Text(f"Login: {dados[0]} Senha: {dados[1]}!"))
        login.value = ""
        senha.value = ""
        page.update()
        login.focus()

    page.add(
        login,
        senha,
        ElevatedButton("Entrar", on_click=btn_click),
        infos,
    )

flet.app(target=main)