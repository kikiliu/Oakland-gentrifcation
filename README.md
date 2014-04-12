WWOD-project
============

Crime Data Notebook: This data set is a good starting point to our project because it has information with lat/long coordinates, which I will be using to generate census-tracts buckets, and use the same buckets to sort not only the crime data (and aggregate it) but also the housing data managed and cleaned by Kiki. So far I have managed to clean the data, there are more steps in which I aggregate it, and experiment the many possibilities in which I can later on display it. The next step after producing the buckets and aggregating it would be to display it using a Google map, something that I have been working on simultaniously. Also, D3 is another path that I have been looking at. It seems like most of the data we have will make more sense once it is layered and resides within a single map. 

Housing Data Notebooks:
ZillowResearchData Notebook: Populate home value of different neighboods in Oarkland from 1996-04 to 2014-02. The home values are calcualated by Zillow using normalization method. Statistically speakly, its error wouldn't affect the price trends. Also, the foreclosure homes are not considered in this calculation as we use it to show an indication of the market change over time. The foreclosure data are retrieved in another file and would be considered in later stage of this project. (http://nbviewer.ipython.org/gist/kikiliu/10518498) 

ZillowAPI Notebook: At the beginning of this project, I used this notebook to extract property information from Zillow and Trulia APIs. It would return more detailed information given a property like longtitude and latitude. However, it only returns the most updated information not historical. The functions are generic and hopefully could be re-use in extracting demographic data by neighbood. (http://nbviewer.ipython.org/gist/kikiliu/10226757)


Census Data Notebook:
Our progress so far isn't consolidated in one notebook because we are working on the tough issue of integration (neighborhoods, tracts, etc.).

We're linking to 3 starter notebooks (here's mine: http://nbviewer.ipython.org/gist/nyborrobyn/10514381). This contains 2010 race/ethnicity data at the tract, block group, and place levels of the census geog. hierarchy.

Thinking through our data and the problem of finding tracts within the city of Oakland, we think we might have an "easy" workaround once Moshe and I merge our notebooks. He supposedly has crime data for all of Oakland. If we combine the notebooks, we can see which tracts are not represented in his data and hopefully drop those columns from my data.

Moshe pointed out that it's possible we'll lose good data if there's a tract in Oakland which is not represented in the crime data. So that's definitely not foolproof, but one way to eliminate some of the extraneous Alameda County tracts outside of Oakland.

We also talked through the racial categories. Seems like it might make sense to consider the white community = white, non-Hispanic + white, Hispanic, the Black community = Black, non-Hispanic + Black, and so forth. This will probably be controversial, but I don't want to NOT count people just because they're in multiple communities.

Considering income, looks like that is collected on the SF3 form, so I need to figure out how to do census calls on that data. There is documentation for 2000 but I don't see any for 2010...will have to look further into that.
