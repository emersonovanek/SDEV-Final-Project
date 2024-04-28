import breezypythongui
from breezypythongui import EasyFrame
import tkinter
from tkinter import PhotoImage

class PurchasingClothing(EasyFrame):
    """Shows images of pre-owned clothing for sale, with prices, sizing, and
    any additional relevant info. User is then able to purchase items."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Purchasing Clothing")
        self.setResizable(False);
        # Thrasher hoodie image
        self.thrasherImage = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        # Thrasher hoodie label
        self.thrasherText = self.addLabel(text = "Brand: Thrasher\n Size: Small\n Price: $15",
                                     row = 1, column = 0, sticky = "NSEW")
        # Empyre denim shorts image
        self.empyreImage = self.addLabel(text = "", row = 0, column = 1, sticky = "NSEW")
        # Empyre denim shorts label
        self.empyreText = self.addLabel(text = "Brand: Empyre\n Size: 32\n Price: $20",
                                   row = 1, column = 1, sticky = "NSEW")
        # Golf Le Fleur sweatshirt image
        self.leFleurImage = self.addLabel(text = "", row = 2, column = 0, sticky = "NSEW")
        # Golf Le Fleur sweatshirt label
        self.leFleurText = self.addLabel(text = "Brand: Golf le Fleur\n Size: Medium\n Price: $25",
                                   row = 3, column = 0, sticky = "NSEW")
        # Golf Wang hoodie image
        self.golfWangImage = self.addLabel(text = "", row = 2, column = 1, sticky = "NSEW")
        # Golf Wang hoodie label
        self.golfWangText = self.addLabel(text = "Brand: Golf Wang\n Size: Medium\n Price: $30",
                                     row = 3, column = 1, sticky = "NSEW")
        self.thrasherGif = PhotoImage(file = "thrasher.gif")
        self.thrasherImage["image"] = self.thrasherGif
        self.empyreGif = PhotoImage(file = "empyre.gif")
        self.empyreImage["image"] = self.empyreGif
        self.leFleurGif = PhotoImage(file = "lefleur.gif")
        self.leFleurImage["image"] = self.leFleurGif
        self.golfWangGif = PhotoImage(file = "golfwang.gif")
        self.golfWangImage["image"] = self.golfWangGif

PurchasingClothing()
