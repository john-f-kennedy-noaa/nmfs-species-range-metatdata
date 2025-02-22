"""
This sample shows how users can walk a metadata structure to find the
information they need quickly.  This sample shows only the XPath to each
item in the metadata and prints it out to the screen.
"""
import hermes
import os
import arcpy

def listKeyValues(d, path=""):
    """ simple recursive print function to walk the metadata structure"""
    # Updated by JFK December 21, 2024 @ 6:43 PM
    #for k,v in d.iteritems():
    for k,v in d.items():
        if path != "":
            path += f"/{k}"
        else:
            path = k
        print( f"Key - {path}" )
        if isinstance(v, dict):
            listKeyValues(v, path)
        #else:
        #    print(path)

def get_all_keys(d):
    keys = []
    for k, v in d.items():
        keys.append(k)
        #print(k)
        if isinstance(v, dict):
            keys.extend(get_all_keys(v))
            #keys.append(get_all_keys(v))
        else:
            if not k.startswith("@") and not k.startswith("#"):
                print(k, keys)
    return keys

##def get_keys(dictionary):
##    result = []
##    for key, value in dictionary.items():
##        if type(value) is dict:
##            new_keys = get_keys(value)
##            result.append(key)
##            for innerkey in new_keys:
##                result.append(f'{key}/{innerkey}')
##        else:
##            result.append(key)
##    return result

def generic_items(dict_or_list):
    if isinstance(dict_or_list, dict):
        return dict_or_list.items()
    if isinstance(dict_or_list, list):
        return enumerate(dict_or_list)

def get_keys(dictionary):
    result = []
    for key, value in generic_items(dictionary):
        if isinstance(value, dict) or isinstance(value, list):
            new_keys = get_keys(value)
            result.append(key)
            for innerkey in new_keys:
                result.append(f'{key}/{innerkey}')
        else:
            result.append(key)
    return result

def main():
    from arcpy import metadata as md
    from lxml import etree
    from io import StringIO

    arcpy.env.workspace = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\hermes-master\National Mapper.gdb"

    for fc in arcpy.ListFeatureClasses():
        if fc == "AbaloneBlack_20210712":

            dataset_md = md.Metadata(fc)
            # get the item's metadata xml
            dataset_md_xml = dataset_md.xml

            # Parse the XML file
            tree = etree.parse(StringIO(dataset_md_xml))

            # Get the root element
            root = tree.getroot()

            #print(eainfo_old_root.tag)
            #print(eainfo_old_root.find("eainfo").tag)
            #print(eainfo_new_root.tag)


            data = hermes.Paperwork(dataset=os.path.join(arcpy.env.workspace, fc)).convert()
            results = get_keys(data)
            for result in sorted(results):
                #print(result)

                #print(f"print('{result} : '+" + "'' if isinstance(data['" + result.replace("/", "']['") + "'])")
                #print('metadata : '+ "" if isinstance(data['metadata'], dict) else data['metadata'])
                result_keys = " 'DICT' if isinstance(data['" + result.replace("/", "']['") + "'], dict) or isinstance(data['" + result.replace("/", "']['") + "'], list) else data['" + result.replace("/", "']['") + "'])"
                print(f"print('{result} :'" + f"{result_keys}")



##                #if not any(l in result for l in ['@Sync', '#text', '@export']):
##                if not any(result.endswith(l) for l in ['@Name', '@Sync', '@value', '#text', '@export', '@esriExtentType', '@addressType', '@dimension', '@code']):
##                    try:
##                        #print(result[9:])
##                        if root.find(f"./{result[9:]}") is not None:
##                            #print(f"./{result[9:]}")
##                            if root.find(f"./{result[9:]}").text:
##                                print(f"\t./{result[9:]}" + "\t" + root.find(f"./{result[9:]}").text)
##
##                            #print(root.find(f"{result[9:]}").tag)
##                            #print(root.find(f"{result[9:]}").text)
##                    except:
##                        pass
##                        #print(f"problem child: {result}")
                del result

            del root, tree
            del results, data
            del dataset_md, dataset_md_xml

    del md, etree, StringIO

if __name__ == "__main__":
    main()
