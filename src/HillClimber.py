def steepestAscentHillClimber(genes):
    bestScore = yield genes
    while True:
        bestIndex = -1
        for index in xrange(len(genes)):
            # flip the bit at that index
            genes[index] = 1 - genes[index]
            score = yield genes
            if bestScore < score:
                bestScore = score
                bestIndex = index
            # flip the bit at that index back to its original value
            genes[index] = 1 - genes[index]
        if bestIndex != -1:
            genes[bestIndex] = 1 - genes[bestIndex]
        else:
            break


def climb(genes, evaluator, method):
    climber = method(genes)
    iteration = climber.next()
    counter = 0
    while True:
        counter += 1
        try:
            iteration = climber.send(evaluator.evaluate(iteration))
        except StopIteration:
            break
    return counter
