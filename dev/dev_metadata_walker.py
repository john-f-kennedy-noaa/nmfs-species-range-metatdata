"""
This sample shows how users can walk a metadata structure to find the
information they need quickly.  This sample shows only the XPath to each
item in the metadata and prints it out to the screen.
"""
import hermes
import os
# Add to test local data JFK 2/1/2025
import tempfile, shutil
import arcpy

def listKeyValues(d, path=""):
    """ simple recursive print function to walk the metadata structure"""
    # Modified by JFK 2/1/2025
    #for k,v in d.iteritems():
    for k,v in d.items():
        if path != "":
            path += "/%s" % k
        else:
            path = k
        # Modified by JFK 2/1/2025
        # print "Key - %s" % path
        print( "Key - %s" % path )
        if isinstance(v, dict):
            listKeyValues(v, path)

def main():
    project_folder   = rf"{os.path.dirname(os.path.dirname(__file__))}"
    project_name     = "Metadata"
    project_gdb      = rf"{project_folder}\{project_name}.gdb"
    fc               = "SpeciesRangeTemplate"
    species_range_fc = rf"{project_gdb}\{fc}"

    # Modified to test local data JFK 2/1/2025
    # arcpy.env.workspace = r"c:\temp\scratch.gdb"
    #arcpy.env.workspace = r".\National Mapper.gdb" # passed
    arcpy.env.workspace = project_gdb
    for fc in arcpy.ListFeatureClasses():
        data = hermes.Paperwork(dataset=os.path.join(arcpy.env.workspace, fc)).convert()
        listKeyValues(data)

if __name__ == "__main__":
    os.chdir(".")  # passed

    scratch_folder = "Scratch"  # passed
    if not os.path.isdir(scratch_folder):  # passed
        os.mkdir(scratch_folder)  # passed

    local_temp = "./TEMP"  # passed
    if not os.path.isdir(local_temp):  # passed
        os.mkdir(local_temp)  # passed

    # Set the new temporary directory
    tempfile.tempdir = local_temp  # passed
    # Verify the change
    #print(tempfile.gettempdir())  # passed

    main()
