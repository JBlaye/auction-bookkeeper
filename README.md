# Auction Book-Keeper

A lightweight script which aims to simplify the organizational back-end, so to speak, and eliminate the need for excessive paperwork of a basic auction. 

### Dependencies
- Python 3.11.x
- openpyxl: https://pypi.org/project/openpyxl/
- python-escpos: https://pypi.org/project/python-escpos/

#### (Note on dependencies)

If installing 'python-escpos' via pip, be sure to specify the 'usb' dependency:

	pip install python-escpos[usb]

While the 'usb' dependency in this reference is indeed an older fork of 'pyusb', it is recommended to use the dependency in which it was built on. 

### Descritpion

A lightwieght script with a rather simplistic cli, designed to allow the user to manage the "book keeping" of a basic auction. 

I built this little tool initially to fill a gap that had formed when the church I work for decided to hold an auction last year. At the time, there was no practical method of keeping track of each bidder, items they bought, or the items themselves. 

So, I created a basic tool to manage all that tomfoolery.

The program consists of two parts:
- Storage/Organization of items & bidders
- Realtime manipulation of either structure

Both items and bidders are stored in memory when operating, but the user can dump the data into a json format for persistence, which the program will auto-load into memory on start if the data files are present. The user can also load the data manually any time they need, either from local files containing the data in json form, or directly from an Excel file. 

During operation, the user can enter various commands to manipulate or view various aspects of either structure. Certain functions also allow the use of a connected ESC/POS printer to print out a basic reciept for the purpose of informing any bidder of their sudden financial decisions. 

### ToDo:
- Rewrite bidder & item structures into one-dimensional lists of objects that track extra details in fields, rather than using 2-3 dimensional dictionaries, which is a huge pain
- Cleanup printer functions or find a better library for printing to usb ESC/POS printers
- Cleanup various messy bits & add a pinch of error handling, not too much tho, gotta keep it lively
- Prettyfi the ui, to be graphical or not to be?
