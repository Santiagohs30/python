from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
import webbrowser

class StyledToggleButton(ToggleButton):
    pass

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        label = Label(text='Selecciona una opción:', font_size=24, color=(0.2, 0.6, 1, 1))
        
        kivy_button = StyledToggleButton(text='Kivy', group='option', background_color=(0.2, 0.6, 1, 1), size_hint=(None, None), size=(200, 75))
        kivy_logo = Image(source='kivy_logo.png', size_hint=(None, None), size=(200, 200))
        
        uq_logo_button = StyledToggleButton(text='UQ', group='option', background_color=(0.8, 0.2, 0.4, 1), size_hint=(None, None), size=(200, 75))
        uq_logo = Image(source='uq_logo.png', size_hint=(None, None), size=(200, 200))

        open_button = Button(text='Abrir Página Seleccionada', background_normal='', background_color=(0.2, 0.6, 1, 1), on_press=self.open_selected_page, size_hint=(None, None), size=(300, 75))

        layout.add_widget(label)
        layout.add_widget(kivy_button)
        layout.add_widget(kivy_logo)
        layout.add_widget(uq_logo_button)
        layout.add_widget(uq_logo)
        layout.add_widget(open_button)
        return layout

    def open_selected_page(self, instance):
        selected_button = [child for child in self.root.children if isinstance(child, StyledToggleButton) and child.state == 'down']
        
        if selected_button:
            selected_text = selected_button[0].text
            url = 'https://kivy.org' if selected_text == 'Kivy' else 'https://www.uniquindio.edu.co'
            try:
                webbrowser.open(url)
            except Exception as e:
                print(f'Error al abrir la página: {e}')
        else:
            print("Por favor, selecciona una opción antes de abrir la página.")

if __name__ == '__main__':
    MyApp().run()
