from tkinter import Entry

class IntEntry(Entry):
    
    def __init__(self, parent, *args, **kwargs):
        Entry.__init__(self, parent, *args, **kwargs)

        vcmd = parent.register(self.isInt)
        self.configure(validate="key", validatecommand=(vcmd, '%P'))
        

    def isInt(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False