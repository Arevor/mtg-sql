import sqlite3
import argparse
import os.path


class DeckToCSV:
    def __init__(self):
        conn = sqlite3.connect('AllCards.db')
        conn.text_factory = str  # utf-8
        self.c = conn.cursor()


    def write_carddets(self, filename, cardname):
        """
        All data for given cardname is retrieved and written to csv output
        :param filename: csv to write to
        :param cardname: cardname to retrieve data for
        :return:
        """
        cardname = (cardname,)
        self.c.execute("SELECT * from AllCards where NAME = ?", cardname)
        text_file = open(filename, 'a')
        text_file.write(str(self.c.fetchone())+ '\n')

    def input_decklist(self, filename):
        """
         extracts the cards from a decklist into a list
        :param filename: decklist
        :return: list of cards contained within decklist
        """
        with open(filename) as f:
            content = f.readlines()
            with open(filename) as gg:
                content = gg.read().splitlines()
            content = [i.split(' ')[1::] for i in content]
            formatted_content = []
            for words in content:
                formatted_content.append(' '.join(words))
            print formatted_content
            return formatted_content

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("decklist", help="text file containing decklist")
    parser.add_argument("output_filename", help="csv output filename")
    args = parser.parse_args()

    if not os.path.isfile(args.decklist):
        print 'Decklist not found'
        return 0

    my_deck = DeckToCSV()
    out_lines = my_deck.input_decklist(args.decklist)
    for line in out_lines:
        my_deck.write_carddets(args.output_filename, line)

if __name__ == "__main__":
    main()
