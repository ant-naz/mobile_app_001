from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):
    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation="vertical")
        self.lbl = Label(text="0", font_size=50, size_hint=(1, .2))
        bl.add_widget(self.lbl)
        gl = GridLayout(cols=4, size_hint=(1, .8))
        bl.add_widget(gl)

        gl.add_widget(Button(text="1", on_press=self._add_num))
        gl.add_widget(Button(text="2", on_press=self._add_num))
        gl.add_widget(Button(text="3", on_press=self._add_num))
        gl.add_widget(Button(text="+", on_press=self._add_symbol))

        gl.add_widget(Button(text="4", on_press=self._add_num))
        gl.add_widget(Button(text="5", on_press=self._add_num))
        gl.add_widget(Button(text="6", on_press=self._add_num))
        gl.add_widget(Button(text="-", on_press=self._add_symbol))

        gl.add_widget(Button(text="7", on_press=self._add_num))
        gl.add_widget(Button(text="8", on_press=self._add_num))
        gl.add_widget(Button(text="9", on_press=self._add_num))
        gl.add_widget(Button(text="*", on_press=self._add_symbol))

        gl.add_widget(Button(text="C", on_press=self._del_symbol))
        gl.add_widget(Button(text="0", on_press=self._add_num))
        gl.add_widget(Button(text="=", on_press=self._calculate))
        gl.add_widget(Button(text="/", on_press=self._add_symbol))

        return bl

    def _updata_label(self):
        self.lbl.text = self.formula

    def _add_num(self, instance):
        if self.formula == '0':
            self.formula = str(instance.text)
        else:
            self.formula += str(instance.text)
        self._updata_label()

    def _add_symbol(self, instance):
        self.formula += str(instance.text)
        self._updata_label()

    def _del_symbol(self, instance):
        self.formula = "0"
        self._updata_label()

    def _calculate(self, instance):
        self.formula = str(eval(self.formula))
        self._updata_label()


if __name__ == '__main__':
    Calculator().run()