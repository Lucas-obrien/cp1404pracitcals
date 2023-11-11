from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayout Demo."""
    def build(self):
        """Build a display box"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Return hello and text input."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear text from ids in app."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
