# patentprocessing
Process and analyze data from http://www.google.com/googlebooks/uspto-patents-applications-text.html 

## PageRank
Compile
```
sbt package
```  

Submit to the cluster
```
spark-submit -v --driver-library-path /usr/lib/hadoop/lib/native --class "PageRank" --master yarn-cluster --deploy-mode cluster target/scala-2.10/patentpagerank_2.10-1.0.jar
```

## Misc
For use on DARPA's Memex cluster
