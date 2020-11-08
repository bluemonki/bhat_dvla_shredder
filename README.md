# bhat_dvla_shredder -- BH Active Trace DVLA data shredder

Based on the data from the DVLA taken from here: https://drive.google.com/drive/folders/1XUJVz5UfdG7m0XDxp5EdSt2FeGik1H_G?usp=sharing

Thanks to Scott Urban (@urban_turbo) https://twitter.com/Urban_Turbo/status/1324744625026928640

So far doesn't do too much, basically builds a smaller CSV of the Poole area with population of over 18s with cars, spits it out as a CSV and I drew a graph in open office with it.

Things that need improvement:
* Understand LSOAN to Postcode relationship -- or make a lookup
* Look at more of the keys to understand the data
* Make it more generic so anyone from anywhere could use it
* Make the graphs without going via CSV + Excel/Open Office
* Add some super nerdy stats stuff into it!
