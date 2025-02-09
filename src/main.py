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
                ft.FloatingActionButton(
                    icon=ft.Icons.ADD,
                    on_click=self.add_task,
                    tooltip="Add a task!"
                ), # The add button right by side of the textbar
            ],
            expand=True,
        )
        self.controls=[ # there is no need to create a general view cause the app's class already is a Column view/display
            self.title,
            self.insert_widget,
            self.tasks_view,
        ]
    
    def add_task(self, e):
        task = Task(self.new_task.value, self.delete_task)
        self.tasks_view.controls.append(task)
        self.new_task.value = "" # Cleaning the value
        self.new_task.hint_text = "More!" # making a hint
        self.update()
        
    def delete_task(self, task):
        self.tasks_view.controls.remove(task)
        self.update()
        

class Task(ft.Column):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete # The Apps func to delete a task :)
        self.task_header = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=True, hint_text="New Task's Name")
        
        self.header_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.task_header,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_ROUNDED,
                            tooltip="Edit Task",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_ROUNDED,
                            tooltip="Delete Task",
                            on_click=self.delete_clicked,
                        ),
                    ]
                )
            ]
        )
        
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_ROUNDED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update Task",
                    on_click=self.save_clicked,
                )
            ],
        )
        
        self.controls = [self.header_view, self.edit_view]
        
    def delete_clicked(self, e): # When clicked calls the func of the app
        self.task_delete(self)
    
    def edit_clicked(self, e):
        self.edit_name.value = self.task_header.label
        self.header_view.visible = False
        self.edit_view.visible = True
        self.update()
    
    def save_clicked(self, e):
        self.task_header.label = self.edit_name.value
        self.header_view.visible = True
        self.edit_view.visible = False
        self.update()
        
def main(page: ft.Page):
    to_do_app = ToDozApp() # The instance
    page.title = to_do_app.name
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    
    page.add(to_do_app)
    
ft.app(main)