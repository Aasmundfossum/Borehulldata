from datetime import datetime
import time
import numpy as np
import pandas as pd
import streamlit as st
#import altair as alt
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium


df = pd.read_excel("GrunnvannsBorehull.xlsx", sheet_name="EnergiBrønn",usecols='G,X,Y')




#print(df)
df = df.sort_values('boreDato')

st.dataframe(df)

datoer = df.iloc[:,0]
pd.to_datetime(datoer)
pd.to_datetime(df.iloc[:,0])


def bronner_hvert_aar(aar):

    datoer_aar = [date for date in df.iloc[:,0] if date.year == aar]
    indeks_aar = []
    for i in range(0,len(datoer_aar)):
        hvor = np.where(datoer == np.datetime64(datoer_aar[i]))
        indeks_aar = np.concatenate((indeks_aar,hvor[0]))
    bronner_aar = df.iloc[int(indeks_aar[0]):int(indeks_aar[-1])+1,:]               #Forutsetter >0 antall brønner hvert enkelt år
    return bronner_aar





#bronner2022 = bronner_hvert_aar(2022)


df = df.head()
map_osm = folium.Map(location=[65.5, 18], zoom_start=4.5)
df.apply(lambda row:folium.CircleMarker(location=[row["y_koordinat"], row["x_koordinat"]],radius=3).add_to(map_osm), axis=1)
map_osm
# call to render Folium map in Streamlit
#st_data = st_folium(map_osm, width=725)









#bronner=bronner_hvert_aar(1992)
#for AAR in range(1993,2024):
#    aarstall = str(AAR)
#    bronner = pd.concat([bronner, bronner_hvert_aar(AAR)])
#    x_aar = bronner.iloc[:,1]
#    y_aar = bronner.iloc[:,2]
#    #plt.figure(figsize=(10,10))
#    fig, ax = plt.subplots()
#    plt.xlim([4, 32])
#    plt.ylim([58, 72])
#    #plt.axis('equal')
#    img = plt.imread("Norgeskart.PNG")
#    ax.imshow(img, extent=[4, 32, 58, 72])
#    ax.scatter(x_aar, y_aar, 0.5)
#    plt.legend([str(AAR)], loc='upper left')
#    plt.savefig('Bilder_til_gif/bronner'+aarstall+'.png')   #Lagrer alle figurene i en mappe, slik at de kan settes sammen til en Gif
#    plt.close()







#chart_data = pd.DataFrame(bronner_hvert_aar(1992),columns=['x_koordinat', 'y_koordinat'])
#c = alt.Chart(chart_data).mark_circle(size=10).encode(
#        alt.X('x_koordinat').scale(domain=(4,32)), alt.Y('y_koordinat').scale(domain=(58,72)), tooltip=['x_koordinat', 'y_koordinat'])

#for AAR in range(1993,2023):
#    tittel = str(AAR)
#    globals()[f'bronner{AAR}']=bronner_hvert_aar(AAR)
#    chart_data = pd.DataFrame(globals()[f'bronner{AAR}'],columns=['x_koordinat', 'y_koordinat'])
#   
#    c = c + alt.Chart(chart_data).mark_circle(size=10).encode(                                #Tittel fungerer ikke...
#        alt.X('x_koordinat').scale(domain=(4,32)), alt.Y('y_koordinat').scale(domain=(58,72)), tooltip=['x_koordinat', 'y_koordinat'])

#    st.altair_chart(c, use_container_width=False)
#    #st.altair_chart(globals()[f'c_{AAR}'], use_container_width=False)
#    time.sleep(0.5)