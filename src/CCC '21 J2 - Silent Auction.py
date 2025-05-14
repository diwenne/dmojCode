bids = {}
for i in range(int(input())):
    name = input()
    bid = int(input())
    bids.setdefault(bid,[]).append(name)

print(bids[max(bids)][0])
