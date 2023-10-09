# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

def mi_funcion():
    print("Función creada por programador/a.")

# Create the menu
menu = ConsoleMenu("Title", "Subtitle", clear_screen=False)

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input: "])

# A FunctionItem_2 runs a Python function developed by the programmer when selected
function_item_2 = FunctionItem("Call a Programmer function", mi_funcion)

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "dir")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(function_item_2)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()