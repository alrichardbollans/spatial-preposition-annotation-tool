import bgui
import bgui.bge_utils
import bge


class SimpleLayout(bgui.bge_utils.Layout):
    """A layout showcasing various Bgui features"""

    def __init__(self, sys, data):
        super().__init__(sys, data)

        # Add widgets here
        # Use a frame to store all of our widgets
        self.frame = bgui.Frame(self, border=0)
        self.frame.colors = [(0, 0, 0, 0) for i in range(4)]

        # # A Label widget
        # self.lbl = bgui.Label(self.frame, text='I sure wish someone would push that button...',
        #         pt_size=70, pos=[0, 0.7], options=bgui.BGUI_CENTERX)

        # # A FrameButton widget
        # self.btn = bgui.FrameButton(self.frame, text='Click Me!', size=[0.3, 0.1], pos=[0, 0.4],
        #         options=bgui.BGUI_CENTERX)

        # text input
        # A few TextInput widgets
        self.input = bgui.TextInput(self.frame, text="I'm active.", size=[.4, .04], pos=[.04, 0.02],
        input_options = 1)

        self.input.activate()
        self.input.on_enter_key = self.on_input_enter

    def on_input_enter(self, widget):
        self.lbl.text = "You've entered: " + widget.text
        widget.text = "You've locked this widget."
        widget.deactivate()
        widget.frozen = 1    



def main(cont):
    own = cont.owner
    mouse = bge.logic.mouse



    if 'sys' not in own:
        # Create our system and show the mouse
        own['sys'] = bgui.bge_utils.System('../../themes/default')
        own['sys'].load_layout(SimpleLayout, None)
        mouse.visible = True
    else:
        own['sys'].run()


cont = bge.logic.getCurrentController()

main(cont)