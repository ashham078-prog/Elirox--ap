from kivy.app import App
from kivy.uix.label import Label

class EliroxApp(App):
    def build(self):
        return Label(text="Hello Elirox! APK Works!")

EliroxApp().run()
