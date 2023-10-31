from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import webbrowser
import os

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.selected_language = 'Python'
        self.image_path = 'python_logo.jpg'  # Ruta relativa de la imagen (en el mismo directorio que el script)

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        label = Label(text='Selecciona un lenguaje de programación:', font_size=24, color=(0.2, 0.6, 1, 1))
        
        languages = ['Python', 'Java', 'JavaScript', 'Ruby']
        spinner = Spinner(values=languages, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5}, 
                          on_text=self.on_spinner_text)

        self.logo_image = Image(source=self.image_path, size_hint=(None, None), size=(200, 200))
        
        open_button = Button(text='Abrir Página', background_normal='', background_color=(0.2, 0.6, 1, 1), 
                             on_press=self.open_selected_page, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})

        layout.add_widget(label)
        layout.add_widget(spinner)
        layout.add_widget(self.logo_image)
        layout.add_widget(open_button)
        return layout

    def on_spinner_text(self, instance, text):
        self.selected_language = text
        if text == 'Python':
            self.image_path = 'python_logo.png'
        elif text == 'Java':
            self.image_path = 'java_logo.png'
        elif text == 'JavaScript':
            self.image_path = 'javascript_logo.png'
        elif text == 'Ruby':
            self.image_path = 'ruby_logo.png'
        self.logo_image.source = self.image_path

    def open_selected_page(self, instance):
        if self.selected_language == 'Python':
            url = 'https://www.python.org/'
        elif self.selected_language == 'Java':
            url = 'https://www.java.com/'
        elif self.selected_language == 'JavaScript':
            url = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'
        elif self.selected_language == 'Ruby':
            url = 'https://www.ruby-lang.org/en/'
        else:
            print("Por favor, selecciona un lenguaje válido.")
            return
        
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f'Error al abrir la página: {e}')

if __name__ == '__main__':
    MyApp().run()
