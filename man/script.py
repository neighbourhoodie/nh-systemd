#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

# import sys
import subprocess
import glob
import xml.etree.ElementTree as ET
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

def write_xml(output_file_name, tree):
     with open(output_file_name, 'wb') as file:
        file.write(bytes('<?xml version="1.0"?> <!--*-nxml-*-->\n', 'utf-8'))
        file.write(bytes('<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN"\n', 'utf-8'))
        file.write(bytes('  "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">\n', 'utf-8'))
        file.write(bytes('<!-- SPDX-License-Identifier: LGPL-2.1-or-later -->\n', 'utf-8'))
        tree.write(file)

def xml_without_meta(tree, output_file_name):
    root = tree.getroot()
    metadata_tags = ['refentryinfo','refmeta', 'refnamediv', 'refsynopsisdiv']

    contents = root.findall('refsect1')
    if not contents:
        print('file has no contents')
        return

    for tag in metadata_tags:
        metadata = root.find(tag)
        root.remove(metadata)
    # Handle includes
    includes = root.findall('xi:include', {'xi': 'http://www.w3.org/2001/XInclude'})
    for include in includes:
        print('atr',include.attrib)
        print('include: ', include.get('href'))
        if include.get('href') == 'version-info.xml':
            #TODO: replace text
            print('yes')
        elif not include.get('xpointer'):
            new_element = ET.Element('para')
            new_element.text = '.. include::' + include.get('href')

            index = list(root).index(include)

            root.remove(include)
            root.insert(index, new_element)
        else:
            #TODO: deal with this
            print('can not deal with this right now')


    write_xml(output_file_name, tree)


def xml_with_only_meta(tree, output_file_name):
    root = tree.getroot()
    contents = root.findall('refsect1')
    if not contents:
        print('file has no contents')
        return
    for content in contents:
        root.remove(content)

    write_xml(output_file_name, tree)


def main():
    ET.register_namespace('xi', 'http://www.w3.org/2001/XInclude')

    files_to_ignore = ['standard-conf.xml',
                    'systemd.directives.xml',
                    'systemd.index.xml',
                    'directives-template.xml',
                    'version-info.xml']
    #TODO: find all the files that are used in includes and ignore/translate them to rst

    # get all the xml files
    path = r'*.xml'
    files = glob.glob(path)

    for filename in files:
        print('starting with file: ', filename)
        if filename in files_to_ignore:
            print(filename, ' ignored')
            return
        # copy file
        tree = ET.parse(filename)
        tree_copy = ET.parse(filename)
        print('2 copies of: ', filename)
        # delete metatags
        output_file_name = 'output.xml'
        xml_without_meta(tree_copy, output_file_name)
        print('no-meta xml of ', filename)
        # delete everything but the metatags
        xml_with_only_meta(tree, filename)
        print('only-meta xml of ', filename)
        # resolve xmlincludes
        # TODO don't loose xml include info in rst
        # find out what includes there are and how many
        # how to port that to rst
        # subprocess.run(["xmllint", "--xinclude", output_file_name])
        print('no-meta xml of ', filename, 'got includes')
        # turn into rst
        subprocess.run(["pandoc", "-t", "rst", "-f", "docbook", "-s", output_file_name, "-o", filename.replace("xml", "rst")])
        print('rst of: ', filename)



if __name__ == '__main__':
    main()
