import random

from Population import Population
from Chromosome import Chromosome

class Generation:

  def __init__(self) -> None:

    self.rateCrossover = 50
    self.maxGenerations = 2

    self.sizePopulation = 10
    self.rateMutation = 10
    self.solution = 'Teste'

    self.Population = None
    self.theBestOne = []

    pass

  def startGenerations(self):
    self.theFirstOne()
    for iterator in range(self.maxGenerations):

      if self.findSolution():
        break

      self.nextGeneration()

  def nextGeneration(self):
    self.defineAble()

    self.Population = Population(self)

    self.crossover()

    self.populate()

  def crossover(self):
    vCountBest = len(self.theBestOne)
    vParentOne = self.theBestOne[random.randint(0,vCountBest-1)]
    vParentTwo = self.theBestOne[random.randint(0,vCountBest-1)]

    vCrossover = 0
    while vCrossover < self.rateCrossover:
      vGene = []
      for iterate in range(len(self.solution)):
        if iterate%2 == 0:
          vGene.append(vParentOne[iterate])
        else:
          vGene.append(vParentTwo[iterate])

      vChromosome = Chromosome(self)
      vChromosome.createDefinedChromosome(vGene)
      self.Population.appendChromosome(vChromosome)

      vCrossover = ((self.Population.currentSize()*100)/self.sizePopulation)

  def defineAble(self):
    vIterate = 0
    vCrossover = 0

    self.theBestOne = []

    while vCrossover < self.rateCrossover:
      self.theBestOne.append(self.Population.getChromosome()[vIterate][0].getGenes())

      vCrossover = ((len(self.theBestOne)*100)/self.sizePopulation)
      vIterate += 1

    print(vGeneration.theBestOne)

  def populate(self):
    self.Population.populate()
    self.Population.sortPopulation()

  def theFirstOne(self) -> None:
    self.Population = Population(self)
    self.populate()

  def findSolution(self) -> bool:
    return ( self.Population.getChromosome()[1] == 100 )

vGeneration = Generation()

vGeneration.startGenerations()
