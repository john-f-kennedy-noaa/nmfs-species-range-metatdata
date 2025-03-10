# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     03/03/2024
# Copyright:   (c) john.f.kennedy 2024
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import os, sys  # built-ins first
import traceback
import importlib
import inspect

#import arcpy  # third-parties second

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

        root_dict = {"Esri"       :  0, "dataIdInfo"  :  1, "mdChar"      :  2,
                     "mdContact"  :  3, "mdDateSt"    :  4, "mdFileID"    :  5,
                     "mdLang"     :  6, "mdMaint"     :  7, "mdHrLv"      :  8,
                     "mdHrLvName" :  9, "mdStanName"  : 10, "mdStanVer"   : 11,
                     "refSysInfo" : 12, "spatRepInfo" : 13, "spdoinfo"    : 14,
                     "dqInfo"     : 15, "distInfo"    : 16, "eainfo"      : 17,
                     "contInfo"   : 18, "spref"       : 19, "spatRepInfo" : 20,
                     "dataSetFn"  : 19, "Binary"      : 100,}

        import json
        json_path = rf"{project_folder}\root_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(root_dict, json_file, indent=4)
        del json_file
        del root_dict
        with open(json_path, "r") as json_file:
            root_dict = json.load(json_file)
        del json_file
        print(root_dict)
        del root_dict
        del json_path
        del json

        esri_dict ={"CreaDate"      :  0, "CreaTime"   :  1, "ArcGISFormat"   : 2,
                    "ArcGISstyle"   :  3, "SyncOnce"   :  4, "DataProperties" : 5,
                    "itemProps"     :  0, "itemName"   :  0, "imsContentType" : 1,
                    "nativeExtBox"  :  2, "westBL"     :  0, "eastBL"   :  1, "southBL"  : 2,
                    "northBL"       :  3, "exTypeCode" :  4, "coordRef" :  1, "type"     : 0,
                    "geogcsn"       :  2, "csUnits"    :  3, "peXml"    :  4, "SyncDate" : 6,
                    "SyncTime"      :  7, "ModDate"    :  8, "ModTime"  :  9,
                    "scaleRange"    : 10, "minScale"   : 11, "maxScale" : 12,
                    "ArcGISProfile" : 13,}

        import json
        json_path = rf"{project_folder}\esri_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(esri_dict, json_file, indent=4)
        del json_file
        del esri_dict
        with open(json_path, "r") as json_file:
            esri_dict = json.load(json_file)
        del json_file
        print(esri_dict)
        del esri_dict
        del json_path
        del json

        dataIdInfo_dict = { "idCitation" :  0, "searchKeys" :  1, "idPurp"    : 2,
                            "idAbs"      :  3, "idCredit"   :  4, "idStatus"  : 5,
                            "idPoC"      :  6, "themeKeys"  :  7, "placeKeys" : 8,
                            "tempKeys"   : 9, "otherKeys"   : 10, "resConst"  : 12,
                            "resMaint"   : 13, "envirDesc"  : 14, "dataLang"  : 15,
                            "dataChar"   : 16, "spatRpType" : 17, "dataExt"   : 18,
                            "" : 19, "tpCat"      : 20,}

        import json
        json_path = rf"{project_folder}\dataIdInfo_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(dataIdInfo_dict, json_file, indent=4)
        del json_file
        del dataIdInfo_dict
        with open(json_path, "r") as json_file:
            dataIdInfo_dict = json.load(json_file)
        del json_file
        print(dataIdInfo_dict)
        del dataIdInfo_dict
        del json_path
        del json

        idCitation_dict = {"idCitation" : 0, "resTitle" : 0, "resAltTitle" : 1,
                           "collTitle"  : 2, "presForm" : 3, "PresFormCd"  : 0,
                           "fgdcGeoform" : 1, "date" : 4, "createDate" : 0,
                           "pubDate"    : 1, "reviseDate" : 2, "citRespParty"  : 6,
                           }

        import json
        json_path = rf"{project_folder}\idCitation_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(idCitation_dict, json_file, indent=4)
        del json_file
        del idCitation_dict
        with open(json_path, "r") as json_file:
            idCitation_dict = json.load(json_file)
        del json_file
        print(idCitation_dict)
        del idCitation_dict
        del json_path
        del json

        contact_dict = {"editorSource" : 0, "editorDigest" : 1,"rpIndName"     : 2,
                        "rpOrgName"    : 3, "rpPosName"    : 4, "rpCntInfo"    : 5,
                        "cntAddress"   : 0, "delPoint"     : 0, "city"         : 1,
                        "adminArea"    : 2, "postCode"     : 3, "eMailAdd"     : 4,
                        "country"      : 5, "cntPhone"     : 1, "voiceNum"     : 0,
                        "faxNum"       : 1, "cntHours"     : 2, "cntOnlineRes" : 3,
                        "linkage"      : 0, "protocol"     : 1, "orName"       : 2,
                        "orDesc"       : 3, "orFunct"      : 4, "OnFunctCd"    : 0,
                        "editorSave"   : 6, "displayName"  : 7, "role"         : 8,
                        "RoleCd"       : 0,
                        }

        import json
        json_path = rf"{project_folder}\contact_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(contact_dict, json_file, indent=4)
        del json_file
        del contact_dict
        with open(json_path, "r") as json_file:
            contact_dict = json.load(json_file)
        del json_file
        print(contact_dict)
        del contact_dict
        del json_path
        del json

        dqInfo_dict = { "dqScope"        : 0,
                            "scpLvl"     : 0,
                            "ScopeCd"    : 0,
                            "scpLvlDesc" : 1,
                            "datasetSet" : 0,
                        "report"         : 1,
                            "measDesc"   : 0,
                            "measResult" : 1,
                        "dataLineage"    : 3,
                            "statement"  : 0,
                            "dataSource" : 1,
                                "srcDesc"    : 0,
                                "srcCitatn"  : 1,
                                    "resTitle"     : 0,
                                    "resAltTitle" : 1,
                                    "collTitle"  : 2,
                                "citOnlineRes" : 2,
                                        "linkage"  : 0,
                                        "protocol" : 1,
                                        "orName"   : 2,
                                        "orDesc"   : 3,
                                        "orFunct" : 4,
                                            "OnFunctCd" : 0,
                                "date"        : 3,
                                    "createDate" : 0,
                                    "pubDate"    : 1,
                                    "reviseDate" : 2,
                                "otherCitDet" : 4,
                                "presForm"    : 5,
                                    "fgdcGeoform" : 0,
                                    "PresFormCd"  : 1,
                                "citRespParty" : 6,
                                    "editorSource" : 0, "editorDigest" : 1,"rpIndName"     : 2,
                                    "rpOrgName"    : 3, "rpPosName"    : 4, "rpCntInfo"    : 5,
                                    "cntAddress"   : 0, "delPoint"     : 0, "city"         : 1,
                                    "adminArea"    : 2, "postCode"     : 3, "eMailAdd"     : 4,
                                    "country"      : 5, "cntPhone"     : 1, "voiceNum"     : 0,
                                    "faxNum"       : 1, "cntHours"     : 2, "cntOnlineRes" : 3,
                                    "linkage"      : 0, "protocol"     : 1, "orName"       : 2,
                                    "orDesc"       : 3, "orFunct"      : 4, "OnFunctCd"    : 0,
                                    "editorSave"   : 6, "displayName"  : 7, "role"         : 8,
                                    "RoleCd"       : 0,
                                "srcMedName" : 7,
                                    "MedNameCd" : 0,
                            "prcStep"    : 3,
                                "stepDesc"   : 0,
                                "stepProc"   : 1,
                                    "editorSource" : 0, "editorDigest" : 1,"rpIndName"     : 2,
                                    "rpOrgName"    : 3, "rpPosName"    : 4, "rpCntInfo"    : 5,
                                    "cntAddress"   : 0, "delPoint"     : 0, "city"         : 1,
                                    "adminArea"    : 2, "postCode"     : 3, "eMailAdd"     : 4,
                                    "country"      : 5, "cntPhone"     : 1, "voiceNum"     : 0,
                                    "faxNum"       : 1, "cntHours"     : 2, "cntOnlineRes" : 3,
                                    "linkage"      : 0, "protocol"     : 1, "orName"       : 2,
                                    "orDesc"       : 3, "orFunct"      : 4, "OnFunctCd"    : 0,
                                    "editorSave"   : 6, "displayName"  : 7, "role"         : 8,
                                    "RoleCd"       : 0,

                                "stepDateTm" : 2,
                                "cntOnlineRes" : 3, "linkage"     : 0,
                                "protocol"   : 1, "orName"       : 2, "orDesc"      : 3,
                                "orFunct"    : 4, "OnFunctCd"    : 0,
                      }

        import json
        json_path = rf"{project_folder}\dqInfo_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(dqInfo_dict, json_file, indent=4)
        del json_file
        del dqInfo_dict
        with open(json_path, "r") as json_file:
            dqInfo_dict = json.load(json_file)
        del json_file
        print(dqInfo_dict)
        del dqInfo_dict
        del json_path
        del json

        RoleCd_dict = {"001" : "Resource Provider", "002" : "Custodian",
                       "003" : "Owner",             "004" : "User",
                       "005" : "Distributor",       "006" : "Originator",
                       "007" : "Point of Contact",  "008" : "Principal Investigator",
                       "009" : "Processor",         "010" : "Publisher",
                       "011" : "Author",            "012" : "Collaborator",
                       "013" : "Editor",            "014" : "Mediator",
                       "015" : "Rights Holder",}

        import json
        json_path = rf"{project_folder}\RoleCd_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(RoleCd_dict, json_file, indent=4)
        del json_file
        del RoleCd_dict
        with open(json_path, "r") as json_file:
            RoleCd_dict = json.load(json_file)
        del json_file
        print(RoleCd_dict)
        del RoleCd_dict
        del json_path
        del json

        #role_dict = {"citRespParty"  : ,
        #             "idPoC"        : ,
        #             "distorCont"   : ,
        #             "mdContact"    : ,
        #             "stepProc"


        tpCat_dict = {"002": '<tpCat><TopicCatCd value="002"></TopicCatCd></tpCat>',
         "007": '<tpCat><TopicCatCd value="007"></TopicCatCd></tpCat>',
         "014": '<tpCat><TopicCatCd value="014"></TopicCatCd></tpCat>',}

        import json
        json_path = rf"{project_folder}\tpCat_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(tpCat_dict, json_file, indent=4)
        del json_file
        del tpCat_dict
        with open(json_path, "r") as json_file:
            tpCat_dict = json.load(json_file)
        del json_file
        print(tpCat_dict)
        del tpCat_dict
        del json_path
        del json

        # ###################### DisMAP ########################################
        contacts = {"citRespParty"     : {"rpIndName" : "Timothy J Haverland",                   "eMailAdd" : "tim.haverland@noaa.gov"},
                        "idPoC"        : {"rpIndName" : "Melissa Karp",                          "eMailAdd" : "melissa.karp@noaa.gov"},
                        "distorCont"   : {"rpIndName" : "NMFS Office of Science and Technology", "eMailAdd" : "tim.haverland@noaa.gov"},
                        "mdContact"    : {"rpIndName" : "John F Kennedy",                        "eMailAdd" : "john.f.kennedy@noaa.gov"},
                        "stepProc"     : [{"rpIndName" : "John F Kennedy",                        "eMailAdd" : "john.f.kennedy@noaa.gov"},
                                          {"rpIndName" : "Melissa Karp",                          "eMailAdd" : "melissa.karp@noaa.gov"},
                                         ],}

        import json
        json_path = rf"{project_folder}\contacts.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(contacts, json_file, indent=4)
        del json_file
        del contacts
        with open(json_path, "r") as json_file:
            contacts = json.load(json_file)
        del json_file
        print(contacts)
        del contacts
        del json_path
        del json

        # ###################### DisMAP ########################################
        # ###################### ESA ########################################

        contacts = {"citRespParty"     : [{"role"  : "Custodian",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "mdContact"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "stepProc"     : [{"role" : "Processor",        "rpIndName" : "Nikki Wildart",       "eMailAdd" : "nikki.wildart@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Dan Lawson",          "eMailAdd" : "dan.lawson@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jeffrey A. Seminoff", "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jennifer Schultz",    "eMailAdd" : "jennifer.schultz@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Jonathan Molineaux",  "eMailAdd" : "jonathan.molineaux@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Marc Romano",         "eMailAdd" : "marc.romano@noaa.gov"},
                                          {"role" : "Processor",        "rpIndName" : "Susan Wang",          "eMailAdd" : "susan.wang@noaa.gov"},
                                         ],}

        import json
        json_path = rf"{project_folder}\contacts.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(contacts, json_file, indent=4)
        del json_file
        del contacts
        with open(json_path, "r") as json_file:
            contacts = json.load(json_file)
        del json_file
        print(contacts)
        del contacts
        del json_path
        del json

        # Declared Varaiables
        # Imports
        # Function Parameters
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
        traceback.print_exc()
    except:
        traceback.print_exc()
    else:
        # While in development, leave here. For test, move to finally
        rk = [key for key in locals().keys() if not key.startswith('__')]
        if rk: print(f"WARNING!! Remaining Keys in the '{inspect.stack()[0][3]}' function: ##--> '{', '.join(rk)}' <--##"); del rk
        return True
    finally:
        pass

if __name__ == "__main__":
    try:
        # Imports
        # Append the location of this scrip to the System Path
        #sys.path.append(os.path.dirname(__file__))
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        project_folder = rf"{os.path.dirname(os.path.dirname(__file__))}"

        main(project_folder=project_folder)

        # Variables
        del project_folder
        # Imports
    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
