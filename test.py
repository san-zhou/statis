import xlwt
import xlsxwriter
#将延时分区段
def numClassify(num):
    num=eval(num)
    if num<=100:
        return "0-100"
    elif num <=200:
        return "100-200"
    elif num <=300:
        return "200-300"
    elif num <=400:
        return "300-400"
    elif num <=500:
        return "400-500"
    elif num <=600:
        return "500-600"
    elif num <=700:
        return "600-700"
    elif num <=800:
        return "700-800"
    elif num <=900:
        return "800-900"
    elif num <=1000:
        return "900-1000"
    elif num <=1100:
        return "1000-1100"
    elif num <=1200:
        return "1100-1200"
    elif num <=1300:
        return "1200-1300"
    elif num <=1400:
        return "1300-1400"
    elif num <=1500:
        return "1400-1500"
    elif num <=1600:
        return "1500-1600"
    elif num <=1700:
        return "1600-1700"
    elif num <=1800:
        return "1700-1800"
    elif num <=1900:
        return "1800-1900"
    elif num <=2000:
        return "1900-2000"
    elif num <=2100:
        return "2000-2100"
    elif num <=2200:
        return "2100-2200"
    elif num <=2300:
        return "2200-2300"
    elif num <=2400:
        return "2300-2400"
    elif num <=2500:
        return "2400-2500"
    elif num <=2600:
        return "2500-2600"
    elif num <=2700:
        return "2600-2700"
    elif num <=2800:
        return "2700-2800"
    elif num <=2900:
        return "2800-2900"
    elif num <= 3000:
        return "2900-3000"
    else:
        return ">3000"
#xlsxwriter写入到xlsx
def writeToexcel2(ipAndDate,delay={}, parallelism={}, channelId=''):
    filename=ipAndDate+channelId+'.xlsx'
    f=xlsxwriter.Workbook(filename)

    worksheet1 = f.add_worksheet('时延统计')
    worksheet2 = f.add_worksheet('并发统计')

    sortKey1 = sorted(delay)
    for i in range(len(sortKey1)):
        worksheet1.write(i, 0, sortKey1[i])  # 表格的第一行开始写。第一列，第二列。。。。
        worksheet1.write(i, 1, delay[sortKey1[i]])
    sortKey=sorted(parallelism)
    for i in range(len(sortKey)):
        worksheet2.write(i, 0, sortKey[i])  # 表格的第一行开始写。第一列，第二列。。。。
        worksheet2.write(i, 1, parallelism[sortKey[i]])
    f.close()
#将渠道对应的时延写入dict
def classify(line,delay,parallelism):
    delayTime=line.split(',')[1][:-2]
    numRange=numClassify(delayTime)
    if(delay.get(numRange)==None):
        delay[numRange]=1
    else:
        delay[numRange]+=1
    time=line[11:19].replace(':','')
    if(parallelism.get(time)==None):
        parallelism[time]=1
    else:
        parallelism[time]+=1
#xlwd写入到xls
def writeToexcel(myList,myDict,date="2017-12-21"):
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    sheet2 = f.add_sheet(u'sheet2', cell_overwrite_ok=True)  # 创建sheet
    for i in range(len(myList)):
        sheet1.write(i, 0, myList[i])  # 表格的第一行开始写。第一列，第二列。。。。
    #sortDict=sorted(myDict.items(),key=lambda d:d[0])
    sortKey=sorted(myDict)
    for i in range(len(sortKey)):
        sheet2.write(i, 0, sortKey[i])  # 表格的第一行开始写。第一列，第二列。。。。
        sheet2.write(i, 1, myDict[sortKey[i]])
    print(sortKey)
    f.save(date+'.xls')  # 保存文件
def readfile(filepath):
    file=open(filepath)
    for line in file.readlines():

        time = line[11:19].replace(':', '')
        if (parallelism.get(time) == None):
            parallelism[time] = 1
        else:
            parallelism[time] += 1

        if line.endswith('906\n'):
            classify(line,delay_906,parallelism_906)
        elif line.endswith('902\n'):
            classify(line, delay_902, parallelism_902)
        elif line.endswith('904\n'):
            classify(line, delay_904, parallelism_904)
        else:
            pass
    file.c
parallelism={}
delay_906={}#时延统计
parallelism_906={}#并发统计
delay_904={}#时延统计
parallelism_904={}#并发统计
delay_902={}#时延统计
parallelism_902={}#并发统计


ip="147"
date="2017-12-22"
filepath='D:\\zhou\\'+ip+'.'+date+'.log'
readfile(filepath)


writeToexcel2(ip+'.'+date,delay_902,parallelism_902,".902")
writeToexcel2(ip+'.'+date,delay_904,parallelism_904,".904")
writeToexcel2(ip+'.'+date,delay_906,parallelism_906,".906")
writeToexcel2(ip+'.'+date,parallelism=parallelism)
