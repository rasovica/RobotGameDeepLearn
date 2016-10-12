import subprocess

#output = subprocess.Popen(["rgrun", "-c 100", "-H", "robot1.py", "simple_bot.py", "-qqqq"], stdout=subprocess.PIPE).communicate()[0]
output = "simple_bot - [0, 100, 0]     - [15, 38] (-22)"


def fitness(output):
    score = [float(a) for a in output.split("[")[1].split("]")[0].split(",") + output.split("[")[2].split("]")[0].split(",")]
    return ((score[0]+1)/(score[1]+1))+((score[3]+1)/(score[4]+1))

print fitness(output)
