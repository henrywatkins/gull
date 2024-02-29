# gull


Terminal-based plotting with seaborn

## Installation

```console
pip install gull
```

## Usage

Plot data from a tabular data file or from stdin, all from the terminal. An ideal companion for awk, grep and other terminal-based processing tools. Uses seaborn as a plotting interface, so for more information see the seaborn website (https://seaborn.pydata.org/)

plot types: 

relplot (default), kinds: scatter, line
catplot, kinds: strip (default), swarm, box, violin, boxen, point, bar, count 
displot, kinds: hist (default), kde, ecdf 
pairplot

Define the plotting parameters and columns to use with a string. 

Example: to plot a scatterplot of data with column names col1, col2, and coloured by the value in col3.

`gull data.csv -p "plot:relplot,kind:scatter,x:col1,y:col2,hue:col3" -c "col1,col2,col3"`

If no column names are specified in the --columns option, the first line of the input will be taken as the column names. 

Usage alongside awk: gull is ideal of using alongside `awk` for basic data processing. e.g. 

```
awk 'NF<10 {print $0,$1 }' /tmp/userdata.txt | gull -p "plot:replot,kind:scatter,x:pos_x,y:pos_y" -c "pos_x,pos_y"
```

Here, we print the first 10 lines of the first two columns, with a ',' as a separator. Then we pass the result to gull to create a scatter plot with the columns names 'pos_x' and 'pos_y'
