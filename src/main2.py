import flet as ft


class ToDozApp(ft.Column): # ihnerance
    # The app is a big column with controls inside
    def __init__(self):
        super().__init__()
        self.name = "To-Doz App"
        self.title = ft.Text("Make Your Day!", size=30, weight="bold")
        self.width = 900
        self.new_task = ft.TextField(hint_text="What's need to be done?", expand=True) # Creation of tasks
        self.tasks_view = ft.Column() # List of new tasks
        self.insert_widget = ft.Row( # The 'input line' 
            controls=[
                self.new_task,
                ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_task), # The add button right by side of the textbar
            ],
            expand=True,
        )
        self.controls=[
            self.title,
            self.insert_widget,
            self.tasks_view,
        ]
    
    def add_task(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value)) # Adding to the task view column a new checkbox obj
        self.new_task.value = "" # Cleaning the value
        self.new_task.hint_text = "More!" # making a hint
        self.update()
        
def main(page: ft.Page):
    to_do_app = ToDozApp() # The instance
    page.title = to_do_app.name
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
    page.add(to_do_app)
    
ft.app(main)