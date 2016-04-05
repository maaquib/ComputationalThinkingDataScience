# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    results = {300:[], 150:[], 75:[], 0:[]}
    for num in results:
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances.copy(), mutProb) for i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            population = []
            for i in range(num + 150):
                if i == num:
                    patient.addPrescription("guttagonol")
                population.append(patient.update())
            results[num].append(population)
            
    for i, k in enumerate(results):
        data = numpy.array (results[k])
        array_final_steps = data.take(-1,1)
        pylab.subplot(2, 2, i)
        pylab.title(str(k))
        pylab.hist(array_final_steps, bins=20)
    
    pylab.show()
    
simulationDelayedTreatment(5)




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    results = {300:[], 150:[], 75:[], 0:[]}
    for num in results:
        for trial in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances.copy(), mutProb) for i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            population = []
            for i in range(150 + num + 150):
                if i == 150:
                    patient.addPrescription("guttagonol")
                if i == 150 + num:
                    patient.addPrescription("grimpex")
                population.append(patient.update())
            results[num].append(population)
            
    for i, k in enumerate(results):
        data = numpy.array (results[k])
        array_final_steps = data.take(-1,1)
        pylab.subplot(2, 2, i)
        pylab.title(str(k))
        pylab.hist(array_final_steps, bins=20)
    
    pylab.show()

simulationTwoDrugsDelayedTreatment(5)