import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [
             Item(name="Cobol programming book", sell_in=10, quality=20),
             Item(name="Old cheese", sell_in=2, quality=0),
             Item(name="Fake moustache", sell_in=5, quality=7),
             Item(name="Collector Lego brick", sell_in=0, quality=80),
             Item(name="Collector Lego brick", sell_in=-1, quality=80),
             Item(name="Concert tickets", sell_in=15, quality=20),
             Item(name="Concert tickets", sell_in=10, quality=49),
             Item(name="Concert tickets", sell_in=5, quality=49),
             Item(name="Fashionable hipster pants", sell_in=3, quality=6),  # <-- :O
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

if __name__ == '__main__':
    unittest.main()
