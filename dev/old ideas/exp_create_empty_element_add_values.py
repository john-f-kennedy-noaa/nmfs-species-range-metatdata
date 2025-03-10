#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     12/01/2025
# Copyright:   (c) john.f.kennedy 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    try:
        import traceback
        from lxml import etree

        #print("Serialisation")
        contact_dict = {"Susan Wang" : {"editorSource"                    : "",
                                        "editorDigest"                    : "",
                                        "rpIndName"                       : "Susan Wang",
                                        "rpOrgName"                       : "Protected Resources Division, West Coast Region, National Marine Fisheries Service",
                                        "rpPosName"                       : "Black Abalone Recovery Coordinator",
                                        "rpCntInfo/cntAddress/delPoint"   : "501 West Ocean Boulevard, Suite 4200",
                                        "rpCntInfo/cntAddress/city"       : "Long Beach",
                                        "rpCntInfo/cntAddress/adminArea"  : "CA",
                                        "rpCntInfo/cntAddress/postCode"   : "90802",
                                        "rpCntInfo/cntAddress/eMailAdd"   : "susan.wang@noaa.gov",
                                        "rpCntInfo/cntAddress/country"    : "US",
                                        "rpCntInfo/cntPhone/voiceNum"     : "(562) 980-4199",
                                        "rpCntInfo/cntPhone/faxNum"       : "(562) 980-4199",
                                        "rpCntInfo/cntHours"              : "0700 - 1800 PST/PDT",
                                        "rpCntInfo/cntOnlineRes/linkage"  : "https://www.fisheries.noaa.gov/about/west-coast-region</linkage>",
                                        "rpCntInfo/cntOnlineRes/protocol" : "REST Service",
                                        "rpCntInfo/cntOnlineRes/orName"   : "West Coast Region NOAA Fisheries",
                                        "rpCntInfo/cntOnlineRes/orDesc"   : "About the West Coast Region of NOAA Fisheries",
                                        "displayName"                     : "Susan Wang",
                                        "editorSave"                      : "True",
                                     },}

        #root = etree.XML('<root><a><b/></a></root>')
        parent = "distorCont"
        root = etree.XML(f'<{parent}><editorSource/><editorDigest/><rpIndName/><rpOrgName/><rpPosName/><rpCntInfo><cntAddress addressType="both"><delPoint/><city/><adminArea/><postCode/><eMailAdd/><country>US</country></cntAddress><cntPhone><voiceNum tddtty=""></voiceNum><faxNum/></cntPhone><cntHours/><cntOnlineRes><linkage/><protocol/><orName/><orDesc/><orFunct><OnFunctCd value="002"></OnFunctCd></orFunct></cntOnlineRes></rpCntInfo><editorSave/><displayName/><role><RoleCd value="005"></RoleCd></role></{parent}>')
        #print(etree.tostring(root))

        for user in contact_dict:
            #print(f"{user}")
            user_dict = contact_dict[user]
            for key in user_dict:
                #print(f"\t{key}")
                element = root.find(f"./{key}")
                element.text = user_dict[key]

        #xml_string = etree.tostring(root, encoding='UTF-8', xml_declaration=True)
        #print(xml_string.decode(), end='')
        #print(etree.tostring(root, method='html', encoding='UTF-8', xml_declaration=True, pretty_print=True).decode(), end='')
        print(etree.tostring(root, encoding='UTF-8', xml_declaration=True, pretty_print=True).decode())






    ##    class ParserTarget:
    ##        events = []
    ##        close_count = 0
    ##        def start(self, tag, attrib):
    ##            self.events.append(("start", tag, attrib))
    ##        def close(self):
    ##            events, self.events = self.events, []
    ##            self.close_count += 1
    ##            return events
    ##
    ##    parser_target = ParserTarget()
    ##
    ##    parser = etree.XMLParser(target=parser_target)
    ##    events = etree.fromstring('<root test="true"/>', parser)
    ##
    ##    print(parser_target.close_count)
    ##
    ##    for event in events:
    ##        print(f'event: {event[0]} - tag: {event[1]}')
    ##        for attr, value in event[2].items():
    ##            print(f' * {attr} = {value}')
    ##
    ##    events = etree.fromstring('<root test="true"/>', parser)
    ##    print(parser_target.close_count)
    ##
    ##    events = etree.fromstring('<root test="true"/>', parser)
    ##    print(parser_target.close_count)
    ##
    ##    events = etree.fromstring('<root test="true"/>', parser)
    ##    print(parser_target.close_count)
    ##
    ##    for event in events:
    ##        print(f'event: {event[0]} - tag: {event[1]}')
    ##        for attr, value in event[2].items():
    ##            print(f' * {attr} = {value}')
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
