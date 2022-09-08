from ctypes import alignment
from distutils.text_file import TextFile
from turtle import bgcolor
import flet
from flet import Column, ElevatedButton, Text, TextField, Row
from flet.ref import Ref

def main(page):

    titulo = Text(
        value="#JUNTOSCONTRAAPEDOFILIA", size=30, color="white", bgcolor="orange", weight="bold", italic=True, text_align="center",
    )

    mensagem = TextField(label="Escreva sua mensagem:")
    btn_send = ElevatedButton("Enviar", bgcolor="green")
    btn_cancel = ElevatedButton("Cancelar", bgcolor="red")

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

flet.app(target=main)