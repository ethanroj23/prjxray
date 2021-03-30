# Background

This is the beginning of a more intentional approach to the graph folding problem.  

In my first attempt, called max_shared_graph_folding, I did not keep track of metrics and comparisons very well.  

In order to achieve a better result, this time I will keep track certain values as I execute each different method all for the part 'xc7a100tfgg676-1'. The values are the following:  


1. Size of the resulting files. (wire_to_node.bin)  
2. Time taken to create every file.  
3. Time it takes to access the data structure and query every wire for the node it belongs to.  
4. Largest # of Subgraphs  


I will record my results below.

3.12.21
<!---
#############################################################################
######################  Greedy Set Cover  ###################################
#############################################################################
-->
# Greedy Set Cover (Initial Approach)

## File Size on Disk:

| Direction  | Size |
| ------------- | ------------- |
| Wire to nodes (128)  | 3.73MB  |
| Node to wires (128)  | 6.52MB  |
| Node to pip wires (128)  | 1.10MB  |  
| Total  | 11.35MB |  

<br/>

## Time taken to create all the files:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 17.03 minutes (just for node to wires I think)

<br/>

## Time it takes to access the data structure and query every wire.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 minute 10 seconds.
<!---
69.67user 0.48system 1:10.16elapsed 99%CPU (0avgtext+0avgdata 189380maxresident)k
216inputs+0outputs (0major+87040minor)pagefaults 0swaps
-->


<br/>

## Largest # of Subgraphs (for all tiles)
| Direction  | Max # of Subgraphs | Tile Type |
| ------------- | ------------- | ----- |
| Wire to nodes| 8 | INT_R |
| Node to wires| 17 | INT_R |
| Node to pip wires| 10| INT_L  |

<br/>
<!---
#############################################################################
######################  Max Shared (old capnp)  #############################
#############################################################################
-->
# Max Shared

## File Size on Disk:

| Direction  | Size |
| ------------- | ------------- |
| Wire to nodes (128)  | 4.60MB  |
| Node to wires (128)  | 6.86MB  |
| Node to pip wires (128)  | 1.27MB  |  
| Total  | 12.73MB  |  

<br/>

## Time taken to create all the files:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7 minutes 45 seconds

<br/>

## Time it takes to access the data structure and query every wire.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 minute 28 seconds. 1 minute 36 seconds. 1 minute 27 seconds
<!---
69.67user 0.48system 1:10.16elapsed 99%CPU (0avgtext+0avgdata 189380maxresident)k
216inputs+0outputs (0major+87040minor)pagefaults 0swaps
-->


<br/>

## Largest # of Subgraphs (for all tiles)
| Direction  | Max # of Subgraphs | Tile Type |
| ------------- | ------------- | ----- |
| Wire to nodes| 25 | INT_R |
| Node to wires| 76 | INT_R |
| Node to pip wires| 29 | INT_R  |


<br/>


<!---
#############################################################################
######################  Max Shared New Capnp  ###############################
#############################################################################
-->
# Max Shared New Capnp

## File Size on Disk:

| Direction  | Size |
| ------------- | ------------- |
| Wire to nodes (128)  | 2.63MB  |
| Node to wires (128)  | 7.26MB  |
| Node to pip wires (128)  | 1.33MB  |  
| Total  | 11.22MB  |  


<br/>

## Time taken to create all the files:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 7 minutes 28 seconds

<br/>

## Time it takes to access the data structure and query every wire.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 minute 28 seconds................

<br/>

## Largest # of Subgraphs (for all tiles)
| Direction  | Max # of Subgraphs | Tile Type |
| ------------- | ------------- | ----- |
| Wire to nodes| 25 | INT_R |
| Node to wires| 76 | INT_R |
| Node to pip wires| 29 | INT_R  |

<br/>


# To-Do  
Determine #tiles per subgraph number

<!---
#############################################################################
######################  Max Shared New Capnp (with every pkey in place)  ###############################
#############################################################################
-->
# Max Shared New Capnp

## File Size on Disk:

| Direction  | Size |
| ------------- | ------------- |
| Wire to nodes (128)  | 2.63MB  |
| Node to wires (128)  | 5.06MB  |
| Node to pip wires (128)  | 0.97MB  |  
| Total  | 8.66MB  |  




How many wires are in each tile?
Percentage of total wires in each tile type?
Number of subgraphs for each tile.