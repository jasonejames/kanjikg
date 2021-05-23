################################################################################
#                                                                              #
#    CS 8750                                                                   #
#    Aritifical Intelligence II                                                #
#                                                                              #
#    Final Project                                                             #
#    Make KanjiKG                                                              #
#    make_kanjikg.py                                                           #
#                                                                              #
#    Jason James                                                               #
#    2021-4-28                                                                 #
#                                                                              #
################################################################################

import random

# Import the XML library.
import xml.etree.ElementTree as xml


# Specify the file name of the dictionary file.
fileName = 'kanjidic2.xml';

# Specify the file name of the KRADFILE file.
kradFileName = 'kradfile-u.txt';


# Specify the file name to save the entities in.
entitiesFileName = 'entity2id.txt';

# Specify the file name to save the relations in.
relationsFileName = 'relation2id.txt';


# Specify the file name to save training data in.
trainFileName = 'KanjiKG-train.txt';

# Specify the file name to save test data in.
testFileName = 'KanjiKG-test.txt';

# Specify the file name to save the validation data in.
validFileName = 'KanjiKG-valid.txt';

# Specify the file name to save all the data in.
allFileName = 'all.txt';


# Specify the types of relations to have in this knowledge graph.
relationsDictionary = {
    'has_radical':       0,
    'has_on_reading':    1,
    'has_kun_reading':   2,
    'has_nanori':        3,
    'has_element':       4,

    'is_radical_of':     5,
    'is_on_reading_of':  6,
    'is_kun_reading_of': 7,
    'is_nanori_of':      8,
    'is_element_of':     9
}


# Make an empty list for kanji.
kanjiList = list()

# Make an empty list for radicals.
radicalsList = list()

# Make an empty list for on readings.
onReadingsList = list()

# Make an empty list for kun readings.
kunReadingsList = list()

# Make an empty list for nanori.
nanoriList = list()

# Make an empty list for elements.
elementsList = list()

# Make an empty list for the triples.
triplesList = list()


# Read the XML file.
tree = xml.parse(fileName)

# print(tree)

# Grab the root node.
rootNode = tree.getroot()

print(rootNode)

# Grab the character nodes.
characterNodes = rootNode.getchildren()

