from Chromosome import Chromosome

class Population:

  def __init__(self, _parent) -> None:
    self.rateMutation =_parent.rateMutation
    self.sizePopulation = _parent.sizePopulation
    self.solution = _parent.solution

    self.chromosome = []

    pass

  def currentSize(self) -> int:
    return len(self.chromosome)

  def populate(self):
    for i in range(self.sizePopulation-self.currentSize()):
      vChromosome = Chromosome(self)
      vChromosome.createRandomChromosome()
      self.appendChromosome(vChromosome)

  def sortPopulation(self) -> None:
    self.chromosome = sorted(self.chromosome, key=lambda x: x[1], reverse=True)

  def appendChromosome(self, pChromosome) -> None:
    self.chromosome.append((pChromosome,pChromosome.getFitness()))

  def getChromosome(self) -> list:
    return self.chromosome
