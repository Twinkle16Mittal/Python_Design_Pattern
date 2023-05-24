#  Factory design pattern is creating concrete classess or objects
# and our abstract factory pattern is going to create a factory that is going to create object family of classes.

from abc import ABC, abstractmethod
class IButton(ABC):

    @abstractmethod
    def press(self):
        return ""

class MacButton(IButton):

    def press(self):
        return "Mac Button Pressed!"

class WinButton(IButton):

    def press(self):
        # import pdb
        # pdb.set_trace
        return "Win Button Pressed!"
    

class ITextBox(ABC):

    @abstractmethod
    def show_text(self):
        return ""

class MacTextBox(ITextBox):

    def show_text(self):
        return "Showing Mac TextBox!"

class WinTextBox(ITextBox):

    def show_text(self):
        return "Showing Win TextBox!"

class IFactory(ABC):

    def create_button(self):
        return ""

    def create_text_box(self):
        return ""


class MacFactory(IFactory):
    def create_button(self):
        return MacButton()

    def create_text_box(self):
        return MacTextBox()


class WinFactory(IFactory):

    def create_button(self):
        return WinButton()

    def create_text_box(self):
        return WinTextBox()


class GUIAbstractFactory:

    @staticmethod
    def create_factory(os_type):
        if os_type == "windows":
            return WinFactory()
        elif os_type == "mac":
            return MacFactory()
        else:
            print("No Match! Showing default value")
            return MacFactory()

def run_code():
    os_type = input("enter os_type: ")
    fact = GUIAbstractFactory.create_factory(os_type)

    button = fact.create_button()
    print(button.press())

    text_box = fact.create_text_box()
    print(text_box.show_text())

if __name__ == "__main__":
    run_code()



"""
Here I have created an example of abstract factory.
so that user just need to specify the os_Type and will depending on the os type window factory will be called which internally will call the another factory for creating the button or textbox.
"""