# Go through each character node.
# for characterNode in characterNodes[0:10]:
for characterNode in characterNodes:

    # Check whether this node is a character element.
    if (characterNode.tag == 'character'):

        # Grab the attributes of this character.
        attributeNodes = characterNode.getchildren()

        kanji = ''

        # Go through each attribute for this character.
        for attributeNode in attributeNodes:

            # Check for the actual character.
            if (attributeNode.tag == 'literal'):

                # Grab the kanji itself.
                kanji = attributeNode.text
                # print(kanji)

                kanjiList.append(kanji)

            # Check for radicals.
            elif (attributeNode.tag == 'radical'):

                # Grab the radical nodes.
                radicalNodes = attributeNode.getchildren()

                # Go through each radical.
                for radicalNode in radicalNodes:

                    # Check if this node is an actual radical.
                    if (radicalNode.tag == 'rad_value'):

                        # Grab the radical's number.
                        radicalNumber = int(radicalNode.text)

                        radicalsList.append(radicalNumber)

                        # Grab the type of number.
                        radicalType = radicalNode.attrib['rad_type']

                        # Make sure it's a classical radical.
                        if (radicalType == 'classical'):

                            # Make a triple.
                            triple = (kanji, 'has_radical', radicalNumber)

                            # Add the triple to the list.
                            triplesList.append(triple)

                            # Make the inverse triple.
                            inverseTriple = (radicalNumber, 'is_radical_of', kanji)

                            # Add the triple to the list.
                            triplesList.append(inverseTriple)

                        # print(radical.tag)
                        # print(radicalNumber)
                        # print(radicalType)

                # print(attribute.text)

            # Check for readings and meanings.
            elif (attributeNode.tag == 'reading_meaning'):

                # Grab the reading meaning group.
                rmGroupNode = attributeNode.getchildren()

                # Go through each node.
                # The node could be a nanori element or an rmgroup element.
                for node in rmGroupNode:

                    # Check if the node is a nanori element.
                    if (node.tag == 'nanori'):

                        # Grab the nanori.
                        nanori = node.text

                        # print('nanori', nanori)

                        # Make a triple for this nanori.
                        triple = (kanji, 'has_nanori', nanori)

                        # Add the triple to the list.
                        triplesList.append(triple)

                        # Make the inverse triple.
                        inverseTriple = (nanori, 'is_nanori_of', kanji)

                        # Add the inverse triple to the list.
                        triplesList.append(inverseTriple)

                        # Add the nanori to the list.
                        nanoriList.append(nanori)

                    # Check if the node is an rmgroup element.
                    if (node.tag == 'rmgroup'):

                        # Go directly to the entries.
                        readingNodes = rmGroupNode[0].getchildren()

                        # Go through each reading.
                        for readingNode in readingNodes:

                            # Make sure it's a reading node.
                            if (readingNode.tag == 'reading'):

                                # Check if it's an on reading.
                                if (readingNode.attrib['r_type'] == 'ja_on'):

                                    # Grab the reading.
                                    reading = readingNode.text

                                    # print(readingNode.tag, readingNode.text)

                                    # Make a triple.
                                    triple = (kanji, 'has_on_reading', reading)

                                    # Add the triple to the list.
                                    triplesList.append(triple)

                                    # Make the inverse triple.
                                    inverseTriple = (reading, 'is_on_reading_of', kanji)

                                    # Add the triple to the list.
                                    triplesList.append(inverseTriple)

                                    onReadingsList.append(reading)

                                # Check if it's a kun reading.
                                if (readingNode.attrib['r_type'] == 'ja_kun'):

                                    # Grab the reading.
                                    reading = readingNode.text

                                    # This character seems to have two kun readings in one place.
                                    if (kanji == '存'):
                                        parts = reading.split(' ')
                                        print(parts)
                                        if (len(parts) > 1):
                                            # Make triples with the first reading.
                                            triple = (kanji, 'has_kun_reading', parts[0])
                                            triplesList.append(triple)
                                            inverseTriple = (parts[0], 'is_kun_reading_of', kanji)
                                            triplesList.append(inverseTriple)
                                            kunReadingsList.append(parts[0])
                                            # Handle the second reading like normal.
                                            reading = parts[1]

                                    # print(readingNode.tag, readingNode.text)

                                    # Make a triple.
                                    triple = (kanji, 'has_kun_reading', reading)

                                    # Add the triple to the list.
                                    triplesList.append(triple)

                                    # Make the inverse triple.
                                    inverseTriple = (reading, 'is_kun_reading_of', kanji)

                                    # Add the triple to the list.
                                    triplesList.append(inverseTriple)

                                    kunReadingsList.append(reading)

# print(elements)

# for element in elements

# print(triplesList)

# print(kanjiList)

# print(radicalsList)

# print(onReadingsList)
# print(set(onReadingsList))

# print(kunReadingsList)

# Open the file.
kradFile = open(kradFileName, 'r')

# Read the file.
text = kradFile.read()

# Close the file.
kradFile.close()

# Split the file into lines.
lines = text.splitlines()

# print(lines)

# Go through each line.
# for line in lines[0:300]:
for line in lines:

    # Check if the line is a comment.
    if (line.startswith('#')):

        # Just go on to the next line.
        continue

    # print(line)

    parts = line.split(' ')

    # print(parts)

    # The kanji is the first item in the list.
    kanji = parts.pop(0)

    # print(parts)

    # Remove the colon.
    parts.remove(':')

    # print(parts)

    # Go through each element.
    for element in parts:

        # Make a triple.
        triple = (kanji, 'has_element', element)

        # Add the triple to the list.
        triplesList.append(triple)

        # Make an inverse triple.
        inverseTriple = (element, 'is_element_of', kanji)

        # Add the triple to the list.
        triplesList.append(inverseTriple)

        # Add the element to the elements list.
        elementsList.append(element)

        # print(triple)
        # print(inverseTriple)



