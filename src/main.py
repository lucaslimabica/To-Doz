import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0) # Setting the var 'data' to storage the counter's value

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()
        
    def decrease_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton( # Adding to the 'page obj' the sum button 
        icon=ft.Icons.ADD, on_click=increment_click
    )
    
    #page.floating_action_button_2 = ft.FloatingActionButton(
    #    icon=ft.Icons.AIRPLANEMODE_ON, on_click=decrease_click
    #)
    
    minus_button = ft.ElevatedButton(
        text="Minus",
        on_click=decrease_click,
        icon=ft.Icons.MINIMIZE
    )
    
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Container(
                        counter,
                        alignment=ft.alignment.center,
                    ),
                    minus_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            expand=True,
        )
    )


ft.app(main)
