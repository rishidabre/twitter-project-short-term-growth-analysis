#!/usr/bin/python

import sys
import snap
from raw_graph_processor import create_graph

# Plots the statistics
def plot_statistics(graph, clust_coeff_file_name, deg_distr_file_name):
    snap.PlotClustCf(graph, clust_coeff_file_name, "Clustering coefficient")
    print("Clustering coefficient plotted.")
    snap.PlotInDegDistr(graph, deg_distr_file_name, "Degree Distribution")
    print("Degree distribution plotted.")
    return

# Main function
def plotter_main():
    args=sys.argv
    if len(args)<4:
        print("Usage: "+args[0]+" <input_file_path> <clust_coeff_file_name> <deg_distr_file_name>")
        quit()
    input_file_path=args[1]
    clust_coeff_file_name=args[2]
    deg_distr_file_name=args[3]
    graph=create_graph(input_file_path)
    plot_statistics(graph, clust_coeff_file_name, deg_distr_file_name)
    return

plotter_main()
