#!/usr/bin/env python
# coding: utf-8

# **Information Visualization Project** 
# 
# Indian Trade Data

# In[1]:


#IMPORT DEPENDENCIES 
import numpy as np 
import pandas as pd 
import pycountry 
from prettytable import PrettyTable
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from raceplotly.plots import barplot

import warnings
warnings.filterwarnings('ignore')

import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)
import plotly as py


# In[2]:


#Import Data Sets

import_data = pd.read_csv('data/2018-2010_import.csv')
import_data.drop_duplicates(keep="first", inplace=True)

export_data = pd.read_csv('data/2018-2010_export.csv')
export_data.drop_duplicates(keep="first", inplace=True)


# In[3]:


import_data.head()
import_data.describe()


# In[4]:


export_data.head()
export_data.describe()


# In[5]:


#Prep Data for Map Based Visualization
countrydict = {'AFGHANISTAN TIS': 'af', 'ALBANIA': 'al', 'ALGERIA': 'dz', 'AMERI SAMOA': 'us', 'ANDORRA': 'ad', 'ANGOLA': 'ao', 'ANGUILLA': 'ai', 'ANTARTICA': 'aq', 'ANTIGUA': 'ag', 'ARGENTINA': 'ar', 'ARMENIA': 'am', 'ARUBA': 'aw', 'AUSTRALIA': 'au', 'AUSTRIA': 'at', 'AZERBAIJAN': 'az', 'BAHAMAS': 'bs', 'BAHARAIN IS': 'bh', 'BANGLADESH PR': 'bd', 'BARBADOS': 'bb', 'BELARUS': 'by', 'BELGIUM': 'be', 'BELIZE': 'bz', 'BENIN': 'bj', 'BERMUDA': 'bm', 'BHUTAN': 'bt', 'BOLIVIA': 'bo', 'BOSNIA-HRZGOVIN': 'ba', 'BOTSWANA': 'bw', 'BR VIRGN IS': 'vg', 'BRAZIL': 'br', 'BRUNEI': 'bn', 'BULGARIA': 'bg', 'BURKINA FASO': 'bf', 'BURUNDI': 'bi', 'C AFRI REP': 'cf', 'CAMBODIA': 'kh', 'CAMEROON': 'cm', 'CANADA': 'ca', 'CAPE VERDE IS': 'cv', 'CAYMAN IS': 'ky', 'CHAD': 'td', 'CHILE': 'cl', 'CHINA P RP': 'cn', 'CHRISTMAS IS.': 'cx', 'COCOS IS': 'cc', 'COLOMBIA': 'co', 'COMOROS': 'km', 'CONGO D. REP.': 'cd', 'CONGO P REP': 'cg', 'COOK IS': 'ck', 'COSTA RICA': 'cr', 'COTE D\' IVOIRE': 'ci', 'CROATIA': 'hr', 'CUBA': 'cu', 'CYPRUS': 'cy', 'CZECH REPUBLIC': 'cz', 'DENMARK': 'dk', 'DJIBOUTI': 'dj', 'DOMINIC REP': 'do', 'DOMINICA': 'do', 'ECUADOR': 'ec', 'EGYPT A RP': 'eg', 'EL SALVADOR': 'sv', 'EQUTL GUINEA': 'gq', 'ERITREA': 'er', 'ESTONIA': 'ee', 'ETHIOPIA': 'et', 'FALKLAND IS': 'fk', 'FAROE IS.': 'fo', 'FIJI IS': 'fj', 'FINLAND': 'fi', 'FR GUIANA': 'gf', 'FR POLYNESIA': 'fr', 'FR S ANT TR': 'fr', 'FRANCE': 'fr', 'GABON': 'ga', 'GAMBIA': 'gm', 'GEORGIA': 'ge', 'GERMANY': 'de', 'GHANA': 'gh', 'GIBRALTAR': 'gi', 'GREECE': 'gr', 'GREENLAND': 'gl', 'GRENADA': 'gd', 'GUADELOUPE': 'gp', 'GUAM': 'gu', 'GUATEMALA': 'gt', 'GUERNSEY': 'gg', 'GUINEA BISSAU': 'gw', 'GUINEA': 'gn', 'GUYANA': 'gy', 'HAITI': 'ht', 'HEARD MACDONALD': 'hm', 'HONDURAS': 'hn', 'HONG KONG': 'hk', 'HUNGARY': 'hu', 'ICELAND': 'is', 'INDONESIA': 'id', 'IRAN': 'ir', 'IRAQ': 'iq', 'IRELAND': 'ie', 'ISRAEL': 'il', 'ITALY': 'it', 'JAMAICA': 'jm', 'JAPAN': 'jp', 'JERSEY         ': 'je', 'JORDAN': 'jo', 'KAZAKHSTAN': 'kz', 'KENYA': 'ke', 'KIRIBATI REP': 'ki', 'KOREA DP RP': 'kp', 'KOREA RP': 'kr', 'KUWAIT': 'kw', 'KYRGHYZSTAN': 'kg', 'LAO PD RP': 'la', 'LATVIA': 'lv', 'LEBANON': 'lb', 'LESOTHO': 'ls', 'LIBERIA': 'lr', 'LIBYA': 'ly', 'LIECHTENSTEIN': 'li', 'LITHUANIA': 'lt', 'LUXEMBOURG': 'lu', 'MACAO': 'mo', 'MACEDONIA': 'mk', 'MADAGASCAR': 'mg', 'MALAWI': 'mw', 'MALAYSIA': 'my', 'MALDIVES': 'mv', 'MALI': 'ml', 'MALTA': 'mt', 'MARSHALL ISLAND': 'mh', 'MARTINIQUE': 'mq', 'MAURITANIA': 'mr', 'MAURITIUS': 'mu', 'MAYOTTE': 'yt', 'MEXICO': 'mx', 'MICRONESIA': 'fm', 'MOLDOVA': 'md', 'MONACO': 'mc', 'MONGOLIA': 'mn', 'MONTENEGRO': 'me', 'MONTSERRAT': 'ms', 'MOROCCO': 'ma', 'MOZAMBIQUE': 'mz', 'MYANMAR': 'mm', 'N. MARIANA IS.': 'mp', 'NAMIBIA': 'na', 'NAURU RP': 'nr', 'NEPAL': 'np', 'NETHERLAND': 'nl', 'NETHERLANDANTIL': 'nl', 'NEW CALEDONIA': 'cn', 'NEW ZEALAND': 'nz', 'NICARAGUA': 'ni', 'NIGER': 'ne', 'NIGERIA': 'ng', 'NIUE IS': 'nu', 'NORFOLK IS': 'nf', 'NORWAY': 'no', 'OMAN': 'om', 'PACIFIC IS]': 'ot', 'PAKISTAN IR': 'pk', 'PALAU': 'pw', 'PANAMA C Z': 'pa', 'PANAMA REPUBLIC': 'pa', 'PAPUA N GNA': 'pg', 'PARAGUAY': 'py', 'PERU': 'pe', 'PHILIPPINES': 'ph', 'PITCAIRN IS.': 'pn', 'POLAND': 'pi', 'PORTUGAL': 'pt', 'PUERTO RICO': 'pr', 'QATAR': 'qa', 'REUNION': 're', 'ROMANIA': 'ro', 'RUSSIA': 'ru', 'RWANDA': 'rw', 'SAMOA': 'ws', 'SAN MARINO': 'sm', 'SAO TOME': 'st', 'SAUDI ARAB': 'sa', 'SENEGAL': 'sn', 'SERBIA': 'rs', 'SEYCHELLES': 'sc', 'SIERRA LEONE': 'si', 'SINGAPORE': 'sg', 'SLOVAK REP': 'sk', 'SLOVENIA': 'si', 'SOLOMON IS': 'sb', 'SOMALIA': 'so', 'SOUTH AFRICA': 'za', 'SOUTH SUDAN ': 'sd', 'SPAIN': 'es', 'SRI LANKA DSR': 'lk', 'ST HELENA': 'sh', 'ST KITT N A': 'kn', 'ST LUCIA': 'lc', 'ST PIERRE': 'pm', 'ST VINCENT': 'vc', 'STATE OF PALEST': 'ps', 'SUDAN': 'sd', 'SURINAME': 'sr', 'SWAZILAND': 'sz', 'SWEDEN': 'se', 'SWITZERLAND': 'ch', 'SYRIA': 'sy', 'TAIWAN': 'tw', 'TAJIKISTAN': 'tj', 'TANZANIA REP': 'tz', 'THAILAND': 'th', 'TIMOR LESTE': 'tl', 'TOGO': 'tg', 'TOKELAU IS': 'tk', 'TONGA': 'to', 'TRINIDAD': 'tt', 'TUNISIA': 'tn', 'TURKEY': 'tr', 'TURKMENISTAN': 'tm', 'TURKS C IS': 'tr', 'TUVALU': 'tv', 'U ARAB EMTS': 'ae', 'U K': 'gb', 'U S A': 'us', 'UGANDA': 'ug', 'UKRAINE': 'ua', 'UNION OF SERBIA & MONTENEGRO': 'rs', 'UNSPECIFIED': 'ot', 'URUGUAY': 'uy', 'US MINOR OUTLYING ISLANDS               ': 'us', 'UZBEKISTAN': 'uz', 'VANUATU REP': 'vu', 'VATICAN CITY': 'va', 'VENEZUELA': 've', 'VIETNAM SOC REP': 'vn', 'VIRGIN IS US': 'us', 'WALLIS F IS': 'wf', 'YEMEN REPUBLC': 'ye', 'ZAMBIA': 'zm', 'ZIMBABWE': 'zw', 'SAHARWI A.DM RP': 'ot', 'NEUTRAL ZONE': 'ot', 'CANARY IS': 'ic', 'PACIFIC IS': 'ot', 'CHANNEL IS': 'je', 'INSTALLATIONS IN INTERNATIONAL WATERS   ': 'ot', 'SINT MAARTEN (DUTCH PART)': 'nl', 'CURACAO': 'cw'}
df_import=import_data.copy()
df_export=export_data.copy()

