import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.1.0')

class NeuralRandom(App):
    def build(self):
        return BoxLayout()

neuralRandom = NeuralRandom()
neuralRandom.run()