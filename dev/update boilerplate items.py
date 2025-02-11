#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/01/2025
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

def strip_escape_characters(escaped_text):
    try:
        from bs4 import BeautifulSoup
        from html import unescape
        soup = BeautifulSoup(unescape(escaped_text), 'lxml')
        unescaped_text = soup.text
        # Deletet Imports
        del BeautifulSoup, unescape, soup
        # Del Function parameters
        del escaped_text

##        from bs4 import BeautifulSoup
##        import html
##
##        soup = BeautifulSoup(escaped_text, 'html.parser')
##
##        # Unescape HTML entities except carriage return
##        unescaped_text = html.unescape(soup.get_text()).replace('\n', '\r\n')
##
##        #print(unescaped_text)
##        # Deletet Imports
##        del BeautifulSoup, html
##        # Del Function parameters
##        del escaped_text, soup

    except:
        traceback.print_exc()
    else:
        return unescaped_text
    finally:
        del unescaped_text
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def process_list(folder, wildcard):
    try:
        from arcpy import metadata as md
        files = [f for f in os.listdir(folder) if wildcard in f]

        for file in files:
            print(file)
            dataset_md = md.Metadata(rf"{folder}\{file}")
            old_description = dataset_md.description
            if old_description:
                new_description = strip_escape_characters(old_description)
                #dataset_md.description = new_description
                #dataset_md.synchronize('SELECTIVE')
                #dataset_md.save()
                print("DESCRIPTION")
                #print(new_description)
                del new_description
            del old_description
            old_accessConstraints = dataset_md.accessConstraints
            if old_accessConstraints:
                new_accessConstraints = strip_escape_characters(old_accessConstraints)
                #dataset_md.accessConstraints = new_accessConstraints
                #dataset_md.synchronize('SELECTIVE')
                #dataset_md.save()
                print("ACCESS CONTRAINTS")
                print(new_accessConstraints)
                del new_accessConstraints
            del old_accessConstraints

            del dataset_md
            del file
        del files

        # Function parameters
        del folder, wildcard
        # Imports
        del md

    except Warning as w:
        print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
    except Exception as e:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def update_access_constraints(folder, wildcard):
    try:
        from arcpy import metadata as md
        files = [f for f in os.listdir(folder) if wildcard in f]

        for file in files:
            print(file)
            dataset_md = md.Metadata(rf"{folder}\{file}")
            dataset_md.accessConstraints = str('&lt;DIV STYLE="text-align:Left;"&gt;&lt;DIV&gt;&lt;DIV&gt;&lt;DIV STYLE="font-size:10pt"&gt;&lt;P&gt;&lt;SPAN&gt;*** Attribution *** Whenever NMFS material is reproduced and re-disseminated, we request that users attribute the material appropriately. Pursuant to 17 U.S. C. 403, parties who produce copyrighted works consisting predominantly of material created by the Federal Government are encouraged to provide notice with such work(s) identifying the U.S. Government material incorporated and stating that such material is not subject to copyright protection. Please cite the species range datasets as indicated in the metadata for each species, or if not indicated, as follows with the appropriate information substituted for all text in {CURLY BRACKETS}: &lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;NOAA Fisheries Service. Endangered Species Act Species Range Geodatabase. Silver Spring, MD: National Oceanic and Atmospheric Administration (NOAA), National Marine Fisheries Service (NMFS), Office of Protected Resources (OPR) [producer] {GEODATABASE PUBLICATION DATE}. {ADD URL}&lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;***No Warranty*** The user assumes the entire risk related to its use of these data. NMFS is providing these data "as is," and NMFS disclaims any and all warranties, whether express or implied, including (without limitation) any implied warranties of merchantability or fitness for a particular purpose. No warranty expressed or implied is made regarding the accuracy or utility of the data on any other system or for general or scientific purposes, nor shall the act of distribution constitute any such warranty. It is strongly recommended that careful attention be paid to the contents of the metadata file associated with these data to evaluate dataset limitations, restrictions or intended use. In no event will NMFS be liable to you or to any third party for any direct, indirect, incidental, consequential, special or exemplary damages or lost profit resulting from any use or misuse of this data. &lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;*** Proper Usage *** The information on government servers are in the public domain, unless specifically annotated otherwise, and may be used freely by the public. Before using information obtained from this server, special attention should be given to the date and time of the data and products being displayed. This information shall not be modified in content and then presented as official government material. This dataset was created to generally represent our best professional judgment of the ranges of listed species based on the best available information at the time of publication, including: geographic factors, time of year, and the biology of each species. The dataset should not be used to infer information regarding the existence or details of other marine features or resources, including, but not limited to, navigable waters, coastlines, bathymetry, submerged features, or man-made structures. Users assume responsibility for determining the appropriate use of this dataset. &lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;*** Temporal Considerations *** Species’ ranges are subject to change or modification. Generally, we become aware of these changes during the 5-year review of the species’ status, as required under the ESA. If changes to the range are deemed necessary, we will make such changes in the database, which will be archived and replaced by an updated version as soon as feasible. It is the user’s responsibility to ensure the most recent species’ range data are being used. &lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;*** Shorelines/Base Layers *** The accuracy of this dataset is dependent upon the accuracy and resolution of the datasets (e.g. shoreline, hydrography, bathymetry, shared administrative boundaries) used in the creation process. Source datasets used are specified in the metadata. These data sources were selected for their suitability to a broad audience, and may not be suitable for specific uses requiring higher-resolution information. Coastlines and water body boundaries change. Unless otherwise noted, where the National Hydrography Dataset or NOAA Medium Resolution Shoreline is used, assume the boundary reaches the most current river, estuary, or coastal shoreline delineation available.&lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;*** Data Limitations ***&lt;/SPAN&gt;&lt;/P&gt;&lt;P&gt;&lt;SPAN&gt;Our data may lack the spatial resolution to capture the entire range of a species, especially outside of a major waterway (e.g., in a very small tributary, or shallow area near a marsh). For section 7 consultations, we recommend that Federal action agencies request technical assistance to verify presence/absence of listed species within their action area.&lt;/SPAN&gt;&lt;/P&gt;&lt;/DIV&gt;&lt;/DIV&gt;&lt;/DIV&gt;&lt;/DIV&gt;')
            #dataset_md.synchronize('SELECTIVE')
            dataset_md.save()
            del dataset_md
            del file
        del files

        # Function parameters
        del folder, wildcard
        # Imports
        del md

    except Warning as w:
        print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
    except Exception as e:
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

