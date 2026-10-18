# Cleans raw/zomato_dataset.csv (download from Kaggle) into data/restaurants.csv and data/cuisines.csv
# Run from the project root:  python scripts/clean_data.py
import pandas as pd, numpy as np, re
raw=pd.read_csv('raw/zomato_dataset.csv'); n0=len(raw)
df=raw.drop_duplicates().copy(); dups=n0-len(df)
df.columns=['Restaurant Name','RatingRaw','Cuisine','PriceRaw','DelivRaw','SafetyRaw','City']
df['Restaurant Name']=df['Restaurant Name'].str.strip()
df['City']=df['City'].replace({'NCR':'Delhi NCR'})
ST={'Agra':'Uttar Pradesh','Ahmedabad':'Gujarat','Ajmer':'Rajasthan','Alappuzha':'Kerala','Aligarh':'Uttar Pradesh','Allahabad':'Uttar Pradesh','Amravati':'Maharashtra','Amritsar':'Punjab','Asansol':'West Bengal','Aurangabad':'Maharashtra','Bangalore':'Karnataka','Bareilly':'Uttar Pradesh','Belgaum':'Karnataka','Bhavnagar':'Gujarat','Bhopal':'Madhya Pradesh','Bhubaneswar':'Odisha','Bikaner':'Rajasthan','Chandigarh':'Chandigarh','Chennai':'Tamil Nadu','Coimbatore':'Tamil Nadu','Cuttack':'Odisha','Darbhanga':'Bihar','Darjeeling':'West Bengal','Dehradun':'Uttarakhand','Delhi NCR':'Delhi NCR','Dhanbad':'Jharkhand','Dharamshala':'Himachal Pradesh','Durgapur':'West Bengal','Firozabad':'Uttar Pradesh','Gaya':'Bihar','Goa':'Goa','Gonda':'Uttar Pradesh','Gorakhpur':'Uttar Pradesh','Guntur':'Andhra Pradesh','Guwahati':'Assam','Haridwar':'Uttarakhand','Hyderabad':'Telangana','Indore':'Madhya Pradesh','Jabalpur':'Madhya Pradesh','Jaipur':'Rajasthan','Jalandhar':'Punjab','Jalgaon':'Maharashtra','Jammu':'Jammu & Kashmir','Jamnagar':'Gujarat','Jamshedpur':'Jharkhand','Jhansi':'Uttar Pradesh','Jodhpur':'Rajasthan','Junagadh':'Gujarat','Kanpur':'Uttar Pradesh','Kharagpur':'West Bengal','Kolhapur':'Maharashtra','Kolkata':'West Bengal','Kota':'Rajasthan','Lucknow':'Uttar Pradesh','Ludhiana':'Punjab','Madurai':'Tamil Nadu','Manali':'Himachal Pradesh','Mangalore':'Karnataka','Manipal':'Karnataka','Meerut':'Uttar Pradesh','Moradabad':'Uttar Pradesh','Motihari':'Bihar','Mumbai':'Maharashtra','Mussoorie':'Uttarakhand','Mysore':'Karnataka','Nagpur':'Maharashtra','Nainital':'Uttarakhand','Nashik':'Maharashtra','Nellore':'Andhra Pradesh','Palakkad':'Kerala','Patiala':'Punjab','Patna':'Bihar','Puducherry':'Puducherry','Pune':'Maharashtra','Raipur':'Chhattisgarh','Rajkot':'Gujarat','Ranchi':'Jharkhand','Rishikesh':'Uttarakhand','Saharanpur':'Uttar Pradesh','Salem':'Tamil Nadu','Sangli':'Maharashtra','Shimla':'Himachal Pradesh','Siliguri':'West Bengal','Solapur':'Maharashtra','Surat':'Gujarat','Thrissur':'Kerala','Tirunelveli':'Tamil Nadu','Trichy':'Tamil Nadu','Trivandrum':'Kerala','Udaipur':'Rajasthan','Ujjain':'Madhya Pradesh','Vadodara':'Gujarat','Varanasi':'Uttar Pradesh','Vellore':'Tamil Nadu','Vijayawada':'Andhra Pradesh','Visakhapatnam':'Andhra Pradesh','Warangal':'Telangana'}
RG={'North':['Delhi NCR','Uttar Pradesh','Uttarakhand','Himachal Pradesh','Punjab','Chandigarh','Jammu & Kashmir','Rajasthan'],
    'West':['Maharashtra','Gujarat','Goa'],'South':['Karnataka','Tamil Nadu','Kerala','Andhra Pradesh','Telangana','Puducherry'],
    'East':['West Bengal','Odisha','Bihar','Jharkhand','Assam'],'Central':['Madhya Pradesh','Chhattisgarh']}
