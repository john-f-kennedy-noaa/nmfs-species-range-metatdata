#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     11/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import traceback

def main():
    try:

        default_list = ['editorSource', 'editorDigest', 'rpIndName', 'rpOrgName', 'rpPosName', 'rpCntInfo', 'cntOnlineRes', 'displayName', 'editorSave', 'role']
        current_list = ['editorSource', 'editorDigest', 'rpIndName', 'rpOrgName', 'rpPosName', 'rpCntInfo', 'editorSave', 'displayName', 'role']

        #print(current_list)

        the_missing = [i for i in default_list if i not in current_list]
        #print(the_missing)

        default_list_dict = {i:default_list.index(i) for i in default_list}
        #print(default_list_dict)

        new_list = current_list + the_missing
        #default_list = []

        #print(default_list)

        for key in default_list_dict:
            #print(key)
            old_index = new_list.index(key)
            new_index = default_list_dict[key]
            new_list.pop(old_index)
            new_list.insert(new_index, key)

        for item in new_list:
            print(item)

    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
