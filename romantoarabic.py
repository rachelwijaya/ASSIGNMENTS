Roman_Arab = {
    "I": "1",
    "II": "2",
    "III": "3",
    "IV": "4",
    "V": "5",
    "VI": "6",
    "VII": "7",
    "VIII": "8",
    "IX": "9",
    "X": "10",
    "XI": "11",
    "XII": "12",
    "XIII": "13",
    "XIV": "14",
    "XV": "15",
    "XVI": "16",
    "XVII": "17",
    "XVIII": "18",
    "XIX": "19",
    "XX": "20",
        }

Arab_Roman = {
        "1": "I",
        "2": "II",
        "3": "III",
        "4": "IV",
        "5": "V",
        "6": "VI",
        "7": "VII",
        "8": "VII",
        "9": "IX",
        "10": "X",
        "11": "XI",
        "12": "XII",
        "13": "XIII",
        "14": "XIV",
        "15": "XV",
        "16": "XVI",
        "17": "XVII",
        "18": "XVIII",
        "19": "XIX",
        "20": "XX",
          }

def roman_to_arabic(n):
    if n.upper() in Roman_Arab:
        print(Roman_Arab[str(n)])

def arabic_to_roman(n):
    if str(n) in Arab_Roman:
        print(Arab_Roman[n])
        
def main():
    n = str(input("Enter number either in Roman or Arabic: "))
    if (n in Arab_Roman):
        Arab_Roman(n)
    elif (n in Roman_Arab):
        Roman_Arab(n)
    else:
        ("Please try again.")
        
main()


    
    