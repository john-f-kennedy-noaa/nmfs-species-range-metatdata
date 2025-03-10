#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     01/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback
import importlib
import inspect

# Third-party modules are loaded second
import arcpy

# Append the location of this scrip to the System Path
sys.path.append(os.path.dirname(__file__))

def readable_date(portal_stamp):
    import datetime as dt
    return dt.datetime.fromtimestamp(portal_stamp/1000).strftime('%B %d %Y at %I:%M.%S %p')

def get_missing_item_attrs(portal_item, item_profile):
    """Returns a list of True/False values for specific
    properties as well as the item id and url (if
    applicable for each item in the portal.
    """
    non_compliance = []
    for attr in item_profile:
        if attr == 'thumbnail':
            if getattr(portal_item, attr) is not None:
                if 'ago_downloaded' in getattr(portal_item, attr):
                    non_compliance.append({attr : True})
                else:
                    non_compliance.append({attr : False})
            else:
                non_compliance.append({attr : None})
        else:
            if getattr(portal_item, attr) is not None:
                non_compliance.append({attr : True})
            else:
                non_compliance.append({attr : False})
    non_compliance.append(portal_item.id)
    non_compliance.append(portal_item.url)
    #non_compliance.append(portal_item.metadata)
    #print(portal_item.metadata)
    return non_compliance

def ideas_1(project_folder):
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        del urllib3

        import pandas as pd
        from arcgis.gis import GIS
        gis = GIS("pro")

##        # Search for Feature Layers owned by the logged-in user
##        my_contents = gis.content.search(query="owner:" + gis.users.me.username, item_type="Feature*", max_items=15)
##
##        titles = []
##
##        for my_content in my_contents:
##            titles.append(my_content.title)
##            del my_content
##        del my_contents
##
##        #for title in sorted(titles):
##        #    print(title)
##        #    del title
##        del titles

        #import os
        import datetime as dt

        day_start = dt.datetime(2024, 12, 30, 0, 0, 0, 0)
        day_end = dt.datetime(2025, 1, 10, 23, 59, 59, 999999)

        start_timestamp = int(day_start.timestamp() * 1000)
        end_timestamp = int(day_end.timestamp() * 1000)

        del day_start, day_end

        content_published_202412 = [item for item in gis.content.search(query=f"owner:{gis.users.me.username}", item_type="Feature Service", max_items=100)
                                    if item.created > start_timestamp and item.created < end_timestamp]
        del end_timestamp, start_timestamp

        title = "Item Title"
        item_type = "Item Type"
        publish = "Published"
        #headings = f"{title:40}{item_type:25}{publish:40}"
        headings = f"{title:40}"
        #print()
        del title, item_type, publish

        titles = []
        for content in content_published_202412:
            #print(f"{content.title:<40}{content.type:25}{readable_date(content.created):40}")
            titles.append(content.title)
            del content

        del content_published_202412

