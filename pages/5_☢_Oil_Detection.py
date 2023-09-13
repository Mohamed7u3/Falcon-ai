import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image
import numpy as np

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

st.title("Oil Detection")

img_file_buffer1 = st.file_uploader("Upload an image3")
row1_col1, row1_col2= st.columns(2)

if img_file_buffer1 is not None:
    image1 = Image.open(img_file_buffer1)
    img_array = np.array(image1) # if you want to pass it to OpenCV
    with row1_col1:
        st.image(image1, caption="true image", use_column_width=True)
    with row1_col2:
        st.image('data/pre.jpg', caption="model-prediction", use_column_width=True)
