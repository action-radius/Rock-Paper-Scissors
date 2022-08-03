import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('2.1.0')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_numbers = str(random.randint(1, 4))
        if self.random_numbers == "1":
            self.random_label.text = "Rock"
                    
        if self.random_numbers == "2":
            self.random_label.text = "Paper"
                    
        if self.random_numbers == "3":
            self.random_label.text = "Well"

        if self.random_numbers == "4":
            self.random_label.text = "Scissors"

class NeuralRandom(App):
    def build(self):
        return MyRoot()

neuralRandom = NeuralRandom()
neuralRandom.run()