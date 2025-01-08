"""
This sample shows how to use Hermes to edit metadata
"""
import hermes
import os


if __name__ == "__main__":
    fc = r"C:\Users\john.f.kennedy\Documents\ArcGIS\Projects\hermes-master\National Mapper.gdb\AbaloneBlack_20210712"
    #  Access the item's metadata
    #
    metadata = hermes.Paperwork(dataset=fc)
    # convert the XML to a dictionary
    #
    data = metadata.convert()
    #  Make some generic changes
    #
    #data['metadata']['dataIdInfo']['idAbs'] = "Hermes Was Here - changed an abstract"
    #data['metadata']['dataIdInfo']['idPurp'] = "Hermes Was Here - changed purpose"
    print(data['metadata'])
    print(data['metadata']['dataIdInfo']['idAbs'])
    print(data['metadata']['dataIdInfo']['idPurp'])
    print(data['metadata']['dataIdInfo']['dataLang']['countryCode']['@Sync'])

    #print('metadata/spatRepInfo/VectSpatRep/topLvl/TopoLevCd/@value :' 'DICT' if isinstance(data['metadata']['spatRepInfo']['VectSpatRep']['topLvl']['TopoLevCd']['@value'], dict) or isinstance(data['metadata']['spatRepInfo']['VectSpatRep']['topLvl']['TopoLevCd']['@value'], list) else data['metadata']['spatRepInfo']['VectSpatRep']['topLvl']['TopoLevCd']['@value'])

    print(data['metadata']['dataIdInfo']['idPoC'])