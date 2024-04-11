# %%
pip install dash-bootstrap-components

# %%
pip install ipython

# %%
#import dependencies
import dash
import dash_bootstrap_components as dbc
from dash import html
from IPython.display import Image, display, Markdown


# %%
#define external stylesheet
external_stylesheets = ['https://bootswatch.com/5/quartz/bootstrap.css']

# %%
#define image URLs
image_urls = [
    "http://www.impawards.com/2023/posters/killers_of_the_flower_moon.jpg", #killers of the flower moon
    "http://www.impawards.com/2023/posters/mission_impossible__dead_reckoning_part_one_ver2.jpg", #mission impossible
    "http://www.impawards.com/2023/posters/oppenheimer_ver3.jpg", #oppenheimer
    "http://www.impawards.com/2023/posters/spiderman_across_the_spiderverse_ver2.jpg", #spider man
    "http://www.impawards.com/2023/posters/no_hard_feelings.jpg", #no hard feelings
    "http://www.impawards.com/2023/posters/little_mermaid_ver4.jpg", #little mermaid
    "https://media.themoviedb.org/t/p/w440_and_h660_face/uUbdc9TMwbazp1zCNzGtXoBHhUa.jpg", #barbie
    "http://www.impawards.com/2023/posters/m3gan.jpg", #m3gan
    "http://www.impawards.com/2023/posters/guardians_of_the_galaxy_vol_three_ver2.jpg", #guardians of the galaxy
    "http://www.impawards.com/2023/posters/love_again.jpg", #love again
    "http://www.impawards.com/2023/posters/air_ver2.jpg" #air
]

# %%
#display images
for url in image_urls:
    display(Image(url=url, width=100, height=150))

# %%
#create carousel items using image URLs
carousel_items = [
    {"key": str(i), "src": url} for i, url in enumerate(image_urls, start=1)
]

#create the carousel component
carousel = dbc.Carousel(
    items=carousel_items,
    controls=False,
    indicators=False,
    interval=2000,
    ride="carousel",
)

# %%
#create a stylized title
title = html.H1("Trending Now", className="display-4 text-center text-white font-weight-bold mt-5")

# %%
#initialize dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#connect the server for Render
server=app.server


# %%
#define app layout
app.layout = html.Div([
    title,  # add the title above the carousel
    carousel
])

# %%
#run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8058)


