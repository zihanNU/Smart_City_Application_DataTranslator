import os
import csv
import gzip

class MEASURE:
   
   def __init__(self, did, cnt, vph,occ,spd,time,date,obflag):
        self.did=did
        self.cnt=cnt
        self.vph=vph
        self.occ=occ
        self.spd=spd
        self.time=time
        self.date=date
        self.obflag=obflag
   def writeCOUNT(self,output):
       #output1.write(self.cnt+'\n')
       output.write(self.did+','+self.obflag+','+self.time+','+self.cnt+','+self.vph+','+self.occ+','+self.spd+'\n')
       output.close
       
path = os.getcwd()
folder = next(os.walk(path))[1]
newpath=path+'\\'+folder[0]
filenames = next(os.walk(newpath))[2]


linkdetail=open("linkwithobsdetail.dat",'r')
detectorids=[]
detectorline=linkdetail.readlines()
for i in range(1,len(detectorline)):
    did=detectorline[i].rstrip('\n').split('\t')[-1]
    if did !='0':
        detectorids.append(did)
linkdetail.close()


linkoutput1=open('linkcounts.dat','w')
linkoutput1.write('param OBSFLOW :=\n')
#linkflow=[]
for obsfile in filenames:
   linkobs=gzip.open(newpath+'\\'+obsfile,'r')
   obsline=linkobs.readlines()
for i in range(1,1000):
               #len(obsline)):
    features=obsline[i].rstrip('\n').split(',')
    did=features[0]
    if did in detectorids:
        timestamp=features[4].split(' ')
        date=timestamp[0]
        time=timestamp[1]
        year=date.split('/')[2]
        month=date.split('/')[0]
        day=date.split('/')[1]
        flag=detectorids.index(did)
        linkoutput2=open('obs_'+year+'_'+month+'_'+day+'.csv','a+')
        l=MEASURE(did,features[8],features[9],features[10],features[11],time,date,str(flag))
        #linkflow.append(l)
        l.writeCOUNT(linkoutput2)
linkobs.close()


           
    
