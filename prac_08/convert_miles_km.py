from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRE_RATE = 1.60934


class ConvertMilesKm(App):
    """An App that converts kilometres to miles."""
    status_text = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    # def handle_press(self, value):
    #     converted_distance = self.convert_to_number(value)
    #     converted_distance *= MILES_TO_KILOMETRE_RATE
    #     self.root.ids.converted_number.text = str(converted_distance)

    def handle_text(self, value):
        converted_distance = self.convert_to_number(value)
        converted_distance *= MILES_TO_KILOMETRE_RATE
        self.root.ids.converted_number.text = str(converted_distance)
        self.update_result(converted_distance)

    def handle_increment(self, value, increment):
        miles = self.convert_to_number(value)
        miles += increment
        self.root.ids.input_number.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.status_text = str(miles * MILES_TO_KILOMETRE_RATE)

    @staticmethod
    def convert_to_number(value):
        try:
            return float(value)
        except ValueError:
            return 0.0


ConvertMilesKm().run()
