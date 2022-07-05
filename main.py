from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')


class MyApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if "0" == self.formula:
            self.formula=""
        self.formula += str(instance.text)
        self.update_label()

    def add_fun(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def rest(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula=str(eval(self.lbl.text))
    def clean(self, instance):
        self.formula='0'
        self.update_label()

    def build(self):
        self.formula="0"

        bl = BoxLayout(orientation='vertical', padding=[15])
        gl = GridLayout(cols=4, spacing=3)

        self.lbl = Label(text='0', font_size=40, size_hint=(1, .4), text_size=(400-30, 400 * .4 - 50), halign='right', valign='middle')
        bl.add_widget(self.lbl)
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text='СLean', on_press=self.clean))
        gl.add_widget(Button(text='/', on_press=self.add_fun))

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_fun))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_fun))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_fun))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.rest))

        bl.add_widget(gl)


        return bl



if __name__ == "__main__":
    MyApp().run()
