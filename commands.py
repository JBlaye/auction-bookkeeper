"""
Desc:
	Helper module containing the majority of function definitions used
	by the main program: auction_bookkeeper.py. This is to help with
	code oraganization and readability.
"""

import openpyxl as xl
from escpos import escpos, printer
import json
from datetime import date

p = printer.Usb(0x04b8, 0x0e28)
p.text("\n\n\nInitialized\n\n")
p.cut()

# Input prefix constants
PREFIX_IN = ")> "
PREFIX_MSG = ")* "

def addItem(items):
	"""
	"""
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
	del items[usr_args[1]]
	print(PREFIX_MSG + "Item entry deleted")


def addBid(bidders):
	# Create new bidder entry
	print("\nEnter bidder #:")
	entry = input(PREFIX_IN)

	print("\nEnter First & Last Name:")
	name = input(PREFIX_IN)

	print("\nEnter Phone #:")
	phone = input(PREFIX_IN)

	# Create nested dict
	bidders[entry] = dict([("name", name), ("phone", phone), ("items", [])])

	return


def remBid(bidders, usr_args):
	# Remove bidder entry and data from main 'bidders' dict
	del bidders[usr_args[1]]


def eItem():
	pass


def eBid():
	pass


def sDict(items, bidders, usr_args):
	# If user added 'i' option, save items dict into json
	if "i" in usr_args:
		print(PREFIX_MSG + "Saving items...")
		with open("items.txt", "w", encoding="utf-8") as f:
			json.dump(items, f)

		print(PREFIX_MSG + "Finished")

	# If user added 'b' option, save bidders dict into json
	if "b" in usr_args:
		print(PREFIX_MSG + "Saving bidders...")
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
		items.clear()

	# If user added 'b' option, empty the bidders dict
	if "b" in usr_args:
		bidders.clear()

	return


def dItem():
	pass


def dBid():
	pass


def pItem():
	pass


def pBid():
	pass


def rec(items, bidders, usr_args):
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
		print(PREFIX_MSG + "Invalid Format")
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
	wb = xl.load_workbook("Missions Auction Donations - 9.23.23.xlsx")
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