df_import.replace(to_replace=countrydict,inplace=True)
df_export.replace(to_replace=countrydict,inplace=True)

countryexports = df_export.groupby('country').agg({'value':'sum'})
countryimports = df_import.groupby('country').agg({'value':'sum'})
countryexports.rename({"value":"export"}, axis=1, inplace=True)
countryimports.rename({"value":"import"}, axis=1, inplace=True)
merged_data = pd.merge(countryimports,countryexports, on='country')
merged_data['td'] = merged_data['export'] - merged_data['import']
merged_data = merged_data.reset_index()
def getcountry(alpha2,nametype):
    try:
        return getattr(pycountry.countries.get(alpha_2=alpha2.upper()),nametype)
    except:
        np.NaN
merged_data['fullcountry'] = merged_data['country'].apply(lambda x: getcountry(x, "name"))
merged_data['country'] = merged_data['country'].apply(lambda x: getcountry(x,"alpha_3"))


# **MAP BASED VISUALIZATION**

# In[6]:


import plotly.graph_objects as go

df = merged_data

fig = go.Figure(data=go.Choropleth(
    locations = df['country'],
    z = df['export'],
    text = df['fullcountry'],
    colorscale = 'peach',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='green',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'Exports<br>Millions US$',
))

fig.update_layout(
    title_text='Exports from India between 2010-2018',
    geo=dict(
        showframe=True,
        showcoastlines=True,
        projection_type='equirectangular'
    )
)


