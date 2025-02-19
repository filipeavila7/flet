import flet as ft

def chamar(page: ft.Page):
    page.title = 'configuração'
    page.window.height = 500
    page.window.width = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.window.resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.center()



    

