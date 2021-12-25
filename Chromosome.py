import random
import string

class Chromosome:

  genes = []
  sizeGene = 0
  rateMutation = 0 #percent
  fitness = None

  solution = None

  def __init__(self, pSizeGene=int,pSolution=str,pRateMutation=int) -> None:
    if (pSizeGene != len(pSolution)):
      raise Exception("O valor o parametro \"pSizeGene\" deve ser igual ao tamanho da solução \"pSolution\"")

    self.sizeGene = pSizeGene
    self.solution = pSolution

    self.rateMutation = pRateMutation

    pass

  def createRandomChromosome(self) -> None:
    for i in range(self.sizeGene):
      self.genes.append(self.getRandomGene())

    self.generateFitness()

  def createDefineChromosome(self,pGenes=[]) -> None:
    self.getRandomGene()
    self.genes = pGenes
    for iterator in range(self.sizeGene):
      if self.getRandomNumber() <= self.getTaxaDeMutacao():
        self.genes[iterator] = self.getRandomGene()

    self.generateFitness()

  def getRandomNumber(self) -> int:
    return random.randint(0, 100)

  def getRandomGene(self) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(1))

  def setTaxaDeMutacao(self, pRateMutation=int) -> None:
    self.rateMutation = pRateMutation

  def getTaxaDeMutacao(self) -> int:
    return self.rateMutation

  def getGenes(self) -> list:
    return self.genes

  def getChromosome(self) -> str:
    vReturn = ''
    for iterator in range(self.sizeGene):
      vReturn += str(self.genes[iterator])

    return vReturn

  def generateFitness(self) -> None:
    vFitness = 0
    for interator in range(self.sizeGene):
      if self.genes[interator] == self.solution[interator]:
        vFitness += 1

    self.setFitness(vFitness)

  def setFitness(self, pFitness) -> None:
    self.fitness = pFitness

  def getFitness(self) -> float:
    #percent
    return ((self.fitness*100)/self.sizeGene)


# chromosome = Chromosome(3, 'ana')

# chromosome.createRandomChromosome()

# print(chromosome.getChromosome())
# print(chromosome.getFitness())

#-------------------------

# chromosome.setTaxaDeMutacao(50)

# chromosome.createDefineChromosome(['a','n','a'])

# print(chromosome.getChromosome())
# print(chromosome.getFitness())
