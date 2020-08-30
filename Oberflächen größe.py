"""

Die Bildschirm Oberfläche soll sich der Fenster größe anpassen.
Z.B. ist das Spielfeld 20x20 Blöcke groß.
Ich muss also definieren wie groß ein block ist.
außerdem muss ich die Blockgröße von der fenster größe abhängig machen.

blockbreite = bildschrimgröße / anzahl der blöcke


"""

from tkinter import ttk
import tkinter
from tkinter import *
from tkinter import Tk


fenster = tkinter.Tk()
fenster.title("Snake spiel von Dominik")
fenster.geometry("300x300")
fenster.configure(background="azure")


def knopf_funktion():
    print("Hello Dominik")
knopf = Button(fenster, text="start ", command=knopf_funktion())
knopf.pack()





fenster.mainloop()
