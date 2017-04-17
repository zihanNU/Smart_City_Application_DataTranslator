import os
import csv
import gzip
from operator import itemgetter


class LINK:
   
   def __init__(self, lid, inode, jnode):
        self.lid=lid
        self.inode=inode
        self.jnode=jnode
        self.flag='0'
        self.obflag='-1'
        self.did='0'
   def displayLINK(self):
       print self.lid, self.inode,self.jnode,self.flag,self.obflag,self.did

class DETECTOR:
   
   def __init__(self, did, inode, jnode):
        self.did=did
        self.inode=inode
        self.jnode=jnode
   def displayDETECTOR(self):
       print self.did, self.inode,self.jnode

class MEASURE:

   def __init__(self, did, cnt, vph, occ, spd, time, date, obflag):
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


def readlinks():
    links=[]
    linkfile=open("linklist.csv",'r')
    linkline=linkfile.readlines()
    for i in range(1,len(linkline)):
        features=linkline[i].rstrip('\n').split(',')[0:3]
        links.append(LINK(features[0],features[1],features[2]))
    linkfile.close()
    return links
   
def readdetlinks():
    detectors=[]
    detectorids=[]
    detectorfile=open("Detector_Link.csv",'r')
    detectorline=detectorfile.readlines()
    for i in range(1,len(detectorline)):
        features=detectorline[i].rstrip('\n').split(',')
        if len(features[4])<2:
           detectors.append(DETECTOR(features[0],features[2],features[3]))
    detectorfile.close()
    count=0
    links=readlinks()
    for l in links:
       for d in detectors:
          if d.inode==l.inode and d.jnode==l.jnode:
             l.flag='1'
             count=count+1
             l.obflag=str(count)
             l.did=d.did
             #l.displayLINK()
             detectorids.append(l.did)
    return detectorids,links

def writeobs(linkfolder,obsfolder,links):
    filenames = next(os.walk(obsfolder))[2]
    detectorflag=[]
    detectors=[]
    for obsfile in filenames:
        linkobs=open(obsfolder+'\\'+obsfile,'r')
        obsdata=[map(str,line.split(',')[0:4]) for line in linkobs]
        newobsdata=sorted(obsdata, key=itemgetter(1))
        linkoutput1=open(linkfolder+'\\'+'linkcounts'+obsfile[4:-1].rstrip('.cs')+'.dat','w')
        linkoutput2=open(linkfolder+'\\'+'linkwithobs'+obsfile[4:-1].rstrip('.cs')+'.dat','w')
        linkoutput1.write('param OBSFLOW :=\n')
        for data in newobsdata:
            obflag=data[1]
            if obflag not in detectorflag:
                count=1
                detectorflag.append(obflag)
                detectors.append(data[0])
            data[1]=str(detectorflag.index(obflag)+1)
            linkoutput1.write(data[1]+'\t'+str(count)+'\t'+data[3]+'\n')
            count=count+1
        for link in links:
            if link.did in detectors:
                link.obflag=str(detectors.index(link.did)+1)
            else:
                link.obflag='-1'
            linkoutput2.write(link.obflag+'\n')
        linkoutput1.write(';')
        linkoutput1.close()
        linkoutput2.close()

def scanmeasures(detectorids,links):
    linkflow=[]
    linkrate=[]
    path = os.getcwd()
    folder = next(os.walk(path))[1]
    newpath=path+'\\'+folder[0]  #get the first folder,where the detector data stored
    filenames = next(os.walk(newpath))[2]
    rate=0.9
    count=0
    for obsfile in filenames:
        obsfolder=path+'\\'+'obs'+obsfile[0:13]  #new a folder named with dates
        if not os.path.exists(obsfolder):
            os.makedirs(obsfolder)
        linkfolder=path+'\\'+'link'+obsfile[0:13]  #new a folder named with dates
        if not os.path.exists(linkfolder):
            os.makedirs(linkfolder)
        linkobs=gzip.open(newpath+'\\'+obsfile,'r')
        obsline=linkobs.readlines()
        for i in range(1,len(obsline)):  #scan detector data
            features=obsline[i].rstrip('\n').split(',')
            did=features[0]
            if did in detectorids:
                timestamp=features[4].split(' ')
                date=timestamp[0]
                time=timestamp[1]
                count=count+1
                year=date.split('/')[2]
                month=date.split('/')[0]
                day=date.split('/')[1]
                linkoutput=open(obsfolder+'\\'+'obs_'+year+'_'+month+'_'+day+'.csv','a+')
                flag=detectorids.index(did)
                l=MEASURE(did,features[8],features[9],features[10],features[11],time,date,str(flag))
                #print l.did,l.cnt,l.spd
                if count<288:
                    linkrate.append(int(l.cnt)>0)
                    linkflow.append(l)                 
                else:
                    linkrate.append(int(l.cnt)>0)
                    linkflow.append(l)
                    #print sum(linkrate), len(linkrate)*rate
                    if sum(linkrate)>=len(linkrate)*rate:  #check observation rate
                        #print l.did,l.cnt,l.spd,count
                        for linki in linkflow:
                            linki.writeCOUNT(linkoutput)
                    count=0
                    del linkrate[:]
                    del linkflow[:]
        linkobs.close()
        writeobs(linkfolder,obsfolder,links)


if __name__ == "__main__":
   detectorids,links=readdetlinks()
   scanmeasures(detectorids,links)

    
