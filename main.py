# -*- coding: utf-8 -*-
"""generating artificial data to test LDA.ipynb

@author: Omar Al-Nablseih

"""



from collections import Counter

import numpy as np


from gensim.corpora import Dictionary

from gensim.models import LdaModel

import pyLDAvis
import pyLDAvis.gensim

random_seed = 50

num_documents = 100

num_topics = 3

num_words = 20


number_of_words_per_document = 100



# Set alpha and beta parameters

alpha = 0.1*np.ones(num_topics)
beta = 0.1*np.ones(num_words)

np.random.seed(random_seed)

# Generate topic distributions for each document

document_topic_distributions = np.random.dirichlet(alpha, num_documents)



# Generate correlated word distributions for each topic

topic_word_distributions = np.random.dirichlet(beta, num_topics)



# Generate words for each document

document_words = []



for doc_topic_dist in document_topic_distributions:

    doc_words = []

    for _ in range(number_of_words_per_document):

        # Choose a topic based on probabilities

        topic_index = np.random.choice(num_topics, p=doc_topic_dist)

        # Choose a word based on probabilities of the selected topic

        word_index = np.random.choice(num_words, p=topic_word_distributions[topic_index])

        doc_words.append(word_index)

    document_words.append(doc_words)



# create dictinioray and corpus

number_id_dict = {str(i): i for i in range(num_words)}



document_words = [[str(word) for word in doc] for doc in document_words]

corpus = []



for document in document_words:

        document_ids = [number_id_dict[word] for word in document if word in number_id_dict]

        word_freq = Counter(document_ids)

        corpus.append([(word_id, freq) for word_id, freq in word_freq.items()])



id2word_dict = {v: k for k, v in number_id_dict.items()}







lda_model = LdaModel(corpus, num_topics=num_topics, id2word= id2word_dict, passes=10, iterations=50, random_state=random_seed,alpha=alpha,  eta=0.1 )







# Get the topic distribution for each document

topic_word_distributions_after = lda_model.get_topics()

document_topic_distributions_after = [lda_model[doc] for doc in corpus]
#visualize the results:
id2word_dict_gensim = Dictionary.from_corpus(corpus)

pyLDAvis.enable_notebook()
data_visualizing = pyLDAvis.gensim.prepare(lda_model,corpus, id2word_dict_gensim)
pyLDAvis.display(data_visualizing)



"""Visualisierung der Ergebnisse aus künstlich erstellten Daten"""

vocab =[str(i) for i in range (0, num_words)]
data_visualizing = pyLDAvis.prepare(topic_term_dists = topic_word_distributions,  doc_topic_dists = document_topic_distributions, doc_lengths =[number_of_words_per_document] * num_documents , vocab = vocab, term_frequency=[0] * num_words )
pyLDAvis.display(data_visualizing)

