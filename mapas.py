import pandas as pd
from IPython.display import display
import plotly.express as px

tabela = pd.read_csv("Cidades.csv")
#display(tabela)

grafico = px.density_mapbox(tabela, lon="geolocation_lng", lat="geolocation_lat", z="quantidade", mapbox_style="open-street-map", zoom=3, radius=10)
grafico.update_layout(margin={"r":0, "t":0, "b":0, "l":0})
grafico.show()