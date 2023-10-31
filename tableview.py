from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Line

class TableView(GridLayout):
    def __init__(self, **kwargs):
        super(TableView, self).__init__(**kwargs)
        self.cols = 3  # Número de columnas en la tabla
        self.spacing = [5, 5]  # Espaciado entre celdas
        
        # Fondo de imagen para la tabla
        with self.canvas.before:
            self.background = Image(source='background.jpg', pos=self.pos, size=self.size, allow_stretch=True, keep_ratio=False)
            Color(1, 1, 1, 1)
            Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

        # Encabezados de la tabla
        self.add_widget(Label(text='Nombre', bold=True))
        self.add_widget(Label(text='Edad', bold=True))
        self.add_widget(Label(text='Ocupación', bold=True))
        
        # Datos de la tabla (puedes cargar estos datos desde una fuente de datos real)
        datos = [
            ('Santiago', '24', 'Ingeniero'),
            ('Miguel', '22', 'Desarrollador'),
            ('Erick', '35', 'Vago'),
            ('Robinson', '38', 'Profesor')
        ]
        
        # Agrega filas de datos a la tabla
        for nombre, edad, ocupacion in datos:
            self.add_widget(Label(text=nombre))
            self.add_widget(Label(text=edad))
            self.add_widget(Label(text=ocupacion))
            
            # Agrega líneas blancas para diferenciar las celdas
            with self.canvas:
                Color(1, 1, 1, 1)  # Color blanco
                Line(points=[self.x, self.y, self.x + self.width, self.y], width=2)  # Línea horizontal superior
                Line(points=[self.x, self.y, self.x, self.y + self.height], width=2)  # Línea vertical izquierda

class MyApp(App):
    def build(self):
        return TableView()

if __name__ == '__main__':
    MyApp().run()
