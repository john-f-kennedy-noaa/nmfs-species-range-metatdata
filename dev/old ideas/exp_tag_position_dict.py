#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     16/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Python Built-in's modules are loaded first
import os, sys
import traceback, inspect

# Third-party modules are loaded second
# import arcpy

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main(project_folder=""):
    try:
        del project_folder

        tag_position_dict = {
                             "dqScope": 0,
                             "report" : {"DQConcConsis" : 1, "DQCompOm" : 2},
                             "dataLineage" : 3,
                            }

        for tag in tag_position_dict:
            print(f"Tag: {tag}" )
            if isinstance(tag_position_dict[tag], dict):
                for key in tag_position_dict[tag]:
                    print(f"\tKey: {key}")
                    position = tag_position_dict[tag][key]
                    print(f"\t{tag}/{key}, {position}")
                    del key
            else:
                position = tag_position_dict[tag]
                print(f"\t{tag}, {position}")
            del position
            del tag

        print(tag_position_dict["dqScope"])
        print(tag_position_dict["report"]["DQConcConsis"])
        print(tag_position_dict["report"]["DQCompOm"])
        print(tag_position_dict["dataLineage"])

        del tag_position_dict

    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: raise Warning(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass
        # Cleanup
        # arcpy.management.ClearWorkspaceCache()

if __name__ == '__main__':
    try:
        main(project_folder=rf"{os.path.dirname(os.path.dirname(__file__))}")
    except Warning as w:
        print(w)