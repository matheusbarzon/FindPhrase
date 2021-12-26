import time
import random

from Population import Population
from Chromosome import Chromosome

class Generation:

  def __init__(self) -> None:

    self.rateCrossover = 25
    self.rateRemained = 75
    self.rateMutation = 12

    self.maxGenerations = 1000
    self.sizePopulation = 250

    self.solution = 'Phrase to find'
    self.untilFind = False

    self.currentGeneration = 0

    self.startTime = 0

    self.printDetails = False
    self.printGeneration = False

    self.Population = None
    self.theBestOne = []
    self.bestSolution = []

    pass

  def startGenerations(self) -> None:
    if self.getPrintDetails():
      self.startTime = time.time()

    self.theFirstOne()

    while self.continueEvolution():
      self.currentGeneration += +1

      if self.getPrintGeneration():
        self.printBestOfPopulation()

      if self.findSolution():
        break

      self.nextGeneration()

    self.showStats()

  def nextGeneration(self) -> None:
    self.defineAble()

    self.Population = Population(self)

    self.crossover()

    self.populate()

  def crossover(self) -> None:
    vCountBest = len(self.theBestOne)

    vCrossover = 0
    while vCrossover < self.rateRemained:
      vParentOne = self.theBestOne[random.randint(0,vCountBest-1)]
      vParentTwo = self.theBestOne[random.randint(0,vCountBest-1)]

      vGene = []
      for iterate in range(len(self.solution)):
        if iterate < len(self.solution)/2:
          vGene.append(vParentOne[iterate])
        else:
          vGene.append(vParentTwo[iterate])

      self.createChromosomeInPopulation(vGene)

      vCrossover = ((self.Population.currentSize()*100)/self.sizePopulation)

  def defineAble(self) -> None:
    vIterate = 0
    vCrossover = 0

    self.theBestOne = []

    while vCrossover < self.rateCrossover:
      self.theBestOne.append(self.Population.getChromosome()[vIterate][0].getGenes())

      vCrossover = ((len(self.theBestOne)*100)/self.sizePopulation)
      vIterate += 1

  def createChromosomeInPopulation(self,pGene) -> None:
    vChromosome = Chromosome(self)
    vChromosome.createDefinedChromosome(pGene)
    self.Population.appendChromosome(vChromosome)

  def populate(self) -> None:
    self.Population.populate()
    self.Population.sortPopulation()

  def theFirstOne(self) -> None:
    self.Population = Population(self)
    self.populate()

  def continueEvolution(self) -> bool:
    vContinueExecution = True
    if not self.untilFind:
      vContinueExecution = (self.currentGeneration < self.maxGenerations)


    return vContinueExecution

  def findSolution(self) -> bool:
    if self.getPrintDetails():
      self.storageBestGene(self.Population.getChromosome()[0])

    return ( self.Population.getChromosome()[0][1] == 100 )

  def showStats(self):
    if self.findSolution():
      print("Find solution? Yes")
    else:
      print("Find solution? No")

    if self.getPrintDetails():
      print("Best solution: ",self.bestSolution[1], self.bestSolution[0].getGenes())
      print("Last solution: ",self.bestOfPopulation())
      print("Answer: "+self.solution)
      print("Generation: "+str(self.currentGeneration)+" of "+str(self.maxGenerations))
      print("Exection time: %s seconds" % (time.time() - self.startTime))
    else:
      print('End of process in '+str(self.currentGeneration)+'º')

  def storageBestGene(self, pGene):
    if len(self.bestSolution) == 0:
      self.bestSolution = pGene
    if pGene[1] > self.bestSolution[1]:
      self.bestSolution = pGene

  def setPrintDetails(self, pPrintDetails) -> None:
    self.printDetails = pPrintDetails

  def getPrintDetails(self) -> bool:
    return self.printDetails

  def bestOfPopulation(self) -> str:
    return self.Population.getChromosome()[0][0].getGenes()

  def printBestOfPopulation(self) -> None:
    print(self.Population.getChromosome()[0][1], self.Population.getChromosome()[0][0].getGenes())

  def setPrintGeneration(self, pPrintGeneration) -> None:
    self.printGeneration = pPrintGeneration

  def getPrintGeneration(self) -> bool:
    return self.printGeneration

  def setUntilFind(self,pUntilFind) -> None:
    self.untilFind = pUntilFind

  def setRateRemained(self,pRateRemained) -> None:
    self.rateRemained = pRateRemained

  def setRateCrossover(self,pRateCrossover) -> None:
    self.rateCrossover = pRateCrossover

  def setMaxGenerations(self,pMaxGenerations) -> None:
    self.maxGenerations = pMaxGenerations

  def setSizePopulation(self,pSizePopulation) -> None:
    self.sizePopulation = pSizePopulation

  def setRateMutation(self,pRateMutation) -> None:
    self.rateMutation = pRateMutation

  def setSolution(self,pSolution) -> None:
    self.solution = pSolution
