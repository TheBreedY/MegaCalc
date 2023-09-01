from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        padding: 5
        spacing: 3
        orientation: 'vertical'
        Label:
            size_hint: (1, 3)
            text: 'MegaCalc'
            font_size: 30
        Button:
            text: 'Обчислити'
            on_press: root.manager.current = 'Calculation'
        Button:
            text: 'Конвертувати'
            on_press: root.manager.current = 'Converting'
        Button:
            text: 'Налаштування'
            on_press: root.manager.current = 'Settings'
        Button:
            id:btnExit
            text: 'Вихід'
            on_press: App.get_running_app().stop()

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'Кнопка налаштувань'
        Button:
            text: 'Назад до меню'
            on_press: root.manager.current = 'Menu'

<CalcScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: '012345'
            font_size: 40
            halign: 'right'
            size_hint: (1, .4)
        GridLayout:
            cols: 4
            spacing: 3
            padding: 5
            size_hint: (1, .5)

            Button:
                text: '7'
            Button:
                text: '8'
            Button:
                text: '9'
            Button:
                text: 'X'

            Button:
                text: '4'
            Button:
                text: '5'
            Button:
                text: '6'
            Button:
                text: '/'

            Button:
                text: '1'
            Button:
                text: '2'
            Button:
                text: '3'
            Button:
                text: '-'

            Button:
                text: '0'
            Button:
                text: '.'
            Button:
                text: '='
            Button:
                text: '+'
    
        AnchorLayout:
            size_hint: (.4, .1)
            anchor_x: 'center'
            anchor_y: 'bottom'
            padding: 5
            Button:
                text: 'Назад до меню'
                on_press: root.manager.current = 'Menu'

<ConvertingScreen>:
    BoxLayout:
        Button:
            text: 'Назад до меню'
            on_press: root.manager.current = 'Menu'

""")

class MenuScreen(Screen):
    pass

class CalcScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ConvertingScreen(Screen):
    pass

class GameApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='Menu'))
        sm.add_widget(CalcScreen(name='Calculation'))
        sm.add_widget(ConvertingScreen(name='Converting'))
        sm.add_widget(SettingsScreen(name='Settings'))

        return sm

if __name__ == '__main__':
    GameApp().run()