%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                              %
%    CS 8750                                                                   %
%    Aritifical Intelligence II                                                %
%                                                                              %
%    Final Project                                                             %
%    Visualize Graph                                                           %
%    visualize_graph.m                                                         %
%                                                                              %
%    Jason James                                                               %
%    2021-5-1                                                                  %
%                                                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Specify the name of the file containing the triples.
file_name = 'all.txt';

% Create an empty directed graph.
graph = digraph();

% Open the file for reading.
file = fopen(file_name, 'r');

% Read the triples file.
data = textscan(file, '%s\t%s\t%s\n');

% Close the file.
fclose(file);

% Get the count for how many triples there are.
count = length(data{1, 1});
% Get the head entities from the triples.
heads = data{1, 1};
% Get the relations from the triples.
relations = data{1, 2};
% Get the tail entities from the triples.
tails = data{1, 3};

% nodes = string(unique(heads))
edge_labels = string(relations);

% Add all the nodes to the graph.
graph = addnode(graph, string(unique(heads)));

% Set which kanji to make a subgraph of.
% kanji = '亀';
% kanji = '田';
kanji = '生';

% Go through all the triples.
for i = 1:count

    % Get the components of this triple.
    head = string(heads(i));
    relation = string(relations(i));
    tail = string(tails(i));

    % Making a graph for all the triples kinda slows things down, so check to
    % see if this triple pertainst to the kanji of interest or not.
    % However, getting rid of the following if should generate the entire graph.
    if (head == kanji || tail == kanji)

        % Add an edge for this relation.
        graph = addedge(graph, head, tail);
    end
end

% Get the nodes that are connected to the node of interest.
preds = predecessors(graph, kanji);
succs = successors(graph, kanji);

% Deduplicate those nodes.
nodes = string(unique([kanji; preds; succs]));

% Create the subgraph.
kanji_graph = subgraph(graph, nodes);

% Indicate the subgraph has been created.
fprintf('Made subgraph\n');

% Displaying the entire graph seemed to not be feasible.
% plot(graph, 'Layout', 'force', 'NodeLabel', graph.Nodes.Name, 'EdgeLabel', edge_labels);

% Display the subgraph.
plot(kanji_graph, 'Layout', 'force', 'NodeLabel', kanji_graph.Nodes.Name);
