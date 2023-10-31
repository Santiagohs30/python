import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class MyGroup(BoxLayout):
    def __init__(self, **kwargs):
        super(MyGroup, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Fondo del grupo
        background = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)
        
        # Botones del grupo
        button1 = Button(text='Ir a Página 1', size_hint_y=None, height=40)
        button1.bind(on_press=lambda instance: self.open_url('https://www.facebook.com/ShangoArmenia/?locale=es_LA'))
        
        button2 = Button(text='Ir a Página 2', size_hint_y=None, height=40)
        button2.bind(on_press=lambda instance: self.open_url('https://chat.openai.com/'))
        
        button3 = Button(text='Ir a Página 3', size_hint_y=None, height=40)
        button3.bind(on_press=lambda instance: self.open_url('https://classroom.google.com/u/0/c/NjE2OTUzMDk0NzY1?hl=es'))
        
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)
    
    def open_url(self, url):
        webbrowser.open(url)

class GroupApp(App):
    def build(self):
        return MyGroup()

if __name__ == '__main__':
    GroupApp().run()
