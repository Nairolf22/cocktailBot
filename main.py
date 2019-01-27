from idlelib import mainmenu

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



from helperFunctions import *

Builder.load_file("start.kv")
Builder.load_file("main.kv")


class StartScreen(Screen):
    pass


class PersonalInformation(Screen):
    pass


class MainMenu(Screen):
    def fill(self, seconds):
        self.ids.cocktail_filling.height = 0
        animation = Animation(height=(settings.height / 10 * settings.windowFactor), duration=seconds)
        animation.start(self.ids.cocktail_filling)
        pass


class BeverageButton(Button):
    def __init__(self, name, duration, main):
        Button.__init__(self)
        self.bevText = name
        self.duration = duration
        self.main = main

    def on_release(self):
        if self.duration:
            self.main.fill(self.duration)


bevDatabase = BevDatabase('beverages.db')
beverages = bevDatabase.getAvailableBeverages()
settings = Settings()

Window.size=(settings.width, settings.height)
mainMenu = MainMenu()
mainMenu.numCols = calcNumCols(len(beverages)+1)
for beverage in beverages:
    bev = BeverageButton(beverage['name'], beverage['duration'], mainMenu)
    mainMenu.ids.bevGrid.add_widget(bev)


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen())
sm.add_widget(PersonalInformation())
sm.add_widget(mainMenu)


class CockGuiApp(App):
    def build(self):
        self.title = 'Florians Cocktail-Bar'
        return sm

    def backToStartPressed(self):
        sm.current = 'start'


if __name__ == '__main__':
    CockGuiApp().run()


