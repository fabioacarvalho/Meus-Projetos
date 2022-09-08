import flet
from flet import ElevatedButton, Page, Text, TextField, Column, Row

def main(page: Page):

    login = TextField(label="Login", keyboard_type="email", autofocus=True, border_radius=10)
    senha = TextField(label="Senha", password=True, border_radius=10 )
    
    infos = Column()

    dados = []

    titulo = Text(
        value="#JUNTOSCONTRAAPEDOFILIA", size=30, color="white", bgcolor="orange", weight="bold", italic=True, text_align="center",
    )

    mensagem = TextField(label="Escreva sua mensagem:")
    btn_send = ElevatedButton("Enviar", bgcolor="green")
    btn_cancel = ElevatedButton("Cancelar", bgcolor="red")

    page.add(Text(f"Initial route: {page.route}"))

    def btn_click(e):
        dados.insert(0, login.value)
    dados.insert(1, senha.value)
    if dados[0] == 'fabio' and dados[1] == '123':
        infos.controls.append(Text(f"Login: {dados[0]} Senha: {dados[1]}!"))
        login.value = ""
        senha.value = ""
        page.update()
        login.focus()
    else:
        infos.controls.append(Text(f"Dados inseridos estão errados!"))
        page.update()
        login.focus()

    def tela_login(route):
        page.add(
            Row(
            [
                titulo
            ],
            alignment="center",
            ),
            Row(
                [
                    mensagem
                ],
                alignment="center",
            ),
            Row(
                [
                    btn_send,
                    btn_cancel
                ],
                alignment="center", spacing=30
            )
        )

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_tela_login = tela_login
    page.add(ElevatedButton("Go to Store", on_click=go_store))

flet.app(target=main)