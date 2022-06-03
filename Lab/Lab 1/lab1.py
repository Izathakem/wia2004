def turn_arnd_time(process):
    tasks = len(process) #number of tasks
    tot = 0
    for i in range(tasks):
        for j in range(i+1): #fcfs so cumulative service time INCLUDING SELF = finish time
            tot += process[j][1]
        tot -= process[i][0] #minus arrival time 
    return tot 

def wait_time(process):
    tasks = len(process) #number of tasks
    tot = 0
    for i in range(tasks):
        for j in range(i): #fcfs so cumulative service time of PREDECESSORS = start time
            tot += process[j][1]
        tot -= process[i][0] #minus arrival time 
    return tot 

#extra step: ensure process array is valid (ie equal column length)
def validate(process):
    for i in range(len(process)-1):
        if len(process[i]) != len(process[i+1]):
            return False
    return True 


# ========== runner code ==========
if __name__ == "__main__":
    process = [[0,3], [2,6], [4,4], [6,5], [8,2]]
    if validate(process):
        tasks = len(process)
        turn_arnd = turn_arnd_time(process)
        wait = wait_time(process)
        print(f'Turn around time: {turn_arnd}')
        print(f'Average turn around time: {turn_arnd/tasks}')
        print(f'Wait time: {wait}')
        print(f'Average wait time: {wait/tasks}')

