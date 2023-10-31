from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Diseño principal utilizando BoxLayout vertical
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Etiqueta informativa
        label = Label(
            text='Ingresa tu texto:',
            font_size='18sp',
            color=(0.2, 0.6, 1, 1)  # Color del texto (formato RGBA)
        )
        
        # TextField personalizado con fondo
        textfield = TextInput(
            font_size='18sp',  # Tamaño de fuente del texto en el TextField
            multiline=False,  # Permite múltiples líneas (False para una sola línea)
            hint_text='Escribe aquí',  # Texto de pista que aparece antes de ingresar texto
            background_color=(0.9, 0.9, 0.9, 1),  # Color de fondo del TextField (formato RGBA)
            cursor_color=(0.2, 0.6, 1, 1),  # Color del cursor (formato RGBA)
            foreground_color=(0, 0, 0, 1)  # Color del texto dentro del TextField (formato RGBA)
        )
        
        # Agregar widgets al diseño principal
        layout.add_widget(label)
        layout.add_widget(textfield)
        return layout

if __name__ == '__main__':
    MyApp().run()
