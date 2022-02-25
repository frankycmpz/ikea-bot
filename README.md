# ikea_bot / @ikeaprodbot
A Python script that tweets a random Ikea product, or in other words, a pseudo-random product button. Uses Tweepy and Beautiful Soup 4. 

So I used to work at Ikea as a cashier. I was in the mood to make a new bot, and after seeing how busy weekends were at Ikea, I decided this was going to be the next idea.

This bot was actually the most difficult bot I've had to make.
1. First, there is no official "random product button" on Ikea's website. If that existed, this project would have been significantly easier. That means I had to make one.
2. Creating a random product generator requires a database. Again, Ikea does not publicly give that out. That means I had to generate my own database of Ikea products.
3. This resulted in having to use Beautiful Soup to parse through Ikea's website. 
