from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
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
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'Menu'

<ConvertingScreen>:
    BoxLayout:
        Button:
            text: 'Back to menu'
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