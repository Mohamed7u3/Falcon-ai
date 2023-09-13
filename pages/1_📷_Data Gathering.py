import streamlit as st
import leafmap
import folium
import ee
import json
from geemap import geojson_to_ee, ee_to_geojson
import geemap
import leafmap.foliumap as lm
import geopandas as gpd
from datetime import date, timedelta
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

st.title("Data Gathering(Download data)")








mapObject = geemap.Map()
mapObject.to_streamlit(height=700)
with st.expander("Search Location", False):
    # SEARCH LOCATION
    keyword = st.text_input("Search for a location:", '')
    if keyword:
        locations = geemap.geocode(keyword)
        if locations is not None and len(locations) > 0:
            str_locations = [str(g)[1:-1] for g in locations]
            location = st.selectbox("Select a location:", str_locations)
            loc_index = str_locations.index(location)
            selected_loc = locations[loc_index]
            lat =  selected_loc.lat
            lon =  selected_loc.lng

            folium.Marker(location=[lat, lon], popup=location).add_to(mapObject)
            mapObject.set_center(lon, lat, 13)
            st.session_state["zoom_level"] = 13
    
    else:
        coords = st.text_input('Search using Lat/Lon (Decimal Degrees)', '')
        if coords:
            locations = geemap.geocode(coords, reverse=True)
            str_locations = [str(g)[1:-1] for g in locations]
            location = str_locations[0]
            loc_index = str_locations.index(location)
            selected_loc = locations[loc_index]
            lat =  selected_loc.lat
            lon =  selected_loc.lng
            folium.Marker(location=[lat, lon], popup=None).add_to(mapObject)
            mapObject.set_center(lon, lat, 16)
            st.session_state["zoom_level"] = 16

with st.expander("Define Processing Parameters"):
    form = st.form(key='processing-params')
    fromDate = form.date_input('Start Date', date.today() - timedelta(days=366))
    toDate = form.date_input('End Date', date.today()-timedelta(days=1))
    cloudCover = form.number_input(label="Cloud Cover Threshold (%)", min_value=0, max_value=50, value=5, step=5)
    satellite = form.selectbox("Landsat Satellite", [
            "Sentinel-1",
            "Sentinel-2"
        ], index=1)

    # Date Validation Check
    if toDate - fromDate < timedelta(days=90):
        st.error('Difference between the two selected data is too small. Try again!')
        st.stop()
    else:
        submit = form.form_submit_button('Submit')

    if submit:
        st.session_state['fromDate'] = fromDate
        st.session_state["toDate"] = toDate
        st.session_state["cloudCover"] = cloudCover
        st.session_state['satellite'] = satellite
def uploaded_file_to_gdf(data, crs):
    import tempfile
    import os
    import uuid
    import zipfile

    _, file_extension = os.path.splitext(data.name)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    with open(file_path, "wb") as file:
        file.write(data.getbuffer())

    if file_path.lower().endswith(".kml"):
        gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
        gdf = gpd.read_file(file_path, driver="KML")
        return gdf
    # If the user uploads a zipped shapefile
    # Only works when te name of the shapefile (XXXX.shp) is same te the name of the uploaded zip file (XXXX.zip)
    elif file_path.lower().endswith(".zip"):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Extract the contents of the zip file into the temp directory
            zip_ref.extractall(os.path.join(tempfile.gettempdir(), file_id))
        # Return the filepath where the file_id.shp along with other components (.shx, .dbf, ...) are placed. 
        return os.path.join(tempfile.gettempdir(), file_id)
    else:
        gdf = gpd.read_file(file_path, crs = crs)
        return gdf
