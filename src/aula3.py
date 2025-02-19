import config
import flet as ft


def main(page = ft.Page):

    page.title = 'aula 3'

    config.chamar(page)
    
    def adicionar (e): # 'e' de evento 
        
        if not nova_tarefa.value:
            nova_tarefa.error_text = 'digite algo para adcionar'  
            page.update() 
            
        else:
            nova_tarefa.error_text = None

            tarefa = ft.Row(

                [
                    ft.Checkbox(label=nova_tarefa.value), # criando uma checkbox q dentro tem uma label com a variavel nova_tarefa
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINED,
                        tooltip='remover tarefa',
                        on_click= lambda e, tarefa=tarefa: remover_tarefa(tarefa)
                    )
                ]
            )
            ft.add(tarefa) 
            nova_tarefa.value = '' # deixar vazio qnd clicar
            nova_tarefa.focus() #dar um foco na label
            nova_tarefa.update() # atualizar

    nova_tarefa = ft.TextField(label='O que voce deseja adicionar fi?', width=300) # hint aparece o textpo na caixinha q sera fuardado na variavel nova_tarefa e label aparece em cima
    
    
    def remover_tarefa(tarefa):
        page.controls.remove(tarefa)
        page.update()

        




    page.add(ft.Row(   # criar uma linha
        [
            nova_tarefa, 
            ft.ElevatedButton('adcionar', on_click=adicionar, bgcolor=ft.colors.YELLOW_500, color=ft.colors.BLACK87) # definindo um botao e sua açao q sera da funcao adcionar(e)
        ]
    ))

    def saudacao(e):  # funcao de saudacao com evento
        if not txt_nome.value:  # caso a label do nome n tenha valor ele tera uma msgt de erro
            txt_nome.error_text = 'por favor, digite seu nome mano'
            page.update()
        else:
            nome = txt_nome.value  # caso tenha valor ele salvara em uma varuiavel chamada nome
            page.clean()
            page.add(ft.Text(f'ola {nome}')) # e exibira uma msg com a variavel
            

   
        


    

    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    

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



    txt_nome = ft.TextField(label='seu nome?')  #label de add seu nome
    page.add(ft.Row(  #numa linha so
        [
            txt_nome, 
            ft.ElevatedButton('diga olá', on_click=saudacao), # botao vai chamar a funcao saudacao
            btn_tema 
        ]
    ))



    def clicar(e):
        ...



    saida_texto = ft.Text()
    btn_submit = ft.ElevatedButton(text='enviar', on_click=clicar, bgcolor= ft.colors.PURPLE_400, color=ft.colors.BLACK87 ) # disabled=True), desabilita o botao
    cor_dropdown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option('deca'),
            ft.dropdown.Option('dura'),
            ft.dropdown.Option('gh'),
            ft.dropdown.Option('trembolona'),
            ft.dropdown.Option('creatina'),
            ft.dropdown.Option('testo')
        ]
    )

        
    page.add(saida_texto, btn_submit, cor_dropdown)


    

ft.app(main)




