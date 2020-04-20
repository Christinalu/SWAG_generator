from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tika import parser # you will need java 8 enviornment to run this

import bs4 as bs
import urllib.request
import re
    
url_text = ''

def uploadFile():
    # NOTE: Now we accept .pdf and .txt file to upload, extract its words to a full "string" paragraph.
    fileRead = filedialog.askopenfile(title = "Select file", filetypes= (("PDF files","*.pdf"),("Text files","*.txt")))
    raw_content = parser.from_file(fileRead.name)

    # print(raw_content['content'])
    return raw_content['content']

def readFromWeb():
    # Need to install BeautifulSoup 4, lxml
    global url_text
    web_url = str(url_text.get())
    print(url_text)
    print(web_url)
    extracted_article = ''

    if web_url != '':
        try:
            website = urllib.request.urlopen(web_url).read()

            soup = bs.BeautifulSoup(website, 'lxml')
            extracted_article = ""
            for item in soup.find_all ('p'):
                extracted_article = extracted_article + item.text

            extracted_article = re.sub(r'\s+',' ',extracted_article)

            extracted_article = re.sub(r'\[[0-9]*\]',' ',extracted_article)
        except:
            messagebox.showwarning(title="Input Error", message="URL Error, please re-enter.")

    # print (extracted_article)
    return extracted_article


def playGUI():
    window = Tk(className=' SWAG generator')  
    window.geometry('500x400')
    fm = Frame(window)
    fm.pack(fill=BOTH)
    Label(fm, text="Welcome to SAWG generator!", height=7, font = ("Consolas")).pack(side=TOP)
    Label(fm, text="Website URL:", font=("Consolas",13)).pack(side = LEFT, expand = True)
    global url_text
    url_text = Entry(fm, width=40, bd=2)
    url_text.pack(side = LEFT, expand = True)
    Button(fm, text="GO!", command=readFromWeb, font=("Consolas",12), bd=1, bg="black", fg="white").pack(side = LEFT, expand = True)
    Label(window, text="or", height=2, font=("Consolas",13)).pack()
    Button(window, text="Upload PDF/txt file", command=uploadFile, font=("Consolas",12), bd=1, bg="black", fg="white").pack()
    
    window.mainloop()
