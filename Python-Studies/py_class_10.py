# Nov 4, 2024.

# Working with recursive functions! First project in a few weeks, after I went through a pretty big burnout from actual coding.
# Happens to the best of us. Most importantly, I think I understood why it happened and how to deal with it, too. So y'all can 
# bet I'll continue to come back stronger than ever, over and over again!

def list_sum(chosenList):
    if len(chosenList) == 1:
        return chosenList[0]
    else:
        return chosenList[0] + list_sum(chosenList[1::])
    
    
yourList = []

for i in range(1, 6):
    yourNumber = float(input(f"({i}/5) Choose a number to be added to your list: "))
    yourList.append(yourNumber)
    
print(list_sum(yourList))