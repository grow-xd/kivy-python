from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config

red = [1, 0, 0, 1] 
green = [0, 1, 0, 1] 
blue = [0, 0, 1, 1] 
purple = [1, 0, 1, 1] 


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        touch.ud['line'].width = 11


class MyPaintApp(App):
    

    def build(self):
        
        colors = [red, green, blue, purple] 
        self.title = 'Rg ka Paint App'
        self.icon = 'paint.ico'
        parent = Widget()
        self.painter = MyPaintWidget(background_color = [white])
        clearbtn = Button(text='Clear',background_color = [1, random(), random(), 1], font_size = 32, size_hint =(1, 15), pos =(900, 200))
        clearbtn2 = Button(text='Clear',background_color = [1, random(), random(), 1], font_size = 32, size_hint =(1, .2), pos =(0, 200)) 
        clearbtn.bind(on_release=self.clear_canvas)
        clearbtn2.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(clearbtn2)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
