Dataparti
==========

A data partitioner for pandas datasets. 

Setup 
------
You can make sure some dependencies by using the installDependencies.sh script as sudo


Example
------

```python
data_test=[[1,2,4],[8,2,4],[6,7,1],[0,3,4],[2,9,3],[0,2,4],[8,2,4],[6,7,1],[2,9,3],[0,2,4],[8,2,4],[6,7,1],[2,9,3],[0,2,4],[8,2,4],[6,7,1],[2,9,3]]
data_in=pd.DataFrame(data=data_test,columns=['X','Y','Z'])
part_out=parti_by(data_in,[0.1,0.1,0.1],'X',time_partitions=[0.3,0.5],time_col='Y')
```

