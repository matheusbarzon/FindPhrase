from Chromosome import Chromosome

class Population:

  chromosome = []
  sizePopulation = 0

  def __init__(self, pSizePopulation) -> None:

    self.sizePopulation = pSizePopulation

    self.rateMutation = 10
    self.solution = 'Teste'

    for i in range(self.sizePopulation):
      vChromosome = Chromosome(self)

      if i == 0:
        vChromosome.createDefineChromosome(['T','e','s','t','e'])
      else:
        vChromosome.createRandomChromosome()

      self.chromosome.append(vChromosome)

    pass


  def getChromosome(self) -> list:
    return self.chromosome
