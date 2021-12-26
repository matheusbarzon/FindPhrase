import random
import string

class Chromosome:

  charactersToRandom = ' ' + string.ascii_letters + string.digits

  def __init__(self, _parent) -> None:
    self.solution = _parent.solution

    self.rateMutation = _parent.rateMutation

    self.fitness = 0
    self.genes = []

    pass

  def createRandomChromosome(self) -> None:
    for i in range(len(self.solution)):
      self.genes.append(self.getRandomGene())

    self.generateFitness()

  def createDefinedChromosome(self,pGenes=[]) -> None:
    self.genes = pGenes
    for iterator in range(len(self.genes)):
      if self.getRandomNumber() <= self.getTaxaDeMutacao():
        self.genes[iterator] = self.getRandomGene()

    self.generateFitness()

  def getRandomNumber(self) -> int:
    return random.randint(0, 100)

  def getRandomGene(self) -> str:
    return ''.join(random.choice(self.charactersToRandom) for _ in range(1))

  def setTaxaDeMutacao(self, pRateMutation=int) -> None:
    self.rateMutation = pRateMutation

  def getTaxaDeMutacao(self) -> int:
    return self.rateMutation

  def getGenes(self) -> list:
    return self.genes

  def getChromosome(self) -> str:
    vReturn = ''
    for interator in range(len(self.genes)):
      vReturn += str(self.genes[interator])

    return vReturn

  def generateFitness(self) -> None:
    vFitness = 0
    for interator in range(len(self.genes)):
      if self.genes[interator] == self.solution[interator]:
        vFitness += 1

    self.setFitness(vFitness)

  def setFitness(self, pFitness) -> None:
    self.fitness = pFitness

  def getFitness(self) -> float:
    return ((self.fitness*100)/len(self.genes))
