import flet as ft  

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
        
def main(page: ft.Page):  
    contador = Contador(valor=0)
    page.add(contador)
    page.update()

ft.app(main)  


'''
🔹 Requisitos do Aplicativo:
✅ Deve conter um TextField para entrada de texto.
✅ Deve ter um ElevatedButton que realiza alguma ação ao ser pressionado.
✅ Deve incluir pelo menos um IconButton para funcionalidade extra.
✅ Deve utilizar uma class para organizar o código.
✅ Deve incluir algum tipo de estilização (exemplo: cores, tamanhos, alinhamento).
'''