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

    items=delay.items()
    i=0
    for k,v in items:
        worksheet1.write(i, 0, k)  # 表格的第一行开始写。第一列，第二列。。。。
        worksheet1.write(i, 1, v)
        i+=1
    sortKey=sorted(parallelism)
    for i in range(len(sortKey)):
        worksheet2.write(i, 0, sortKey[i])  # 表格的第一行开始写。第一列，第二列。。。。
        worksheet2.write(i, 1, parallelism[sortKey[i]])
    f.close()
#将渠道对应的时延写入dict
def classify(line,delay,parallelism):
    delayTime=line.split(',')[1][:-2]
    if delayTime.find(">") != -1:
        delayTime = delayTime.split("> ")[1]
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
    file.close()
#初始化时延统计字典
def initMydic(delay):
    delay['0-100'] = 0
    delay['100-200'] = 0
    delay['200-300'] = 0
    delay['300-400'] = 0
    delay['400-500'] = 0
    delay['500-600'] = 0
    delay['600-700'] = 0
    delay['700-800'] = 0
    delay['800-900'] = 0
    delay['900-1000'] = 0
    delay['1000-1100'] = 0
    delay['1100-1200'] = 0
    delay['1200-1300'] = 0
    delay['1300-1400'] = 0
    delay['1400-1500'] = 0
    delay['1500-1600'] = 0
    delay['1600-1700'] = 0
    delay['1700-1800'] = 0
    delay['1800-1900'] = 0
    delay['1900-2000'] = 0
    delay['2000-2100'] = 0
    delay['2100-2200'] = 0
    delay['2200-2300'] = 0
    delay['2300-2400'] = 0
    delay['2400-2500'] = 0
    delay['2500-2600'] = 0
    delay['2600-2700'] = 0
    delay['2700-2800'] = 0
    delay['2800-2900'] = 0
    delay['2900-3000'] = 0
    delay['>3000'] = 0

delay={}
delay_crm={}
delay_902={}#时延统计
delay_903={}#时延统计
delay_904={}#时延统计
delay_906={}#时延统计
delay_910={}#时延统计
delay_100={}
delay_100069={}#时延统计



parallelism={}
parallelism_crm={}
parallelism_902={}#并发统计
parallelism_903={}#并发统计
parallelism_904={}#并发统计
parallelism_906={}#并发统计
parallelism_910={}#并发统计
parallelism_100={}#并发统计
parallelism_100069={}#并发统计


initMydic(delay)
initMydic(delay_crm)
initMydic(delay_902)
initMydic(delay_903)
initMydic(delay_904)
initMydic(delay_906)
initMydic(delay_910)
initMydic(delay_100)
initMydic(delay_100069)


date="2018-01-06"
def readfile(date):
    ipList=['135','139','142','143','145','147']
    #ipList=['135']
    for ip in ipList:
        filepath='D:\\zhou\\'+ip+'.'+date+'.log'
        print("read file: "+filepath)
        file=open(filepath)
        i=0
        for line in file.readlines():
            classify(line,delay,parallelism)
            if line.endswith('906\n'):
                classify(line,delay_906,parallelism_906)
                classify(line, delay_crm, parallelism_crm)
            elif line.endswith('902\n'):
                classify(line, delay_902, parallelism_902)
                classify(line, delay_crm, parallelism_crm)
            elif line.endswith('903\n'):
                classify(line, delay_903, parallelism_903)
            elif line.endswith('904\n'):
                classify(line, delay_904, parallelism_904)
                classify(line, delay_crm, parallelism_crm)
            elif line.endswith('910\n'):
                classify(line, delay_910, parallelism_910)
            elif line.endswith('100\n'):
                classify(line, delay_100, parallelism_100)
            elif line.endswith('100069\n'):
                classify(line, delay_100069, parallelism_100069)
            else:
                pass
        file.close()

readfile(date)

print(delay)
writeToexcel2(date,delay_crm,parallelism_crm,".crm")
writeToexcel2(date,delay_902,parallelism_902,".902")
writeToexcel2(date,delay_903,parallelism_903,".903")
writeToexcel2(date,delay_904,parallelism_904,".904")
writeToexcel2(date,delay_906,parallelism_906,".906")
writeToexcel2(date,delay_910,parallelism_910,".910")
writeToexcel2(date,delay_100,parallelism_100,".100")
writeToexcel2(date,delay_100069,parallelism_100069,".100069")
writeToexcel2(date,delay,parallelism=parallelism)
