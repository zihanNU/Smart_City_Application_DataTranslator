input file£º
1£©linklist.csv: it has 5 columes, which are OBJECTID,INODE,JNODE,LENGTH,LANES. These are the first 5 columes obtained from the feature table of shp file. 
2)Detector_Link.csv: it has 6 columes, which are DetectorID,Detector Name,Link I Node,Link J Node,Status. Status will denote anything unusual for this detector, such as not in use or observation rate is too low. 
3)detectordata: a folder which have the Detector_Station_Report,example 140831-140906_Detector_Station_Report.csv

output file£º
1)link'date' (example:link140831-140906), a folder which saves linkcounts and linkwithobs for each date
2)obs'data' (example:obs140831-140906), a folder which saves detailed link observation for each date