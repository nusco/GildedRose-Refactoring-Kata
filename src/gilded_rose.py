MIN_QUALITY = 0
MAX_QUALITY = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_quality_for(item)

    def update_quality_for(self, item):
        if item.name == "Old cheese":
            if item.quality < MAX_QUALITY:
                item.quality = item.quality + 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0: 
                if item.quality < MAX_QUALITY:
                    item.quality = item.quality + 1
            return    
        
        elif item.name == "Concert tickets":
            if item.quality < MAX_QUALITY:
                item.quality = item.quality + 1
                self.increment_quality_for_concert_tickets(item)
        else:
            if item.quality > 0:
                if item.name != "Collector Lego brick":
                    item.quality = item.quality - 1

        if item.name != "Collector Lego brick":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Concert tickets":
                if item.quality > 0:
                    if item.name != "Collector Lego brick":
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        
    def increment_quality_for_concert_tickets(self, item):
        if item.sell_in < 11:
            if item.quality < MAX_QUALITY:
                item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < MAX_QUALITY:
                item.quality = item.quality + 1
    
class Item:
    def __init__(self, name, sell_in, quality):
        if quality > MAX_QUALITY and not name.startswith("Collector"):
            raise Exception("Too much quality!")
        if quality < MIN_QUALITY:
            raise Exception("Not enough quality!")
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
