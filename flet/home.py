from ctypes import alignment
from distutils.text_file import TextFile
from tkinter import Grid
import flet
from flet import Column, ElevatedButton, Text, TextField, Row, FilePicker, FilePickerResultEvent, FilePickerUploadFile
from flet.ref import Ref

def main(page):

    

    titulo = Text(
        value="Automação de Mensagens", size=40, color="white", bgcolor="blue", weight="bold", italic=True, text_align="center",
    )


    # --------- VARIAVEIS -------------#
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


    # --------- RENDERIZAÇÃO PAGINA -------------#
    page.add(
        
        Row(
            [
                titulo
            ],
            alignment="center",
        ),
        Column([
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
        ], alignment="center")
    )

flet.app(target=main)