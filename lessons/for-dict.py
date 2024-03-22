"""Practice with Dictionaries and for loops."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
# print out the keys tha have True values
# in_stock[key] is going to be True, False, True
    value: bool = in_stock[key]
    if in_stock[key] is True: #can just be in_stock[key] 
        print(key)