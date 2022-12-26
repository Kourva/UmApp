# The Um App
# by Kourva

# Imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

# Main class
class UmApp(App):
    
    # Build method
    def build(self):
        
        # Grid layout
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(
            Image(
                source="um_adaptive_fore.png"
            )
        )

        # label widget
        self.text = Label(
                        text= "So It's just UM :0".upper(),
                        font_size= 18,
                        color= '#00FFFF'
                        )
        self.window.add_widget(self.text)

        # Returns window
        return self.window

# Run
UmApp().run()
