from subprocess import *
import time

# note that find / is remove from the command list, it takes long time.
commands = [
    'sleep 3',
    'ls -l /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
    ]


# I was not able to use the multithreading or creating subprocesses running at the
#same time.
def perform(process):
    b = Popen(process, shell=True)
    t1 = time.time()
    b.wait()
    t2 = time.time()
    return((t2-t1),process)

# I used a loop to iterate through the commands list and execute every commands and store its time.
def report(cmds = commands):
    
    result = []
    for i in cmds:
       result.append(perform(i))


    total= sum([i[0] for i in result])
    print("Report : \n========\nTotal elapsed time:\t{}\nAverage:\t\t{}\nMaximum:\t\t{}\nMinimum:\t\t{}".format(total, (total/len(result)) ,max(result), min(result)))
        

report()
