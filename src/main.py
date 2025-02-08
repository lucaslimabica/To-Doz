import flet as ft

def main(page: ft.Page):
    def add_button_clicked(e):
        page.add(
            ft.Checkbox(label=new_task.value)
        )
        new_task.value = ""
        page.update()
    
    page.title = "To-Doz" # Defining the app's UI
    page.add(
        ft.Text(value="Hello, World!"),
    )
        
    new_task = ft.TextField(hint_text="What's need to be done?") # The datafield to insert the tasks
    page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_button_clicked)) # Calling the 'page.add' for each new entry in 'new_task' field above

ft.app(main)