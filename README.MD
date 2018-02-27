# D6 Password Generator
One of the ways of generating an approximately random pass phrase is to use a six sided die to generate pass phrases.  Each word in the database is indexed in five digit base-six numbers.  This means that five rolls of a D6 will give you the index of one word.  Thus to generate a five word pass phrase, 25 dice need to e rolled. Python is used to allow for much quicker generation of much longer passphrases. 

Part of the intention of creating passphrases with dice is to keep the password completely off of electronic systems, and this program inherently defeats that purpose.  While I see the point of this level of caution, for most cases this high level of paranoia is unnecessary.

## Use

The pwd_gen.py file creates a SQLite database from a CSV, where the csv columns are as follows:

Base-6 Index          | Word
--------------------- | ------------------------------------


