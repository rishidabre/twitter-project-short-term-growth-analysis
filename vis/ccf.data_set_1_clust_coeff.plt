#
# Clustering coefficient. G(277, 6405). Average clustering: 0.8093  OpenTriads: 56182 (0.4148)  ClosedTriads: 79258 (0.5852) (Sat Apr 29 17:53:10 2017)
#

set title "Clustering coefficient. G(277, 6405). Average clustering: 0.8093  OpenTriads: 56182 (0.4148)  ClosedTriads: 79258 (0.5852)"
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
set output 'ccf.data_set_1_clust_coeff.png'
plot 	"ccf.data_set_1_clust_coeff.tab" using 1:2 title "" with linespoints pt 6
