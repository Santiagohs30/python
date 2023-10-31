from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # Diseño principal utilizando BoxLayout vertical
        layout = BoxLayout(orientation='vertical')
        
        # Imagen de fondo ocupando la mitad de la pantalla verticalmente
        with layout.canvas.before:
            # Reemplaza 'background.jpg' con la ruta de tu imagen de fondo
            Rectangle(source='background.jpg', pos=layout.pos, size=(Window.width, Window.height / 2))

        # Imagen para ocupar la mitad de la interfaz verticalmente
        image = Image(source='image.jpg', allow_stretch=True, keep_ratio=False, size=(Window.width, Window.height / 2))
        layout.add_widget(image)
        
        # BoxLayout para contener el Label y crear un recuadro
        box = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Texto con marcado para el Label (puedes personalizar el estilo según tus preferencias)
        texto_personalizado = (
            "[color=000000][b][size=40]¡BIENVENIDOS A LA IA DE MSE![/size][/b][/color]\n\n"
           
        )
        
        # Label con texto personalizado y marcado
        label = Label(
            text=texto_personalizado,
            markup=True,  # Habilita el marcado de texto
            valign='middle',  # Alineación vertical del texto (middle para centrado vertical)
            halign='center',  # Alineación horizontal del texto (center para centrado horizontal)
            size_hint_y=None,  # Permite que el label se ajuste al tamaño del contenido en el eje Y
            height=300,  # Altura del label para acomodar el texto
            color=(0, 0, 0, 1)  # Color del texto: negro (formato RGBA)
        )
        
        # Agregar el Label al BoxLayout
        box.add_widget(label)
        
        # Agregar el BoxLayout al diseño principal
        layout.add_widget(box)
        return layout

if __name__ == '__main__':
    MyApp().run()
