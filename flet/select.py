from typing import Text
import flet
from flet import FilePicker, FilePickerResultEvent, ElevatedButton, FilePickerUploadFile, TextField, Row

def main(page):

    contatos = TextField(label="Selecione a Planilha de Contatos ", disabled=True, width=800)
    imagem = TextField(label="Selecione a Imagem ", disabled=True, width=800)


    def path_plan():
        file_picker = FilePicker()
        page.overlay.append(file_picker)
        page.update()
        file_picker.pick_files(allow_multiple=True)
        file_picker.get_directory_path()

    def path_img():

        file_picker_img = FilePicker()
        page.overlay.append(file_picker_img)
        page.update()
        file_picker_img.pick_files(allow_multiple=True)
        
    

    page.add(
        Row([
            contatos, 
            ElevatedButton("Procurar Planilha", on_click=path_plan )
        ], alignment="center"),
        Row([
            imagem,
            ElevatedButton("Procurar Imagem", on_click=path_img),
            
        ], alignment="center"),
        Row([

        ]),
        Row([

        ]),
        Row([

        ]),
        
    )
        
flet.app(target=main)