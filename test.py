import datetime

worktodo = 72
now = datetime.datetime.now()
deadline = datetime.datetime.fromisoformat('2021-03-28')
daystodawn = deadline - now
oneday = datetime.timedelta(days=1)
tempdate = now
#print(tempdate.weekday())
workdone = 0
workload = 1
workload = 1


for day in range(daystodawn.days):
    if workdone >= worktodo:
    # arbeit erledigt wenn 72 beweise durchgearbeitet sind
        print("workdone")
        print(tempdate)
        break
    if not(tempdate.weekday() == 6) and not(tempdate.weekday() == 5):
        workdone = workdone + workload
        if tempdate.weekday() == 4:
            workdone = workdone + 2
    print("{}: {}".format(tempdate.date(), workdone))
    tempdate = tempdate + oneday

print(workdone)



#    if tempdate.weekday() 
#    tempdate
