# puzzleSolver: Solving the "puzzle.csv"

import folium
import math
import pandas as pd

headers = ['lng', 'lat']
df = pd.read_csv("https://drive.google.com/uc?export=download&id=10h4D4vqqlr-F0g9Ch20GQ7C1oxx3RL33", names=headers)
x = df['lat']
y = df['lng']

print(df.head(n=5))

def plotPoints(df, map):
    for i in range(len(df)):
        """ plots all points in a dataframe in folium, which generates an HTML file with all \
        points plotted on an interactive, lightweight map."""
        x = df['lat'][i]
        y = df['lng'][i]
        marker = folium.CircleMarker(location=[y, x])
        marker.add_to(map)
        
def expandCoords(df, multiplier):
    # multiplies all coordinates in dataframe by a given multiplier.
    for x in range(len(df)):
        df['lat'][x] = (df['lat'][x] * multiplier)
        df['lng'][x] = (df['lng'][x] * multiplier)
        
mult = 180/math.pi

expandCoords(df, mult)
print()
print("After Expansion:")
print(df.head(n=5))

newfolmap = folium.Map(location=[42.366083, -71.082194], zoom_start=2, tiles="CartoDB positron")
plotPoints(df, newfolmap)
newfolmap.save("finalmap.html")