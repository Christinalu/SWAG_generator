from tkinter import *
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk
from tika import parser # you will need java 8 enviornment to run this

import bs4 as bs
import tkinter as tk
import urllib.request
import re
import TF_IDF_Summarizer  # summarizer v1
import sentence_score_summarizer # summarizer v2
import disease_analysis
    
url_text = ''
content1 = ''
content2 = ''

# some colors
background = '#66cccc'
foreground = '#f1ccb8'
button_color = '#ED5752'
bg2 = '#400082'
img = Image.open('image\\swag.png')
img = img.resize((160, 40), Image.ANTIALIAS)

def uploadFile():
    global content1, content2
    # Browse .pdf or .txt file from user
    fileRead = filedialog.askopenfile(title = "Select file", filetypes= (("PDF files","*.pdf"),("Text files","*.txt")))
    raw_content = parser.from_file(fileRead.name)
    text = raw_content['content']
    text = re.sub(r'\[[0-9]*\]',' ',text)
    text = re.sub(r'\s+',' ',text)

    content2 = TF_IDF_Summarizer.main_function(text)
    # disease "professional name" analysis chart
    disease_analysis.print_analysis(text)
    content1 = sentence_score_summarizer.main_func(text)
    

def readFromWeb(): # Need to install BeautifulSoup 4, lxml
    global url_text, content1, content2
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
        
                    
        content2 = TF_IDF_Summarizer.main_function(extracted_article)
        # disease "professional name" analysis chart
        disease_analysis.print_analysis(extracted_article)
        content1 = sentence_score_summarizer.main_func(extracted_article)


def playGUI():
    global url_text
    # initialize the window and frame
    window = Tk(className=' Summary Text Analysis Generator')
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
    Label(fm, text="Summary Text Analysis Generator",height=4, font = ('Times', 18, 'bold'), bg=background, fg='white', highlightcolor='white').pack(side=TOP)
    
    # enter website or upload file
    Label(fm, text="Website URL:", font=("Consolas",13), bg=background).pack(side = LEFT, expand = True)
    url_text = Entry(fm, width=50, bd=2)
    url_text.pack(side = LEFT, expand = True)
    Button(fm, text="GO!", command=readFromWeb, font=("Consolas",12, 'bold'), bd=1, bg=button_color, fg="white").pack(side = LEFT, expand = True)
    Label(window, text="or", height=2, bg=background, font=("Consolas",13)).pack()
    Button(window, text="Upload PDF/txt file", command=uploadFile, font=("Consolas",12, 'bold'), bd=1, bg=button_color, fg="white").pack()

    # exit to the summary board
    Button(window, text="See your Summary Report -->", font=('Consolas', 12,'bold'), command=window.destroy, bg="yellow", fg=bg2).pack(side=RIGHT)
    window.mainloop()


def summaryGUI(text1, text2):
    text_bg = '#361642'
    root = Tk(className=' Summary Board')
    root.geometry('1100x500')
    root.config(bg=text_bg)
    
    # Titles
    fm = Frame(root)
    fm.configure(bg=text_bg)
    fm.pack(side=TOP, fill=X)
    Label(fm, height=1, width=23, text="Summarizor_Version_1", fg=text_bg, font = ('Times', 16, 'bold')).pack(side=LEFT, expand=True)
    Label(fm, height=1, width=23, text="Summarizor_Version_2", fg=text_bg, font = ('Times', 16, 'bold')).pack(side=RIGHT, expand=True)
    
    # Scrollbar and output text
    S1 = Scrollbar(root)
    S2 = Scrollbar(root)
    T1 = Text(root, spacing2=3, font=('Consolas', 12, 'bold'), height=20, width=50, bg=text_bg, fg='white')
    T2 = Text(root, spacing2=3, font=('Consolas', 12, 'bold'), height=20, width=50, bg=text_bg, fg='white')
    S1.pack(side=LEFT, fill=Y)
    S2.pack(side=RIGHT, fill=Y)
    T1.pack(side=LEFT, fill=Y)
    T2.pack(side=RIGHT, fill=Y)
    S1.config(command=T1.yview)
    S2.config(command=T2.yview)
    T1.config(yscrollcommand=S1.set)
    T2.config(yscrollcommand=S2.set)

    T1.insert(tk.END, text1)
    T2.insert(tk.END, text2)

    # export user's preferred file
    Button(root, text="Choose this -->", command=exportRightFile, font=("Consolas", 12, 'bold'), bd=1, bg=background, fg="white").pack(side=BOTTOM)
    Button(root, text="<-- Choose this", command=expotLeftFile, font=("Consolas", 12, 'bold'), bd=1, bg=background, fg="white").pack(side=BOTTOM)
    Button(root, text="Main Page", command=root.destroy, font=("Consolas", 12, 'bold'), bd=1, bg=background, fg="white").pack(side=TOP)
    
    root.mainloop()

def expotLeftFile(): # for sentence_score_summarizer
    global content1
    f = open("summary_report_v1.txt", "w")
    f.write(content1)
    f.close()
    sys.exit()

def exportRightFile(): # for TF_IDF_Summarizer
    global content2
    f = open("summary_report_v2.txt", "w")
    f.write(content2)
    f.close()
    sys.exit()

if __name__ == '__main__':

    while True:
        playGUI()
        if content1 != '' and content2 != '':
            summaryGUI(content1, content2)