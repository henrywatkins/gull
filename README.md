# GullPlot

Terminal-based plotting with seaborn. 

## Installation

```
pip install gullplot
```

## Usage

GullPlot allows you to create plots from tabular data directly in the terminal. It's an ideal companion for command-line data processing tools like awk and grep.

### Basic Usage

```bash
# Plot from a CSV file
gullplot data.csv -p "plot:relplot,kind:scatter,x:col1,y:col2,hue:col3"

# Plot from stdin (pipe data)
cat data.csv | gullplot - -p "plot:relplot,kind:scatter,x:col1,y:col2"

# Save plot to a file
gullplot data.csv -p "plot:relplot,kind:scatter,x:col1,y:col2" -o plot.png

# Specify column names if they're not in the first row
gullplot data.csv -p "plot:relplot,kind:scatter,x:col1,y:col2" -c "col1,col2,col3"

# Use a different separator for CSV data
gullplot data.tsv -p "plot:relplot,kind:scatter,x:col1,y:col2" -s "\t"
```

### Supported Plot Types

- **relplot** (default): Scatter and line plots
  - kinds: scatter, line
- **catplot**: Categorical plots
  - kinds: strip (default), swarm, box, violin, boxen, point, bar, count
- **displot**: Distribution plots
  - kinds: hist (default), kde, ecdf
- **pairplot**: Pairwise relationships in dataset

### Script Format

The plotting script uses a simple key:value format:

```
plot:plot_type,kind:plot_kind,x:x_column,y:y_column,hue:color_column,...
```

For example:
```
plot:catplot,kind:violin,x:category,y:value,hue:group
```

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
hatch run fmt
```

## License

MIT