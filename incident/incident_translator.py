class Incident:
   entCount = 0

   def __init__(self, upnode,dnnode,sttime,edtime,loss):
      self.upnode = upnode
      self.dnnode = dnnode
      self.sttime = sttime
      self.edtime = edtime
      self.loss = loss
      Incident.entCount += 1
   
   def writeEvent(output):
       output.write(Incident.count+'\n')
       output.write(self.upnode+'\t'+self.dnnode+'\t'+self.sttime+'\t'+self.edtime+'\t'+self.loss+'\n')

class workzone:
   zoneCount = 0

   def __init__(self, upnode,dnnode,sttime,edtime,loss):
      self.upnode = upnode
      self.dnnode = dnnode
      self.sttime = sttime
      self.edtime = edtime
      self.loss = loss
      self.slmt = '55'
      self.rate = '0.5'
      Incident.entCount += 1

def readevents(efile):
    incidents=[]
    roadwork=[]
    eline=efile.readlines()
    entfolder=path+'\\'+'obs'+entfile[0:13]  #new a folder named with dates
        if not os.path.exists(entfolder):
            os.makedirs(entfolder)
    for i in range(1,len(linkline)):
        features=eline[i].rstrip('\n').split(',')
        lat=features[14]
        lon=features[15]
        timestamp=features[1].split(' ')
        date=timestamp[0]
        sttime=timestamp[1]
        year=date.split('/')[2]
        month=date.split('/')[0]
        day=date.split('/')[1]
        linkoutput=open(entfolder+'\\'+'obs_'+year+'_'+month+'_'+day+'.csv','a+')
    linkfile.close()
    return links