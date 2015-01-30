import unittest

from gilded_rose import *

class GildedRoseTest(unittest.TestCase):
    def test_quality_never_falls_below_zero(self):
        item = Item(name="Dirty sock", sell_in=2, quality=MIN_QUALITY)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(MIN_QUALITY, item.quality)

    def test_old_cheese_raises_in_quality_over_time(self):
        cheese = Item(name="Old cheese", sell_in=2, quality=0)
        gilded_rose = GildedRose([cheese])
        
        gilded_rose.update_quality()

        self.assertEquals(1, cheese.quality)

    def test_sellin_decreases_over_time(self):
        item = Item(name="Old car", sell_in=2, quality=22)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(1, item.sell_in)

    def test_quality_decreases_twice_as_fast_after_sell_in(self):
        item = Item(name="Old car", sell_in=0, quality=22)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()

        self.assertEquals(20, item.quality)

    def test_quality_never_exceeds_the_max_quality(self):
        item = Item(name="Old cheese", sell_in=2, quality=MAX_QUALITY)
        gilded_rose = GildedRose([item])
        
        gilded_rose.update_quality()
        
        self.assertEquals(MAX_QUALITY, item.quality)

    def test_quality_cannot_be_more_than_the_max_quality_to_begin_with(self):
        self.assertRaises(Exception, lambda: Item(name="Old shoe", sell_in=2, quality=MAX_QUALITY + 1))

    def test_quality_cannot_be_less_than_the_min_quality_to_begin_with(self):
        self.assertRaises(Exception, lambda: Item(name="Smelly dog", sell_in=2, quality=MIN_QUALITY - 1))

    def test_quality_can_be_more_than_max_quality_for_collector_items(self):
        collector_item = Item(name="Collector old shoe", sell_in=2, quality=MAX_QUALITY + 1)

        self.assertEquals(MAX_QUALITY + 1, collector_item.quality)

    def test_quality_does_not_degrade_for_collector_items(self):
        collector_item = Item(name="Collector Lego brick", sell_in=2, quality=20)
        gilded_rose = GildedRose([collector_item])
        
        gilded_rose.update_quality()

        self.assertEquals(20, collector_item.quality)

 #            Item(name="Cobol programming book", sell_in=10, quality=20),
 #            Item(name="Fake moustache", sell_in=5, quality=7),
 #            Item(name="Collector Lego brick", sell_in=0, quality=80),
 #            Item(name="Collector Lego brick", sell_in=-1, quality=80),
 #            Item(name="Concert tickets", sell_in=15, quality=20),
 #            Item(name="Concert tickets", sell_in=10, quality=49),
 #            Item(name="Concert tickets", sell_in=5, quality=49),
             # Item(name="Fashionable hipster pants", sell_in=3, quality=6),  # <-- :O

if __name__ == '__main__':
    unittest.main()
