
# coding: utf-8

# In[2]:

get_ipython().magic(u'pylab --no-import-all inline')


# In[3]:

import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series, Index
import pandas as pd

from itertools import islice


# In[4]:

import census
import us

import settings


# In[5]:

c = census.Census(key=settings.CENSUS_KEY)


# In[6]:

us.states.STATES[4].fips


# In[7]:

def tracts(variables='NAME'):
    
    for tract in c.sf1.get((variables), {'for': 'tract:*', 'in': 'state:%s county:%s' % (us.states.STATES[4].fips
, '001')}):
        yield tract
        
    
tracts().next()


# In[8]:

#P0010001/Total Pop, P0050004/African-American Not Hispanic, P0050010/Hispanic, 
#P0050006/Asian, not Hispanic P0050003/White, not Hispanic 
o_tracts = [tract for tract in tracts(variables="NAME,P0010001,P0050004,P0050010,P0050006,P0050003")]

#add income!!!!!!

#put list into dataframe
tract_df = pd.DataFrame(o_tracts)




# In[9]:

tract_df['African-American, not Hispanic'] = tract_df['P0050004']
tract_df['White, not Hispanic'] = tract_df['P0050003']
tract_df['Asian, not Hispanic'] = tract_df['P0050006']
tract_df['Total Pop'] = tract_df['P0010001']
tract_df['Hispanic'] = tract_df['P0050010']

#show only columns that have legible names; set index by tract
alameda_tracts_df = tract_df[['NAME','tract','Total Pop','African-American, not Hispanic',           'Asian, not Hispanic', 'Hispanic', 'White, not Hispanic', 'county','state']].set_index(['tract'])

#sort by income


#transpose so tracts are columns 
alameda_tracts_df.transpose().head()


# In[10]:

tract_df.P0010001.astype(int).sum()


# In[11]:

def places(variables="NAME"):
    
    for state in us.states.STATES:
        geo = {'for':'place:*', 'in':'state:{s_fips}'.format(s_fips=us.states.STATES[4].fips)}
        for place in c.sf1.get(variables, geo=geo):
            yield place
   


# In[12]:

ca_places = [place for place in places(variables="NAME,P0010001,P0050004,P0050010,P0050006,P0050003")]

#put list into dataframe
ca_places_df = pd.DataFrame(ca_places)
ca_places_df.head()


# In[13]:

#turn numbers into integers
ca_places_df.P0010001 = ca_places_df.P0010001.astype(int)
ca_places_df.P0050003 = ca_places_df.P0050003.astype(int)
ca_places_df.P0050004 = ca_places_df.P0050004.astype(int)
ca_places_df.P0050006 = ca_places_df.P0050006.astype(int)
ca_places_df.P0050010 = ca_places_df.P0050010.astype(int)

ca_places_df[['NAME','P0010001','P0050003', 'P0050004','P0050006', 'P0050010']].sort('P0010001', ascending=False).head()


# In[14]:

ca_places_df.describe()


# In[15]:

o_towns = ca_places_df[ca_places_df['NAME'].str.startswith('O')]
o_towns.sort('P0010001', ascending=False).head()


# In[16]:

list(islice(tracts(),1))


# In[17]:

# http://api.census.gov/data/2010/sf1?get=P0010001&for=block+group:*&in=state:02+county:170

def block_groups_in_county(variables='NAME,P0010001', state_fips='06', county_fips='001'):
    geo = {'for':'block group:*',
           'in':'state:{s_fips} county:{c_fips}'.format(s_fips=state_fips,
                                                    c_fips=county_fips)}
    for block_group in c.sf1.get(variables, geo=geo):
        yield block_group
        


# In[23]:

from itertools import islice

list(islice(block_groups_in_county(), 5))

#islice takes iterable things (generators, for loops, other iteration)
#put None in place of 10 above


# In[28]:

#list comprehension for grabbing data from above function
bgs = [bg for bg in block_groups_in_county(variables="NAME,P0010001,P0050004")]

#put list into dataframe
bg_df = pd.DataFrame(bgs)
bg_df.set_index(['NAME']).transpose()

#working!

