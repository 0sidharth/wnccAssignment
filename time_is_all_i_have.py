import statistics

fd = open('timestat.txt', 'r')
content = fd.readlines()

real = []
sys = []
user = []
flag = 0
out = 0
count = 0
letter = 0

for line in content:
    count = count + 1
    for i in line:
        if (count % 4) == 2:
            if i == ' ':
                flag = 1
            elif flag == 1:
               letter = letter + 1
               if letter == 1:
                   out += int(i) * 60
               if letter == 3:
                    out += int(i)
               if letter == 5:
                   out += int(i) * 0.1
               if letter == 6:
                   out += int(i) * 0.01
               if letter == 7:
                   out += int(i) * 0.001
                   real.append(out)
                   out = 0
                   flag = 0
                   letter = 0
        elif (count % 4) == 3:
            if i == ' ':
                flag = 1
            elif flag == 1:
               letter = letter + 1
               if letter == 1:
                   out += int(i) * 60
               if letter == 3:
                    out += int(i)
               if letter == 5:
                   out += int(i) * 0.1
               if letter == 6:
                   out += int(i) * 0.01
               if letter == 7:
                   out += int(i) * 0.001
                   user.append(out)
                   out = 0
                   flag = 0
                   letter = 0
        elif (count % 4) == 0:
            if i == ' ':
                flag = 1
            elif flag == 1:
               letter = letter + 1
               if letter == 1:
                   out += int(i) * 60
               if letter == 3:
                   out += int(i)
               if letter == 5:
                   out += int(i) * 0.1
               if letter == 6:
                   out += int(i) * 0.01
               if letter == 7:
                   out += int(i) * 0.001
                   sys.append(out)
                   out = 0
                   flag = 0
                   letter = 0

realDev = statistics.stdev(real)
realAvg = statistics.mean(real)
sysDev = statistics.stdev(sys)
sysAvg = statistics.mean(sys)
userDev = statistics.stdev(user)
userAvg = statistics.mean(user)
realCount = 0
sysCount = 0
userCount = 0

for i in real:
    if i > realAvg - realDev and i < realAvg + realDev:
        realCount = realCount + 1
for i in sys:
    if i > sysAvg - sysDev and i < sysAvg + sysDev:
        sysCount = sysCount + 1
for i in user:
    if i > userAvg - userDev and i < userAvg + userDev:
        userCount = userCount + 1

print "Number of runs: ", count / 4
print "Average Time statistics"
print "real ", realAvg, " user ", userAvg, " sys ", sysAvg
print "Standard deviation of Time statistics"
print "real ", realDev, " user ", userDev, " sys ", sysDev
print "Number of runs within (average - standard deviation) to (average + standard deviation)"
print "real ", realCount, " user ", userCount, " sys ", sysCount
