#
# Clustering coefficient. G(205, 4272). Average clustering: 1.0194  OpenTriads: -3199 (-0.0601)  ClosedTriads: 56434 (1.0601) (Sat Apr 29 17:53:25 2017)
#

set title "Clustering coefficient. G(205, 4272). Average clustering: 1.0194  OpenTriads: -3199 (-0.0601)  ClosedTriads: 56434 (1.0601)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.data_set_2_clust_coeff.png'
plot 	"ccf.data_set_2_clust_coeff.tab" using 1:2 title "" with linespoints pt 6
