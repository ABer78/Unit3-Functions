# The raise syntax
# Basic syntax
"""
raise ExceptionTypeP("Your message!")
Examples:
raise ValueError("Quantity must be at least 1")
raise TypeError("Expected a player object, got a potato")
raise PermissionError("You are not a mod, nice try though")
"""


# Just returning
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    # rest of code . . .


# Raising exception
def open_loot_box(player, qty):
    if qty <= 0:
        return ValueError("Bad qty!")
    # rest of code . . .


VALID_PROTEINS = ["chicken", "steak", "barbacoa", "carnitas"]
VALID_RICE = ["white", "brown", "none"]
VALID_BEANS = ["black", "pinto", "none"]
MAX_FREE_EXTRAS = 3


def build_bowl(protein, rice, extras):
    """Build a Chipotle bowl with validation

    Raises:
    ValueError - if "protein" is invalid
    TypeError - if "extras" is not a list
    """
    # check if "extras" is a list
    if not isinstance(extras, list):
        raise TypeError("Extras must be a list")
    # validate protein
    if protein.lower() not in VALID_PROTEINS:
        raise ValueError(f"'{protein}' isn't valid. Choose from: {VALID_PROTEINS}")
    return {"protein": protein.lower(), "rice": rice, "extras": extras, "price": 10.00}


# Test the function
try:
    bowl = build_bowl("chicken", "brown", "corn")
    print(f"Created: {bowl}")
except Exception as e:
    print(f"Error: {e}")
