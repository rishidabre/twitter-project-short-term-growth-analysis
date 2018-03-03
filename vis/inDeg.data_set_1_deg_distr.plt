#
# Degree Distribution. G(277, 6405). 88 (0.3177) nodes with in-deg > avg deg (46.2), 0 (0.0000) with >2*avg.deg (Sat Apr 29 17:53:10 2017)
#

set title "Degree Distribution. G(277, 6405). 88 (0.3177) nodes with in-deg > avg deg (46.2), 0 (0.0000) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.data_set_1_deg_distr.png'
plot 	"inDeg.data_set_1_deg_distr.tab" using 1:2 title "" with linespoints pt 6
