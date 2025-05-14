streams_start = int(input())
stream_lengths = []
for i in range(streams_start):
    streamlength = int(input())
    stream_lengths.append(streamlength)
while True:
    command = int(input())
    if command == 99:
        streamsplit = int(input())
        leftsplit = int(input())
        leftsplitpercent = leftsplit/100
        besplit = stream_lengths[streamsplit-1]
        stream_lengths[streamsplit - 1] = besplit*leftsplitpercent
        stream_lengths.insert(streamsplit, besplit*(1-leftsplitpercent))
    if command == 88:
        streamjoin = int(input())
        aftersplit = stream_lengths[streamjoin-1] + stream_lengths[streamjoin]
        stream_lengths[streamjoin-1] = aftersplit
        stream_lengths.pop(streamjoin)

        # stream_lengths[str(streamsplit+1)] = stream_lengths[streamsplit+1]*leftsplitpercent/100
    if command == 77:
        break

print(' '.join(map(str, map(int,stream_lengths))),end="")