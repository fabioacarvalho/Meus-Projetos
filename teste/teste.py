import flet
from flet import FilePicker, ElevatedButton, Row

def main(page):
    file_picker = FilePicker()
    page.overlay.append(file_picker)
    page.update()

    page.add(ElevatedButton("Choose files...",
    on_click=lambda _: file_picker.pick_files(allow_multiple=True))
    )

flet.app(target=main)