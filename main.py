from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

class MenuWindow(Screen):
    pass

class IntroWindow(Screen):
    pass

class StatisWindow(Screen):
    pass

class MyApp(App):
    def build(self):
        return StatisWindow()

if __name__ == '__main__':
    MyApp().run()

