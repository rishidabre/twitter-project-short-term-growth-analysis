#!/usr/bin/python

import sys
import time
import datetime
from raw_graph_processor import get_nodes_and_edges

_GEPHI_FILE_EXTENSION_=".gexf"
_GEXF_PART_I_="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"\
    "<gexf xmlns:viz=\"http:///www.gexf.net/1.1draft/viz\" version=\"1.1\" xmlns=\"http://www.gexf.net/1.1draft\">\n"\
    "<meta lastmodifieddate=\""+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d+%H:%M')+"\">\n"\
    "<creator>Gephi 0.7</creator>\n"\
    "</meta>\n"\
    "<graph defaultedgetype=\"undirected\" idtype=\"string\" type=\"static\">\n"
_GEXF_PART_II_="</graph>\n"\
    "</gexf>\n"

# Writes the data to a Gephi format file
def write_to_file((nodes, edges), output_file_path):
    with open(output_file_path, 'w+r') as f_output:
        # Write the first part of the gexf file
        f_output.write(_GEXF_PART_I_)
        print("Writing nodes...")
        total_nodes=str(len(nodes))
        # Write the nodes start tag
        f_output.write("<nodes count=\""+total_nodes+"\">\n")
        x=0
        for node_id in nodes:
            x+=1
            print("["+str(x)+"/"+total_nodes+"]")
            # Write each node
            f_output.write("<node id=\""+node_id+"\" label=\""+node_id+"\"/>\n")
        # Write the nodes end tag
        f_output.write("</nodes>\n")
        print("Nodes written.")
        print("Writing edges...")
        total_edges=str(len(edges))
        # Write the edges start tag
        f_output.write("<edges count=\""+total_edges+"\">\n")
        x=0
        print("Nodes: ["+total_nodes+"], Edges: ["+total_edges+"]")
        for an_edge in edges:
            x+=1
            print("["+str(x)+"/"+total_edges+"]")
            from_id=an_edge[0]
            to_id=an_edge[1]
            edge_id=from_id+"_"+to_id
            # Write each edge
            f_output.write("<edge id=\""+edge_id+"\" source=\""+from_id+"\" target=\""+to_id+"\"/>\n")
        # Write the edges end tag
        f_output.write("</edges>\n")
        print("Edges written.")
        # Write the second part of the gexf file
        f_output.write(_GEXF_PART_II_)
    print("Gephi file "+output_file_path+" created.")

# Main function
def main():
    args=sys.argv
    if len(args)!=3:
        print "Usage: "+args[0]+" <input_file_path> <output_file_name>"
        quit()
    input_file_path=args[1]
    output_file_name=args[2]
    print("Input file path: "+input_file_path)
    output_file_path=output_file_name+_GEPHI_FILE_EXTENSION_
    print("Output file path: "+output_file_path)
    nodes_and_edges=get_nodes_and_edges(input_file_path)
    write_to_file(nodes_and_edges, output_file_path)
    return

main()
