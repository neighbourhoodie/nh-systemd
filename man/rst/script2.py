#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

# import sys
import glob
import xml.etree.ElementTree as ET
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree


def main():
    ET.register_namespace('xi', 'http://www.w3.org/2001/XInclude')

    files_to_ignore = ['standard-conf.xml',
                    'systemd.directives.xml',
                    'systemd.index.xml',
                    'directives-template.xml',
                    'version-info.xml',
                    'standard-specifiers.xml',

                    'systemd-system.conf.xml',
                    'systemd-debug-generator.xml',
                    'hostname.xml',
                    'systemd.environment-generator.xml',
                    'systemd-environment-d-generator.xml',
                    'systemd-nspawn.xml',
                    'systemd-rc-local-generator.xml',
                    'resolved.conf.xml',
                    'vconsole.conf.xml',
                    'systemd-journal-upload.service.xml',
                    'systemd-journal-remote.service.xml',
                    'systemctl.xml',
                    'systemd.generator.xml',
                    'systemd-vmspawn.xml',
                    'logind.conf.xml',
                    ]
    #TODO: find all the files that are used in includes and ignore/translate them to rst

    # get all the xml files
    path = r'*.xml'
    files = glob.glob(path)

    allIncludes = []

    for filename in files:
        print('starting with file: ', filename)
        if filename in files_to_ignore:
            print(filename, ' ignored')
        else:
          tree = ET.parse(filename)
          root = tree.getroot()
          includes = root.findall(".//{http://www.w3.org/2001/XInclude}include")
        #   includes = root.findall('xi:include', {'xi': 'http://www.w3.org/2001/XInclude'})
          for include in includes:
            if not include.get('xpointer'):
                allIncludes.append(include.get('href'))
            else:
                #TODO: deal with this
                allIncludes.append(include.get('href'))
                if include.get('href') not in files_to_ignore:
                  print('can not deal with this right now:', include.get('href'))

    allIncludes_set = set(allIncludes)

    print('Includes: ', allIncludes_set)



if __name__ == '__main__':
    main()
