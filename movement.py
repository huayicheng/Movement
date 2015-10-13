#!D:\Python27\python
#Move all the datas in values directory to values-en directory.
#All the datas in values directory that don't exist in values-en directory
#Author:HuaShuncai
#Date:20151013

import os
import shutil as sut
from xml.dom import minidom as md

def get_string_nodes_from_xml(file_abs_path,string_tag_name):
    """
@param file_abs_path:xml file absolute path
@return a list consis of all string nodes in the param xml file
"""

    doc = md.parse(file_abs_path)
    root = doc.documentElement
    return root.getElementsByTagName(string_tag_name)

def do_copy_job(string_file_name,values_dir_path,values_en_dir_path,string_tag_name):
    """
@param string_file_name whose data need to be copied
@param values_dir_path the data source
@param values_en_dir_path the data target
"""

    values_string_nodes = get_string_nodes_from_xml(values_dir_path + os.sep + string_file_name,string_tag_name)
    print "len(values_string_nodes):",len(values_string_nodes)
    values_en_string_nodes = get_string_nodes_from_xml(values_en_dir_path + os.sep + string_file_name,string_tag_name)
    print "len(values_en_string_nodes):",len(values_en_string_nodes)

if __name__ == "__main__":
    #string tag name
    STRING_TAG_NAME = "string"
    STRING_TAG_NAME_ATTR = "name"

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

    #now,create 2 dom trees for every strings xml in 2 values* directories
    for i in all_strings_xml_files:
        value_string_nodes = get_string_nodes_from_xml(".." + os.sep + VALUES_DIR_NAME + os.sep + os.path.basename (i),STRING_TAG_NAME)
        print "there are",len(value_string_nodes),"string nodes in",".." + os.sep + VALUES_DIR_NAME + os.sep + os.path.basename (i)
        #break;

        value_en_string_nodes = get_string_nodes_from_xml(os.getcwd () + os.sep + os.path.basename (i),STRING_TAG_NAME)
        print "there are",len(value_en_string_nodes),"string nodes in",os.getcwd () + os.sep + os.path.basename (i)
        #if len(value_en_string_nodes) < 5:
        #   for j in value_en_string_nodes:
        #      print "the node's attribute is",j.getAttribute(STRING_TAG_NAME_ATTR)

        #whether the 2 lengthes of lists are equal to each other
        #if so,do nothing,if not,do copy job
        #copy the data which exists in values folder string xml but not exists in values-en folder string xml to values-en folder string xml
        if len(value_string_nodes) != len(value_en_string_nodes):
            print "the node number in values folder is different from that in values-en folder:",i

            #do copy job here
            do_copy_job(os.path.basename (i),".." + os.sep + VALUES_DIR_NAME,os.getcwd (),STRING_TAG_NAME)

    #back
    os.chdir ("..")
