"""
Name: auction_bookkeeper.py
Creation: 2023-09-21
Author: Joshua Blaye

Dependenices:
- pyusb
- openpyxl
- python-escpos

Desc:
	A basic program to handle the 'book keeping' of a simple auction.

	Creates two main, multi-dimensional dictionaries - 'items' & 'bidders'
	to organize all the necessary information. The main loop creates
	a simple 'cli' with a list of commands to access and manipulate
	the dictionaries in various ways.

	The operator can enter commands to load data, save data, dynamically
	add or remove bidders and items, display information about bidders and
	items, and print receipts for bidders at any time.

	ToDo: (In descending order of priority)
	- Re-write bidder & item data structures as one-dimensional lists of
		objects to improve organization, readability, & referencing
	- Find better module/api for interaction with reciept printer
	- Create better ui for program - formatted cli or gui?

"""

import json
import commands as cds

# Init Dicts
items = {}
bidders = {}

# Populate dicts with data from persistent json & create empty files
# if either does not already exist
try:
	with open("items.txt", "r", encoding="utf-8") as f:
		items = json.load(f)
except:
	print("{}'Items' File Not Found - Creating empty file".format(
		cds.PREFIX_MSG))
	with open("items.txt", "x", encoding="utf-8"):
		pass


try:
	with open("bidders.txt", "r", encoding="utf-8") as f:
		bidders = json.load(f)
except:
	print("{}'Bidders' File Not Found - Creating empty file".format(
		cds.PREFIX_MSG))
	with open("bidders.txt", "x", encoding="utf-8"):
		pass


# Init Possible command inputs tuple
cds_list = ("exit", "help", "additem", "remitem", "addbid", "rembid",
			"eitem", "ebid", "sdict", "ldict", "cdict", "ditem", "dbid",
			"pitem", "pbid", "rec", "sold", "loadxl", "total")

# Display help function, displays available commands with some help text
def display_help():
	print("""
Available Commands: (Note: not case sensitive)
exit - Exits the program

help - Displays this message

addItem - Prompts user to add item entry

remItem - Deletes item entry, requires item #

addBid - Prompts user to add Bidder entry

remBid - Deletes bidder entry, requires bidder #

eItem - Allows user to edit details of an item entry
	format:

eBid - Allows user to edit details of a bidder entry
	format:

sDict - Saves current items and/or bidders to respective files
	format: sDict 'dict-letter' 'dict-letter'
	enter 'i' for 'items' dict AND/OR 'b' for 'bidders' dict

lDict - Loads items and/or bidders from respective files
	format: lDict 'dict-letter' 'dict-letter'
	enter 'i' for 'items' dict AND/OR 'b' for 'bidders' dict

cDict - clear dictionary
	format: cDict 'dict-letter' 'dict-letter'
	enter 'i' for 'items' dict AND/OR 'b' for 'bidders' dict

dItem - Displays information about item entry, requires item #

dBid - Displays information about bidder entry, requies bidder #

pItem - Prints item entry info on a slip of paper, requires item #

pBid - Prints bidder entry info on a slip of paper, requires bidder #

rec - Prints a receipt for a bidder, requires bidder #

sold - Quick method of adding an item to the list of bought items
	for a bidder
	format: sold 'item #' 'bidder #' 'price'

loadXL - Reloads items from a Microsoft Excel file

total - Displays total amount payed by all bidders""")

# Init Main control loop & list of user args - 'usr_in'
main_loop = True
usr_in = []

while main_loop:
	# Get user input and split up into a list to easily access arguments
	usr_in = input("\n)> ").split(" ")

	# First check if command exists as an option, then find
	# corresponding function
	if usr_in[0].lower() not in cds_list:
		print(")* Invalid Command")
		continue

	# Exit command
	elif usr_in[0].lower() == cds_list[0]:
		main_loop = False

	# Help command
	elif usr_in[0].lower() == cds_list[1]:
		display_help()

	# Add Item command
	elif usr_in[0].lower() == cds_list[2]:
		cds.addItem(items)

	# Remove item command
	elif usr_in[0].lower() == cds_list[3]:
		# Check if the user forgot to add args to the command
		if len(usr_in) <= 1:
			print(cds.PREFIX_MSG + "Error: Missing command args")
			continue

		else:
			cds.remItem(items, usr_in)

	# Add bidder command
	elif usr_in[0].lower() == cds_list[4]:
		cds.addBid(bidders)

	# Remove bidder command
	elif usr_in[0].lower() == cds_list[5]:
		# Check if the user forgot to add args to the command
		if len(usr_in) <= 1:
			print(cds.PREFIX_MSG + "Error: Missing command args")
			continue

		else:
			cds.remBid(bidders, usr_in)

	# Edit item command
	elif usr_in[0].lower() == cds_list[6]:
		cds.eItem()

	# Edit bidder command
	elif usr_in[0].lower() == cds_list[7]:
		cds.eBid()

	# Save dictionary command
	elif usr_in[0].lower() == cds_list[8]:
		# Check if the user forgot to add args to the command
		if len(usr_in) <= 1:
			print(cds.PREFIX_MSG + "Error: Missing command args")
			continue

		else:
			cds.sDict(items, bidders, usr_in)

	# Load dictionary command
	elif usr_in[0].lower() == cds_list[9]:
		# Check if the user forgot to add args to the command
		if len(usr_in) <= 1:
			print(cds.PREFIX_MSG + "Error: Missing command args")
			continue

		else:
			cds.lDict(items, bidders, usr_in)

	# Clear dictionary command
	elif usr_in[0].lower() == cds_list[10]:
		# Check if the user forgot to add args to the command
		if len(usr_in) <= 1:
			print(cds.PREFIX_MSG + "Error: Missing command args")
			continue

		else:
			cds.cDict(items, bidders, usr_in)

	# Display item command
	elif usr_in[0].lower() == cds_list[11]:
		cds.dItem()

	# Display bidder command
	elif usr_in[0].lower() == cds_list[12]:
		cds.dBid()

	# Print item command
	elif usr_in[0].lower() == cds_list[13]:
		cds.pItem()

	# Print bidder command
	elif usr_in[0].lower() == cds_list[14]:
		cds.pBid()

	# Reciept print command
	elif usr_in[0].lower() == cds_list[15]:
		cds.rec(items, bidders, usr_in)

	# Item sold command
	elif usr_in[0].lower() == cds_list[16]:
		# Check if the user forgot to add args to the command
		if len(usr_in) <= 3:
			print(cds.PREFIX_MSG + "Error: Missing command args")
			continue

		else:
			cds.sold(items, bidders, usr_in)

	# Load XL document command
	elif usr_in[0].lower() == cds_list[17]:
		cds.loadXL(items)

	# Display total command
	elif usr_in[0].lower() == cds_list[18]:
		cds.totalAmt(items, bidders)

# Save current 'items' & 'bidders' dicts to json before exiting
with open("items.txt", "w", encoding="utf-8") as f:
	json.dump(items, f)

with open("bidders.txt", "w", encoding="utf-8") as f:
	json.dump(bidders, f)

# Exit msg
print("\n)* Program Exited\n")
