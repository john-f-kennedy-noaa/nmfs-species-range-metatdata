import arcpy
import os, sys
from arcgis.gis import GIS

portal = "https://noaa.maps.arcgis.com/"
user = "John.F.Kennedy_noaa"

LogInAGOL = False
if LogInAGOL:
    # For example: 'http://www.arcgis.com/'
    arcpy.SignInToPortal(portal)
    #print(f"Signed into Portal: {arcpy.GetActivePortalURL()}")
    print(f"Connecting to {portal}")
    gis = GIS(portal)
del LogInAGOL

gis = GIS(portal, use_gen_token=True)

sd_fs_name = "AbaloneBlack_20210712"

#items = gis.content.search(query="owner:" + gis.users.me.username)

# Find the SD, update it, publish /w overwrite and set sharing and metadata
print("Search for original SD on portal…")
search_my_contents = gis.content.search(
                                        #query=f"{'FeatureSharingDraftExample'} AND owner:{user}",
                                        # title:{} AND owner:{}
                                        query=f"title: {sd_fs_name} AND owner:{user}",
                                        item_type="*",
                                        sort_field="tile" ,
                                        sort_order="asc",
                                        max_items = 1000,
                                        outside_org=False
                                        )
titles = []
#print(search_my_contents)
for search_my_content in search_my_contents:
    #print(search_my_content)
    title = search_my_content.title
    if title not in titles:
        titles.append(title)
    print(f"Found SD: {search_my_content.title}\n\t Type: {search_my_content.type}\n\t URL: {search_my_content.url}")
for title in titles:
    print(f"Found: {title}")
##adItems = gis.content.search(f"owner:{user}", item_type="Feature Layer")[0]
##if adItems:
##    print(f"Found SD: {adItems.title}, ID: {adItems.id} n Uploading and overwriting…")