from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    context_text=self.text_area_1.text
    question_text=self.text_box_1.text

    output=anvil.server.call('ques_ans',question_text,context_text)

    if output:
      # self.output.visible=True
      self.rich_text_1.content=output 

