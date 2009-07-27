# -*- coding: iso-8859-1 -*-
# plot_results.py
# DC simulation methods
# Copyright 2009 Giuseppe Venturini

# This file is part of the ahkab simulator.
#
# Ahkab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# Ahkab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License v2
# along with ahkab.  If not, see <http://www.gnu.org/licenses/>.

"""
This module offers the functions needed to plot the results
of a simulation
"""


import Gnuplot, numpy
import printing

def read_data_header(filename):
	fp = open(filename, "r")
	line = fp.readline()
	if line[0] == '#':
		labels = line[1:].split()
	else:
		printing.print_general_error("Unrecognized file: "+filename)
	fp.close()
	return labels

def read_data(filename, label, labels=None):
	if labels == None:
		labels = read_data_header(filename)
	try:
		index = labels.index(label)
	except ValueError:
		printing.print_general_error("Unrecognized data set: "+label)
	fp = open(filename, "r")
	data = []
	for line in fp:
		if line.strip()[0] != '#':
			data.append(float(line.split()[index]))
	fp.close()
	data = numpy.array(data)
	return data

def split_netlist_label(label):
	label = label.trim()
	l2, l1 = label[2:-1].split(",")
	return label[0]+l2.trim(), label[0]+l1.trim()

def plot_data(title, x, y2, y1, filename, analysis, outfilename):
	g = Gnuplot.Gnuplot()
	g.title(title)
	if x=='T':
		g.xlabel('t [s]')
	elif x[0] == 'V':
		g.xlabel(x + "V")
	elif x[0] == 'I':
		g.xlabel(x+" [A]")
	if y2[0] == 'V':
		g.ylabel("V [V]")
	elif y2[0] == 'I':
		g.ylabel("I [A]")
	gdata = []
	gx = read_data(filename, x)
	for y1label, y2label in zip(y1,y2):
		if y1label is not None and y1label != '':
			data1 = read_data(filename, y1label)
			ylabel = y2+"-"+y1
		else:
			ylabel = y2label
			data1 = 0
		data2 =  read_data(filename, y2label)
		d = Gnuplot.Data(gx, data2-data1, title=ylabel+" ("+analysis+")", with_='linespoints')
		gdata.append(d)
	# ghastly interface!! a workaround would be awesome... suggestion?
	if len(gdata) == 1:
		g.plot(gdata[0])
	if len(gdata) == 2:
		g.plot(gdata[0],gdata[1])
	if len(gdata) == 3:
		g.plot(gdata[0],gdata[1],gdata[2])
	if len(gdata) == 4:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3])
	if len(gdata) == 5:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3],gdata[4])
	if len(gdata) == 6:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3],gdata[4],gdata[5])
	if len(gdata) == 7:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3],gdata[4],gdata[5],gdata[6])
	if len(gdata) == 8:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3],gdata[4],gdata[5],gdata[6],gdata[7])
	if len(gdata) == 9:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3],gdata[4],gdata[5],gdata[6],gdata[7],gdata[8])
	if len(gdata) == 10:
		g.plot(gdata[0],gdata[1],gdata[2],gdata[3],gdata[4],gdata[5],gdata[6],gdata[7],gdata[8],gdata[9])
	if outfilename is not None:
		g.hardcopy(outfilename, terminal='png', color=1)
	raw_input('Please press return to continue...\n')
	g.reset()
	del data1, data2, g, d, gdata

if __name__ == '__main__':
	filename = 'colpitts_graph.tran'
	labels = read_data_header(filename)
	print labels
	for label in labels[1:]:
                print label
		plot_data("Plot "+label, labels[0], [label], [None], filename, "tran", "plot-"+label+".png")