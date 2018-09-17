"""Class defining a policy parser"""

class PolicyParser():
    """Class for extracting the privacy policy from the xml element

    The PolicyParser is a class that contains the root of the xml file
    and parses the data. The class assumes that the polciies in the xml file
    are divided into set of 'SECTION' tags. Each 'SECTION' tag having a single
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
    sub_element_names : list
        List of strings
    privacy_policy : list
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
        privacy_policy : list
            Privacy policy as a list of strings
        """
        for sections in self.root:
            self.privacy_policy.extend(self.get_subtitle_and_text(sections))

        return self.privacy_policy
