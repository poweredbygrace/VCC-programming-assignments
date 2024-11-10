import random

def printIntro():
    print("This program simulates a game of racquetball between two players, A and B.")
    print("The program requires the probability of Player A and Player B winning their serves.")
    print("It will simulate multiple games and report the win statistics for each player.\n")

def getInput():
    probA = float(input("Enter the probability of Player A winning a serve (0 to 1): "))
    probB = float(input("Enter the probability of Player B winning a serve (0 to 1): "))
    n = int(input("Enter the number of games to simulate: "))
    return probA, probB, n

def simulatematch(probA, probB, n):
    winsA = 0
    winsB = 0

    for sim in range(n):
        serving = 'Player A'
        while True:
            rand_val = random.random()
            print(rand_val)
            if serving == 'Player A':
                if rand_val < probA:
                    winsA += 1
                    print('Player A win\n')
                    break
                else:
                    serving = 'Player B'
                    print('New serve \n')
            else:
                if random.random() < probB:
                    winsB += 1
                    print('Player B win\n')
                    break
                else:
                    serving = 'Player A'
                    print('New serve \n')

    totalGames = winsA + winsB
    print("\nGames simulated:", totalGames)
    print(f"Wins for A: {winsA} ({winsA / totalGames * 100:.1f}%)")
    print(f"Wins for B: {winsB} ({winsB / totalGames * 100:.1f}%)")

def main():
    printIntro()
    probA, probB, n = getInput()
    simulatematch(probA, probB, n)

# Run the program
if __name__ == "__main__":
    main()
