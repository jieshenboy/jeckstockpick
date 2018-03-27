
rfileName = 'alive.txt'
wfileName = 'newalive.txt'
with open(wfileName, 'w') as wfp:
    with open(rfileName,'r') as rfp:
        lines = rfp.readlines()
        for line in lines:
            lineList = line.split('\t')
            wline = lineList[0]+':'+lineList[1]
            wfp.write("'"+wline+ "'"+','+'\r\n')





