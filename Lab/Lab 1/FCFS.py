
def fcfs():
    print("hello")
    # processes ["name", arrivalTime, burstTime]
    processes = [["P1", 2, 6], ["P2", 5, 2], ["P3", 1, 8], ["P4", 0, 3], ["P5", 4, 4]]
    # sort array based on arrivalTime
    sortedProcesses = []
    counter = 0
    while len(sortedProcesses) < 5:
        for i in range(len(processes)):
            for j in range(len(processes[i])):
                if counter == processes[i][1]:
                    sortedProcesses.append(processes[i])
                    break
        counter+=1
    queue = []
    executing = []
    time = 0
    stop = False
    executing.append(sortedProcesses[0])
    counter = sortedProcesses[0][2]
    print("Time:", time)
    print("Executing:", executing)
    print("Queue:", queue)
    time += 1
    counter -= 1
    waitingTime = 0
    turnaroundTime = 0
    while stop == False:
        waitingTime += len(queue)
        for i in range(len(sortedProcesses)):
            for j in range(len(sortedProcesses[i])):
                if counter == 0 and len(executing) > 0:
                    turnaroundTime += time - executing[0][1]
                    executing.pop(0)
                    if len(queue) > 0:
                        executing.append(queue.pop(0))
                        counter = executing[0][2]
                        break
                if time == sortedProcesses[i][1]:
                    if len(executing) == 0 and len(queue) > 0:
                        executing.append(queue.pop(0))
                    else:
                        queue.append(sortedProcesses[i])
                        break
                else:
                    continue
        print("Time:", time)
        print("Executing:", executing)
        print("Queue:", queue)
        time +=1
        counter -=1
        if len(executing) == 0:
            stop = True
    print("\nTotal Waiting Time:", waitingTime)
    print("Total turnaround Time:", turnaroundTime)
    print("Avg. waiting Time:", waitingTime / len(processes))
    print("Avg. turnaround Time:", turnaroundTime / len(processes))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fcfs()

