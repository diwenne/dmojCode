votes = int(input())
who_voted = str(input())
votesA = who_voted.count("A")
votesB = who_voted.count("B")
if votesA == votesB:
    print("Tie")
elif votesA > votesB:
    print("A")
elif votesA < votesB:
    print("B")