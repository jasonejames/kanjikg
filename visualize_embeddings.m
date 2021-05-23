%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                              %
%    CS 8750                                                                   %
%    Aritifical Intelligence II                                                %
%                                                                              %
%    Final Project                                                             %
%    Visualize Embeddings                                                      %
%    visualize_embeddings.m                                                    %
%                                                                              %
%    Jason James                                                               %
%    2021-5-1                                                                  %
%                                                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Based on tutorial and examples from MATLAB documentation:
% https://www.mathworks.com/help/textanalytics/ref/wordembedding.html
%

%
% Visualize the Relations
%

% Load the vectors into MATLAB.
% These vectors are the relation embeddings produced by Pykg2vec.
data = importdata('rel_embedding.tsv');

% Load functions weren't working the way I wanted, so I hard coded the relations.
labels = ["has_element", "has_kun_reading", "has_nanori", "has_on_reading", "has_radical", "is_element_of", "is_kun_reading_of", "is_nanori_of", "is_on_reading_of", "is_radical_of"];

% Perform tSNE on the relation vectors.
vectors = tsne(data, 'NumDimensions', 3);

% Display the relation vectors visualization.
figure('Name', 'Relation Embeddings Visualization');
textscatter3(vectors, labels);

%
% Visualize the Entities
%

% Load the entity embeddings vectors into MATLAB.
% These vectors are the entity embeddings produced by Pykg2vec.
data = importdata('ent_embedding.tsv');
% Entries 19843 through 20145 are '' in the labels array below. My guess is
% that it's some sort of encoding or font issue. Anyway, just ignore these
% vectors and cut them from the data.
data = data(1:end - (20145 - 19842), :);

% Load the labels that correspond to the entity embeddings vectors.
% These vectors are the entity labels produced by Pykg2vec.
labels = readcell('ent_labels.tsv', 'FileType', 'text');
% Entries 19843 through 20145 are '', so cut those entries from the labels.
labels = labels(1:end - (20145 - 19842), :);
% Convert to strings so the function will work.
labels = string(labels);

% Perform tSNE on the entity vectors.
vectors = tsne(data, 'NumDimensions', 3);

% Display the entity vectors visualization.
figure('Name', 'Entity Embeddings Visualization');
textscatter3(vectors, labels);
% By default, not all the points have a label, but that can be adjusted by
% changing the value for 'TextDensityPercentage'.
% textscatter3(vectors, labels, 'TextDensityPercentage', 100);

% The following lines of code can be uncommented to do some k-means clustering on the entities.

% Do some clustering.
% clusters = kmeans(vectors, 5, 'dist', 'sqeuclidean');
% clusters = kmeans(vectors, 214, 'dist', 'sqeuclidean');

% Display the clustering results.
% figure('Name', 'Clustered Entity Embeddings Visualization');
% textscatter3(vectors, labels, 'ColorData', categorical(clusters));
