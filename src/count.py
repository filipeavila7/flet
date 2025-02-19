import flet as ft

def main(page: ft.Page):
    page.title = 'primeiro app flet'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    num1 = ft.TextField(value=0, text_align=ft.TextAlign.RIGHT)

    def menos(e):
        num1.value = str(int(num1.value) - 1)
        page.update


    def mais(e):  # e de evento
        num1.value = str(int(num1.value) + 1)
        page.update
    
    btn_mais = ft.IconButton(ft.icons.ADD, on_click=mais)
    btn_menos = ft.IconButton(ft.icons.REMOVE, on_click=menos)



    def alterar_tema(e):  
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED
            btn_tema.tooltip = 'Alterar o tema para escuro'  # Correção aqui
            page.bgcolor = ft.Colors.WHITE
           # t.bgcolor = ft.Colors.BLACK
           # t.color = ft.Colors.WHITE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED
            btn_tema.tooltip = 'Alterar para tema claro'  # Correção aqui
            page.bgcolor = ft.Colors.BLACK
           # t.bgcolor = ft.Colors.WHITE
           # t.color = ft.Colors.BLACK

        page.update()


    btn_tema = ft.IconButton(    
    icon=ft.icons.WB_SUNNY_OUTLINED,  # Ícone
    tooltip='Alterar o tema',  # Aparece quando passar o mouse
    on_click=alterar_tema)  # Ação de clique
    
    
    page.add(

        ft.Row(
            [
              ft.IconButton(ft.icons.REMOVE, on_click= menos),
              num1,
              ft.IconButton(ft.icons.ADD, on_click=mais),
              


            ]
        )
    )        


ft.app(main)