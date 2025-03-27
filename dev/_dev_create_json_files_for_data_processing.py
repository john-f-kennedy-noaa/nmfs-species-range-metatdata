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

        root_dict = {"Esri"        :  0,
                     "dataIdInfo"  :  1,
                     "mdLang"      :  2,
                     "mdChar"      :  3,
                     "distInfo"    :  4,
                     "mdHrLv"      :  5,
                     "mdHrLvName"  :  6,
                     "refSysInfo"  :  7,
                     "spatRepInfo" :  8,
                     "spdoinfo"    :  9,
                     "eainfo"      : 10,

                     "mdContact"   :  20,
                     "mdFileID"    :  21,
                     "dqInfo"      :  22,
                     "mdMaint"     : 10,
                     "spref"       : 14,
                     "contInfo"    : 17,
                     "dataSetFn"   : 18,
                     "Binary"      : 100,
                     "mdDateSt"    :  6,
                     "mdTimeSt"    :  6,
                     #"mdStanName"  : 60,
                     #"mdStanVer"   : 61,
                     }

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

        esri_dict ={"CreaDate"       : 0,
                    "CreaTime"       : 1,
                    "ArcGISFormat"   : 2,
                    "ArcGISstyle"    : 3,
                    "ArcGISProfile"  : 4,
                    "SyncOnce"       : 5,
                    "DataProperties" : 6,
                        "lineage"      : 0,
                        "itemProps"    :  1,
                            "itemName"       :  0,
                            "imsContentType" : 1,
                        "nativeExtBox" :  2,
                            "westBL"     : 0,
                            "eastBL"     : 1,
                            "southBL"    : 2,
                            "northBL"    : 3,
                            "exTypeCode" : 4,
                        "itemLocation" : 3,
                            "linkage"  : 0,
                            "protocol" : 1,
                        "coordRef"     : 4,
                            "type"    : 0,
                            "geogcsn" : 1,
                            "csUnits" : 2,
                            "projcsn" : 3,
                            "peXml"   : 4,
                    "SyncDate"       :  7,
                    "SyncTime"       :  8,
                    "ModDate"        :  9,
                    "ModTime"        : 10,
                    "scaleRange"     : 11,
                    "minScale"       : 12,
                    "maxScale"       : 13,
                   }

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

        dataIdInfo_dict = { "envirDesc"  :  0,
                            "dataLang"   :  1,
                            "dataChar"   :  2,
                            "idCitation" :  3,
                                "resTitle"     : 0,
                                "resAltTitle"  : 1,
                                "collTitle"    : 2,
                                "date"         : 3,
                                "presForm"     : 4,
                                    "PresFormCd" : 0,
                                "citRespParty" : 5,
                            "spatRpType" :  4,
                            "dataExt"    :  5,
                                "exDesc"  : 0,
                                "geoEle"  : 1,
                                    "GeoBndBox" : 0,
                                        "exTypeCode" : 0,
                                        "westBL"     : 1,
                                        "eastBL"     : 2,
                                        "northBL"    : 3,
                                        "southBL"    : 4,
                                "tempEle" : 2,
                                    "TempExtent" : 0,
                                        "exTemp" : 0,
                                            "TM_Period"  : 0,
                                                "tmBegin" : 0,
                                                "tmEnd"   : 1,
                                            "TM_Instant" : 1,
                                                "tmPosition" : 0,
                            "searchKeys" :  1,
                            "idPurp"     :  2,
                            "idAbs"      :  3,
                            "idCredit"   :  4,
                            "idStatus"   :  5,
                            "resConst"   :  6,
                            "discKeys"   :  7,
                                "keyword"   : 0,
                                "thesaName" : 1,
                                    "resTitle" : 0,
                                    "date"     : 1,
                                        "createDate" : 0,
                                        "pubDate"    : 1,
                                        "reviseDate" : 2,
                                    "citOnlineRes" : 2,
                                        "linkage" : 0,
                                        "orFunct" : 1,
                                            "OnFunctCd" : 0,
                                    "thesaLang" : 2,
                                        "languageCode" : 0,
                                        "countryCode"  : 1,
                            "themeKeys"  :  8,
                                "keyword"   : 0,
                                "thesaName" : 1,
                                    "resTitle" : 0,
                                    "date"     : 1,
                                        "createDate" : 0,
                                        "pubDate"    : 1,
                                        "reviseDate" : 2,
                                    "citOnlineRes" : 2,
                                        "linkage" : 0,
                                        "orFunct" : 1,
                                            "OnFunctCd" : 0,
                                    "thesaLang" : 2,
                                        "languageCode" : 0,
                                        "countryCode"  : 1,
                            "placeKeys"  :  9,
                                "keyword"   : 0,
                                "thesaName" : 1,
                                    "resTitle" : 0,
                                    "date"     : 1,
                                        "createDate" : 0,
                                        "pubDate"    : 1,
                                        "reviseDate" : 2,
                                    "citOnlineRes" : 2,
                                        "linkage" : 0,
                                        "orFunct" : 1,
                                            "OnFunctCd" : 0,
                                    "thesaLang" : 2,
                                        "languageCode" : 0,
                                        "countryCode"  : 1,
                            "tempKeys"   : 10,
                                "keyword"   : 0,
                                "thesaName" : 1,
                                    "resTitle" : 0,
                                    "date"     : 1,
                                        "createDate" : 0,
                                        "pubDate"    : 1,
                                        "reviseDate" : 2,
                                    "citOnlineRes" : 2,
                                        "linkage" : 0,
                                        "orFunct" : 1,
                                            "OnFunctCd" : 0,
                                    "thesaLang" : 2,
                                        "languageCode" : 0,
                                        "countryCode"  : 1,
                            "otherKeys"  : 11,
                                "keyword"   : 0,
                                "thesaName" : 1,
                                    "resTitle" : 0,
                                    "date"     : 1,
                                        "createDate" : 0,
                                        "pubDate"    : 1,
                                        "reviseDate" : 2,
                                    "citOnlineRes" : 2,
                                        "linkage" : 0,
                                        "orFunct" : 1,
                                            "OnFunctCd" : 0,
                                    "thesaLang" : 2,
                                        "languageCode" : 0,
                                        "countryCode"  : 1,
                            "idPoC"      : 11,
                            "resMaint"   : 12,

                            "tpCat"      : 18,
                           }

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

        idCitation_dict = {"idCitation" : 0,
                                "resTitle"    : 0,
                                "resAltTitle" : 1,
                                "collTitle"   : 2,
                                "presForm"    : 3,
                                    "PresFormCd"  : 0,
                                    "fgdcGeoform" : 1,
                                "date"        : 4,
                                    "createDate" : 0,
                                    "pubDate"    : 1,
                                    "reviseDate" : 2,
                                "citRespParty"  : 6,
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

        distInfo_dict = {"distributor" : 0,
                            "distFormat" : 0,
                                "formatName"   : 0,
                                "formatVer"    : 1,
                                "fileDecmTech" : 2,
                                "formatInfo"   : 3,
                            "distorTran" : 1,
                                "unitsODist" : 0,
                                "transSize"  : 1,
                                "onLineSrc"  : 2,
                                   "linkage" : 0,
                                   "protocol" : 1,
                                   "orName" : 2,
                                   "orDesc" : 3,
                                   "orFunct" : 4,
                                      "OnFunctCd" : 0,
                            "distorCont" : 2,
                           }

        import json
        json_path = rf"{project_folder}\distInfo_dict.json"
        # Write to File
        with open(json_path, 'w') as json_file:
            json.dump(distInfo_dict, json_file, indent=4)
        del json_file
        del distInfo_dict
        with open(json_path, "r") as json_file:
            distInfo_dict = json.load(json_file)
        del json_file
        print(distInfo_dict)
        del distInfo_dict
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
        contact_dict = {"citRespParty" : [{"role"  : "Custodian",        "rpIndName" : "Timothy J Haverland", "eMailAdd" : "tim.haverland@noaa.gov"},],
                        "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Melissa Ann Karp",    "eMailAdd" : "melissa.karp@noaa.gov"},],
                        "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "Timothy J Haverland", "eMailAdd" : "tim.haverland@noaa.gov"},],
                        "mdContact"    : [{"role"  : "Author",           "rpIndName" : "John F Kennedy",      "eMailAdd" : "john.f.kennedy@noaa.gov"},],
                        "stepProc"     : [{"role"  : "Processor",        "rpIndName" : "John F Kennedy",      "eMailAdd" : "john.f.kennedy@noaa.gov"},
                                          {"role"  : "Processor",        "rpIndName" : "Melissa Ann Karp",    "eMailAdd" : "melissa.karp@noaa.gov"},
                                         ],}

        import json
        json_path = rf"{project_folder}\contact_dict.json"
        # Write to File
        #with open(json_path, 'w') as json_file:
        #    json.dump(contact_dict, json_file, indent=4)
        #del json_file
        #del contact_dict
        with open(json_path, "r") as json_file:
            contact_dict = json.load(json_file)
        del json_file
        print(contact_dict)
        del contact_dict
        del json_path
        del json

        # ###################### DisMAP ########################################
        # ###################### ESA ########################################

        contact_dict = {"citRespParty" : [{"role"  : "Custodian",        "rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "idPoC"        : [{"role"  : "Point of Contact", "rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "distorCont"   : [{"role"  : "Distributor",      "rpIndName" : "NMFS Office of Protected Resources", "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "mdContact"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "srcCitatn"    : [{"role"  : "Author",           "rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},],
                        "stepProc"     : [{"role" : "Processor",         "rpIndName" : "Nikki Wildart",                      "eMailAdd" : "nikki.wildart@noaa.gov"},
                                          {"role" : "Processor",         "rpIndName" : "Dan Lawson",                         "eMailAdd" : "dan.lawson@noaa.gov"},
                                          {"role" : "Processor",         "rpIndName" : "Jeffrey A. Seminoff",                "eMailAdd" : "jeffrey.seminoff@noaa.gov"},
                                          {"role" : "Processor",         "rpIndName" : "Jennifer Schultz",                   "eMailAdd" : "jennifer.schultz@noaa.gov"},
                                          {"role" : "Processor",         "rpIndName" : "Jonathan Molineaux",                 "eMailAdd" : "jonathan.molineaux@noaa.gov"},
                                          {"role" : "Processor",         "rpIndName" : "Marc Romano",                        "eMailAdd" : "marc.romano@noaa.gov"},
                                          {"role" : "Processor",         "rpIndName" : "Susan Wang",                         "eMailAdd" : "susan.wang@noaa.gov"},
                                         ],}

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

        # Declared Variables
        del project_folder
        # Imports
    except:
        traceback.print_exc()
    else:
        pass
    finally:
        pass