S2R={s:r for r,l in RG.items() for s in l}
assert set(df.City)<=set(ST), set(df.City)-set(ST)
df['State']=df.City.map(ST); df['Region']=df.State.map(S2R); assert df.Region.notna().all()
df['Brand']=df['Restaurant Name'].str.split(' - ').str[0].str.strip()
# rating
r=pd.to_numeric(df.RatingRaw,errors='coerce'); df['Rating']=r
df['Rating Status']=np.where(r.notna(),'Rated',np.where(df.RatingRaw=='New','New','Unrated'))
bands=[('Below 3.0',0),('3.0 - 3.4',1),('3.5 - 3.9',2),('4.0 - 4.4',3),('4.5 and above',4)]
def rb(x):
    if pd.isna(x): return (None,None)
    return bands[0]if x<3 else bands[1]if x<3.5 else bands[2]if x<4 else bands[3]if x<4.5 else bands[4]
t=df.Rating.map(rb); df['Rating Band']=t.str[0].fillna('Not rated'); df['Rating Band Order']=t.str[1].fillna(5).astype(int)
# price
p=df.PriceRaw.str.replace(r'[^\d]','',regex=True).replace('',np.nan).astype(float); df['Price for One']=p
def pb(x):
    if pd.isna(x): return (None,None)
    return ('Budget (up to 100)',1) if x<=100 else ('Value (101-200)',2) if x<=200 else ('Mid-range (201-400)',3) if x<=400 else ('Premium (above 400)',4)
t=df['Price for One'].map(pb); df['Price Band']=t.str[0].fillna('Not listed'); df['Price Band Order']=t.str[1].fillna(5).astype(int)
# delivery
m=df.DelivRaw.str.extract(r'^(\d+) min$')[0].astype(float)
df['Delivery Minutes']=m.where((m>=5)&(m<=120))
out_cnt=int(m.notna().sum()-df['Delivery Minutes'].notna().sum())
def ds(s,mi):
    if s.startswith(('Currently not','Temporarily','Permanently')): return 'Closed / not accepting'
    if s.startswith('Opening hours'): return 'Hours not available'
    if s.startswith('Opens'): return 'Opens later'
    if s.startswith('Closes in'): return 'Closing soon'
    return 'Delivering'
df['Delivery Status']=[ds(s,mi) for s,mi in zip(df.DelivRaw,m)]
def sp(x):
    if pd.isna(x): return (None,None)
    return ('Fast (under 25 min)',1) if x<25 else ('Standard (25-39 min)',2) if x<40 else ('Slow (40+ min)',3)
t=df['Delivery Minutes'].map(sp); df['Delivery Speed']=t.str[0].fillna('Not delivering now'); df['Delivery Speed Order']=t.str[1].fillna(4).astype(int)
df['Safety Level']=np.where(df.SafetyRaw.str.contains('Max Safety'),'Max Safety','WHO Protocol')
df=df.reset_index(drop=True); df['Restaurant ID']=np.arange(1,len(df)+1)
cu=df[['Restaurant ID','Cuisine']].dropna().copy()
cu['Cuisine']=cu.Cuisine.str.split(',')
cu=cu.explode('Cuisine'); cu['Cuisine']=cu.Cuisine.str.strip(); cu=cu[cu.Cuisine!='']
df['Primary Cuisine']=df.Cuisine.str.split(',').str[0].str.strip().fillna('Not specified')
df['Cuisine Count']=df['Restaurant ID'].map(cu.groupby('Restaurant ID').size()).fillna(0).astype(int)
cols=['Restaurant ID','Restaurant Name','Brand','City','State','Region','Rating','Rating Status','Rating Band','Rating Band Order','Primary Cuisine','Cuisine Count','Price for One','Price Band','Price Band Order','Delivery Minutes','Delivery Speed','Delivery Speed Order','Delivery Status','Safety Level']
out=df[cols]; out.to_csv('data/restaurants.csv',index=False,encoding='utf-8'); cu.to_csv('data/cuisines.csv',index=False,encoding='utf-8')
print('raw',n0,'dups removed',dups,'rows',len(out),'cuisine rows',len(cu),'delivery outliers nulled',out_cnt)
print(out.isna().sum()[out.isna().sum()>0].to_dict()); print(out['Rating Status'].value_counts().to_dict()); print(out['Delivery Status'].value_counts().to_dict())
print(cu.Cuisine.nunique(),'cuisines'); print(out.Region.value_counts().to_dict())
