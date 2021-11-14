import matplotlib.pyplot as plt
#import re

with open('2021-09-29_14-44-39.txt','r') as f:
    day = 1440
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
    
    def title():
        plt.ylabel('Количество импульсов в сек.')
        plt.xlabel('Время ,мин.')

    fig = plt.figure()

    #plt.title('Потоки нейтронов')
    f1 = fig.add_subplot(2,2,1) 
    title()
    f2 = fig.add_subplot(2,2,2)
    title()
    f3 = fig.add_subplot(2,2,3)
    title()
    f4 = fig.add_subplot(2,2,4)
    title()

    ax1 = f1.plot(x, y0 ,'r.-', linewidth=1.0)
    ax2 = f2.plot(x, y1 ,'b--', linewidth=1.5)
    ax3 = f3.plot(x, y2 ,'g', linewidth=2.0)
    ax41 = f4.plot(x, y0 ,'r.-', linewidth=1.0)
    ax42 = f4.plot(x, y1 ,'b--', linewidth=1.5)
    ax43 = f4.plot(x, y2 ,'g', linewidth=2.0)
    
    f1.grid(True)
    f2.grid(True)
    f3.grid(True)
    f4.grid(True)
    
    plt.show()


        #stime = re.split(' |:|.',spl)
