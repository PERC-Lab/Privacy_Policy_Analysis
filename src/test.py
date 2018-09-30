"""Module to test the PolicyParser"""

import os
from os import path

import xml.etree.ElementTree as ET
import json

from gensim.models import Word2Vec

import io

from create_dataset import PolicyDataset

CWD = os.getcwd()
DATASET_PATH = path.join(CWD, 'dataset', 'corpus')

policy_dataset = PolicyDataset(DATASET_PATH)

dataset = policy_dataset.get_dataset()

policy_dataset = []

print("Creating dataset...")

for _, policy in dataset.items():
    for each_line in policy:
        policy_dataset.append(each_line)

print("Dataset created!")
print("Creating embedding...")
policy_embedding = Word2Vec(policy_dataset, size=100, workers=6)
policy_embedding.save('1010_policy_embedding_d100.model')
print("1 done. 2 to go")
policy_embedding = Word2Vec(policy_dataset, size=200, workers=6)
policy_embedding.save('1010_policy_embedding_d200.model')
print("2 done. 1 to go")
policy_embedding = Word2Vec(policy_dataset, size=300, workers=6)
policy_embedding.save('1010_policy_embedding_d300.model')
print("Done")


# def write_new_line(policy, fp):
#     for line in policy:
#         fp.write(str(line) + '\n')

# encoding = 'utf-8'
# with io.open('privacy_policy_tokens.txt', 'w', encoding=encoding) as fp:
#     for _, values in dataset.items():
#         write_new_line(values, fp)



# with open('privacy_policy_tokens.json', 'r') as fp:

#     privacy_tokens_dictionary = json.loads(fp.read())
#     with open('privacy_policy_tokens.txt', 'w') as write_file:

#         for _, values in privacy_tokens_dictionary.items():
#             write_file.write(str(values))
