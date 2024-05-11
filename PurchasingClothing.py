import os
from breezypythongui import EasyFrame
import tkinter
from tkinter import PhotoImage

class PurchasingClothing(EasyFrame):
    """Shows images of pre-owned clothing for sale, with prices, sizing, and
    any additional relevant info. User is then able to purchase items."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, width=1000, height=1000, title="Purchasing Clothing")
        # Makes the window resizeable
        self.setResizable(True)
        self.count = 0

        # Thrasher hoodie image
        self.thrasherImage = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        # Thrasher hoodie label
        self.thrasherText = self.addLabel(text = "Brand: Thrasher\n Size: Small\n Price: $15",
                                          row = 1, column = 0, sticky = "NSEW")
        # View more details button
        self.addButton(text="View More Details", row = 2, column = 0, command = self.openThrasherFileButtonClick)
        # Add to cart
        self.thrasherCartButton = self.addCheckbutton(text = "Add to Cart", row = 3, column = 0, command = self.thrasherAddCart)


        # Empyre denim shorts image
        self.empyreImage = self.addLabel(text = "", row = 0, column = 1, sticky = "NSEW")
        # Empyre denim shorts label
        self.empyreText = self.addLabel(text = "Brand: Empyre\n Size: 32\n Price: $20",
                                        row = 1, column = 1, sticky = "NSEW")
        # View more details button
        self.addButton(text="View More Details", row = 2, column = 1, command = self.openEmpyreFileButtonClick)
        # Add to cart
        self.empyreCartButton = self.addCheckbutton(text = "Add to Cart", row = 3, column = 1, command = self.empyreAddCart)


        # Golf Le Fleur sweatshirt image
        self.fleurImage = self.addLabel(text = "", row = 7, column = 0, sticky = "NSEW")
        # Golf Le Fleur sweatshirt label
        self.fleurText = self.addLabel(text = "Brand: Golf le Fleur\n Size: Medium\n Price: $25",
                                       row = 8, column = 0, sticky = "NSEW")
        # View more details
        self.addButton(text="View More Details", row = 9, column = 0, command = self.openFleurFileButtonClick)
        # Add to cart
        self.fleurCartButton = self.addCheckbutton(text = "Add to Cart", row = 10, column = 0, command = self.fleurAddCart)


        # Golf Wang hoodie image
        self.wangImage = self.addLabel(text = "", row = 7, column = 1, sticky = "NSEW")
        # Golf Wang hoodie label
        self.wangText = self.addLabel(text = "Brand: Golf Wang\n Size: Medium\n Price: $30",
                                      row = 8, column = 1, sticky = "NSEW")
        # View more details
        self.addButton(text="View More Details", row = 9, column = 1, command = self.openWangFileButtonClick)
        # Add to cart
        self.wangCartButton = self.addCheckbutton(text = "Add to Cart", row = 10, column = 1, command = self.wangAddCart)


        # Assign PhotoImage attribute to Thrasher GIF
        self.thrasherGif = PhotoImage(file="thrasher.gif")
        # Adjust the image size
        self.thrasherGif = self.thrasherGif.subsample(16, 16)
        # Set the image command to the GIF file
        self.thrasherImage["image"] = self.thrasherGif


        # Assign PhotoImage attribute to Empyre GIF
        self.empyreGif = PhotoImage(file="empyre.gif")
        # Adjust the image size
        self.empyreGif = self.empyreGif.subsample(16, 16)
        # Set the image command to the GIF file
        self.empyreImage["image"] = self.empyreGif


        # Assign PhotoImage attribute to Golf le Fleur GIF
        self.fleurGif = PhotoImage(file="lefleur.gif")
        # Adjust the image size
        self.fleurGif = self.fleurGif.subsample(16, 16)
        # Set the image command to the GIF file
        self.fleurImage["image"] = self.fleurGif


        # Assign PhotoImage attribute to the Golf Wang GIF
        self.wangGif = PhotoImage(file="golfwang.gif")
        # Adjust the image size
        self.wangGif = self.wangGif.subsample(16, 16)
        # Set the image command to the GIF file
        self.wangImage["image"] = self.wangGif

        # Proceed to check out button
        self.addButton(text = "Proceed to Check Out", row = 12, column = 0, columnspan = 2)

    def openThrasherFileButtonClick(self):
        """Opens the text file containing details about the Thrasher hoodie."""
        open("thrasherdetails.txt", "r")
        

    def openEmpyreFileButtonClick(self):
        """Opens the text file containing details about the Empyre denim shorts."""
        open("empyredetails.txt", "r")

    def openFleurFileButtonClick(self):
        """Opens the text file containing details about the Golf le Fleur sweatshirt."""
        open("fleurdetails.txt", "r")

    def openWangFileButtonClick(self):
        """Opens the text file containing details about the Golf Wang hoodie."""
        open("wangdetails.txt", "r")

    def thrasherAddCart(self):
        self.count += 15

    def empyreAddCart(self):
        self.count += 20

    def fleurAddCart(self):
        self.count += 25

    def wangAddCart(self):
        self.count += 30

# Instantiate the PurchasingClothing class
app = PurchasingClothing()
# Run the application
app.mainloop()
