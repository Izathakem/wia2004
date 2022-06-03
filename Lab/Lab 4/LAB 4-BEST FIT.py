# BEST-FIT

# Function to allocate memory to blocks
# as per Best fit algorithm
# m number of available blocks
# n number of processes
def bestFit(blockS, m, processS, n):

    # Stores block id of the block
    # allocated to a process
    allocation = [-1] * n

    # pick each process and find suitable
    # blocks according to its size ad
    # assign to it
    for i in range(n):

        # Find the best fit block for
        # current process
        bestIdx = -1
        for j in range(m):
            if blockS[j] >= processS[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockS[bestIdx] > blockS[j]:
                    bestIdx = j

        # If we could find a block for
        # current process
        if bestIdx != -1:

            # allocate block j to p[i] process
            allocation[i] = bestIdx

            # Reduce available memory in this block.
            blockS[bestIdx] -= processS[i]

    print("Process No. Process Size	 Block no.")
    for i in range(n):
        print(i + 1, "		 ", processS[i],
              end="		 ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


# Driver code
if __name__ == '__main__':

    blockS = list(int(num) for num in input(
        "Please enter block size: ").strip().split())

    processS = list(int(num) for num in input(
        "Please enter process size: ").strip().split())


m = len(blockS)
n = len(processS)

bestFit(blockS, m, processS, n)
