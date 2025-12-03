import sys

BANK_BATTERIES = 12


def main(infile):
    output = 0
    with open(infile) as f:
        for line in f:
            output += max_jolt(line.rstrip())
    return output


def max_jolt(s):
    sequence = [int(c) for c in s]
    # dp[i][j] = the maximum joltage of batteries 0..j where you can take at
    # most i+1 batteries
    dp = [[0] * len(sequence) for _ in range(BANK_BATTERIES)]

    # base case, 1 battery remaining. Always take the single greatest
    max_battery = 0
    for j in range(len(sequence)):
        max_battery = max(max_battery, sequence[j])
        dp[0][j] = max_battery

    for i in range(1, BANK_BATTERIES):
        for j in range(len(sequence)):
            # cannot take more batteries than batteries remaining
            if j < i:
                continue
            dp[i][j] = max(dp[i-1][j-1] * 10 + sequence[j], dp[i][j-1])

    return dp[BANK_BATTERIES-1][len(sequence)-1]


print(main(sys.argv[1]))