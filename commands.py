"""Helper Module defining command & utility functions

This module defines each function called on when the user enters any
one of the valid commands, as determined by the main script, as well as
a few utility functions.

It also contains a few string constants like 'PREFIX_IN' to use with any 
messages or prompts.

Attributes:
	PREFIX_IN: a string constant for input prompt
	PREFIX_MSG: a string constant for returning msgs from script
	PREFIX_ERROR: a string constant for displaying important error msgs

Functions:
	addItem: Prompts user to add a new auction item to 'items' dict
	remItem: Removes entered item from 'items' dict
	addBid: Prompts user to add a new auction bidder to 'bidder' dict
	remBid: Removes entered bidder from 'bidder' dict
	eItem: Not yet implemented
	eBid: Not yet implemented
	sDict: Saves 'items' AND/OR 'bidders' dicts to persistent file
	lDict: Loads 'items' AND/OR 'bidders' dicts from persistent file
	cDict: Clears 'items' AND/OR 'bidders' dicts of all data in memory
	dItem: Not yet implemented
	dBid: Not yet implemented
	pItem: Not yet implemented
	pBid: Not yet implemented
	rec: Prints reciept for entered bidder
	sold: Records item bought by a bidder, along with purchased price
	loadXL: Loads 'items' dict data from local XL file
	totalAmt: Displays total profit of auction

ToDo:
""" 

import openpyxl as xl
from escpos import escpos, printer
import json
from datetime import date
from itemclass import Item
from bidderclass import Bidder


# Input prefix constants
PREFIX_IN = ")> "
PREFIX_MSG = ")* "
PREFIX_ERROR = "(!) ERROR (!)"


# Try initializing printer object & set a null object to disable
# all printer functions if printer is not properly initialized
try:
	p = printer.Usb(0x04b8, 0x0e28)
	p.text("\n\n\nInitialized\n\n")
	p.cut()

except:
	print(PREFIX_ERROR, """
USB Printer Not Found!
	--Continuing execution, printer functions are disabled--

	Printer is either disconnected or unique id is not defined.
	Restart program with printer connected to resume normal operation.
		""")

	p = None


def canUse(usr_in, val):
	"""A function used throughout to ensure that when the user inputs
	a command, their input can be used as the desired type and converts
	their input according to the set parameter type of 'val'"""

	try:
		return val(usr_in)

	except ValueError:
		print(PREFIX_MSG + "Error: Invalid Command Value")
		return False


def pack(dict_in):
	"""Returns a single dict used to store 'items' or 'bidders' in json
	
	Arguments:
		- dict_in

	Converts dict_in, a dictionary full of objects, into a dictionary
	full of lists. Uses the instance method exp() to get a list representation of all its
	fields so that it can be stored as a dictionary of lists in json."""

	packed_dict = {}

	if len(dict_in) == 0:
		return dict_in

	else:
		for obj in dict_in:
			packed_list.append(obj.exp())

		return packed_list



def unpackItems(list_in):
	"""Returns the useable 'items' list of objects"""
	pass
	"""
	items_list = []

	if len(list_in) == 0:
		return list_in

	else:
		for element in list_in:
			items_list.append(Item(data_in=element))

		return items_list
	"""

def unpackBidders(list_in):
	"""Returns the useable 'bidders' list of objects"""
	pass

	


def addItem(items):
	""""""

	print(PREFIX_MSG + "Not yet implemented")
	pass 
	"""
	# Create entry # ID and nested dictionary
	entry = num_items + 1

	# Set item desc
	print("\nEnter a short desc:")
	desc = input(PREFIX_IN)

	# Set item value
	print("\nEnter value:")
	loop = True
	value = 0.0
	while loop:
		try:
			value = float(input(PREFIX_IN))
			loop = False

		except ValueError:
			print("\n" + PREFIX_MSG + "Invalid value, please try again:")

	print("\nEnter donator's First & Last name:")
	donator = input(PREFIX_IN)
	
	# Build nested dictionary
	items[entry] = dict([("desc", desc), ("value", value),
							("donator", donator), ("price", 0.0)])
	temp_dict = items[entry]

	# Display item info after creation
	print("\n" + PREFIX_MSG + "Added item #" + entry)
	print("Item desc: " + temp_dict["desc"])
	print("Item value: " + str(temp_dict["value"]))
	print("Donator: " + temp_dict["donator"])

	return
	"""

def remItem(items, usr_args):
	# Remove item entry and data from main 'items' dict

	usr_in = canUse(usr_args[1], val=int)
	if not usr_in:
		return

	try:
		del items[str(usr_in)]

	except KeyError:
		print(PREFIX_MSG + "Error: Invalid item #")
		return

	print(PREFIX_MSG + "Item entry deleted")


def addBid(bidders):
	# Create new bidder entry
	print("\nEnter bidder #:")
	entry_num = input(PREFIX_IN)

	print("\nEnter First & Last Name:")
	name = input(PREFIX_IN)

	# Create nested dict
	bidders[entry_num] = Bidder()
	bidders[entry_num].id = entry_num
	bidders[entry_num].name = name

	return


