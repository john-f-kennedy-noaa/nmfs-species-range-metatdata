import hermes
if __name__ == "__main__":
    fc = r"{os.environ['USERPROFILE']}\Documents\ArcGIS\Projects\hermes-master\National Mapper.gdb\AbaloneBlack_20210712"
    paperwork = hermes.Paperwork(dataset=fc)
    data = paperwork.convert()
    # Updated by JFK December 21, 2024 @ 6:28 PM
    #for k,v in data.iteritems():
    for k,v in data.items():
        print( k, v )