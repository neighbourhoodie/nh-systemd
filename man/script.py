#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

import sys
import subprocess
import xml.etree.ElementTree as ET
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

def xml_without_meta(tree, output_file_name):
    root = tree.getroot()
    metadata_tags = ['refentryinfo','refmeta', 'refnamediv', 'refsynopsisdiv']

    for tag in metadata_tags:
        metadata = root.find(tag)
        root.remove(metadata)

    tree.write(output_file_name)

def xml_with_only_meta(tree, output_file_name):
    root = tree.getroot()
    contents = root.findall('refsect1')
    for content in contents:
        root.remove(content)

    tree.write(output_file_name)

# run include?

# turn into rst


def main():
    filename = sys.argv[1] # TODO: get all xml files and loop
    files_to_ignore = ['standard-conf.xml',
                     'systemd.directives.xml',
                     'systemd.index.xml',
                     'directives-template.xml']
    if filename in files_to_ignore:
        return
    # copy file
    tree = ET.parse(filename)
    tree_copy = ET.parse(filename)
    # delete metatags
    output_file_name = 'output.xml'
    xml_without_meta(tree_copy, output_file_name)
    # delete everything but the metatags
    xml_with_only_meta(tree, filename)
    # resolve xmlincludes
    subprocess.run(["xmllint", "--xinclude", output_file_name])
    # turn into rst
    subprocess.run(["pandoc", "-t", "rst", "-f", "docbook", "-s", output_file_name, "-o", filename.replace("xml", "rst")])



if __name__ == '__main__':
    main()
