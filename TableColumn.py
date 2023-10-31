from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle


class DataTable(GridLayout):
    def __init__(self, **kwargs):
        super(DataTable, self).__init__(cols=1, spacing=10, **kwargs)
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        
        data = [
            "Nombre: Alice",
            "Edad: 25",
            "Ciudad: Nueva York",
            "Nombre: Bob",
            "Edad: 30",
            "Ciudad: Los Ángeles",
            "Nombre: Charlie",
            "Edad: 22",
            "Ciudad: Chicago",
            "Nombre: Eva",
            "Edad: 28",
            "Ciudad: Miami",
            "Nombre: David",
            "Edad: 35",
            "Ciudad: San Francisco"
        ]

        for item in data:
            self.add_widget(Label(text=item, size_hint_y=None, height=30))

class ImageBackground(Widget):
    def __init__(self, source, **kwargs):
        super(ImageBackground, self).__init__(**kwargs)
        self.background = Rectangle(source=source, pos=self.pos, size=self.size)
        self.bind(pos=self.update_background, size=self.update_background)

    def update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

class TableApp(App):
    def build(self):
        background = ImageBackground(source='background.jpg')
        data_table = DataTable()
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        scroll_view.add_widget(data_table)

        main_widget = Widget()
        main_widget.add_widget(background)
        main_widget.add_widget(scroll_view)

        return main_widget

if __name__ == '__main__':
    TableApp().run()
