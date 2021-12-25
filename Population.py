import string

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
        self.chromosome.append(vChromosome)
        vChromosome = Chromosome(self)
        vChromosome.createDefineChromosome(['T','e','s','t','x'])
        self.chromosome.append(vChromosome)
        vChromosome = Chromosome(self)
        vChromosome.createDefineChromosome(['T','e','s','x','x'])
        self.chromosome.append(vChromosome)
        vChromosome = Chromosome(self)
        vChromosome.createDefineChromosome(['T','e','x','x','x'])
        self.chromosome.append(vChromosome)
        vChromosome = Chromosome(self)
        vChromosome.createDefineChromosome(['T','x','x','x','x'])
      else:
        vChromosome.createRandomChromosome()

      self.chromosome.append(vChromosome)


    pass


  def getChromosome(self) -> list:
    return self.chromosome

p = Population(3)
# p.getChromosome()

for i in p.getChromosome():
  print(i.getGenes())


# chromosome = Chromosome('ana',10)

# chromosome.createRandomChromosome()

# print(chromosome.getChromosome())
# print(chromosome.getFitness())

# chromosome.createDefineChromosome(['a','n','a'])

# print(chromosome.getChromosome())
# print(chromosome.getFitness())