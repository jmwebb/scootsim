import geopandas as gpd
# Set the filepath and load in a shapefile
fp = '../data/la-county-neighborhoods-current/l.a. county neighborhood (current).shp'
la_neighbs = gpd.read_file(fp)
# Print data type so we can see that this is not a normal dataframe, but a GEOdataframe
print('L.A. County GIS dataset type: {}'.format(type(la_neighbs)))
la_neighbs.head()
