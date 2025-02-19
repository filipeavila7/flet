import config  # Importando o arquivo de configuração (config.py)
import flet as ft  # Importando a biblioteca flet para criar a interface gráfica

def main(page = ft.Page):  # Função principal que é chamada para renderizar a página

    page.title = 'aula 3'  # Definindo o título da página no navegador

    config.chamar(page)  # Chamando uma função do módulo 'config', provavelmente para configurar algo na página
    
    def adicionar (e):  # Função para adicionar uma nova tarefa
        if not nova_tarefa.value:  # Verificando se o campo de texto para adicionar tarefa está vazio
            nova_tarefa.error_text = 'digite algo para adcionar'  # Definindo um erro de validação
            page.update()  # Atualizando a página para mostrar a mensagem de erro
        else:
            nova_tarefa.error_text = None  # Se o campo não está vazio, removendo a mensagem de erro

            # Criando um container de linha (Row) para a tarefa
            tarefa = ft.Row([])

            # Criando um Checkbox com o texto da nova tarefa
            checkbox = ft.Checkbox(label=nova_tarefa.value)

            # Criando o botão de editar com ícone de "editar"
            btn_editar = ft.IconButton(
                icon=ft.icons.EDIT,  # Definindo o ícone de editar
                tooltip='editar tarefa',  # Tooltip que aparece quando o mouse passa por cima
                on_click= lambda e: editar_tarefa(tarefa,checkbox)  # Chamando a função de edição da tarefa
            )

            # Criando o botão de remover com ícone de "remover"
            botao_remover = ft.IconButton(
                icon=ft.icons.DELETE_OUTLINED,  # Ícone de remover
                tooltip="remover tarefa",  # Tooltip que aparece quando o mouse passa por cima
                on_click= lambda e: remover_tarefa(tarefa)  # Chamando a função para remover a tarefa
            )

            tarefa.controls.extend([checkbox, botao_remover, btn_editar])  # Adicionando os componentes à tarefa

            page.add(tarefa)  # Adicionando a tarefa à página
            nova_tarefa.value = ''  # Limpando o campo de entrada
            nova_tarefa.focus()  # Focando no campo para o usuário digitar uma nova tarefa
            nova_tarefa.update()  # Atualizando a página

    # Definindo o campo de texto para inserir nova tarefa
    nova_tarefa = ft.TextField(label='O que voce deseja adicionar fi?', width=300)
    
    def remover_tarefa(tarefa):  # Função para remover a tarefa
        page.controls.remove(tarefa)  # Removendo a tarefa da página
        page.update()  # Atualizando a página para refletir as mudanças

    def editar_tarefa(tarefa, checkbox):  # Função para editar a tarefa
        campo_edicao = ft.TextField(label=checkbox)  # Criando um campo de edição com o valor da tarefa atual

        def salvar_edicao(e):  # Função para salvar a edição (não implementada)
            ...

    # Criando o layout para adicionar novas tarefas
    page.add(ft.Row(  # Adicionando uma linha com o campo de texto e o botão
        [
            nova_tarefa,  # Campo de texto para adicionar tarefa
            ft.ElevatedButton('adcionar', on_click=adicionar, bgcolor=ft.colors.YELLOW_500, color=ft.colors.BLACK87)  # Botão para adicionar tarefa
        ]
    ))

    def saudacao(e):  # Função de saudação
        if not txt_nome.value:  # Verificando se o campo de nome está vazio
            txt_nome.error_text = 'por favor, digite seu nome mano'  # Adicionando erro de validação
            page.update()  # Atualizando a página
        else:
            nome = txt_nome.value  # Pegando o valor do campo de nome
            page.clean()  # Limpando a página
            page.add(ft.Text(f'ola {nome}'))  # Exibindo a saudação na página

    page.theme_mode = ft.ThemeMode.DARK  # Definindo o tema inicial como escuro
    page.update()  # Atualizando a página

    def alterar_tema(e):  # Função para alterar o tema
        if page.theme_mode == ft.ThemeMode.DARK:  # Se o tema atual for escuro
            page.theme_mode = ft.ThemeMode.LIGHT  # Altera para o tema claro
            btn_tema.icon = ft.icons.NIGHTS_STAY_OUTLINED  # Mudando o ícone do botão
            btn_tema.tooltip = 'Alterar o tema para escuro'  # Mudando o tooltip
            page.bgcolor = ft.Colors.WHITE  # Alterando a cor de fundo para branco
        else:
            page.theme_mode = ft.ThemeMode.DARK  # Alterando para o tema escuro
            btn_tema.icon = ft.icons.WB_SUNNY_OUTLINED  # Mudando o ícone do botão
            btn_tema.tooltip = 'Alterar para tema claro'  # Mudando o tooltip
            page.bgcolor = ft.Colors.BLACK  # Alterando a cor de fundo para preto

        page.update()  # Atualizando a página

    # Botão para alterar o tema da página
    btn_tema = ft.IconButton(    
        icon=ft.icons.WB_SUNNY_OUTLINED,  # Ícone do botão
        tooltip='Alterar o tema',  # Tooltip do botão
        on_click=alterar_tema  # Ação ao clicar no botão
    )

    # Definindo o campo de texto para inserir o nome
    txt_nome = ft.TextField(label='seu nome?')
    
    # Adicionando a linha com o campo de nome e botões
    page.add(ft.Row(
        [
            txt_nome,  # Campo de nome
            ft.ElevatedButton('diga olá', on_click=saudacao, bgcolor=ft.colors.YELLOW_400, color=ft.colors.BLACK87),  # Botão para enviar saudação
            btn_tema  # Botão de alterar tema
        ]
    ))

    def clicar(e):  # Função associada ao clique do botão de envio
        ...

    # Definindo o texto e o botão de envio
    saida_texto = ft.Text()
    btn_submit = ft.ElevatedButton(text='enviar', on_click=clicar, bgcolor= ft.colors.PURPLE_400, color=ft.colors.BLACK87 )
    
    # Dropdown com várias opções
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

    # Adicionando o texto, botão e dropdown à página
    page.add(saida_texto, btn_submit, cor_dropdown)

# Iniciando o app
ft.app(main)