def main():
    try:
        from time import gmtime, localtime, strftime, time

        # Set a start time so that we can see how log things take
        start_time = time()

        print(f"{'-' * 90}")
        print(f"Python Script:  {os.path.basename(__file__)}")
        print(f"Location:       {os.path.dirname(__file__)}")
        print(f"Python Version: {sys.version} Environment: {os.path.basename(sys.exec_prefix)}")
        print(f"{'-' * 90}\n")

        folder = rf"{os.path.dirname(__file__)}\Export"

        #process_list(folder=folder, wildcard=".xml")
        update_access_constraints(folder=folder, wildcard=".xml")

        del folder

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time

        print(f"\n{'-' * 90}")
        print(f"Python script: {os.path.basename(__file__)} successfully completed {strftime('%a %b %d %I:%M %p', localtime())}")
        print(u"Elapsed Time {0} (H:M:S)".format(strftime("%H:%M:%S", gmtime(elapse_time))))
        print(f"{'-' * 90}")
        del elapse_time, end_time, start_time
        del gmtime, localtime, strftime, time

    except Warning as w:
        print(f"{w} captured in the '{inspect.stack()[0][3]}' function")
    except Exception as e:
        print(f"{e} captured in the '{inspect.stack()[0][3]}' function")
    except:
        traceback.print_exc()
    else:
        return True
    finally:
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk

if __name__ == '__main__':
    main()
