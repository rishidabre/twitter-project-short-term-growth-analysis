#!/usr/bin/python

import snap
from subprocess import check_output
from time import time

# To maintain mapping of nodes to their IDs (required due to their long lengths)
node_map=[]

# Converts given input file to a gephi format output file
def get_nodes_and_edges(input_file_path):
    t1=time()
    nodes=[]
    edges=[]
    with open(input_file_path, 'r') as f_input:
        total_lines=check_output(["grep", "-vc", "^$", input_file_path]).replace('\n','')
        print("Total lines: "+str(total_lines))
        x=0
        for iline in f_input:
            x+=1
            print("[%s,%s]"%(x,total_lines))
            line_split=iline.replace('\n','').replace('\r','').split()
            from_id=line_split[0]
            if from_id not in node_map:
                node_map.append(from_id)
            from_index=node_map.index(from_id)
            if from_index not in nodes:
                nodes.append(from_index)
            to_id=line_split[1]
            if to_id not in node_map:
                node_map.append(to_id)
            to_index=node_map.index(to_id)
            if to_index not in nodes:
                nodes.append(to_index)
            edge_id="%s_%s"%(from_index,to_index)
            edges.append((from_index, to_index))
    t2=time()
    print "Time taken to get nodes and edges: %s seconds."%(t2-t1)
    return (nodes, edges)

# Creates graphs from the given input file
def create_graph(input_file_path):
    #UGraph=snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    nodes_and_edges=get_nodes_and_edges(input_file_path)
    graph=snap.TUNGraph.New()
    nodes=nodes_and_edges[0]
    edges=nodes_and_edges[1]
    for node in nodes:
        try:
            graph.AddNode(long(node))
        except Exception as e:
            print "Problem in node: %s"%node
            print "Type of node: %s"%type(node)
            raise
    for edge in edges:
        graph.AddEdge(long(edge[0]), long(edge[1]))
    return graph
