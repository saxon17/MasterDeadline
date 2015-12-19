
f=open('20_s.txt' ,'rb')
# print f.read()
f.seek(0,0)
# HexText = ''
line = ''
lineMark = 0
count = 0
d = {}

while 1:
    count += 1
    byte = f.read(1)
    line += byte.encode('hex') + ' '
    if byte == '':
        print str(lineMark)+':',line
        d[lineMark] = line.split(' ')
        break
    else:
            hexstr =  "%s" % byte.encode('hex')
            #     decnum = int(hexstr, 16)
            #     print byte, hexstr
            #     HexText += hexstr
            if  count == 16:
                    print str(lineMark)+':',line
                    d[lineMark] = line.split(' ')
                    line =''
                    lineMark += 10
                    count = 0
total_segments_count = int((d[720][1]),16)
Unknowpara = int(d[710][3]+d[710][4]+d[710][5],16)
print 'Unknowpara:',int(d[710][3]+d[710][4]+d[710][5],16)
print 'total segments count:',int((d[720][1]),16)
print 'The first seg:' ,d[720][7],d[720][8],d[720][9]

# next_Line = current_line = 720
#
# current_offset = 7
def getVideoDurInHexTable(lineMark,current_line,offset):
    Vedio_count = 1
    videoDurFirstByte_lst= []
    while(1):
        if current_line > lineMark:
            break
        # print Vedio_count,d[current_line][offset],'(',current_line,offset,')'
        videoDurFirstByte_lst.append(d[current_line][offset])
        if offset+12 > 15:
            current_line += 10
            offset = (offset+12)%16
        else:
            offset += 12
        Vedio_count += 1
    return  videoDurFirstByte_lst
def magic(string):
    return int(string,16)
def getDoublueVideoSeg(lst):

    list1 = lst[::2]
    list2 = lst[1::2]
    # print list1
    # print list2
    DiFlen = len(list1)-len(list2)
#     print 'DiFlen:',DiFlen
    if DiFlen > 0:
        list2 += [0] * DiFlen
    else:
        list1 += [0] * (-DiFlen)
    # print list1
    # print list2
    return [x+y for x, y in zip(list1, list2)]
A = getVideoDurInHexTable(lineMark,720,7)
B = getVideoDurInHexTable(lineMark,720,8)
C = getVideoDurInHexTable(lineMark,720,9)
Seg_dur_hex_lst = map(lambda t,:t[0]+t[1]+t[2],zip(A,B,C))
Seg_dur_hex_lst = map(magic,Seg_dur_hex_lst)

Sigle_Segments_Duration_lst =  map(lambda x:x/Unknowpara,Seg_dur_hex_lst)


for index,dur in enumerate(getDoublueVideoSeg(Sigle_Segments_Duration_lst)):
    print 'video'+str(index+1),dur






f.close()