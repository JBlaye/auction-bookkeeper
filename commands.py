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
	pack: Returns a single dict used to store data in json
	unpack: Returns a useable dict, populated with objects
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
	rec: Prints a reciept for the entered bidder #
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
p = None

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
	"""Returns a single dict used to store data in json

	Arguments:
		- dict_in

	Converts dict_in, a dictionary full of objects, into a dictionary
	full of lists. Uses the instance method exp() to get a list
	representation of all its fields so that it can be stored as a
	dictionary of lists in json."""

	if len(dict_in) == 0:
		return dict_in

	elif len(dict_in) >= 1:
		packed_dict = {}

		for k, obj in dict_in.items():
			packed_dict[k] = obj.exp()

		return packed_dict



def unpack(dict_in, obj):
	"""Returns a useable dict, populated with objects"""
	
	if len(dict_in) == 0:
		return dict_in

	elif len(dict_in) >= 1:
		unpacked_dict = {}

		for k, list_obj in dict_in.items():
			unpacked_dict[k] = obj(data_in=list_obj)

		return unpacked_dict


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
		with open("items.txt", "w", encoding="utf-8") as wf:
			json.dump(pack(items), wf, indent=4)

		print(PREFIX_MSG + "Finished")

	# If user added 'b' option, save bidders dict into json
	if "b" in usr_args:
		print(PREFIX_MSG + "Saving Bidders...")
		with open("bidders.txt", "w", encoding="utf-8") as wf:
			json.dump(pack(bidders), wf, indent=4)

		print(PREFIX_MSG + "Finished")

	return


def lDict(items, bidders, usr_args):
	# If user added 'i' option, load items dict from json
	if "i" in usr_args:
		print(PREFIX_MSG + "Loading items...")
		with open("items.txt", "r", encoding="utf-8") as rf:
			items = unpack(json.load(rf), Item)

		print(PREFIX_MSG + "Finished")

	# If user added 'b' option, load bidders dict from json
	if "b" in usr_args:
		print(PREFIX_MSG + "Loading bidders...")
		with open("bidders.txt", "r", encoding="utf-8") as rf:
			bidders = unpack(json.load(rf), Bidder)

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
	"""Prints a reciept for the entered bidder #"""

	bidder_id = usr_args[1]

	# Check if printer has been properly initialized & if entered bidder
	# is valid
	if p == None:
		print(PREFIX_MSG + "Printer functions disabled.")
		return

	elif bidder_id not in bidders:
		print(PREFIX_MSG + "Error: Invalid bidder ID#")
		return

	# Total up price of each item bought by bidder, also the est-value
	total_price = 0.0
	total_val = 0.0
	for key in bidders[bidder_id].cart:
		total_price += items[key].price
		total_val += items[key].est_val

	# Series of text strings to create receipt format
	p.set(align="center", width=2, height=2)
	p.text("--Mission Hill Auction--")

	p.set(width=1, height=1)
	p.text("\n\nBidder #: " + bidder_id)
	p.text("\n" + bidders[bidder_id].name)

	p.text("\n\nItems\n----------")
	for key in bidders[bidder_id].cart:
		tmp_item = items[key]
		p.text("\n\n#{:<4} {:<16} {:>20.2f}".format(key, tmp_item.desc,
			tmp_item.price))

	p.text("\n\n-{:<20} {:>20.2f}".format("Total", total_price))
	p.text("\n\n\nTax Credit: {:.2f}\n---------------\n{}".format(total_price
		- total_val, date.today()))
	p.cut()

	return


def sold(items, bidders, usr_args):
	"""Add item to bidder 'cart' and set the bid 'price' of the item"""
	
	item_id = usr_args[1]
	bidder_id = usr_args[2]
	sold_price = canUse(usr_args[3], float)

	if not sold_price:
 		return

	elif item_id not in items or bidder_id not in bidders:
		print(PREFIX_MSG + "Error: Invalid item or bidder ID#")
		return

	else:
		items[item_id].price = sold_price
		bidders[bidder_id].cart.append(str(items[item_id].id))


def loadXL(items):
	"""Populate 'items' data structure from entered xl file."""

	print("\nEnter XL Sheet file path: (does not need extension .xlsx)")
	fp = input(PREFIX_IN)

	print("\nEnter Worksheet Name:")
	ws_name = input(PREFIX_IN)

	try:
		wb = xl.load_workbook(fp + ".xlsx")
		ws = wb[ws_name]

	except (xl.utils.exceptions.InvalidFileException, KeyError):
		print(PREFIX_MSG + "Error: Invalid Filename path or worksheet")
		return


	# Iterate thru each row and create a nested dict for each entry
	print(PREFIX_MSG + "Loading items from XL...")
	for row in ws.iter_rows(min_row=2, max_row=200,
							max_col=5, values_only=True):
		posid = None

		if row[0] == None:
			posid = "empty"
		else:
			posid = int(row[0])

		if row[1] is None:
			desc = ""
		else:
			desc = row[1]


		if row[2] is None:
			value = 0.01
		else:
			value = row[2]


		if row[3] == None or row[4] == None:
			donator = ""
		else:
			donator = str(row[3]) + " " + str(row[4])


		items[posid] = Item(posid)
		items[posid].desc = desc
		items[posid].donator = donator
		items[posid].est_val = value

	print(PREFIX_MSG + "Finished")
	return


def totalAmt(items, bidders):
	pass
