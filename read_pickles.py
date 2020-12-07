import pickle


def read_from_pickle_concatenate():
    PICKLED_FILES = ["corpora1.pkl", "corpora2.pkl"]  # Modify to match filenames

    all_lemmas = []
    for FILENAME in PICKLED_FILES:
        # Loading the corpora from the pickled file
        with open(FILENAME, 'rb') as f:
            all_lemmas_corpus = pickle.load(f)
            all_lemmas.extend(all_lemmas_corpus)

    return all_lemmas
