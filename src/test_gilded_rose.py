import unittest

from gilded_rose import Item, GildedRose, MAX_QUALITY

class GildedRoseTest(unittest.TestCase):
    def test_old_cheese_raises_in_quality_over_time(self):
        cheese = Item(name="Old cheese", sell_in=2, quality=0)
        gilded_rose = GildedRose([cheese])
        
        gilded_rose.update_quality()

        self.assertEquals(1, cheese.quality)

    def test_quality_never_exceeds_the_max_quality(self):
        cheese = Item(name="Old cheese", sell_in=2, quality=MAX_QUALITY)
        gilded_rose = GildedRose([cheese])
        
        gilded_rose.update_quality()
        
        self.assertEquals(MAX_QUALITY, cheese.quality)

    def test_quality_cannot_be_more_than_the_max_quality_to_begin_with(self):
        self.assertRaises(Exception, lambda: Item(name="Old shoe", sell_in=2, quality=MAX_QUALITY + 1))

    def test_quality_can_be_more_than_max_quality_for_collector_items(self):
        collector_item = Item(name="Collector old shoe", sell_in=2, quality=MAX_QUALITY + 1)

        self.assertEquals(MAX_QUALITY + 1, collector_item.quality)

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
             # Item(name="Fashionable hipster pants", sell_in=3, quality=6),  # <-- :O
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[1].quality)

if __name__ == '__main__':
    unittest.main()
