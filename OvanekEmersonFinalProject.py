from breezypythongui import EasyFrame
import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk

class PurchasingClothing(EasyFrame):
    """Shows images of pre-owned clothing for sale, with prices, sizing, and
    any additional relevant info. User is then able to purchase items."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, width=1000, height=1000, title="Purchasing Clothing")
        self.setResizable(True) # Makes the window resizeable
        self.count = 0 # Initializes the count for the end total

        self.thrasherImage = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW") # Thrasher hoodie image
        self.thrasherText = self.addLabel(text = "Brand: Thrasher\n Size: Small\n Price: $15",
                                          row = 1, column = 0, sticky = "NSEW") # Thrasher hoodie label

        self.addButton(text="View More Details", row = 2, column = 0, command = self.openThrasherDetails) # View more details button
        self.thrasherCartButton = self.addCheckbutton(text = "Add to Cart", row = 3, column = 0, command = self.thrasherAddCart) # Add to cart

        self.empyreImage = self.addLabel(text = "", row = 0, column = 1, sticky = "NSEW") # Empyre denim shorts image
        self.empyreText = self.addLabel(text = "Brand: Empyre\n Size: 32\n Price: $20",
                                        row = 1, column = 1, sticky = "NSEW") # Empyre denim shorts label
        self.addButton(text="View More Details", row = 2, column = 1, command = self.openEmpyreDetails) # View more details button
        self.empyreCartButton = self.addCheckbutton(text = "Add to Cart", row = 3, column = 1, command = self.empyreAddCart) # Add to cart

        self.fleurImage = self.addLabel(text = "", row = 7, column = 0, sticky = "NSEW") # Golf Le Fleur sweatshirt image
        self.fleurText = self.addLabel(text = "Brand: Golf le Fleur\n Size: Medium\n Price: $25",
                                       row = 8, column = 0, sticky = "NSEW") # Golf Le Fleur sweatshirt label
        self.addButton(text="View More Details", row = 9, column = 0, command = self.openFleurDetails) # View more details button
        self.fleurCartButton = self.addCheckbutton(text = "Add to Cart", row = 10, column = 0, command = self.fleurAddCart) # Add to cart

        self.wangImage = self.addLabel(text = "", row = 7, column = 1, sticky = "NSEW") # Golf Wang hoodie image
        self.wangText = self.addLabel(text = "Brand: Golf Wang\n Size: Medium\n Price: $30",
                                      row = 8, column = 1, sticky = "NSEW") # Golf Wang hoodie label
        self.addButton(text="View More Details", row = 9, column = 1, command = self.openWangDetails) # View more details button
        self.wangCartButton = self.addCheckbutton(text = "Add to Cart", row = 10, column = 1, command = self.wangAddCart) # Add to cart


        self.thrasherGif = PhotoImage(file="thrasher.gif") # Assign PhotoImage attribute to Thrasher GIF
        self.thrasherGif = self.thrasherGif.subsample(16, 16) # Adjust the image size
        self.thrasherImage["image"] = self.thrasherGif # Set the image command to the GIF file

        self.empyreGif = PhotoImage(file="empyre.gif") # Assign PhotoImage attribute to Empyre GIF
        self.empyreGif = self.empyreGif.subsample(16, 16) # Adjust the image size
        self.empyreImage["image"] = self.empyreGif # Set the image command to the GIF file

        self.fleurGif = PhotoImage(file="lefleur.gif") # Assign PhotoImage attribute to Golf le Fleur GIF
        self.fleurGif = self.fleurGif.subsample(16, 16) # Adjust the image size
        self.fleurImage["image"] = self.fleurGif # Set the image command to the GIF file

        self.wangGif = PhotoImage(file="golfwang.gif") # Assign PhotoImage attribute to the Golf Wang GIF
        self.wangGif = self.wangGif.subsample(16, 16) # Adjust the image size
        self.wangImage["image"] = self.wangGif # Set the image command to the GIF file

        self.totalLabel = self.addLabel(text = "Subtotal: ${:,.2f}".format(int(self.count)), row = 11,
                                        column = 0, sticky = "NSEW", columnspan = 2) # Displays the running total
        self.checkOutButton = self.addButton(text = "Proceed to Check Out", row = 12, column = 0,
                                             columnspan = 2, command = self.checkOut) # Proceed to check out button
        
    def openThrasherDetails(self):
        """Opens a new window with expanded details about the Thrasher hoodie."""
        win = ThrasherWindow(self)

    def openEmpyreDetails(self):
        """Opens a new window with expanded details about the Empyre denim shorts."""
        win = EmpyreWindow(self)

    def openFleurDetails(self):
        """Opens a new window with expanded details about the Golf le Fleur sweatshirt."""
        win = FleurWindow(self)

    def openWangDetails(self):
        """Opens a new window with expanded details about the Golf Wang hoodie."""
        win = WangWindow(self)

    def thrasherAddCart(self):
        """Adds the total of the Thrasher hoodie to the subtotal."""
        self.count += 15
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to remove from cart
        self.thrasherCartButton = self.addCheckbutton(text = "Remove from Cart", row = 3,
                                                 column = 0, command = self.thrasherRemoveCart)

    def thrasherRemoveCart(self):
        """Removes the total of the Thrasher hoodie from the subtotal if previously added."""
        self.count -= 15
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to add to cart
        self.thrasherCartButton = self.addCheckbutton(text = "Add to Cart", row = 3, column = 0,
                                                      command = self.thrasherAddCart)

    def empyreAddCart(self):
        """Adds the total of the Empyre denim shorts to the subtotal."""
        self.count += 20
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to remove from cart
        self.empyreCartButton = self.addCheckbutton(text = "Remove from Cart", row = 3,
                                                    column = 1, command = self.empyreRemoveCart)

    def empyreRemoveCart(self):
        """Removes the total of the Empyre denim shorts from the subtotal if previously added."""
        self.count -= 20
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to add to cart
        self.thrasherCartButton = self.addCheckbutton(text = "Add to Cart", row = 3, column = 1,
                                                      command = self.empyreAddCart)

    def fleurAddCart(self):
        """Adds the total of the Golf le Fleur sweatshirt to the subtotal."""
        self.count += 25
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to remove from cart
        self.fleurCartButton = self.addCheckbutton(text = "Remove from Cart", row = 10, column = 0,
                                                   command = self.fleurRemoveCart)

    def fleurRemoveCart(self):
        """Removes the total of the Golf le Fleur sweatshirt from the subtotal if previously added."""
        self.count -= 25
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to add to cart
        self.fleurCartButton = self.addCheckbutton(text = "Add to Cart", row = 10, column = 0,
                                                   command = self.fleurAddCart)

    def wangAddCart(self):
        """Adds the total of the Golf Wang hoodie to the subtotal."""
        self.count += 30
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to remove from cart
        self.wangCartButton = self.addCheckbutton(text = "Remove from Cart", row = 10, column = 1,
                                                  command = self.wangRemoveCart)

    def wangRemoveCart(self):
        """Removes the total of the Golf Wang hoodie from the subtotal if previously added."""
        self.count -= 30
        # Updates the running subtotal
        self.totalLabel["text"] = "Subtotal: ${:,.2f}".format(int(self.count))
        # Modifies the cart button to allow the user to add to cart
        self.wangCartButton = self.addCheckbutton(text = "Add to Cart", row = 10, column = 1,
                                                  command = self.wangAddCart)

    def checkOut(self):
        """Opens a new window to initiate the check out process."""
        if self.count == 0:
            # Displays error message for total of $0.00
            win = InvalidTotal(self)
        else:
            # Opens the check out window
            win = CheckOutWindow(self)

class ThrasherWindow(tk.Toplevel):
    def __init__(self, parent):
        """This window provides more details for the Thrasher hoodie."""
        super().__init__(parent)
        # Button to close the window. The details are written as the label so that the user can click anywhere within the window
        tk.Button(self, text = "This item measures 19 inches wide and 24 inches long.\nThis item is in great condition with no visible stains, holes, or flaws.\n\nClick anywhere in this window to close.",
                  command = self.destroy).pack(expand = True)

class EmpyreWindow(tk.Toplevel):
    def __init__(self, parent):
        """This window provides more details for the Empyre denim shorts."""
        super().__init__(parent)
        # Button to close the window. The details are written as the label so that the user can click anywhere within the window
        tk.Button(self, text = "This item measures 16 inches wide and 15 inches long.\nThe inseam measures 6 inches long.\nThis item is in great condition with no visible stains, holes, or flaws.\n\nClick anywhere in this window to close.",
                  command = self.destroy).pack(expand = True)

class FleurWindow(tk.Toplevel):
    def __init__(self, parent):
        """This window provides more details for the Golf le Fleur sweatshirt."""
        super().__init__(parent)
        # Button to close the window. The details are written as the label so that the user can click anywhere within the window
        tk.Button(self, text = "This item measures 20.5 inches wide and 23.5 inches long.\nThis item is in great condition with no visible stains, holes, or flaws.\n\nClick anywhere in this window to close.",
                  command = self.destroy).pack(expand = True)

class WangWindow(tk.Toplevel):
    def __init__(self, parent):
        """This window provides more details for the Golf Wang hoodie."""
        super().__init__(parent)
        # Button to close the window. The details are written as the label so that the user can click anywhere within the window
        tk.Button(self, text = "This item measures 21 inches wide and 30 inches long in total.\nFrom the shoulder to the bottom, the length measures 23 inches.\nThis item is in great condition with no visible stains, holes, or flaws.\n\nClick anywhere in this window to close.",
                  command = self.destroy).pack(expand = True)

class InvalidTotal(tk.Toplevel):
    def __init__(self, parent):
        """This window provides an error message when the subtotal is equal to $0.00. The user can continue shopping."""
        super().__init__(parent)
        # Button to close the window. The error message is written as the label so that the user can click anywhere within the window
        tk.Button(self, text = "ERROR:\n\nTotal must be greater than $0.00.\n\nClick anywhere in this window to continue shopping.",
                  command = self.destroy).pack(expand = True)

class CheckOutWindow(tk.Toplevel, PurchasingClothing):
    """Provides input fields in order to complete the check out process."""
    def __init__(self, purchasing_clothing):
        """Sets up the main window."""
        window = Tk() # Creates the new window
        window.title("Check Out") # Titles the new window
        frame = tk.Frame(window) # Creates the parent frame
        frame.pack() # Positions the parent frame
        
        shippingEntryFrame = tk.LabelFrame(frame, text = "Shipping Information") # Creates the frame for entering shipping information
        shippingEntryFrame.grid(row = 0, column = 0, padx = 20, pady = 20) # Position for the shipping information entry frame

        firstNameLabel = tk.Label(shippingEntryFrame, text = "First Name:") # Label for first name entry
        firstNameLabel.grid(row = 0, column = 0) # Position of first name entry label
        firstNameEntry = tk.Entry(shippingEntryFrame) # Creates entry box for user input of first name
        firstNameEntry.grid(row = 1, column = 0) # Position of first name entry box
        firstNameValidMsg = tk.Label(shippingEntryFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        firstNameValidMsg.grid(row = 2, column = 0) # Position of validation error message

        lastNameLabel = tk.Label(shippingEntryFrame, text = "Last Name:") # Label for last name entry
        lastNameLabel.grid(row = 0, column = 1) # Position of last name entry label
        lastNameEntry = tk.Entry(shippingEntryFrame) # Creates entry box for user input of last name
        lastNameEntry.grid(row = 1, column = 1) # Position of last name entry box
        lastNameValidMsg = tk.Label(shippingEntryFrame, text = "", fg = "red") # Empty label intended to display a validation message
        lastNameValidMsg.grid(row = 2, column = 1)  # Position of validation error message

        streetAddressLabel = tk.Label(shippingEntryFrame, text = "Street Address:") # Label for street address entry
        streetAddressLabel.grid(row = 0, column = 2) # Position of street address entry label
        streetAddressEntry = tk.Entry(shippingEntryFrame) # Creates entry box for user input of street address
        streetAddressEntry.grid(row = 1, column = 2) # Position of street address entry box
        streetAddressValidMsg = tk.Label(shippingEntryFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        streetAddressValidMsg.grid(row = 2, column = 2) # Position of validation error message

        cityLabel = tk.Label(shippingEntryFrame, text = "City:") # Label for city entry
        cityLabel.grid(row = 3, column = 0) # Position of city entry label
        cityEntry = tk.Entry(shippingEntryFrame) # Creates entry box for user input of city
        cityEntry.grid(row = 4, column = 0) # Position of city entry box
        cityValidMsg = tk.Label(shippingEntryFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        cityValidMsg.grid(row = 5, column = 0) # Position of validation error message

        stateLabel = tk.Label(shippingEntryFrame, text = "State / Territory:") # Label for state / territory drop down
        stateLabel.grid(row = 3, column = 1) # Position of state / territory drop down label
        stateDropDown = ttk.Combobox(shippingEntryFrame, state = "readonly", values = ["Choose your state / territory", "Alabama", "Alaska", "American Samoa",
                                                                   "Arizona", "Arkansas", "Armed Forces Americas", "Armed Forces Pacific",
                                                                   "Armed Forces Other", "California", "Colorado", "Connecticut", "Delaware",
                                                                   "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho",
                                                                   "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
                                                                   "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
                                                                   "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                                                                   "New Mexico", "New York", "North Carolina", "North Dakota",
                                                                   "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                                                                   "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
                                                                   "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia",
                                                                   "Washington", "West Virginia", "Wisconsin", "Wyoming"]) # Drop down selection of state / territory
        stateDropDown.grid(row = 4, column = 1) # Position of state / territory drop down
        stateValidMsg = tk.Label(shippingEntryFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        stateValidMsg.grid(row = 5, column = 1) # Position of validation error message

        zipLabel = tk.Label(shippingEntryFrame, text = "Zip Code:") # Label for zip code entry
        zipLabel.grid(row = 3, column = 2) # Position of zip code entry label
        zipEntry = tk.Entry(shippingEntryFrame) # Creates entry box for user input of zip code
        zipEntry.grid(row = 4, column = 2) # Position of zip code entry box
        zipValidMsg = tk.Label(shippingEntryFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        zipValidMsg.grid(row = 5, column = 2) # Position of validation error message

        for widget in shippingEntryFrame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5) # Applies padding to all widgets in shippingEntryFrame


        paymentFrame = tk.LabelFrame(frame, text = "Payment Information") # Creates the payment information frame
        paymentFrame.grid(row = 1, column = 0, padx = 20, pady = 20) # Position of payment information frame

        # First name on card
        cardFirstNameLabel = tk.Label(paymentFrame, text = "First Name on Card:") # Label for entry of first name on card
        cardFirstNameLabel.grid(row = 0, column = 0) # Position of first name on card entry label
        cardFirstNameEntry = tk.Entry(paymentFrame) # Creates entry box for user input of first name on card
        cardFirstNameEntry.grid(row = 1, column = 0) # Position of first name on card entry box
        cardFirstNameValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        cardFirstNameValidMsg.grid(row = 2, column = 0) # Position of validation error message

        # Last name on card
        cardLastNameLabel = tk.Label(paymentFrame, text = "Last Name on Card:") # Label for entry of last name on card
        cardLastNameLabel.grid(row = 0, column = 1) # Position of last name on card entry label
        cardLastNameEntry = tk.Entry(paymentFrame) # Creates entry box for user input of last name on card
        cardLastNameEntry.grid(row = 1, column = 1) # Position of last name on card entry box
        cardLastNameValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        cardLastNameValidMsg.grid(row = 2, column = 1) # Position of validation error message

        # Card number
        cardNumberLabel = tk.Label(paymentFrame, text = "Card Number:") # Label for card number entry
        cardNumberLabel.grid(row = 0, column = 2) # Position of card number entry label
        cardNumberEntry = tk.Entry(paymentFrame) # Creates entry box for user input of card number
        cardNumberEntry.grid(row = 1, column = 2) # Position of card number entry box
        cardNumberValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        cardNumberValidMsg.grid(row = 2, column = 2) # Position of validation error message

        # Expiration month
        expMonthLabel = tk.Label(paymentFrame, text = "Expiration Month:") # Label for expiration month drop down
        expMonthLabel.grid(row = 3, column = 0) # Position of expiration month drop down label
        expMonthDropDown = ttk.Combobox(paymentFrame, state = "readonly", values = ["Select the expiration month", "01", "02", "03", "04", "05", "06", "07", "08",
                                                                "09", "10", "11", "12"]) # Drop down selection of expiration month
        expMonthDropDown.grid(row = 4, column = 0) # Position of expiration month drop down
        expMonthValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        expMonthValidMsg.grid(row = 5, column = 0) # Position of validation error message

        # Expiration year
        expYearLabel = tk.Label(paymentFrame, text = "Expiration Year:") # Label for expiration year drop down
        expYearLabel.grid(row = 3, column = 1) # Position of expiration year drop down
        expYearDropDown = ttk.Combobox(paymentFrame, state = "readonly", values = ["Select the expiration year", "2024", "2025", "2026",
                                                               "2027", "2028", "2029"]) # Drop down selection of expiration year
        expYearDropDown.grid(row = 4, column = 1) # Position of expiration year drop down
        expYearValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation error message
        expYearValidMsg.grid(row = 5, column = 1) # Position of validation error message

        # CVV / CVN
        cvvLabel = tk.Label(paymentFrame, text = "CVV / CVN:") # Label for CVV / CVN entry
        cvvLabel.grid(row = 3, column = 2) # Position of CVV / CVN entry label
        cvvEntry = tk.Entry(paymentFrame) # Creates entry box for user input of CVV / CVN
        cvvEntry.grid(row = 4, column = 2) # Position of CVV / CVN entry box
        cvvValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation message
        cvvValidMsg.grid(row = 5, column = 2) # Position of validation error message

        for widget in paymentFrame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5) # Applies padding to all widgets in paymentFrame


        contactFrame = tk.LabelFrame(frame, text = "Contact Information") # Creates the contact information frame
        contactFrame.grid(row = 2, column = 0, padx = 20, pady = 20) # Position of the contact information frame

        # Phone number
        phoneLabel = tk.Label(contactFrame, text = "Phone Number:") # Label for phone number entry
        phoneLabel.grid(row = 0, column = 0) # Position of phone number entry label
        phoneEntry = tk.Entry(contactFrame) # Creates entry box for user input of phone number
        phoneEntry.grid(row = 1, column = 0) # Position of phone number entry box
        phoneValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation message
        phoneValidMsg.grid(row = 2, column = 0) # Position of validation error message

        # Email
        emailLabel = tk.Label(contactFrame, text = "E-mail Address:") # Label for e-mail entry
        emailLabel.grid(row = 0, column = 1) # Position of e-mail entry label
        emailEntry = tk.Entry(contactFrame) # Creates entry box for user input of e-mail
        emailEntry.grid(row = 1, column = 1) # Position of e-mail entry box
        emailValidMsg = tk.Label(paymentFrame, text = "", fg = "red") # Empty label intended to display a validation message
        emailValidMsg.grid(row = 2, column = 1) # Position of validation error message

        # Optional checks
        phonePromoCheck = tk.Checkbutton(contactFrame, text = "Keep me updated through SMS") # Check button to opt-in to promotional text messages
        phonePromoCheck.grid(row = 0, column = 2) # Position of SMS promo check button
        
        emailPromoCheck = tk.Checkbutton(contactFrame, text = "Keep me updated through e-mail") # Check button to opt-in to promotional e-mails
        emailPromoCheck.grid(row = 1, column = 2) # Position of e-mail promo check button

        for widget in contactFrame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5) # Applies padding to all widgets in contactFrame
        
        summaryFrame = tk.LabelFrame(frame, text = "Summary") # Creates the summary frame
        summaryFrame.grid(row = 3, column = 0) # Position of the summary frame within the main frame
        summaryButton = tk.Button(summaryFrame, text = "View Order Summary", command = self.openTotalWindow).pack() # Creates a button to view the order summary, validates input
        summaryButton.grid(row = 0, column = 0) # Position of the button
        

        for widget in summaryFrame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5) # Applies padding to all widgets in summaryFrame

    def openTotalWindow(self):
        """Opens the window to display the total."""
        win = TotalWindow(self) # Names the new window

class TotalWindow(tk.Toplevel):
    def __init__(self, purchasing_clothing):
        window = Tk() # Creates the new window
        window.title("Total") # Titles the new window
        frame = tk.Frame(window) # Creates the parent frame
        frame.pack() # Positions the parent frame

# Run the application
if __name__ == "__main__":
    PurchasingClothing().mainloop()
