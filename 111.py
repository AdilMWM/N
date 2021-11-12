import matplotlib.pyplot as plt
#import re

with open('2021-09-29_14-44-39.txt','r') as f:
    day=1440
    y1 = []
    y2 = []
    y0 = []
    x = []    
    list = [next(f) for x in range(-1,day)]        ##2021.09.29 14:44 - 2021.09.30 14:44 --- 60*24=1440
    for spl in list:
        scount = spl.split()
        spl1 = spl.replace('.',' ')
        spl2 = spl1.replace(':',' ')
        stime = spl2.split(" ")
        L = len(scount)
        t = []
        count = []
        time = []

        for n in range(2, L, 4):  
            count.append(float(scount[n]))

        for i in range(0,5):
            time.append(float(stime[i]))

        y = count
        t.append(time[0]*12*30*24*60 + time[1]*30*24*60 + time[2]*24*60 + time[3]*60 + time[4] - 1048117844.0)
        x.append(t[0])
        y0.append(y[0])
        y1.append(y[1])
        y2.append(y[2])
    
    fig = plt.figure()
    plt.plot(x, y0 ,'r.-', linewidth=1.0)
    plt.plot(x, y1 ,'b--', linewidth=2.0)
    plt.plot(x, y2 ,'g', linewidth=3.0)
    plt.title('Потоки нейтронов')
    plt.ylabel('Количество импульсов в сек.')
    plt.xlabel('Время ,мин.')
    plt.grid(True)
    plt.show()

        
        

        
        
        
        #stime = re.split(' |:|.',spl)
        
        #start = time1[0]*12*30*24*60 + time1[1]*30*24*60 + time1[2]*24*60 + time1[3]*60 + time1[4]
        #print(start)

        #print (time+count)
