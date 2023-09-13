import streamlit as st
import leafmap
import folium
import leafmap.foliumap as lm
from PIL import Image
import numpy as np
from streamlit_folium import folium_static
import os


st.set_page_config(layout="wide")

st.sidebar.info(
    """
    Falcon AI 
    is Team  focuses on the fusion of remote sensing 
    and artificial intelligence (AI) techniques for environmental analysis and infrastructure  management

    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Mohamed Sobhi <https://medium.com/@mo.sob7y111>
    [GitHub](https://github.com/Mohamed7u3) | [Twitter](https://twitter.com/Mohamed31669608) | [YouTube](https://www.youtube.com/channel/UCzYJnTLv6TVSVpWuE4y-vTQ) | [LinkedIn](https://www.linkedin.com/in/mohamed-sobhi-ba1554185)
    """
)

st.title("Crop type classification with satellite imagery")
#url = 'https://cog-iowa.s3.us-east-2.amazonaws.com/IOWA/output_cog_1.tif'

#m = leafmap.Map()
#m.add_raster(out_cog, palette="terrain", layer_name="Local COG")
#leafmap.cog_validate(url)
#leafmap.cog_validate(url, verbose=True)
#m.add_tilelayer(url, name='COG', attribution='<a href="http://www.cogeo.org/">Cloud
#m.add_cog_layer(url, palette="gist_earth", name="Remote COG")
#m.to_streamlit()



#Map = geemap.Map()
#Map.add_cog_layer(url, name="Fire (post-event)")
#Map.to_streamlit()


st.components.v1.html(open('data\last.html').read(), width=800, height=600)

