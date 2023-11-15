from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Lucas", "Cameron", "Hayden", "Faith", "Chandler"]  # Add siblings to names

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            print(f"Hello {name}")
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
