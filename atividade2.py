import flet as ft


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
class Contador(ft.Column):  
    def __init__(self, valor):
        super().__init__()  

        self.valor = 0  
        self.texto = ft.Text(valor)  
        
        self.btn_mais = ft.IconButton(ft.Icons.ADD, on_click=self.incrementar)  
        self.btn_menos = ft.IconButton(icon=ft.Icons.REMOVE, on_click=self.decrementar)  

        self.controls = [      
        self.texto,
        self.btn_mais,
        self.btn_menos
    ]

    def incrementar(self, e):  
        self.valor += 1  
        self.texto.value = self.valor
        self.update()  

    def decrementar(self, e):
        if self.valor > 0: 
            self.valor -= 1  
            self.texto.value = self.valor  
            self.update()
            
        
  

 
# Função principal da aplicação
def main(page: ft.Page):
      
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

    # Botão para excluir tarefas selecionadas
    btn_remover_tarefa = ft.ElevatedButton('Excluir',color=ft.colors.PURPLE_500 ,on_click=remover_tarefa)
    # Botão para adicionar uma nova tarefa
    btn_add_tarefa = ft.ElevatedButton('Adicionar',color=ft.colors.PURPLE_500, on_click=add_tarefa)

    
    
    
    page.title = 'app'
    page.window.resizable = False
    page.window.width = 500  # Largura
    page.window.height = 500  # Altura
    page.window.center()

    # Adicionando os controles na página (arranjo dos elementos)
    page.add(
        ft.Column([  # Usando uma coluna para organizar os controles verticalmente
            ft.Row([nova_tarefa_field, btn_add_tarefa]),  # Colocando o campo de nova tarefa e o botão de adicionar lado a lado (em uma linha)
            ft.Row([btn_remover_tarefa, btn_tema]), # Botão de remover tarefas selecionadas
            lista_tarefas  # Coluna onde as tarefas serão exibidas
            
        ])
    )
    contador = Contador(valor=0)
    page.add(ft.Row([contador, ft.Text(value='Contador', size=30, color=ft.colors.BLUE_300)]))
    page.update()


    

# Inicializa a aplicação Flet
ft.app(main)
