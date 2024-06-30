from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

# Установка разрешения и соотношения сторон
Config.set('graphics', 'width', '2400')
Config.set('graphics', 'height', '1800')  # 2400 / 4 * 3 = 1800
Config.set('graphics', 'resizable', False)

# Определение интерфейса в формате KV
kv = '''
FloatLayout:
    MDTextField:
        hint_text: "Search"
        pos_hint: {"center_x": 0.5, "top": 0.95}
        size_hint_x: 0.8
        size_hint_y: None
        height: "48dp"
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    MyApp().run()


#asdfsad