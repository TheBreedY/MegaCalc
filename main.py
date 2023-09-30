from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

# Builder.load_string("""
# <MenuScreen>:
#     BoxLayout:
#         padding: 5
#         spacing: 3
#         orientation: 'vertical'
#         Label:
#             size_hint: (1, 3)
#             text: 'MegaCalc'
#             font_size: 30
#         Button:
#             text: 'Обчислити'
#             on_press: root.manager.current = 'Calculation'
#         Button:
#             text: 'Конвертувати'
#             on_press: root.manager.current = 'Converting'
#         Button:
#             text: 'Налаштування'
#             on_press: root.manager.current = 'Settings'
#         Button:
#             id:btnExit
#             text: 'Вихід'
#             on_press: App.get_running_app().stop()

# <SettingsScreen>:
#     BoxLayout:
#         Button:
#             text: 'Кнопка налаштувань'
#         Button:
#             text: 'Назад до меню'
#             on_press: root.manager.current = 'Menu'

# <CalcScreen>:
#     BoxLayout:
#         orientation: 'vertical'
#         Label:
#             text: '0'
#             font_size: 40
#             halign: 'right'
#             size_hint: (1, .4)
#         GridLayout:
#             cols: 4
#             spacing: 3
#             padding: 5
#             size_hint: (1, .5)

#             Button:
#                 text: '7'
#             Button:
#                 text: '8'
#             Button:
#                 text: '9'
#             Button:
#                 text: 'X'

#             Button:
#                 text: '4'
#             Button:
#                 text: '5'
#             Button:
#                 text: '6'
#             Button:
#                 text: '/'

#             Button:
#                 text: '1'
#             Button:
#                 text: '2'
#             Button:
#                 text: '3'
#             Button:
#                 text: '-'

#             Button:
#                 text: '0'
#             Button:
#                 text: '.'
#             Button:
#                 text: '='
#             Button:
#                 text: '+'
    
#         AnchorLayout:
#             size_hint: (.4, .1)
#             anchor_x: 'center'
#             anchor_y: 'bottom'
#             padding: 5
#             Button:
#                 text: 'Назад до меню'
#                 on_press: root.manager.current = 'Menu'

# <ConvertingScreen>:
#     BoxLayout:
#         Button:
#             text: 'Назад до меню'
#             on_press: root.manager.current = 'Menu'

# """)

Builder.load_file('Builder.kv')

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        # mainlayout = BoxLayout(orientation='vertical', padding=5, spacing=3)
        # mainlayout.add_widget(Label(size_hint=(1, 3), font_size=30, text='MegaCalc'))
        # mainlayout.add_widget(Button(text='Обчислити', on_press=self.changeScreen('Calculation')))
    
    # def changeScreen(self, screenName):
    #     self.manager.current = screenName


class CalcScreen(Screen):
    
    def __init__(self, **kwargs):
        super(CalcScreen, self).__init__(**kwargs)

        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None

        layout = BoxLayout(orientation='vertical')
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        equals_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        backtoMenuButton = Button(text='Назад до меню')
        backtoMenuButton.bind(on_press=self.switch_to_menu)
        layout.add_widget(backtoMenuButton)

        self.add_widget(layout)

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_solution(self, instance):
        text = self.result.text
        try:
            solution = str(eval(self.result.text))
            self.result.text = solution
        except Exception:
            self.result.text = 'Error'
    
    def switch_to_menu(self, instance):
        self.manager.current = 'Menu'

class SettingsScreen(Screen):
    pass

class ConvertingScreen(Screen):
#     def __init__(self, **kwargs):
#         super(ConvertingScreen, self).__init__(**kwargs)

#         bl = BoxLayout()

#         # Список систем числення
#         number_systems = ['Decimal', 'Binary', 'Ternary', 'Quaternary', 'Hexadecimal']

#         # Випадаючий список для вибору системи числення
#         self.dropdown = DropDown()
#         for system in number_systems:
#             btn = Button(text=system, size_hint_y=None, height=30)
#             btn.bind(on_release=lambda btn, system=system: self.dropdown.select(system))
#             self.dropdown.add_widget(btn)

#         # Кнопка для вибору системи числення
#         self.number_system_button = Button(text='Select Number System', size_hint=(None, None))
#         self.number_system_button.bind(on_release=self.dropdown.open)
#         self.dropdown.bind(on_select=self.on_select)

#         # Текстове поле для введення числа
#         self.number_input = TextInput(hint_text='Enter number to convert', multiline=False)

#         # Результат конвертації
#         self.result_label = Label(text='', halign='center')

#         # Кнопка для виконання конвертації
#         self.convert_button = Button(text='Convert', on_press=self.convert)

#         # Розміщення елементів на екрані
#         self.add_widget(self.number_system_button)
#         self.add_widget(self.number_input)
#         self.add_widget(self.convert_button)
#         self.add_widget(self.result_label)

#         bl.add_widget(self.dropdown)

#     def on_select(self, instance, value):
#         self.number_system_button.text = value

#     def convert(self, instance):
#         number = self.number_input.text.strip()
#         system = self.number_system_button.text

#         try:
#             if system == 'Decimal':
#                 result = str(int(number, 10))
#             elif system == 'Binary':
#                 result = bin(int(number, 10))[2:]
#             elif system == 'Ternary':
#                 result = baseN(int(number, 10), 3)
#             elif system == 'Quaternary':
#                 result = baseN(int(number, 10), 4)
#             elif system == 'Hexadecimal':
#                 result = hex(int(number, 10))[2:].upper()
#             elif system == 'Roman':
#                 # Реалізуйте конвертацію в римські числа за потреби
#                 pass
#             else:
#                 result = 'Invalid Number System'

#             self.result_label.text = f'{number} in {system} is {result}'
#         except ValueError:
#             self.result_label.text = 'Invalid Input'
        
# def baseN(num, base):
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = ''
#     if num == 0:
#         return '0'
#     while num > 0:
#         result = digits[num % base] + result
#         num //= base
#     return result

    pass


class CalcApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='Menu'))
        sm.add_widget(CalcScreen(name='Calculation'))
        sm.add_widget(ConvertingScreen(name='Converting'))
        sm.add_widget(SettingsScreen(name='Settings'))

        sm.current = 'Menu'

        return sm

if __name__ == '__main__':
    CalcApp().run()