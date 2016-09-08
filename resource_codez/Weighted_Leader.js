import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Set;
 
class Nodes
{
 
 
int id=0;
 
int outdegree=0;
 
int indegree=0;
 
Set<Integer> refset=new HashSet<Integer>();
 
double[] score=new double[2];
 
}
public class WLR
{
 
 
public static Map<Integer,Nodes> nodemap=new HashMap<Integer,Nodes>();
 
public static void readin(String path)
{
 
try
{
 
String s=null;
BufferedReader in=new BufferedReader(new FileReader(path));
 
while((s=in.readLine())!=null)
{
 
String[] tempt=s.split("\t");
int fn=Integer.parseInt(tempt[0]);
int sn=Integer.parseInt(tempt[1]);
Nodes fnn=nodemap.get(fn);
Nodes snn=nodemap.get(sn);
 
if(fnn==null)
{
 
 
Nodes newfn=new Nodes();
 
newfn.id=fn;
 
newfn.outdegree=2;
newfn.indegree=1;
 
newfn.score[0]=1;
 
newfn.score[1]=0;
newfn.refset.add(-1);
 
nodemap.put(fn,newfn);
 
}
else
{
 
 
fnn.outdegree=fnn.outdegree+1;
 
}
 
if(snn==null)
{
 
 
Nodes newsn=new Nodes();
 
newsn.id=sn;
 
newsn.indegree=2;
 
newsn.outdegree=1;
 
newsn.refset.add(fn);
newsn.refset.add(-1);
 
newsn.score[0]=1;
 
newsn.score[1]=0;
 
nodemap.put(sn, newsn);
 
}
 
else
{
 
 
snn.indegree=snn.indegree+1;
 
snn.refset.add(fn);
 
}
 
}
 
}
catch(Exception e)
{
 
e.printStackTrace();
 
}
 
}
 
public static void PageRank()
{
 
 
 
double bound=0.0001;
Random rand=new Random(47);
 
String readinpath="youtube//youtube.txt";
 
int oldIndex=0;
int newIndex=1;
 
readin(readinpath);
System.out.println("nodemap.size():"+nodemap.size());
int totalIndegree=0;
for(int lid:nodemap.keySet())
{
 
Nodes ln=nodemap.get(lid);
totalIndegree=totalIndegree+ln.indegree;
 
}
int nodeNum=nodemap.size();
 
 
Nodes g=new Nodes();
 
g.id=-1;
 
g.outdegree=nodeNum;
 
g.indegree=nodeNum;
 
g.score[0]=0;
g.score[1]=0;
 
nodemap.put(-1,g);
 
 
 
for(int iterNum=0;iterNum<100000;iterNum++)
{
 
System.out.println("this is the "+iterNum+"times iterator.");
for(int i:nodemap.keySet())
{
 
Nodes nowNode=nodemap.get(i);
nowNode.score[newIndex]=0;
 
}
 
//for(int i=0;i<nodeNum;i++)
for(int i:nodemap.keySet())
{
 
Nodes nowNode=nodemap.get(i);
Set<Integer> reflset=nowNode.refset;
 
for(int j:reflset)
{
 
if(j!=-1)
{
 
Nodes refnode=nodemap.get(j);
nowNode.score[newIndex]=nowNode.score[newIndex]+refnode.score[oldIndex]/refnode.outdegree;
 
}
else
{
 
Nodes refnode=nodemap.get(j);
nowNode.score[newIndex]=nowNode.score[newIndex]+refnode.score[oldIndex]*nowNode.indegree/totalIndegree;
 
}
 
}
if(i!=-1)
{
 
g.score[newIndex]=g.score[newIndex]+nowNode.score[oldIndex]/nowNode.outdegree;
 
}
 
}
double diff=0.0;
for(int i:nodemap.keySet())
{
 
diff=diff+Math.abs(nodemap.get(i).score[newIndex]-nodemap.get(i).score[oldIndex]);
 
}
if(diff<bound)
{
 
break;
 
}
oldIndex=newIndex;
newIndex=1-oldIndex;
 
}
try
{
 
FileWriter out=new FileWriter("youtube//WPR.txt");
for(int i:nodemap.keySet())
{
 
if(i!=-1)
{
 
Nodes outNode=nodemap.get(i);
double pr=outNode.score[newIndex]+nodemap.get(-1).score[newIndex]*outNode.indegree/totalIndegree;
out.write(nodemap.get(i).id+"\t"+pr+"\n");
out.flush();
//System.in.readLine();
 
}
 
}
 
}
catch(Exception e)
{
 
e.printStackTrace();
 
}
 
}
public static void main(String[] args)
{
 
PageRank();
 
}
 
}