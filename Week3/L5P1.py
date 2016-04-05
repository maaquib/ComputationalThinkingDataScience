balls = []
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    yes = 0.0
    for i in range(numTrials):
        balls = [1, 1, 1, 2, 2, 2]
        match = True
        first = True
        for j in range(3):
            c = chooseBall(balls)
            if first:
                choice = c
                first = False
            elif choice != c:
                match = False
                break
            else:
                continue
        if match:
            yes += 1.0
    return (yes/numTrials)
        

def chooseBall(balls):
    idx = random.choice(range(len(balls)))
    choice = balls[idx]
    balls.remove(balls[idx])
    return choice