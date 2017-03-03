This is an extension of the [MTG-JSON](https://github.com/mtgjson/mtgjson) project. 

This program was last updated in May 2016 (up to and including BFZ block)

it turns a decklist of this form:

InputDeckList.txt
```
4 Island
4 Snapcaster Mage
4 Polluted Delta
```
into a CSV output with columns of:

```name, manacost, cmc, coloridentity, artist, number, type, text, printings, 
flavor, layout, multiverseid, power, toughness, rarity, subtypes, types```

# Example to run
``` 
$ python mtg-sql.py InputDeckList.txt CSV_Output.csv
```
# Dependencies 
* python 2.7

