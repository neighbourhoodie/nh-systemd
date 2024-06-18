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

    handle_programlisting(root)
    handle_includes(root)

    write_xml(output_file_name, tree)


def handle_programlisting(tree):
    programlistings = tree.findall(".//programlisting")
    print('programlistings', programlistings)
    for programlisting in programlistings:
        # get inlcude Subelement
        include = programlisting.find(".//{http://www.w3.org/2001/XInclude}include")
        print('program include: ', include.get('href'))
        filename = include.get('href')

        new_element = ET.Element('para')
        new_element.text = '{include="' + filename + '"}'

        map = { c: p for p in tree.iter() for c in p }
        parent = map[programlisting]
        index = list(parent).index(programlisting)
        parent.remove(programlisting)
        parent.insert(index, new_element)


def handle_includes(tree):
    includes = tree.findall(".//{http://www.w3.org/2001/XInclude}include")
    print('includes', includes)
    for include in includes:
        print('atr',include.attrib)
        print('include: ', include.get('href'))
        if include.get('href') == 'version-info.xml':
            # replaces the version include to a "placeholder"
            # https://pandoc.org/lua-filters.html#replacing-placeholders-with-their-metadata-value
            xpointer = include.get('xpointer')
            new_element = ET.Element('para')
            new_element.text = '%' + xpointer + '%'
            map = { c: p for p in tree.iter() for c in p }
            parent = map[include]
            # print('parent', parent)
            index = list(parent).index(include)
            parent.insert(index, new_element)
        elif not include.get('xpointer'):
            new_element = ET.Element('para')
            # new_element.text = '.. include::' + include.get('href')
            new_element.text = '{.include}\n' + include.get('href')

            map = { c: p for p in tree.iter() for c in p }
            parent = map[include]
            index = list(parent).index(include)
            parent.insert(index, new_element)
        else:
            #TODO: deal with this
            print('can not deal with this right now')


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
    # path = r'*.xml'
    path = r'sd_event_add_inotify.xml'
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

        # turn into rst
        subprocess.run(["pandoc", "-t", "rst", "-f", "docbook", "-s", output_file_name, "-o", filename.replace("xml", "rst")])
        print('rst of: ', filename)



if __name__ == '__main__':
    main()
