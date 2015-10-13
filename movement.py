#!D:\Python27\python
#Move all the datas in values directory to values-en directory.
#All the datas in values directory that don't exist in values-en directory
#Author:HuaShuncai
#Date:20151013

import os
import shutil as sut

if __name__ == "__main__":

    #2 directories:one is from directory,the other is to directory
    VALUES_DIR_NAME = "values"
    VALUES_EN_DIR_NAME = "values-en"

    #exist the 2 directories?
    print "Directory",VALUES_DIR_NAME,"exist?",os.path.exists (VALUES_DIR_NAME)
    print "Directory",VALUES_EN_DIR_NAME,"exist?",os.path.exists (VALUES_EN_DIR_NAME)

    #---------------------------------
    #the 2 directories must exist here
    #---------------------------------
    
    #enter values directory
    os.chdir (VALUES_DIR_NAME)

    #list all the xml files in values directory
    all_xml_files = os.listdir (os.getcwd ())
    print "all xml files in",VALUES_DIR_NAME,"directory is",all_xml_files
    print "there is",len(all_xml_files),"files"

    #list all the strings xml files in value directory
    all_strings_xml_files = [i for i in all_xml_files if i.startswith("strings")]
    print "all string xml files in",VALUES_DIR_NAME,"directory is",all_strings_xml_files
    print "there is",len(all_strings_xml_files),"files"

    #whether every strings file in values directory exists in values-en directory too
    #if so,do nothing,if not,do copy job
    #1.enter the values-en directory
    os.chdir (".." + os.sep + VALUES_EN_DIR_NAME)
    print "current work directory is",os.getcwd ()

    for i in all_strings_xml_files:
        if not os.path.exists (os.path.basename (i)):
            print i,"doesn't exist in",VALUES_EN_DIR_NAME
            #do copy job here
        else:
            print i,"exists in",VALUES_EN_DIR_NAME

    

    #back
    os.chdir ("..")
