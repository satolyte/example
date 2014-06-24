CS51 Final Project Write-up: Spell Check

Molly Yang, Jose Castillo, Shannon Lytle, Alex Chen

Instructions for running code:

Initial: If the file trie.pkl doesn’t exist, run ./scrape.py to build the initial dictionary.

Autocorrect: 
./acorrect.py “string to correct”
Function searches trie dictionary for words within specified Levenshtein distance (2) and returns the most probable option using Bayes’ theorem. 

Autocomplete:
./acomplete.py “string to complete”
Searches trie dictionary for other prefixes within specified Levenshtein distance (1) and returns the most probable descendant using Bayes’ theorem.

Autocomplete interactive:
./interface.py
Type in the first Entry box. As you type, suggestions should appear and update in the bottom Entry box. After words are completed, i.e. space bar is hit, the bottom box should reflect words that have already been entered and change focus to the newest prefix in the user query. 

Add words to dictionary:
./add.py “string to add”
This function loads the current dictionary from the pickle, modifies it, deletes the old pickle, and creates a new pickle. 

