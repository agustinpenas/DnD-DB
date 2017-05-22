import csv
import sys
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def bestTurn():
	fileSin = 'TurnoSinMenos5.txt' 
	fileCon = 'TurnoConMenos5.txt'

	file = open(fileSin, "r")
	valuesSin = sorted([int(i) for i in file.readlines()])[0:9999]
	promedioSin = np.mean(valuesSin)
	desvioSin = np.std(valuesSin)


	file = open(fileCon, "r")
	valuesCon = sorted([int(i) for i in file.readlines()])[0:9999]
	promedioCon = np.mean(valuesCon)
	desvioCon = np.std(valuesCon)

	y = []
	y.append(promedioSin)
	y.append(promedioCon)
	stdy = []
	stdy.append(desvioSin)
	stdy.append(desvioCon)
	print y, stdy
	stds    = [(0,0), stdy]
	ind = np.arange(1,3) 
	width = .75     

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, y, width, yerr=stdy)

	ax.set_ylabel('Comparacion Burst')
	ax.set_xticks(ind + 0.4)
	ax.set_xticklabels(('Sin menos 5','Con menos 5'))
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	rects1[0].set_color('g')
	rects1[1].set_color('r')

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	remove_values_from_list(valuesSin,0)
	remove_values_from_list(valuesCon,0)
	print 'Minimo Sin: ' + str(min(valuesSin))
	print 'Minimo Con: ' + str(min(valuesCon))
	print 'Maximo Sin: ' + str(max(valuesSin))
	print 'Maximo Con: ' + str(max(valuesCon))
	plt.show()

def bestBurst():
	fileSin = 'SinMenos5.txt' 
	fileCon = 'ConMenos5.txt'
	fileCombinacion = 'Combinacion.txt'

	file = open(fileSin, "r")
	valuesSin = sorted([int(i) for i in file.readlines()])[0:9999]
	promedioSin = np.mean(valuesSin)
	desvioSin = np.std(valuesSin)


	file = open(fileCon, "r")
	valuesCon = sorted([int(i) for i in file.readlines()])[0:9999]
	promedioCon = np.mean(valuesCon)
	desvioCon = np.std(valuesCon)

	file = open(fileCombinacion, "r")
	valuesCombinacion = sorted([int(i) for i in file.readlines()])[0:9999]
	promedioCombinacion = np.mean(valuesCombinacion)
	desvioCombinacion = np.std(valuesCombinacion)

	y = []
	y.append(promedioSin)
	y.append(promedioCon)
	y.append(promedioCombinacion)
	stdy = []
	stdy.append(desvioSin)
	stdy.append(desvioCon)
	stdy.append(desvioCombinacion)
	print y, stdy
	ind = np.arange(1,4) 
	width = .75     

	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, y, width, yerr=stdy)

	ax.set_ylabel('Comparacion Burst')
	ax.set_xticks(ind + 0.4)
	ax.set_xticklabels(('Sin menos 5','Con menos 5','Combinacion'))
	plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
	rects1[0].set_color('g')
	rects1[1].set_color('r')
	rects1[2].set_color('b')

	def autolabel(rects):
	    """
	    Attach a text label above each bar displaying its height
	    """
	    for rect in rects:
	        height = rect.get_height()
	        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
	                '%d' % int(height),
	                ha='center', va='bottom')

	autolabel(rects1)
	plt.show()		



def main():
	#cVsAsm()
	bestBurst()
	#write2vs4ClocksPorPixel()

if __name__ == "__main__":
	main()