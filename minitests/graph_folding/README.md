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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 46.7 seconds
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 56.5 seconds
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 minutes 3 seconds

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


| Number of Wires  | Percentage of total | Tile Type | Average of Distinct Patterns |
| ------------- | ------------- | ----- | -- |
|3069924|	30.69924	|INT_R|2947.3|
|3069924|	30.69924	|INT_L|2939.3|
|753504|	7.53504	|CLBLM_L|155|
|737802|	7.37802	|CLBLM_R|164.5|
|525232|	5.25232	|CLBLL_R|122.5|
|455714|	4.55714	|CLBLL_L|106.5|
|299904|	2.99904	|VBRK|
|264367|	2.64367	|BRAM_L|
|196116|	1.96116	|INT_INTERFACE_R|
|171902|	1.71902	|BRAM_INT_INTERFACE_L|
|163104|	1.63104	|DSP_R|
|119713|	1.19713	|INT_INTERFACE_L|
|81552|	0.81552	|DSP_L|
|74976|	0.74976	|INT_FEEDTHRU_2|
|65604|	0.65604	|INT_FEEDTHRU_1|
|53568|	0.53568	|LIOI3|
|49656|	0.49656	|IO_INT_INTERFACE_L|
|47076|	0.47076	|CMT_FIFO_R|
|45982|	0.45982	|BRAM_R|
|41351|	0.41351	|VFRAME|
|37062|	0.37062	|BRKH_INT|
|33300|	0.333	|GTP_INT_INTERFACE|
|32456|	0.32456	|L_TERM_INT|
|32424|	0.32424	|CLK_FEED|
|29896|	0.29896	|BRAM_INT_INTERFACE_R|
|28597|	0.28597	|HCLK_L|
|28597|	0.28597	|HCLK_R|
|27264|	0.27264	|LIOB33|
|26784|	0.26784	|RIOI3|
|24828|	0.24828	|IO_INT_INTERFACE_R|
|23538|	0.23538	|CMT_FIFO_L|
|16228|	0.16228	|R_TERM_INT|
|15488|	0.15488	|CMT_TOP_R_LOWER_B|
|14604|	0.14604	|R_TERM_INT_GTX|
|13632|	0.13632	|RIOB33|
|13148|	0.13148	|CMT_TOP_R_UPPER_B|
|12656|	0.12656	|CMT_TOP_R_UPPER_T|
|11904|	0.11904	|LIOI3_TBYTESRC|
|9916|	0.09916	|CMT_TOP_R_LOWER_T|
|8609|	0.08609	|PCIE_BOT|
|8524|	0.08524	|PCIE_INT_INTERFACE_L|
|8524|	0.08524	|PCIE_INT_INTERFACE_R|
|8404|	0.08404	|VBRK_EXT|
|7742|	0.07742	|CMT_TOP_L_LOWER_B|
|6572|	0.06572	|CMT_TOP_L_UPPER_B|
|6326|	0.06326	|CMT_TOP_L_UPPER_T|
|6136|	0.06136	|B_TERM_INT|
|6084|	0.06084	|T_TERM_INT|
|5952|	0.05952	|RIOI3_TBYTESRC|
|5952|	0.05952	|LIOI3_TBYTETERM|
|5934|	0.05934	|HCLK_CLB|
|4956|	0.04956	|CMT_TOP_L_LOWER_T|
|4800|	0.048	|CFG_CENTER_MID|
|4414|	0.04414	|CFG_CENTER_BOT|
|4368|	0.04368	|CLK_HROW_BOT_R|
|4368|	0.04368	|CLK_HROW_TOP_R|
|4127|	0.04127	|NULL|
|4000|	0.04	|CLK_BUFG_REBUF|
|3210|	0.0321	|GTP_CHANNEL_2|
|3210|	0.0321	|GTP_CHANNEL_3|
|3210|	0.0321	|GTP_CHANNEL_0|
|3210|	0.0321	|GTP_CHANNEL_1|
|2976|	0.02976	|RIOI3_TBYTETERM|
|2896|	0.02896	|LIOI3_SING|
|2466|	0.02466	|MONITOR_BOT|
|2260|	0.0226	|CFG_CENTER_TOP|
|2244|	0.02244	|MONITOR_MID|
|2037|	0.02037	|PCIE_TOP|
|1784|	0.01784	|CMT_PMV|
|1664|	0.01664	|CLK_PMV|
|1638|	0.01638	|BRKH_TERM_INT|
|1600|	0.016	|HCLK_VBRK|
|1506|	0.01506	|GTP_COMMON|
|1480|	0.0148	|HCLK_INT_INTERFACE|
|1448|	0.01448	|RIOI3_SING|
|1416|	0.01416	|BRKH_B_TERM_INT|
|1350|	0.0135	|HCLK_BRAM|
|1144|	0.01144	|CLK_BUFG_TOP_R|
|1144|	0.01144	|CLK_BUFG_BOT_R|
|1140|	0.0114	|MONITOR_TOP|
|1128|	0.01128	|LIOB33_SING|
|1008|	0.01008	|HCLK_DSP_R|
|892|	0.00892	|CMT_PMV_L|
|750|	0.0075	|HCLK_IOI3|
|636|	0.00636	|HCLK_CMT|
|588|	0.00588	|BRKH_DSP_R|
|576|	0.00576	|BRKH_BRAM|
|564|	0.00564	|RIOB33_SING|
|496|	0.00496	|HCLK_DSP_L|
|424|	0.00424	|BRKH_CLB|
|384|	0.00384	|BRKH_CLK|
|360|	0.0036	|HCLK_FEEDTHRU_2|
|358|	0.00358	|CLK_MTBF2|
|353|	0.00353	|CLK_PMV2|
|353|	0.00353	|CLK_PMV2_SVT|
|352|	0.00352	|CLK_PMVIOB|
|330|	0.0033	|HCLK_FEEDTHRU_1|
|294|	0.00294	|BRKH_DSP_L|
|276|	0.00276	|HCLK_CMT_L|
|228|	0.00228	|HCLK_TERM|
|228|	0.00228	|HCLK_FIFO_L|
|204|	0.00204	|HCLK_IOB|
|172|	0.00172	|HCLK_L_BOT_UTURN|
|172|	0.00172	|HCLK_R_BOT_UTURN|
|128|	0.00128	|CLK_TERM|
|123|	0.00123	|PCIE_NULL|
|120|	0.0012	|HCLK_VFRAME|
|36|	0.00036	|BRKH_CMT|
|28|	0.00028	|HCLK_TERM_GTX|
|28|	0.00028	|HCLK_GTX|
|24|	0.00024	|BRKH_GTX|
|8|	8.0e-05	|TERM_CMT|



