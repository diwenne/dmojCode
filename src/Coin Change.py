n = int(input())
d = int(input())
denom = []
for i in range(d):
    denom.append(int(input()))
dp = [n+1 for _ in range(n+1)]
dp[0] = 0
for current in range(1,n+1):
    for coin in denom:
        if current - coin >= 0:
            dp[current] = min(dp[current],1+dp[current-coin])
if dp[n] != n+1:
    print("Roberta wins in " + str(dp[n]) + " strokes.")
else:
    print("Roberta acknowledges defeat.")
