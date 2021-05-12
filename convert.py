import re

# Regex containing 4 groups:
# - ([0-9]*): Number of a certain byte unit.
# - (K|k|M|m|G|g|T|t|P|p|E|e|Z|z|Y|y|): Metric prefix of the byte unit.
# - (I|i): Indicates if the unit is a multiple-byte unit.
regex = re.compile(r"^([0-9]*)(K|k|M|m|G|g|T|t|P|p|E|e|Z|z|Y|y|)(i|I)?")

def convert(val, unit, bi):
    ans = int(val)

    if unit != '':
        switcher = {
            "K": 1,
            "k": 1,
            "M": 2,
            "m": 2,
            "G": 3,
            "g": 3,
            "T": 4,
            "t": 4,
            "P": 5,
            "p": 5,
            "E": 6,
            "e": 6,
            "Z": 7,
            "z": 7,
            "Y": 8,
            "y": 8,
        }

        power = switcher.get(unit, -1)
        if power != -1:
            if bi is None:
                ans *= pow(1000, power) 
            else:
                ans *= pow(1024, power)
        
    return ans