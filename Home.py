import streamlit as st
import leafmap.foliumap as leafmap
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
    Mohamed Sobhi <https://medium.com/@mo.sob7y111>
    [GitHub](https://github.com/Mohamed7u3) | [Twitter](https://twitter.com/Mohamed31669608) | [YouTube](https://www.youtube.com/channel/UCzYJnTLv6TVSVpWuE4y-vTQ) | [LinkedIn](https://www.linkedin.com/in/mohamed-sobhi-ba1554185)
    """
)

st.sidebar.title("Support")
st.sidebar.info(
    """
    If you want to reward my work, I'd love a cup of coffee from you. Thanks!
    (https://wa.me/+201147284401)
    """
)


st.title("Remote sensing for sustainable resource management based on AI")
with st.expander(label= "Description"):
    st.markdown(
        """
        This graduation project thesis focuses on the fusion of remote sensing and artificial
    intelligence (AI) techniques for environmental analysis and infrastructure management.
    The thesis consists of interconnected projects that address data gathering and
    processing, water resources management, anomaly detection in crop patterns, crop
    classification, and oil storage detection .
    The projects aim to automate the workflow of satellite imagery data processing,
    facilitating near-real-time access to ESA archive data. Utilizing remote sensing
    technology, comprehensive tools are developed for water resources management and
    drought monitoring. The thesis also explores anomaly detection in crop patterns and
    accurate crop classification, with a focus on rice crops in California. Additionally, the
    research investigates the detection and classification of oil storage facilities using highresolution satellite data and AI algorithms.
    The fusion of remote sensing and AI techniques throughout the projects enables
    efficient data analysis, informed decision-making and optimized resource management.
    The outcomes provide practical tools and methodologies for researchers, policymakers,
    and industry professionals in diverse fields. The research contributes to sustainability,
    precision agriculture, and infrastructure management, leveraging the potential of
    advanced technologies.
        """
    )

st.info("Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")




col9, col55 = st.columns([0.25, 0.75])
with col9:
    st.image('data/Team/DR.png', caption="Dr.Mohamed Mourad", width=250)
with col55:
    st.write('\n')
    st.write('\n')
    st.write('\n')

    st.info("""
             
             Dr Mohammed Mourad currently works at Beni-Suef University, Faculty of Navigation Science & Space technology (NSST), space communication department. Working on researches in Electronic Engineering, Communication Engineering, Wireless and Telecommunications. He also is a Research Assistant at Nahda University Electrical communication and computer department.
             Ph.D. of Electronics & Communication Engineering.

             """)
col1, col2, col3, col4 = st.columns( [0.25, 0.25, 0.25, 0.25])
with col1:
    image = Image.open('data/Team/Sobhy.png')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Mohamed Sobhi")
    with col1.expander("Email"):
        st.write('Mo.sob7y111@gmail.com')
with col2:
    image = Image.open('data/Team/Tawheed.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Mohamed Tawheed")
with col3:
    image = Image.open('data/Team/Sahar.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Sahar Abdulalim")
with col4:
    image = Image.open('data/Team/Manar.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Manar Marwan")

col5, col6,col7, col8 = st.columns( [0.25, 0.25, 0.25, 0.25])
with col5:
    image = Image.open('data/Team/N3ma.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Neama Ahmed")
with col7:
    image = Image.open('data/Team/Belal.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Belal Mousa")
with col8:
    image = Image.open('data/Team/Khaled.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Khaled Amin")

with col6:
    image = Image.open('data/Team/Mahmoud.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Mahmoud Hisham")

with col2.expander("Email"):
   st.write('mohatawheed@gmail.com')
with col3.expander("Email"):
   st.write('sahaar208@gmail.com')
with col4.expander("Email"):
   st.write('manarmarwan26@gmail.com')
with col5.expander("Email"):
   st.write('neamaahmedali9098@gmail.com')
with col8.expander("Email"):
   st.write('khaled.amin7614@gmail.com')
with col9.expander("Email"):
   st.write('mohamedmourad2008@gmail.com') 
with col7.expander("Email"):
   st.write('belalzourob99@gmail.com') 

with col6.expander("Email"):
   st.write('mahmoudhisham526@gmail.com')

col11, col21, col31, col41 = st.columns( [0.25, 0.25, 0.25, 0.25])
with col11:
    image = Image.open('data/Team/fares.jpg')
    new_image = image.resize((250, 250))
    st.image(new_image, caption="Fares Tarek")
with col11.expander("Email"):
   st.write('fares.tarek2277@gmail.com')
   