def remBid(bidders, usr_args):
	# Remove bidder entry and data from main 'bidders' dict
	usr_in = canUse(usr_args[1], val=int)
	if not usr_in:
		return

	try:
		del bidders[str(usr_in)]

	except KeyError:
		print(PREFIX_MSG + "Error: Invalid bidder #")
		return

	print(PREFIX_MSG + "Bidder entry deleted.")


def eItem():
	print(PREFIX_MSG + "Not yet implemented")
	pass


def eBid():
	print(PREFIX_MSG + "Not yet implemented")
	pass


def sDict(items, bidders, usr_args):
	# If user added 'i' option, save items dict into json
	if "i" in usr_args:
		print(PREFIX_MSG + "Saving Items...")
		with open("items.txt", "w", encoding="utf-8") as f:
			json.dump(items, f)

		print(PREFIX_MSG + "Finished")

	# If user added 'b' option, save bidders dict into json
	if "b" in usr_args:
		print(PREFIX_MSG + "Saving Bidders...")
		with open("bidders.txt", "w", encoding="utf-8") as f:
			json.dump(bidders, f)

		print(PREFIX_MSG + "Finished")

	return


def lDict(items, bidders, usr_args):
	# If user added 'i' option, load items dict from json
	if "i" in usr_args:
		print(PREFIX_MSG + "Loading items...")
		with open("items.txt", "r", encoding="utf-8") as f:
			items = json.load(f)

		print(PREFIX_MSG + "Finished")

	# If user added 'b' option, load bidders dict from json
	if "b" in usr_args:
		print(PREFIX_MSG + "Loading bidders...")
		with open("bidders.txt", "r", encoding="utf-8") as f:
			bidders = json.load(f)

		print(PREFIX_MSG + "Finished")

	return
			

def cDict(items, bidders, usr_args):
	# If user added 'i' option, empty the items dict
	if "i" in usr_args:
		print(PREFIX_MSG + "Clearing Items...")
		items.clear()
		print(PREFIX_MSG + "Finished")

	# If user added 'b' option, empty the bidders dict
	if "b" in usr_args:
		print(PREFIX_MSG + "Clearing Bidders...")
		bidders.clear()
		print(PREFIX_MSG + "Finished")

	return


def dItem():
	print(PREFIX_MSG + "Not yet implemented")
	pass


def dBid():
	print(PREFIX_MSG + "Not yet implemented")
	pass


def pItem():
	print(PREFIX_MSG + "Not yet implemented")
	pass


def pBid():
	print(PREFIX_MSG + "Not yet implemented")
	pass


def rec(items, bidders, usr_args):
	# Check if printer has been properly initialized
	if p == None:
		print(PREFIX_MSG + "Printer functions disabled.")
		return

	# Create temp dict ref for nested dict at 'entry'
	tmp_bidder = bidders[usr_args[1]]

	# Total up item prices and values
	total_price = 0.0
	total_val = 0.0
	for entry in tmp_bidder["items"]:
		tmp_item = items[entry]
		total_price += tmp_item["price"]
		total_val += tmp_item["value"]

	# Series of text strings to create receipt format
	p.set(align="center", width=2, height=2)
	p.text("--Mission Hill Auction--")

	p.set(width=1, height=1)
	p.text("\n\nBidder #: " + usr_args[1])
	p.text("\n" + tmp_bidder["name"])

	p.text("\n\nItems\n----------")
	for entry in tmp_bidder["items"]:
		tmp_item = items[entry]
		p.text("\n\n#{:<4} {:<16} {:>20.2f}".format(entry, tmp_item["desc"], tmp_item["price"]))

	p.text("\n\n-{:<20} {:>20.2f}".format("Total", total_price))
	p.text("\n\n\nTax Credit: {:.2f}\n---------------\n{}".format(total_price - total_val, date.today()))
	p.cut()

	return


def sold(items, bidders, usr_args):
	# Quickly add item entry to list of items bought for bidder
	# and set bought price in respective item entry
	try:
		tmp_items = items[usr_args[1]]
		tmp_bidders = bidders[usr_args[2]]
	except (IndexError, KeyError):
		print(PREFIX_MSG + "Error :Invalid Entry")
		return

	try:
		tmp_items["price"] = float(usr_args[3])

	except:
		print(PREFIX_MSG + "Invalid Price")
		tmp_items["price"] = 0.0

	items_bought = tmp_bidders["items"]
	items_bought.append(usr_args[1])

	return


def loadXL(items):
	# Create workbook object and select worksheet
	wb = xl.load_workbook("Missions Auction Donations.xlsx")
	ws = wb["Items and Donators"]

	# Iterate thru each row and create a nested dict for each entry
	for row in ws.iter_rows(min_row=2, max_row=153,
							max_col=5, values_only=True):

		if row[1] is None:
			desc = ""
		else:
			desc = row[1]

		if row[2] is None:
			value = "0.01"

		else:
			value = row[2]

		if row[3] == None or row[4] == None:
			donator = ""

		else:
			donator = str(row[3]) + " " + str(row[4])

		items[str(int(row[0]))] = dict([("desc", desc), ("value", value),
									("donator", donator), ("price", 0.0)])

	return


def totalAmt(items, bidders):
	total = 0.0

	for key, value in items.items():
		total += value["price"]
		
	print("\n{}Total Amount Payed: {:.2f}".format(PREFIX_MSG, total))

	return

