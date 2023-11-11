"""
Dynamic Label App

Estimate : 30 minutes
Actual : 40 minutes
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicLabels(App):
    """Construct Dynamic Labels App."""

    def __init__(self, **kwargs):
        """Initialise list of names."""
        super().__init__(**kwargs)
        self.names = ["Lucas", "Cameron", "Hayden", "Faith", "Chandler"]  # Add siblings to names

    def build(self):
        """Build Dynamic Labels."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create a widget for each name in a list."""
        for name in self.names:
            temp_label = Label(text=name)
            print(f"Hello {name}")
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