# Open the file.
relationsFile = open(relationsFileName, 'w')

# Go through all the entries in the relations dictionary.
for (key, value) in relationsDictionary.items():
    relationsFile.write(str(key))
    relationsFile.write('\t')
    relationsFile.write(str(value))
    relationsFile.write('\n')

# Close the file.
relationsFile.close()



# Deduplicate the lists.
radicalsList = list(set(radicalsList))
kanjiList = list(set(kanjiList))
onReadingsList = list(set(onReadingsList))
kunReadingsList = list(set(kunReadingsList))
nanoriList = list(set(nanoriList))
elementsList = list(set(elementsList))
triplesList = list(set(triplesList))

# Concatenate the entities.
entitiesList = list()
entitiesList = entitiesList + radicalsList
entitiesList = entitiesList + kanjiList
entitiesList = entitiesList + onReadingsList
entitiesList = entitiesList + kunReadingsList
entitiesList = entitiesList + nanoriList
entitiesList = entitiesList + elementsList

# Deduplicate the list.
entitiesList = list(set(entitiesList))


offset = 0

# Open the file.
entitiesFile= open(entitiesFileName, 'w')

# Go through each entity in the list of entities.
for (index, entity) in enumerate(entitiesList):
    entitiesFile.write(str(entity))
    entitiesFile.write('\t')
    entitiesFile.write(str(index))
    entitiesFile.write('\n')

# Close the file.
entitiesFile.close()

# print(radicalsList)

# random.shuffle(radicalsList)

# print(radicalsList)

# Shuffle the triples.
random.shuffle(triplesList)

testCount = int(0.1 * len(triplesList))
validCount = int(0.1 * len(triplesList))

offset = 0

# Open the file.
testFile = open(testFileName, 'w')

# Go through the triples for the test file.
for i in range(0, testCount):

    # Grab a triple.
    triple = triplesList[i]

    testFile.write(str(triple[0]))
    testFile.write('\t')
    testFile.write(str(triple[1]))
    testFile.write('\t')
    testFile.write(str(triple[2]))
    testFile.write('\n')

# Close the file.
testFile.close()

offset = testCount

# Open the file.
validFile = open(validFileName, 'w')

# Go through the triples for the validation file.
for i in range(offset, validCount + offset):

    # Grab a triple.
    triple = triplesList[i]

    validFile.write(str(triple[0]))
    validFile.write('\t')
    validFile.write(str(triple[1]))
    validFile.write('\t')
    validFile.write(str(triple[2]))
    validFile.write('\n')

# Close the file.
validFile.close()

offset = offset + validCount

# Open the file.
trainFile = open(trainFileName, 'w')

# Go through the triples for the training file.
for i in range(offset, len(triplesList)):

    # Grab a triple.
    triple = triplesList[i]

    trainFile.write(str(triple[0]))
    trainFile.write('\t')
    trainFile.write(str(triple[1]))
    trainFile.write('\t')
    trainFile.write(str(triple[2]))
    trainFile.write('\n')

# Close the file.
trainFile.close()


# Open the file.
allFile = open(allFileName, 'w')

# Go through the triples for the all data file.
for triple in triplesList:

    allFile.write(str(triple[0]))
    allFile.write('\t')
    allFile.write(str(triple[1]))
    allFile.write('\t')
    allFile.write(str(triple[2]))
    allFile.write('\n')

# Close the file.
allFile.close()



print('Kanji:', len(kanjiList))
print('Radicals:', len(radicalsList))
print('On Readings:', len(onReadingsList))
print('Kun Readings:', len(kunReadingsList))
print('Nanori:', len(nanoriList))
print('Elements:', len(elementsList))
print()
print('Entities:', len(entitiesList))
print('Relations:', len(relationsDictionary))
print('Triples:', len(triplesList))
