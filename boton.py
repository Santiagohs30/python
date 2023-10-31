from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import webbrowser

class StyledButton(Button):
    pass

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Fondo de la aplicación
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        label = Label(text='Haz clic en el botón para abrir la documentación de Kivy!', font_size=24, color=(1, 1, 1, 1))
        label2 = Label(text='welcome to kivy by: miguel, santiago, erick', font_size=24, color=(1, 1, 1, 1))
        button = StyledButton(text='Documentación en Kivy', background_normal='button_normal.png', background_down='button_down.png', color=(0.2, 0.6, 1, 1))
        button.bind(on_press=self.open_kivy_docs)
        
        layout.add_widget(label)
        layout.add_widget(label2)
        layout.add_widget(button)
        return layout

    def open_kivy_docs(self, instance):
        try:
            webbrowser.open('https://kivy.org/doc/stable/')
        except Exception as e:
            print(f'Error al abrir la documentación de Kivy: {e}')

if __name__ == '__main__':
    MyApp().run()
