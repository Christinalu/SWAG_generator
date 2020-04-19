from tkinter import *
from tkinter import filedialog

from tika import parser # you will need java 8 enviornment to run this


class GUI:
    def __init__(self, window):
        self.window = window
        window.geometry('500x400')
        fm = Frame(window)
        Label(fm, text="Welcome to SAWG generator!", height=8, font = ("Consolas")).pack(side=TOP)
        Button(fm, text="Upload PDF file", command=self.uploadFile, font=("Consolas",12), bd=1, bg="black", fg="white").pack(side=TOP, expand=YES)
        fm.pack(fill=BOTH, expand=YES)
        

    def uploadFile(self):
        # NOTE: Now we accept .pdf and .txt file to upload, extract its words to a full "string" paragraph.
        fileRead = filedialog.askopenfile(title = "Select file", filetypes= (("PDF files","*.pdf"),("Text files","*.txt")))
        # all file content is now store in "raw_content", TODO: how to deal with those paragraphs with NLTK?
        raw_content = parser.from_file(fileRead.name)

        # print(raw_content['content'])

        
if __name__ == "__main__":
    root = Tk(className=' SWAG generator')    
    display = GUI(root)    
    root.mainloop()
