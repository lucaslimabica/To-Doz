import flet as ft

def main(page: ft.Page):
    def add_button_clicked(e):
        tasks_views.controls.append(ft.Checkbox(label=new_task.value)) # Add a checkbox with the name from the 'new task' field
        new_task.value = ""
        page.update()
    
    # SETTING THE APP'S CONTROLS 
    page.title = "To-Doz" # App's name
    title = ft.Text(value="Make Your Day!") # Tittle
    new_task = ft.TextField(hint_text="What's need to be done?", expand=True) # The datafield to insert the tasks
    insert_widget = ft.Row(
            controls=[
                new_task,
                ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_button_clicked), # The add button right by side of the textbar
            ],
            expand=True,
            spacing=10,
        )
    tasks_views = ft.Column() # List of tasks
    
    # SETTING THE MAIN VIEW
    view = ft.Column(
        width=900,
        controls=[
            title,
            insert_widget,
            tasks_views,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # INSERTING THE VIEW
    page.add(view)

ft.app(main)