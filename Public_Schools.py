#IMPORT PACKAGES 
import geopandas as gpd
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

#READ IN FILES
csv = pd.read_csv(r'filelocation')
districts = gpd.read_file(r'filelocation')

csv = csv.rename(columns={'School\nCode':'ID', 'Grade Span':'Grades','School Performance \nGrade\n(SPG)':'Grade'})
districts = districts.rename(columns={'LEA_SCHOOL':'ID','URL_ADDRES':'URL','SCHOOL_NAM':'Name','MAIL_CITY':'City', 'COUNTY':'County', 'MAIL_ADDR':'Address'})

school_shape = districts.merge(csv, on='ID')

school_shape = school_shape[['ID','Name','Grade','Grades','Address', 'City','County','URL','geometry']]

school_shape.to_file(r'filelocation')

print(school_shape.columns)
print(school_shape.shape)



