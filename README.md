# Privacy_Policy_Analysis

A repository for hosting code and dataset, and managing the workflow for the paper.

## CODE

This repository contains code to extract privacy policies, create a dataset, create and save the word embeddings from the dataset. Specifically it contains code to work on the 1,010 privacy policies from Fei Liu et. al's work.

>Liu, Fei, Nicole Lee Fella, and Kexin Liao. "Modeling language vagueness in privacy policies using deep neural networks." 2016 AAAI Fall Symposium Series. 2016.

The dataset can be downloaded from the [Usable Privacy Org Website](https://usableprivacy.org/data). To download click on the ACL/COLING 2014 Dataset.

### MODULES

There are two modules that can be useful when using the 1,010 privacy policies - `create_dataset.py` and `create_embedding.py`. The `create_dataset.py` module extracts all the data for each privacy policy and saves it as a json file.

#### USAGE

The module uses commandline arguments to create and save the dataset. Following is an example for how to use -

`$ python src/create_dataset.py --dataset_path <enter-path-to-dataset-folder>/ --json_file <enter-filepath-with-name-of-json-file>`

##### EXAMPLE**

`$ python src/create_dataset.py --dataset_path code/acl_dataset --json_file code/acl_dataset/dataset_as.json`

Another module is the `create_embedding.py` module which takes in the path to the dataset and filepath to save the embedded words. The module uses Gensim algorithm to create the embeddings.

#### USAGE

`$ python src/create_embedding.py --dataset_path <enter-path-to-dataset-folder>/ --dim <enter-dimension-size-of-embedding> --embedding_file_path <enter-filepath-with-model-file>`

##### EXAMPLE

`$ python src/create_embedding.py --dataset_path code/acl_dataset/ --dim 100 --embedding_file_path code/acl_dataset/embedding_dim_100.model`