from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk
from tika import parser # you will need java 8 enviornment to run this

import bs4 as bs
import urllib.request
import re
    
url_text = ''
extracted_content = ''

# some colors
background = '#66cccc'
foreground = '#f1ccb8'
button_color = '#ED5752'
bg2 = '#400082'
img = Image.open('src\\swag.png')
img = img.resize((160, 40), Image.ANTIALIAS)

def uploadFile():
    # NOTE: Now we accept .pdf and .txt file to upload, extract its words to a full "string" paragraph.
    fileRead = filedialog.askopenfile(title = "Select file", filetypes= (("PDF files","*.pdf"),("Text files","*.txt")))
    raw_content = parser.from_file(fileRead.name)

    # print(raw_content['content'])
    global extracted_content
    extracted_content =  raw_content['content']

def readFromWeb():
    # Need to install BeautifulSoup 4, lxml
    global url_text, extracted_content
    web_url = str(url_text.get())
    print(web_url)
    extracted_article = ''
    # https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic
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
    extracted_content = extracted_article


def playGUI():
    window = Tk(className=' SWAG generator')
    window.configure(bg=background)
    window.geometry('600x500')
    fm = Frame(window)
    fm.configure(bg=background)
    fm.pack(fill=BOTH)
    # logo part
    logo_img = ImageTk.PhotoImage(img)
    logo = Label(fm, height=160, width=250,image=logo_img, bg=bg2)
    logo.image = logo_img
    logo.pack()
    # title
    Label(fm, text="automatic Sentiment Word Analysis Generator",height=4, font = ('Times', 18, 'bold'), bg=background, fg='white', highlightcolor='white').pack(side=TOP)
    # enter website or upload file
    Label(fm, text="Website URL:", font=("Consolas",13), bg=background).pack(side = LEFT, expand = True)
    global url_text
    url_text = Entry(fm, width=50, bd=2)
    url_text.pack(side = LEFT, expand = True)
    Button(fm, text="GO!", command=readFromWeb, font=("Consolas",12, 'bold'), bd=1, bg=button_color, fg="white").pack(side = LEFT, expand = True)
    Label(window, text="or", height=2, bg=background, font=("Consolas",13)).pack()
    Button(window, text="Upload PDF/txt file", command=uploadFile, font=("Consolas",12, 'bold'), bd=1, bg=button_color, fg="white").pack()
    
    window.mainloop()