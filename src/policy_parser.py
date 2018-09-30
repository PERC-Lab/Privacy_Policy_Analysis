"""Class defining a policy parser"""

import xml.etree.ElementTree as ET
from os import path

import click


class PolicyParser():
    """Class for extracting the privacy policy from the xml element

    The PolicyParser is a class that contains the root of the xml file
    and parses the data. The class assumes that the polciies in the xml file
    are divided into a set of 'SECTION' tags. Each 'SECTION' tag having a single
    'SUBTITLE' and 'SUBTEXT' tag within them.

    Parameters
    ----------
    policy_root : xml.etree.ElementTree
        Root of the xml file
    sub_element_names : list
        List of strings (default=['SUBTITLE', 'SUBTEXT'])

    Attributes
    ----------
    root : xml.etree.ElementTree
        Root of the xml file
    sub_element_names : List
        List of name of sub_elements in 'SECTION' tag
    privacy_policy : List
        List of all the text in the privacy policy as a list
    """

    def __init__(self, policy_root, sub_element_names=None):
        self.root = policy_root
        if sub_element_names is None:
            self.sub_elt_names = ['SUBTITLE', 'SUBTEXT']
        self.privacy_policy = []

    @staticmethod
    def get_text(element, sub_elt_name):
        """Returns the text of the subelement

        Parameters
        ----------
        element : Element
            xml.etree.ElementTree.Element - 'SECTION' of a privacy policy
        sub_elt_name : String
            Either 'SUBTITLE' or 'SUBTEXT'

        Returns
        -------
        sub_elt_text : String
            String of the sub-element, either SUBTITLE,
            or SUBTEXT.
        """
        sub_elt_text = element.find(sub_elt_name).text

        if sub_elt_text is None:
            sub_elt_text = ''

        return sub_elt_text

    def get_subtitle_and_text(self, element):
        """Wrapper function that merges subtitle and subtext
        into a list of strings

        Parameters
        ----------
        element : Element
            xml.etree.ElementTree.Element - 'SECTION' of the root

        Returns
        -------
        section_text : List
            List of text for each text.
        """
        section_text = []

        for subsection in self.sub_elt_names:
            section_text.append(self.get_text(element, subsection))

        return section_text

    def get_privacy_policy(self):
        """Takes in the root and iterates over the 'SECTION' elements and
        then returns a list of strings

        Returns
        -------
        privacy_policy : List
            Privacy policy as a list of strings
            Each item in the list is either a 'SUBTITLE' or 'SUBTEXT' tag
        """
        for sections in self.root:
            self.privacy_policy.extend(self.get_subtitle_and_text(sections))

        return self.privacy_policy

def check_filepath(ctx, param, value):
    """Validates that the filepath entered is correct"""

    try:
        assert path.exists(value)
        return value
    except AssertionError:
        raise click.BadParameter('The path to the file does not exist.')


@click.command()
@click.option('--filepath', prompt='Enter file path',
              callback=check_filepath,
              help='Path to the policy xml file')
def main(filepath):
    "MAIN"

    xml_file = ET.parse(filepath)
    parser = PolicyParser(xml_file.getroot())

    print(parser.get_privacy_policy())

if __name__ == '__main__':
    main() #pylint: disable=E1120
