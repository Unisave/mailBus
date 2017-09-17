#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, '../staticAssets/templatea')),
    trim_blocks=False)

import argparse
parser = argparse.ArgumentParser(description='This program was developed by Sooraj Antony to perform terminal level integration of the Template generator Jinja server')
parser.add_argument('-r','--recipient',help='Recipient Full Name', required=True)
args = parser.parse_args()
## show values ##
recipient = args.recipient


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html(recipient):
    fname = "output.html"
    parent_dict = [{'Yes':'val1','No':'val2'},{'Later':'val3','Other':'val4'}]
    sender = "Hirrr.com"
    context = {
        'recipient': recipient,
        'parent_dict': parent_dict
        'logoTracker': tokenID
    }
    #
    with open(fname, 'w') as f:
        html = render_template('guiSkeleton.html', context)
        f.write(html)


def main():
    create_index_html(recipient)

#############################################################################

if __name__ == "__main__":
    main()