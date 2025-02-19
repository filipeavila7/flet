import flet as ft 

def main(page: ft.Page):

    # Classe de texto em uma variável t
    t = ft.Text(  
        value='Olá Mundo',  # Texto
        size=50,  # Tamanho da fonte
        color=ft.Colors.PURPLE_800,  # Cor da fonte    
        italic=True,  # Itálico
        weight=ft.FontWeight.BOLD,  # Negrito
       # bgcolor=ft.Colors.BLACK87,  # Cor de fundo do texto
        font_family='Poppins',  # Fonte
    )

    # Elementos de texto simples
    elementos = [
        ft.Text(
            value='SHIPIN',
            size=50,
        ),


        ft.Text(
            value='dark souls',
            size=20,
            bgcolor= ft.Colors.AMBER_100,
            color= ft.Colors.RED_300 ),

        ft.Text(
            value='dark souls 3',
            size=20,
            bgcolor= ft.Colors.AMBER_100,
            color= ft.Colors.RED_300 ),


         ft.Text(
            value='bloodborn',
            size=20,
            bgcolor= ft.Colors.AMBER_100,
            color= ft.Colors.RED_300 ),


        ft.Text(
            value='elden ring',
            size=20,
            bgcolor= ft.Colors.AMBER_100,
            color= ft.Colors.RED_300 ),
    ]
         
        

    # Função para alterar o tema
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

        page.update()  # Atualiza a página

    # Botão para mudar o tema
    btn_tema = ft.IconButton(    
        icon=ft.icons.WB_SUNNY_OUTLINED,  # Ícone
        tooltip='Alterar o tema',  # Aparece quando passar o mouse
        on_click=alterar_tema  # Ação de clique
    )

    # Configurações da página
    page.title = 'Configuração da Página'  # Título da página
    page.bgcolor = ft.Colors.AMBER_200  # Cor de fundo da página
    page.theme_mode = ft.ThemeMode.LIGHT  # Tema claro por padrão
    page.window.width = 500  # Largura
    page.window.height = 500  # Altura
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
    # page.padding = ft.padding.all(50) # fazer as margens de todos os lados
    # page.padding = ft.padding.only(top=10, right= 50, left=50, bottom=10) # definir o tamanho das margens de cada lado
    page.spacing = 200 #espaçamento
    page.window.always_on_top = False # ficar sempre em primeiro plano ou nao
    page.window.title_bar_hidden = False # esconder os botao de fechar e minimizar de cima
    page.window.frameless = False
    page.window.full_screen = False # tela cheia
    page.window.max_width= 500   #tamanho maximo
    page.window.min_width = 500   # tamanho minimo
    page.window.max_height = 500   
    page.window.min_height = 500
    
    page.window.resizable = True
    page.window.movable = True



    def janela_evento (e):     #mostrar as acoes do usuario
        match e.data:
            case 'moved':
                print('moveu a pagina')
            case 'resized':
                print('redimencionou a pagina')
            case 'minimize':
                print('minimizou a pagina')
            case _:
                print('outra ação')

    page.window.on_event = janela_evento
        




    # Adicionando os elementos à página
    page.add(*elementos,t, btn_tema)
    #inserir rapidamente
    page.add(ft.Text(value='patock', size=35))

    # Atualizando a página
    page.update() 

# Executando o app
ft.app(main)
