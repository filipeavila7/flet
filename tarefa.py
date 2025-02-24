import flet as ft
import config

# Classe Tarefa: responsável por exibir uma tarefa com seu texto e a possibilidade de editar
class Tarefa(ft.Row):
    def __init__(self, texto):
        super().__init__()  # Chama o construtor da classe pai (ft.Row), que é responsável por organizar os elementos na linha
        self.checkbox = ft.Checkbox()  # Cria um checkbox para marcar a tarefa
        self.texto_view = ft.Text(texto)  # Exibe o texto da tarefa
        self.editar_texto = ft.TextField(texto, visible=False)  # Cria um campo de texto para edição (inicialmente invisível)
        self.btn_editar = ft.IconButton(icon=ft.icons.EDIT, on_click=self.editar)  # Cria um botão de edição
        self.btn_salvar = ft.IconButton(visible=False, icon=ft.icons.SAVE, on_click=self.salvar)  # Cria um botão de salvar (inicialmente invisível)

        # Define quais controles (elementos) serão mostrados na linha
        self.controls = [
            self.checkbox,          # Checkbox para marcar a tarefa
            self.editar_texto,      # Campo de edição (visível quando a tarefa é editada)
            self.texto_view,        # Texto da tarefa (visível inicialmente)
            self.btn_editar,        # Botão de editar
            self.btn_salvar         # Botão de salvar
        ]
    
    # Função chamada ao clicar no botão de editar
    def editar(self, e):
        # Esconde o botão de editar e mostra o botão de salvar
        self.btn_editar.visible = False
        self.btn_salvar.visible = True
        # Esconde o texto atual da tarefa e mostra o campo de edição
        self.texto_view.visible = False
        self.editar_texto.visible = True
        self.update()  # Atualiza a interface com as mudanças

    # Função chamada ao clicar no botão de salvar
    def salvar(self, e):
        # Esconde o botão de salvar e mostra o botão de editar novamente
        self.btn_editar.visible = True
        self.btn_salvar.visible = False
        # Exibe o texto atualizado da tarefa e esconde o campo de edição
        self.texto_view.visible = True
        self.editar_texto.visible = False
        # Atualiza o texto da tarefa com o novo valor digitado no campo de edição
        self.texto_view.value = self.editar_texto.value
        self.update()  # Atualiza a interface com as mudanças

# Função principal da aplicação
def main(page: ft.Page):
    config.chamar(page)  # Função de configuração que você importou (provavelmente para configurar a aparência ou outras definições)
    page.theme_mode = ft.ThemeMode.LIGHT  # Define o modo de tema da página como claro (LIGHT)

    tarefas = []  # Lista para armazenar todas as tarefas

    # Campo de entrada para digitar a nova tarefa
    nova_tarefa_field = ft.TextField(label='Nova Tarefa')
    # Coluna onde as tarefas serão exibidas
    lista_tarefas = ft.Column()

    # Função para adicionar uma nova tarefa
    def add_tarefa(e):
        # Verifica se o campo de texto não está vazio (ignorando espaços)
        if nova_tarefa_field.value.strip():
            # Cria uma nova tarefa com o texto digitado
            nova_tarefa = Tarefa(texto=nova_tarefa_field.value)
            # Adiciona a nova tarefa à lista de tarefas
            tarefas.append(nova_tarefa)
            # Adiciona a nova tarefa ao controle lista_tarefas (a coluna que as exibe)
            lista_tarefas.controls.append(nova_tarefa)
            # Limpa o campo de texto após adicionar a tarefa
            nova_tarefa_field.value = ''
            page.update()  # Atualiza a interface com a nova tarefa

    # Função para remover tarefas que têm o checkbox marcado
    def remover_tarefa(e):
        # Itera sobre as tarefas (copiando a lista para evitar problemas durante a remoção)
        for tarefa in tarefas[:]:
            # Verifica se o checkbox da tarefa está marcado
            if tarefa.checkbox.value:
                # Remove a tarefa da lista de controles da página
                lista_tarefas.controls.remove(tarefa)
                # Remove a tarefa da lista interna de tarefas
                tarefas.remove(tarefa)
        page.update()  # Atualiza a interface após a remoção

    # Botão para excluir tarefas selecionadas
    btn_remover_tarefa = ft.ElevatedButton('Excluir', on_click=remover_tarefa)
    # Botão para adicionar uma nova tarefa
    btn_add_tarefa = ft.ElevatedButton('Adicionar', on_click=add_tarefa)

    # Adicionando os controles na página (arranjo dos elementos)
    page.add(
        ft.Column([  # Usando uma coluna para organizar os controles verticalmente
            ft.Row([nova_tarefa_field, btn_add_tarefa]),  # Colocando o campo de nova tarefa e o botão de adicionar lado a lado (em uma linha)
            btn_remover_tarefa,  # Botão de remover tarefas selecionadas
            lista_tarefas  # Coluna onde as tarefas serão exibidas
        ])
    )

# Inicializa a aplicação Flet
ft.app(main)
