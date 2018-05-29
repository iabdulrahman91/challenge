from subprocess import *
import time


commands = [
    'sleep 3',
    'ls -l /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
    ]


def perform(process):
    b = Popen(process, shell=True)
    t1 = time.time()
    b.wait()
    t2 = time.time()
    return((t2-t1),process)

def report(cmds = commands):
    
    result = []
    for i in cmds:
       result.append(perform(i))


    total= sum([i[0] for i in result])
    print("Report : \n========\nTotal elapsed time:\t{}\nAverage:\t\t{}\nMaximum:\t\t{}\nMinimum:\t\t{}".format(total, (total/len(result)) ,max(result), min(result)))
        

report()
