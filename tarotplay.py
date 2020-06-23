'''
Author: thelotech
Last Edited: 06/23/2020
Summary: Creating a Tarot Card program with the following pulls:
- Card of the Day
- Three Card Pull
- Card Description 
'''

# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
# # 										  # # 
# #  ACE'S SUPER AWESOME TAROT CARD PROGRAM   # # 
# # 										  # #
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #

# Importing the 'random' module we will need for drawing a random card.
import random

# # # # # # # # # # # # # # 
# CREATING THE TAROT DECK #
# # # # # # # # # # # # # # 

# Major Arcana created by adding the list items:
# ----------------------------------------------
majorArcana = [
    '0 - The Fool',
    'I - The Magician',
    'II - The High Priestess',
    'III - The Empress',
    'IV - The Emperor',
    'V - The Hierophant',
    'VI - The Lovers',
    'VII - The Chariot',
    'VIII - Strength',
    'IX - The Hermit',
    'X - Wheel of Fortune',
    'XI - Justice',
    'XII - The Hanged Man',
    'XIII - Death',
    'XIV - Temperance',
    'XV - The Devil',
    'XVI - The Tower',
    'XVII - The Star',
    'XVIII - The Moon',
    'XIX - The Sun',
    'XX - Judgement',
    'XXI - The World']


# Minor Arcana list created by making two lists, then generating 
# a list of all possible combinations to make the deck.
# ---------------------------------------------------------------
minorArcanaNumber = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Knight', 'Queen', 'King']
minorArcanaSuit = ['Cups', 'Pentacles', 'Swords', 'Wands']
minorArcana = []

for cardNumber in range(len(minorArcanaNumber)):
    for cardSuit in range(len(minorArcanaSuit)):
        minorArcana.append(f'{minorArcanaNumber[cardNumber]} of {minorArcanaSuit[cardSuit]}')


# Creating the entire deck by merging the Major/Minor Arcana lists:
# -----------------------------------------------------------------
tarotDeck = minorArcana + majorArcana


# # # # # # # # # # # # # # # # # # #  
# DRAWING CARDS FROM THE TAROT DECK #
# # # # # # # # # # # # # # # # # # # 

# Drawing a random card from the deck
# ------------------------------------
input('Hit ENTER to draw a Tarot Card!')
print(' ')
print('Your Card of the Day is the',random.choice(tarotDeck),'!')
print(' ')
print(' ')

