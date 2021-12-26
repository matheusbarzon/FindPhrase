from Generation import Generation

class Main:

  def __init__(self) -> None:
    pass


generation = Generation()

#percent of best chromosome to crossover
generation.setRateCrossover(25)

#percent of the previous gene of chromosome in the next generation
generation.setRateRemained(75)

#percent of mutation in defined chromosome
generation.setRateMutation(12)

#number max of generaions
generation.setMaxGenerations(1000)

#number max os population/chromosome
generation.setSizePopulation(250)

#solution to find
generation.setSolution('Phrase to find')

#ignore de max of generation and keep going until find solution
generation.setUntilFind(False)


generation.setPrintDetails(True)
generation.setPrintGeneration(True)

generation.startGenerations()