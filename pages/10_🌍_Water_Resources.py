import streamlit as st
import geemap.foliumap as geemap
from PIL import Image

st.set_page_config(layout="wide")

st.sidebar.title("About")
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
    Manar marawan <https://medium.com/@mo.sob7y111>
    [GitHub](https://github.com/Mohamed7u3) | [Twitter](https://twitter.com/Mohamed31669608) | [YouTube](https://www.youtube.com/channel/UCzYJnTLv6TVSVpWuE4y-vTQ) | [LinkedIn](https://www.linkedin.com/in/mohamed-sobhi-ba1554185)
    """
)

st.title( "Water Resources")
st.write('Water resources analysis is crucial for sustainable water management, environmental protection, and economic development. Soil moisture analysis is an important component of water resources analysis, providing insights into water availability, environmental impacts, and climate change impacts on water resources. By creating drought monitoring systems using soil moisture analysis, we can identify areas at risk of drought and develop effective policies and strategies for mitigating the impacts of drought and ensuring the sustainable use of water resources.')

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image('data/water.jpg', caption="SMAP L4 data analysis")
with row1_col2:
    st.image('data/manar.gif', caption="Drought monitor 2023", width= 400)