# In[7]:


import plotly.graph_objects as go

df = merged_data

fig = go.Figure(data=go.Choropleth(
    locations = df['country'],
    z = df['import'],
    text = df['fullcountry'],
    colorscale = 'greens',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'Imports<br>Millions US$',
))
fig.update_layout(
    title_text='Imports to India between 2010-2018',
    geo=dict(
        showframe=True,
        showcoastlines=True,
        projection_type='equirectangular'
    )
)


# In[8]:


#Graph Based Visulaitation


yearsimp = pd.DataFrame(import_data.groupby('year').sum())
yearsimp.drop('HSCode',axis=1,inplace=True)
yearsimp.rename(columns={'value':'Imports'},inplace=True)

eyears = pd.DataFrame(export_data.groupby('year').sum())
eyears.rename(columns={'value':'Exports'},inplace=True)

total = pd.concat([yearsimp, eyears], axis = 1)

bar1 = go.Bar(x = total.index,y = total.Exports,name = "Exports",text = total.Exports,texttemplate='%{y:.2s}',textposition='outside')
bar2 = go.Bar(x = total.index,y = total.Imports,name = "Imports",text = total.Imports,texttemplate='%{y:.2s}',textposition='outside')
fig = go.Figure(data=[bar2,bar1])
fig.update_layout(paper_bgcolor="white")
fig.update_layout(plot_bgcolor="white")
fig.update_layout(colorway=['#d43d51','#00876c'])
fig.update_layout(title_font_family="Open Sans")
fig.update_layout(title='Import - Export in terms of US Dollars')
fig.show()


# In[9]:


#Donut Charts


