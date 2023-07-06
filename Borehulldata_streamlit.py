import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

filename = 'GrunnvannsBorehull.xlsx'

# -----------------------------------------------------------------------------------
energibronn = pd.read_excel(filename, sheet_name = 'EnergiBrønn', usecols='G')
energibronn_type = pd.read_excel(filename, sheet_name = 'EnergiBrønn', usecols='E')

energibronn = energibronn.to_string()
energibronn_type = energibronn_type.to_string()

startaar = 1995
sluttaar = 2023
aarstall = np.arange(startaar,sluttaar+1)
antall_per_aar = np.zeros(len(aarstall))

for aar in range(startaar,sluttaar+1):
    antall_per_aar[aar-startaar] = energibronn.count(str(aar)+'-')

fig = plt.figure()
plt.bar(aarstall, antall_per_aar)
plt.xlabel("Årstall")
plt.ylabel("Antall brønner boret")
plt.title("Antall brønner boret i Norge per år")
#plt.show()

liten = energibronn_type.count('Enkelthusholdning')
stor = energibronn_type.count('Større anlegg')
gaard = energibronn_type.count('Gårdsbruk')
turist = energibronn_type.count('Turistnæring')

fig_type = plt.figure()
plt.bar(['Enkelthusholdning','Større anlegg','Gårdsbruk','Turistnæring'],[liten,stor,gaard,turist])
plt.xlabel("Type")
plt.ylabel("Antall brønner boret")
plt.title("Antall av ulike typer boret i Norge")


# ------------------------------------------------------------------------------------

grunnvannsbronn = pd.read_excel(filename, sheet_name = 'GrunnvannBrønn', usecols='G')
grunnvannsbronn = grunnvannsbronn.to_string()

for aar in range(startaar,sluttaar+1):
    antall_per_aar[aar-startaar] = grunnvannsbronn.count(str(aar)+'-')

fig2 = plt.figure()
plt.bar(aarstall, antall_per_aar)
plt.xlabel("Årstall")
plt.ylabel("Antall brønner boret")
plt.title("Antall brønner boret i Norge per år")
# ------------------------------------------------------------------------------------

lgnbronn = pd.read_excel(filename, sheet_name = 'LGNBrønn', usecols='H')
lgnbronn = lgnbronn.to_string()

for aar in range(startaar,sluttaar+1):
    antall_per_aar[aar-startaar] = lgnbronn.count(str(aar)+'-')

fig3 = plt.figure()
plt.bar(aarstall, antall_per_aar)
plt.xlabel("Årstall")
plt.ylabel("Antall brønner boret")
plt.title("Antall brønner boret i Norge per år")
# ------------------------------------------------------------------------------------


# Streamlit-nettside:

st.title('Statistikk for borehull i Norge')
st.write('Lalala')

st.header('Energibrønner:')
st.pyplot(fig)
st.pyplot(fig_type)

st.header('Grunnvannsbrønner')
st.pyplot(fig2)

st.header('LGN-brønner')
st.pyplot(fig3)