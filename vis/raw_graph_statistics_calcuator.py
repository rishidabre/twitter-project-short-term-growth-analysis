#!/usr/bin/python

import sys
import snap
from raw_graph_processor import create_graph

# Calculates the average clustering coefficient of the grah
def calculate_average_clustering_coefficient(graph):
    NIdCCfH=snap.TIntFltH()
    snap.GetNodeClustCf(graph, NIdCCfH)
    avg_clust_coeff=0
    x=0.0
    for item in NIdCCfH:
        x+=1.0
        clust_coeff=NIdCCfH[item]
        avg_clust_coeff+=clust_coeff
#        print item, clust_coeff
    avg_clust_coeff/=x
    return avg_clust_coeff

# Calculates the size of largest connected component
def calculate_diameter_of_largest_connected_component(graph):
    MxScc=snap.GetMxScc(graph)
    diameter=snap.GetBfsFullDiam(MxScc, graph.GetNodes())
    return diameter

# Calculates the number of connected components
def calculate_number_of_connected_components(graph):
    ComponentDist=snap.TIntPrV()
    snap.GetSccSzCnt(graph, ComponentDist)
#    for comp in ComponentDist:
#        print "Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2())
    connected_components=len(ComponentDist)
    return connected_components

# Main function
def main():
    args=sys.argv
    if len(args)<2:
        print("Usage: "+args[0]+" <input_file_path>")
        quit()
    input_file_path=args[1]
    graph=create_graph(input_file_path)
    print "Calculating the average clustering coefficient..."
    avg_clust_coeff=calculate_average_clustering_coefficient(graph)
    print "Average clustering coefficient: "+str(avg_clust_coeff)
    print "Calculating the diameter of largest connected component..."
    diameter=calculate_diameter_of_largest_connected_component(graph)
    print "Diameter of largest connected componnet: "+str(diameter)
    print "Calculating the number of connected components..."
    connected_components=calculate_number_of_connected_components(graph)
    print "Number of connected components: "+str(connected_components)
    return

main()
