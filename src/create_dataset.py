"""Module defining the class for creating the privacy policy dataset"""

import os
import xml.etree.ElementTree as ET
from os import path

from nltk.tokenize import sent_tokenize

from policy_parser import PolicyParser

CWD = os.getcwd()

class PolicyDataset():
    """This class contains methods to extract,
    create, and modify the dataset

    Parameters
    ----------
    dataset_path : str
        Filepath where the xml files are stored

    Attributes
    ----------
    path : str
        Filepath where the xml files are stored
    dataset : list
        Actual dataset as a list of lists
    _dataset_ : list
        List of lists. Each inner list is a word
    """

    def __init__(self, dataset_path):
        self.path = dataset_path
        self.dataset = {}
        self._dataset_ = []

    @staticmethod
    def _get_parser_(policy_file_path):
        """Returns `PolicyParser` object

        Parameters
        ----------
        policy_file_path : str
            Filepath to the xml file

        Returns
        -------
        PolicyParser
            PolicyParser object with root
            of the file whose path is passed
            as a parameter
        """

        xml_file = ET.parse(policy_file_path)
        return PolicyParser(xml_file.getroot())

    def _extract_file_data(self, file_path):
        """Returns the data from a single xml file

        Parameters
        ----------
        file_path : str
            Filepath to a single file

        Returns
        -------
        list
            A list of strings
        """

        parser = self._get_parser_(file_path)
        return parser.get_privacy_policy()

    def _create_dataset(self):
        """Function that loops over the xml
        files and extracts the policies from each file
        """
        for policy_file in os.listdir(self.path):

            policy_file_path = path.join(self.path, policy_file)

            if path.isfile(policy_file_path) and policy_file.endswith('xml'):
                self.dataset[policy_file] = self.tokenize_policy(policy_file_path)


    def tokenize_policy(self, policy_file_path):
        """Returns a policy as a list of lists.
        Inner list being of tokens.

        Each section is converted into sentences.
        Then for each sentence if it is less than 3 
        words it is disregarded

        Returns
        list:
            A list of lists. Inner list being of tokens for a sentence
        """
        policy = self._extract_file_data(policy_file_path)
        tokenized_policy = []

        for each_section in policy:
            sentences = sent_tokenize(each_section)

            for each_sentence in sentences:
                tokens = self._tokenize(each_sentence)
                if tokens is not None:
                    tokenized_policy.append(tokens)

        return tokenized_policy


    def get_dataset(self):
        """Returns the dataset as a list of lists

        Returns
        -------
        list
            A list of lists. Each inner list
            being a policy
        """

        if self.dataset == {}:
            self._create_dataset()

        return self.dataset
        # dataset is a list of strings. Convert it into list of lists

    @staticmethod
    def _tokenize(text, min_num=3):
        """Takes in a string, and returns tokens.

        If sentence has less than `min_num` number of tokens, it is disregarded.

        Parameters
        ----------
        text : str
            The string which is to be converted into tokens
        min_num : int
            The minimum number of tokens that should be in a sentence (default=3)
            In case it is -1, then all strings are returned

        Returns
        -------
        list
            List of  sentences with each sentence having
            at least `min_num` number of tokens
        """
        tokens = text.split()

        return None if len(tokens) < min_num else tokens

    # def save_dataset


# TODO
# 1. Segment into sentences
# 2. Remove sentences with less than 3 words
# 3. Tokenize them into a list of tokens
