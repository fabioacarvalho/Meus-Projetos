import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors, TextField, Column, Row, FilePicker, FilePickerResultEvent, FilePickerUploadFile


def main(page: Page):
    page.title = "Routes Example"
    titulo = Text(
        value="Automação de Mensagens", size=40, color="white", bgcolor="blue", weight="bold", italic=True, text_align="center",
    )

    # --------- VARIAVEIS -------------#

    login = TextField(label="Login", keyboard_type="email", autofocus=True, border_radius=10, width=500)
    senha = TextField(label="Senha", password=True, border_radius=10, width=500 )
    infos = Column()

    dados = []

    mensagem = TextField(label="Escreva sua mensagem:", width=800)
    btn_send = ElevatedButton("Enviar", bgcolor="green")
    btn_cancel = ElevatedButton("Cancelar", bgcolor="red")

    contatos = TextField(label="Selecione a Planilha de Contatos ", disabled=True, width=800)
    imagem = TextField(label="Selecione a Imagem ", disabled=True, width=800)

    # --------- FUNÇÕES -------------#

    def path_plan():
        file_picker = FilePicker()
        page.overlay.append(file_picker)
        page.update()
        file_picker.pick_files(allow_multiple=True)

    def path_img():

        file_picker_img = FilePicker()
        page.overlay.append(file_picker_img)
        page.update()
        file_picker_img.pick_files(allow_multiple=True)

    def btn_click(e):
        
        dados.insert(0, login.value)
        dados.insert(1, senha.value)

        if dados[0] == 'fabio' and dados[1] == '123':
            #infos.controls.append(Text(f"Login: {dados[0]} Senha: {dados[1]}!"))
            login.value = ""
            senha.value = ""
            page.update()
            page.go("/robo")
            
        else:
            infos.controls.append(Text(f"Dados inseridos estão errados!"))
            page.update()
            login.focus()
     
        
    # --------- NAVEGAÇÃO ENTRE PAGINAS -------------#

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    Row([
                        login,
                    ], alignment="center"),
                    Row([
                        senha,
                    ], alignment="center"),
                    Row([
                        infos,
                    ], alignment="center"),
                
                    AppBar(title=Text("Login"), bgcolor=colors.SURFACE_VARIANT),
                    Row([
                        ElevatedButton("Entrar", on_click=btn_click, bgcolor="green"),
                    ], alignment="center"),
                    
                ],
            )
        )
        if page.route == "/robo":
            page.views.append(
                View(
                    "/robo",
                    [
                        AppBar(title=Text("sair"), bgcolor=colors.SURFACE_VARIANT),
                        Row(
                            [
                                titulo
                            ],
                            alignment="center",
                        ),
                        Row([
                            contatos, 
                            ElevatedButton("Procurar Planilha", on_click=path_plan )
                        ], alignment="center"),
                        Row([
                            imagem,
                            ElevatedButton("Procurar Imagem", on_click=path_img),
                            
                        ], alignment="center"),
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
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # --------- RENDERIZAÇÃO PAGINA -------------#

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main)