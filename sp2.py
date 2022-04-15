file = open('data/s.dat','r')
read = file.readlines()
n = 0
#global y1
y={}
for stri in read:
    n+= 1 #номер строки данных  
    splitstr = stri.split()
    y = splitstr[4:]
    y = [int(i) for i in y] 
    summ = sum(y)

    y1 = []
    
    if summ > 0:
        y1 = y
        y1 = [str(e) for e in y1]
        
        y_str = ''.join([str(ii) + ' ' for ii in y1])
        #y_str.append(splitstr[0])
        y_str1 =splitstr[0] + ' ' + splitstr[1] + ' ' +  splitstr[2] + ' ' +  splitstr[3] + ' ' +  y_str + '\n' 
        
        #y11 = str(y1)
        #y11 = [''.join(e) for e in y1]
        #y_str = ''.join(y11)
        file1 = open('data/s111.dat','a')
        file1.write(y_str1)
        file1.close
    


