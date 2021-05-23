# KanjiKG




## About

KanjiKG started out as one of my contributions to a team project on translation-based embeddings of knowledge graphs in an artificial intelligence course. We wanted to try out some embedding approaches on a novel knowledge graph, so I produced the triples for KanjiKG from the data in KANJIDIC2 and KRADFILE. 




## Files

* `make_kanjikg.py` is a Python 3 script that generates the triples of the knowledge graph. To run, it needs the dictionary files `kanjidic2.xml` and `kradfile-u.txt`. Upon successfully running, the script produces several output files. `KanjiKG-train.txt`, `KanjiKG-valid.txt`, and `KanjiKG-test.txt` are splits of the triples suitable for input into Pykg2vec. `all.txt` is all the triples in a single file. The formatting of these files is that each line contains a triple and there are tabs between the head entity and the relation as well as the relaiton and the tail entity. `entity2id.txt` and `relation2id.txt` are basically mappings of the entities and relations, respetively, to integers. Some implementations of embedding algorithms that we had looked at before going with Pykg2vec needed these files, but Pykg2vec itself does not.
* `visualize_embeddings.m` is a MATLAB script that plots the relation embeddings and entity embeddings in 3D. It uses `rel_embedding.tsv`, `ent_embedding.tst`, and `ent_labels.tsv`, which are outputs from Pykg2vec.
* `visualize_graph.m` is a MATLAB script that plots a subgraph of the knowledge graph. There is a variable to set which entity the subgraph is a plot of. It uses the `all.txt` file output by the `kanjikg.py` script.




## Resources

* `kanjidic2.xml` is an XML file with dictionary entries for kanji. The file can be obtained from the [KANJIDIC Project](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project).
* `kradfile-u.txt` is a text file that lists which elements are in a kanji. Information about the file can be found at [KRADFILE](http://www.edrdg.org/krad/kradinf.html), however I got the actual file from the [archive server](http://ftp.edrdg.org/pub/Nihongo/00INDEX.html).
* [Pykg2vec](https://github.com/Sujit-O/pykg2vec) is a Python package that has implementations of TransE, TransH, and TransR as well as other knowledge graph embedding algorithms.
