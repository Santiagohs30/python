from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
import webbrowser

class StyledCheckBox(CheckBox):
    pass

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Fondo de la aplicación
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        label = Label(text='Haz clic en el checkbox para abrir la página de Kivy:', font_size=24, color=(1, 1, 1, 1))
        checkbox = StyledCheckBox(active=False, color=(0.2, 0.6, 1, 1))
        checkbox.bind(active=self.on_checkbox_active)
        button = Button(text='Abrir Página de Kivy', background_normal='', background_color=(0.2, 0.6, 1, 1), on_press=self.open_kivy_page)

        layout.add_widget(label)
        layout.add_widget(checkbox)
        layout.add_widget(button)
        return layout

    def on_checkbox_active(self, instance, value):
        if value:
            print("Checkbox activado")
        else:
            print("Checkbox desactivado")

    def open_kivy_page(self, instance):
        checkbox = self.root.children[1]  # El checkbox es el segundo widget en el layout
        if checkbox.active:
            try:
                webbrowser.open('https://kivy.org')
            except Exception as e:
                print(f'Error al abrir la página de Kivy: {e}')
        else:
            print("Por favor, selecciona el checkbox para abrir la página de Kivy.")

if __name__ == '__main__':
    MyApp().run()
