from estnltk import Text # Estonian lemmatization
from estnltk.corpus_processing.parse_enc import parse_enc_file_iterator # corpora parsing
from gensim.models import Word2Vec # main model
from gensim.models import KeyedVectors # for loading pre-trained models
from pathlib import Path # operating system independent file paths
from platform import python_version
import tempfile # for saving model
import pickle # for serializing the corpora
import sys

vertFile = sys.argv[1]
corpora_path = './corpora/verts/' + vertFile
pickleName = vertFile[:-5]


corpora_names = [corpora_path]


all_lemmas = []

for i in range(len(corpora_names)):
    # input file
    input_file = corpora_names[i]
    print("Reading corpora file", input_file)

    # iterate over corpus and extract Text objects one-by-one
    for text in parse_enc_file_iterator(input_file, 
                                        tokenization="preserve_partially", 
                                        line_progressbar='ascii',
                                        restore_morph_analysis=True): #Add logger?

        lemmas = text.original_morph_analysis.lemma
        all_lemmas.append([lemma[0] for lemma in lemmas if lemma[0] != None])


with open(pickleName+'.pkl', 'wb') as f:
    pickle.dump(all_lemmas, f)

f.close()


