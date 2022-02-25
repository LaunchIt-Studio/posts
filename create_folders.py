import os
import datetime
import time

main_folder = '2022'

if not os.path.exists(main_folder):
    os.mkdir(main_folder)
    for weekNumber in range(1, 53):
        mon = datetime.datetime.strptime('2022-W{}-1'.format(weekNumber), "%Y-W%W-%w").date()
        wed = mon + datetime.timedelta(days=2)
        fri = mon + datetime.timedelta(days=4)
        week_folder = "WEEK_{:02d}".format(weekNumber)
        os.mkdir("{}/{}".format(main_folder,week_folder))
        os.mkdir("{}/{}/{}".format(main_folder,week_folder, mon.strftime('%m-%d-%Y')))
        os.mkdir("{}/{}/{}".format(main_folder,week_folder, wed.strftime('%m-%d-%Y')))
        os.mkdir("{}/{}/{}".format(main_folder,week_folder, fri.strftime('%m-%d-%Y')))
else:    
    print("Folders already created!")
