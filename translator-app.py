from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
#root.iconbitmap('image.jpg')
root['bg'] = 'skyblue'

#Header
root.title('Made by Abhishek with ❤️')
Label(root, text="Language Translator", font="Ariel 20 bold").pack()

Label(root,text="Enter text", font="Ariel 13 bold", bg="white smoke").place(x=165, y=90)


Label(root,text="Enter text", font="Ariel 13 bold", bg="white smoke").place(x=-165, y=90)

Input_text = Entry(root, width = 60)
Input_text.place(x=30, y=130)
Input_text.get()

from translate import Translator

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600,y=130)

language = list(LANGUAGES.values())
print(len(language))

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('choose language')

def Translate():
    translator = Translator(to_lang = dest_lang.get(), from_lang='en')
    translated = translator.translate(text = Input_text.get())  
    #print(translated)
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated)
    
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command= Translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=180)
    
root.mainloop()    


#107 Languages it can translate
#['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']