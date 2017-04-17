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
   def writeLINK(self,output1,output2):
       output1.write(self.obflag+'\n')
       output2.write(self.lid+'\t'+self.inode+'\t'+self.jnode+'\t'+self.flag+'\t'+self.obflag+'\t'+self.did+'\n')
             

class DETECTOR:
   
   def __init__(self, did, inode, jnode):
        self.did=did
        self.inode=inode
        self.jnode=jnode
   def displayDETECTOR(self):
       print self.did, self.inode,self.jnode

linkobs1=open("linkwithobs.dat",'w')   
linkobs2=open("linkwithobsdetail.dat",'w')
linkobs2.write('linkid\tinode\tjnode\tflag\tobflag\tdetectorid\n')
               
links=[]        
linkfile=open("linklist.csv",'r')
linkline=linkfile.readlines()
for i in range(1,len(linkline)):
    features=linkline[i].rstrip('\n').split(',')[0:3]
    links.append(LINK(features[0],features[1],features[2]))
#print "t1"
linkfile.close()
   
detectors=[]        
detectorfile=open("Detector_Link.csv",'r')
detectorline=detectorfile.readlines()
for i in range(1,len(detectorline)):
    features=detectorline[i].rstrip('\n').split(',')
    if len(features[4])<2:
       detectors.append(DETECTOR(features[0],features[2],features[3]))
detectorfile.close()        
#print "t2"
count=0
for l in links:
   for d in detectors: 
      if d.inode==l.inode and d.jnode==l.jnode:
         l.flag='1'
         count=count+1
         l.obflag=str(count)
         l.did=d.did
         l.displayLINK()
   l.writeLINK(linkobs1,linkobs2)
linkobs1.close()
linkobs2.close()
           
    