with st.expander("Select Area of Interest (AOI)", False):
        optionsList = ["Search EE Assets", "Enter URL", "Upload Shapefile/GeoJSON"]
        option = st.radio("Select Option", optionsList)
        if option == optionsList[1]:
            url_data = st.text_input("Enter GeoJSON URL","")
            if url_data == '':
                st.info("Enter URL")
                pass
            else:
                gdf = gpd.read_file(url_data)
                st.session_state["aoi"] = geemap.geopandas_to_ee(gdf, geodesic=True)
                ee_obj = st.session_state['aoi'] 
                gdf['center'] = gdf.centroid
                gdf['lon'] = gdf.center.apply(lambda p: p.x)
                gdf['lat'] = gdf.center.apply(lambda p: p.y)
                lon = gdf.lon.mean()
                lat = gdf.lat.mean()
                zoomLevel = 10
                mapObject.addLayer(ee_obj, {}, 'AOI')
                mapObject.set_center(lon, lat, zoomLevel)
                st.session_state["aoi"] = ee_obj # Saving AOI to Session State
        elif option == optionsList[0]:
            ee_asset_search = st.text_input("Search EarthEngine FeatureCollection Asset", "")
            ee_assets_from_search = geemap.search_ee_data(ee_asset_search)
            asset_options = [asset['title'] for asset in ee_assets_from_search]
            if ee_asset_search == '':
                st.info("Search EE using keyword")
            elif len(asset_options) > 0:
                selected_ee_asset = st.selectbox("Select EE Asset", asset_options)
                selected_asset_index = asset_options.index(selected_ee_asset)
                asset = ee_assets_from_search[selected_asset_index]
                featureID = asset['id']
                ee_obj = ee.FeatureCollection(featureID)
                st.session_state['aoi'] = ee_obj
                mapObject.addLayer(ee_obj, {}, selected_ee_asset)
            else:
                st.info('Asset Not Found! Use a diffent keyword.')
        elif option == optionsList[2]:
            uploaded_file = st.file_uploader(
                    "Upload a GeoJSON or a Zipped Shapefile to use as an AOI.",
                    type=["geojson", "zip"]
                    )
            crs = {"init": "epsg:4326"}
            
            if uploaded_file != None:
                file_ext = uploaded_file.name.split('.')[-1]
                if file_ext == 'zip':
                    # Get Path to the temp directory where all contents of the shapefile are located
                    tempDirPath = uploaded_file_to_gdf(uploaded_file, crs)
                    # Get the name of the shapefile
                    shpName = uploaded_file.name.split('.zip')[0]
                    import os
                    # Read using geopandas
                    gdf = gpd.read_file(os.path.join(tempDirPath, (shpName + '.shp')))
                    
                    st.session_state["aoi"] = geemap.geopandas_to_ee(gdf, geodesic=False)
                    ee_obj = st.session_state['aoi']

                    from shapely.geometry import Polygon, Point

                    minx, miny, maxx, maxy = gdf.geometry.total_bounds
                    gdf_bounds = gpd.GeoSeries({
                        'geometry': Polygon([Point(minx, maxy), Point(maxx, maxy), Point(maxx, miny), Point(minx, miny)])
                    }, crs="EPSG:4326")
                    area = gdf_bounds.area.values[0]
                    center = gdf_bounds.centroid
                    center_lon = float(center.x); center_lat = float(center.y)
                    
                    if area > 5:
                        zoomLevel = 8
                    elif area > 3:
                        zoomLevel = 10
                    elif area > 0.1 and area < 0.5:
                        zoomLevel = 11
                    else:
                        zoomLevel = 13
                    
                    # print(area, zoomLevel)
                    mapObject.addLayer(ee_obj, {}, 'aoi')
                    # mapObject.set_center(st.session_state.lon, st.session_state.lat, zoomLevel)
                    mapObject.set_center(center_lon, center_lat, zoomLevel)
                    st.session_state["aoi"] = ee_obj
                elif uploaded_file is None:
                    pass
                else:
                    gdf = uploaded_file_to_gdf(uploaded_file, crs)
                    st.session_state["aoi"] = geemap.geopandas_to_ee(gdf, geodesic=False)
                    ee_obj = st.session_state['aoi']
                    from shapely.geometry import Polygon, Point

                    minx, miny, maxx, maxy = gdf.geometry.total_bounds
                    gdf_bounds = gpd.GeoSeries({
                        'geometry': Polygon([Point(minx, maxy), Point(maxx, maxy), Point(maxx, miny), Point(minx, miny)])
                    }, crs="EPSG:4326")

                    area = gdf_bounds.area.values[0]
                    center = gdf_bounds.centroid
                    center_lon = float(center.x); center_lat = float(center.y)
                    
                    if area > 5:
                        zoomLevel = 8
                    elif area > 3:
                        zoomLevel = 10
                    elif area > 0.1 and area < 0.5:
                        zoomLevel = 11
                    elif area < 2 and area > 1:
                        zoomLevel = 9
                    else:
                        zoomLevel = 13
                    
                    mapObject.addLayer(ee_obj, {}, 'aoi')
                    mapObject.set_center(center_lon, center_lat, zoomLevel)
                    st.session_state["aoi"] = ee_obj

