"""Module to create the dataset and save the embeddings"""

from gensim.models import Word2Vec
import click

from create_dataset import PolicyDataset

def get_ds_as_list(dataset):
    """Converts a list of lists to a list"""
    policy_as_list = []

    for _, policy in dataset.items():
        for each_line in policy:
            policy_as_list.append(each_line)

    return policy_as_list

@click.command()
@click.option('--dataset_path',
              prompt='Enter path to dataset',
              help='Path the folder containing 1,010 privacy policies')
@click.option('--dim',
              prompt='Embedding dimension',
              help='The number of dimensions for each embedding')
@click.option('--embedding_file_path',
              prompt='Enter File path for embedding',
              help='File path to save the embedding')
def main(dataset_path, dim, embedding_file_path):
    """Create and save the word embedding"""

    print('[INFO] Creating dataset...')
    privacy_policy_ds = PolicyDataset(dataset_path).get_dataset()
    print('[INFO] Dataset created!')

    print('[INFO] Creating Embedding...')
    privacy_policy_embedding = Word2Vec(get_ds_as_list(privacy_policy_ds),
                                        size=int(dim),
                                        workers=6)
    print('[INFO] Embedding created! Saving the model...')

    privacy_policy_embedding.save(embedding_file_path)

    print('[INFO] Done!')

if __name__ == '__main__':
    main()  # pylint: disable=E1120
