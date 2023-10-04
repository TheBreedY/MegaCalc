from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Builder.load_file('Builder.kv')

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

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
    def __init__(self, **kwargs):
        super(ConvertingScreen, self).__init__(**kwargs)

class ConvertingFromDecimalToBinaryScreen(Screen):
    def __init__(self, **kwargs):
        super(ConvertingFromDecimalToBinaryScreen, self).__init__(**kwargs)

        self.last_was_operator = None
        self.last_button = None

        layout = BoxLayout(orientation='vertical')
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['=', '0', 'C']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        # equals_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # equals_button.bind(on_press=self.on_solution)
        # layout.add_widget(equals_button)

        backtoMenuButton = Button(text='Назад до меню')
        backtoMenuButton.bind(on_press=self.switch_to_menu)
        layout.add_widget(backtoMenuButton)

        self.add_widget(layout)

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            self.on_solution()
        else:
            new_text = current + button_text
            self.result.text = new_text

    def decimal_to_binary(self, decimal_num):
        binary_num = bin(int(decimal_num))
        return binary_num[2:]

    def on_solution(self):
        text = self.result.text
        try:
            solution = str(self.decimal_to_binary(text))
            self.result.text = solution
        except Exception:
            print(text, Exception)
            self.result.text = 'Error'

    def switch_to_menu(self, instance):
        self.manager.current = 'Menu'

class ConvertingFromBinaryToDecimalScreen(Screen):
    def __init__(self, **kwargs):
        super(ConvertingFromBinaryToDecimalScreen, self).__init__(**kwargs)

        self.last_was_operator = None
        self.last_button = None

        layout = BoxLayout(orientation='vertical')
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['=', '0', 'C']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        # equals_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # equals_button.bind(on_press=self.on_solution)
        # layout.add_widget(equals_button)

        backtoMenuButton = Button(text='Назад до меню')
        backtoMenuButton.bind(on_press=self.switch_to_menu)
        layout.add_widget(backtoMenuButton)

        self.add_widget(layout)

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            self.on_solution()
        else:
            new_text = current + button_text
            self.result.text = new_text

    def binary_to_decimal(self, binary_num):
        decimal_num = int(binary_num, 2)
        return decimal_num

    def on_solution(self):
        text = self.result.text
        try:
            solution = str(self.binary_to_decimal(text))
            self.result.text = solution
        except Exception:
            print(text, Exception)
            self.result.text = 'Error'

    def switch_to_menu(self, instance):
        
        self.manager.current = 'Menu'

class CalcApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='Menu'))
        sm.add_widget(CalcScreen(name='Calculation'))
        sm.add_widget(ConvertingScreen(name='Converting'))
        sm.add_widget(SettingsScreen(name='Settings'))
        sm.add_widget(ConvertingFromDecimalToBinaryScreen(name='DecimalToBinary'))
        sm.add_widget(ConvertingFromBinaryToDecimalScreen(name='BinaryToDecimal'))

        sm.current = 'Menu'

        return sm

if __name__ == '__main__':
    CalcApp().run()