export_data.isnull().sum()
import_data.isnull().sum()
export_data['value'] = export_data['value'].fillna(0)
import_data['value'] = import_data['value'].fillna(0)
replacement = {
    'PRODUCTS OF ANIMAL ORIGIN, NOT ELSEWHERE SPECIFIED OR INCLUDED.':
    'ANIMAL PRODUCTS',
    'NUCLEAR REACTORS, BOILERS, MACHINERY AND MECHANICAL APPLIANCES; PARTS THEREOF.':
    'NUCLEAR EQUIPMENT',
    'OPTICAL, PHOTOGRAPHIC CINEMATOGRAPHIC MEASURING, CHECKING PRECISION, MEDICAL OR SURGICAL INST. AND APPARATUS PARTS AND ACCESSORIES THEREOF;':
    'OPTICAL INSTRUMENTS',
    'FURNITURE; BEDDING, MATTRESSES, MATTRESS SUPPORTS, CUSHIONS AND SIMILAR STUFFED FURNISHING; LAMPS AND LIGHTING FITTINGS NOT ELSEWHERE SPECIFIED OR INC':
    'FURNITURE',
    'ELECTRICAL MACHINERY AND EQUIPMENT AND PARTS THEREOF; SOUND RECORDERS AND REPRODUCERS, TELEVISION IMAGE AND SOUND RECORDERS AND REPRODUCERS,AND PARTS.':
    'ELECTRICAL MACHINERY',
    'ARTICLES OF APPAREL AND CLOTHING ACCESSORIES, NOT KNITTED OR CROCHETED.':
    'CLOTHING',
    'VEHICLES OTHER THAN RAILWAY OR TRAMWAY ROLLING STOCK, AND PARTS AND ACCESSORIES THEREOF.':
    'SPARE PARTS',
    'MINERAL FUELS, MINERAL OILS AND PRODUCTS OF THEIR DISTILLATION; BITUMINOUS SUBSTANCES; MINERAL WAXES.':
    'MINERALS, FUELS AND OILS',
    'NATURAL OR CULTURED PEARLS,PRECIOUS OR SEMIPRECIOUS STONES,PRE.METALS,CLAD WITH PRE.METAL AND ARTCLS THEREOF;IMIT.JEWLRY;COIN.':
    'PEARLS & PRECIOUS METALS',
    'ANIMAL OR VEGETABLE FATS AND OILS AND THEIR CLEAVAGE PRODUCTS; PRE. EDIBLE FATS; ANIMAL OR VEGETABLE WAXEX.':
    'ANIMAL & VEGETABLE FATS'
}
export_data['Commodity'] = export_data['Commodity'].replace(replacement)
import_data['Commodity'] = import_data['Commodity'].replace(replacement)


# In[10]:


import_data_grouped_by_country=import_data.groupby('country',as_index=False).sum()
import1 = import_data_grouped_by_country.sort_values(by=['value'], ascending=False)
import11=import1.drop(['HSCode','year'], axis=1)

countries = list(import11.country.head(10))
values = list(import11.value.head(10))
colors = ['#d43d51','#00876c','#45a074','#72b97c','#9fd184','#cee98f','#fedb79','#fab560','#f38f52','#e7674e']#explsion
explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=countries,colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal') 
plt.title('Indian Imports: Top 10 Countries')
plt.tight_layout()
plt.show()


# In[11]:


export_data_grouped_by_country=export_data.groupby('country',as_index=False).sum()
export1 = export_data_grouped_by_country.sort_values(by=['value'], ascending=False)
export11=export1.drop(['HSCode','year'], axis=1)

countries = list(export11.country.head(10))
values = list(export11.value.head(10))
colors = ['#d43d51','#00876c','#45a074','#72b97c','#9fd184','#cee98f','#fedb79','#fab560','#f38f52','#e7674e']#explsion
explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=countries,colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Indian Exports: Top 10 Countries')
plt.tight_layout()
plt.show()


# In[12]:


import31=import_data.copy()
export31=export_data.copy()
import31=import31.groupby('Commodity',as_index=False).sum().sort_values(by=['value'], ascending=False)
export31=export31.groupby('Commodity',as_index=False).sum().sort_values(by=['value'], ascending=False)


# In[13]:


commodities = list(export31.Commodity.head(10))
values = list(export31.value.head(10))
colors = ['#d43d51','#00876c','#45a074','#72b97c','#9fd184','#cee98f','#fedb79','#fab560','#f38f52','#e7674e']#explsion
explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)

fig1, ax1 = plt.subplots()

ax1.pie(values, labels=commodities,colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')  
plt.title('Indian Exports: Top 10 Commodities')
plt.tight_layout()
plt.show()


# In[14]:


commodities = list(import31.Commodity.head(5))
values = list(import31.value.head(5))
colors = ['#d43d51','#00876c','#45a074','#72b97c','#9fd184','#cee98f','#fedb79','#fab560','#f38f52','#e7674e']#explsion
explode = (0.05,0.05,0.05,0.05,0.05)
fig1, ax1 = plt.subplots()

ax1.pie(values, labels=commodities,colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')  
plt.title('Indian Imports: Top 5 Commodities')
plt.tight_layout()
plt.show()


# In[15]:


#Line Graph
import21=import_data.copy()
export21=export_data.copy()
import21=import21.groupby('year',as_index=False).sum()
export21=export21.groupby('year',as_index=False).sum()


plt.plot( 'year', 'value', data=import21,marker='o', color='red', linewidth=4,label="Exports")
plt.plot( 'year', 'value', data=export21, marker='o', color='blue', linewidth=4, linestyle='dashed', label="Imports")
plt.legend()
plt.show()

