import flet as ft

def main(page: ft.Page):
    page.title = "My First App"
    page.add(
        ft.Text(value="Hello, World!"),
    )

ft.app(main)