##        print(headings)
##        for title in sorted(titles):
##            print(title)
##            del title
        del headings
        #del titles

        item_profile = ['description', 'thumbnail', 'snippet']

        item_profile_status = {}

        user = gis.users.me
        print(f"{user.username.upper()}\n{'-'*50}")
        print(f"\tRoot Folder: {user.username.lower()}\n\t{'='*25}")
        if user.items():
            print(f"\t\t- {len(user.items())} items")
            for item in user.items():
                missing_item_atts = get_missing_item_attrs(item, item_profile)
                #item_profile_status[item.title[:50] + '_' + str(int(item.created/1000))] = missing_item_atts
                if item.title[:50] in titles:
                    item_profile_status[item.title[:50]] = missing_item_atts
                del item
        else:
            print(f"\t\t- {len(user.items())} items")
        if user.folders:
              for folder in user.folders:
                  if user.items(folder=folder):
                      print(f"\t{folder['title']}\n\t{'='*25}")
                      print(f"\t\t- {len(user.items(folder=folder))} items")
                      for item in user.items(folder=folder):
                          missing_item_atts = get_missing_item_attrs(item, item_profile)
                          #item_profile_status[item.title[:50] + '_' + str(int(item.created/1000))] = missing_item_atts
                          if item.title[:50] in titles:
                                item_profile_status[item.title[:50]] = missing_item_atts
                          del item
                  else:
                      print(f"\t{folder['title'].capitalize()}\n\t{'='*25}")
                      print(f"\t\t-0 items")
                  del folder
        print("\n")

        del user
        del titles

        #print(item_profile_status)
        new_item_profile = item_profile + ['itemID', 'url']
        #print(new_item_profile)

        #pd.set_option('display.max_colwidth', 175) # for display of lengthy text values
        #item_profile_df = pd.DataFrame(data=item_profile_status, index=new_item_profile).T
        #print(item_profile_df)
        #del item_profile_df

        #for key in item_profile_status:
        #    print(key)
        #    print(item_profile_status[key])
        #    del key

        del item_profile_status
        del new_item_profile
        del item_profile, missing_item_atts

        # Variables
        del gis

        # Imports
        del GIS, dt, pd

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def download_agol_metadata(project_folder=""):
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        del urllib3
        from arcgis.gis import GIS
        gis = GIS("pro")

        import datetime as dt

        day_start = dt.datetime(2023, 4, 1, 0, 0, 0, 0)
        day_end = dt.datetime(2024, 7, 31, 23, 59, 59, 999999)

        start_timestamp = int(day_start.timestamp() * 1000)
        end_timestamp = int(day_end.timestamp() * 1000)

        del day_start, day_end

        #titles = [item.title for item in gis.content.search(query=f"owner:{gis.users.me.username}", item_type="Feature Service", max_items=1000) if item.created > start_timestamp and item.created < end_timestamp]
        #for title in sorted(titles):
        #    #print(title)
        #    del title

        titles = list()

        item_profile = ['description', 'thumbnail', 'snippet']
        item_profile_status = {}

        items = [item for item in gis.content.search(query=f"owner:{gis.users.me.username}", item_type="Feature Service", max_items=1000) if item.created > start_timestamp and item.created < end_timestamp]

        for item in items:
            print(f"Name: {item.name}")
            print(f"\tID:    {item.id}")
            print(f"\tTitle: {item.title}")
            if not item.title in titles: titles.append(item.title)
            missing_item_atts = get_missing_item_attrs(item, item_profile)
            if item.title[:100] not in item_profile_status:
                item_profile_status[item.title[:100]] = missing_item_atts
            del missing_item_atts

            metadata_folder = rf"{project_folder}\Export"
            metadata_file   = rf"{metadata_folder}\metadata.xml"
            if os.path.isfile(metadata_file):
                os.remove(metadata_file)

            dataset_item = gis.content.get(item.id)
            dataset_item.download_metadata(save_folder=rf'{metadata_folder}')
            if os.path.isfile(metadata_file):
                tmp_cwd = os.getcwd()
                os.chdir(metadata_folder)
                if item.name:
                    if os.path.isfile(f"{item.name}_AGOL.xml"):
                        os.remove(f"{item.name}_AGOL.xml")
                    os.rename("metadata.xml", f"{item.name}_AGOL.xml")
                elif not item.name:
                    if os.path.isfile(f"{item.title}_AGOL.xml"):
                        os.remove(f"{item.title}_AGOL.xml")
                    os.rename("metadata.xml", f"{item.title}_AGOL.xml")
                os.chdir(tmp_cwd)
                del tmp_cwd

            del metadata_file, metadata_folder
            del dataset_item

            del item

        del items
        del item_profile
        del end_timestamp, start_timestamp

        item_profile = ['description', 'thumbnail', 'snippet']
        item_profile_status = {}
        user = gis.users.me
        fss = []
        #print(f"{user.username.upper()}\n{'-'*50}")
        #print(f"\tRoot Folder: {user.username.lower()}\n\t{'='*25}")
        if user.items():
            #print(f"\t\t- {len(user.items())} items")
            for item in user.items():
                #print(f"Item Name:     {item.name}")
                #print(f"\tDescription: {item.description}")

                missing_item_atts = get_missing_item_attrs(item, item_profile)
                #item_profile_status[item.title[:50] + '_' + str(int(item.created/1000))] = missing_item_atts
                if item.title in titles:
                    if item.title[:100] not in item_profile_status:
                        item_profile_status[item.title[:100]] = missing_item_atts
                        if item.title not in fss:
                            fss.append(item.title)
                #xml_string = item.download_metadata(rf"{project_folder}\Export")
                #if xml_string:
                #    print(xml_string)
                #else:
                #    pass
                #del xml_string
                del missing_item_atts
                del item
        else:
            pass
            #print(f"\t\t- {len(user.items())} items")
##        if user.folders:
##            for folder in user.folders:
##                if user.items(folder=folder):
##                    #print(f"\t{folder['title']}\n\t{'='*25}")
##                    #print(f"\t\t- {len(user.items(folder=folder))} items")
##                    for item in user.items(folder=folder):
##                        missing_item_atts = get_missing_item_attrs(item, item_profile)
##                        #item_profile_status[item.title[:50] + '_' + str(int(item.created/1000))] = missing_item_atts
##                        if item.title in titles:
##                            if item.title[:100] not in item_profile_status:
##                                item_profile_status[item.title[:100]] = missing_item_atts
##                                if item.title not in fss:
##                                    fss.append(item.title)
##                        del missing_item_atts
##                        del item
##                else:
##                    pass
##                    #print(f"\t{folder['title'].capitalize()}\n\t{'='*25}")
##                    #print(f"\t\t-0 items")
##                del folder
##        #print("\n")
##        del user

        #for fs in fss:
        #    #print(fs)
        #    del fs

##        print(len(item_profile_status.keys()))
##        print(len(list(set(titles))))
##        print(len(list(set(fss))))
        for key in item_profile_status:
            #print(f"{key:<40} {item_profile_status[key][:5]}")
            print(f"{key:<40} {item_profile_status[key]}")
            del key

##        if len(list(set(titles))) >= len(list(set(fss))):
##            print([t for t in titles if t not in fss])
##        else:
##            print([fs for fs in fss if fs not in titles])

        #print(list(set(titles)))
        #print(list(set(fss)))

        del titles, fss
        del item_profile
        del item_profile_status

        #del new_item_profile

        # Variables
        del gis

        # Imports
        del GIS, dt

        # Function parameters
        del project_folder

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

def main(project_folder=""):
    try:
        from time import gmtime, localtime, strftime, time
        # Set a start time so that we can see how log things take
        start_time = time()
        print(f"{'-' * 80}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       ..\Documents\ArcGIS\Projects\..\{os.path.basename(os.path.dirname(__file__))}\{os.path.basename(__file__)}")
        print(f"Python Version: {sys.version}")
        print(f"Environment:    {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 80}\n")

        download_agol_metadata(project_folder)

        # Variables
        # Imports
        # Function parameters
        del project_folder

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        print(f"\n{'-' * 80}")
        print(f"Python script: {os.path.basename(__file__)}\nCompleted: {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 80}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Exception:
        pass
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

if __name__ == '__main__':
    try:
        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"

        main(project_folder)

        del project_folder



    except:
        traceback.print_exc()