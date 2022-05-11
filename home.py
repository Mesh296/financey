import kivy.clock
import kivymd.uix.textfield
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager

Window.size = (360, 800)

class Home(Screen):
    pass


class FinanceAPP(MDApp):

    def __init__(self):
        super(FinanceAPP, self).__init__()
        self.theme_cls = ThemeManager()

    def build(self): #build and load .kv file
        global screen_manager
        self.theme_cls.material_style = "M3"
        screen_manager = ScreenManager(transition=kivy.uix.screenmanager.WipeTransition())

        kv = Builder.load_file("home.kv")
        screen_manager.add_widget(Home(name="HomeScr"))

        return screen_manager




if __name__ == "__main__":
    FinanceAPP().run()