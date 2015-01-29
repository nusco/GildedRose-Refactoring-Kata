## Gilded Rose Specifications

Welcome to the Gilded Rose thrift shop! We buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in quality as they approach their sell-in date, so we have a software program that keeps track of that. The developer who built the system has left to open a bar in Ibiza, and the maintenance work has been passed on to you.

Here are the rules of our system:

* Items have a *SellIn* value, which is the number of days we have left to sell the item.
* Items have a *Quality* value, which tells you how valuable the item is.
* At the end of each day, our system lowers both values for each item.
* Once the *SellIn* date has passed, *Quality* degrades twice as fast.
* The *Quality* of an item is never negative.
* ***Old cheese*** actually increases in *Quality* as it gets older.
* The *Quality* of an item is never more than 50, except for ***Collector*** items.
* ***Collector*** items have no SellIn and never decrease in Quality.
* ***Concert tickets***, like cheese, increase in *Quality* as their *SellIn* value approaches zero. Their *Quality* increases by 2 when there are 10 days or less, and by 3 when there are 5 days or less. However, their *Quality* drops to 0 after the concert.

We also started selling need fancy fashionable items, so we need to add a **new feature** to the system:

* ***Fashionable*** items degrade in *Quality* twice as fast as normal items.

Feel free to make any changes to the *UpdateQuality()* method and to add new code, as long as everything still works correctly.
