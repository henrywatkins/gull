import re
from io import StringIO

import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from gull.__about__ import __version__

sns.set_style("whitegrid")


@click.command(
    context_settings={"help_option_names": ["-h", "--help"]}
)  # , invoke_without_command=True)
@click.version_option(version=__version__, prog_name="gull")
@click.argument("input_file", type=click.File("r"), default="-")
@click.option(
    "--program",
    "-p",
    type=str,
    required=True,
    help="Script string, the paramters and columns to use in plotting",
)
@click.option(
    "--output", "-o", type=str, help="File where you would like to save image output"
)
@click.option(
    "--file",
    "-f",
    type=click.File("r"),
    help="Script file. Instead of using a string, you can define the plotting paramters in a file",
)
@click.option(
    "--separator",
    "-s",
    type=str,
    default=",",
    help="Separator for input data, default is ',' ",
)
@click.option(
    "--columns",
    "-c",
    type=str,
    default=None,
    help="Column names for the input data, if not present in the file",
)
@click.option(
    "--columns",
    "-c",
    type=str,
    default=None,
    help="Column names for the input data, if not present in the file",
)
def gull(program, columns, input_file, output, file, separator):
    """Terminal-based plotting with seaborn

    Plot data from a tabular data file or from stdin, all from the terminal. An ideal companion for awk, grep and other terminal-based processing tools. Uses seaborn as a plotting interface, so for more information see the seaborn website (https://seaborn.pydata.org/)

    plot types:

    relplot (default), kinds: scatter, line

    catplot, kinds: strip (default), swarm, box, violin, boxen, point, bar, count

    displot, kinds: hist (default), kde, ecdf

    pairplot

    Define the plotting parameters and columns to use with a string.

    Example: to plot a scatterplot of data with column names col1, col2, and coloured by the value in col3.

    gull data.csv -p "plot:relplot,kind:scatter,x:col1,y:col2,hue:col3" -c "col1,col2,col3"

    if no column names are defined via the --columns option, the first line of the  file is assumed to be the column names.
    """
    if file:
        program = file.read()
    try:
        plot_type, plot_args = parse_script(program)
    except:
        print("Invalid script format, unable to parser program script")
        return
    column_names = parse_columns(columns)
    contents = input_file.read()
    name_dict = {"names": column_names} if len(column_names) > 0 else {}
    df = pd.read_csv(StringIO(contents), sep=separator, **name_dict)
    fig = plot_type(data=df, **plot_args)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    if output:
        fig.figure.savefig(output)
    else:
        plt.show()


def parse_columns(column_string):
    if column_string:
        return column_string.strip().split(",")
    else:
        return []


def parse_script(script_string):
    """Parse the script string and return the dictionary"""
    # sting of format plot:l1,kind:l2,x:l3,y:l3,hue:l5,col:l6,size:l7,style:l8
    elements = script_string.strip()
    elements_dict = dict(
        [
            (i.split(":")[0].strip(), i.split(":")[1].strip())
            for i in elements.split(",")
        ]
    )
    plot_types = {
        "relplot": sns.relplot,
        "catplot": sns.catplot,
        "displot": sns.displot,
        "pairplot": sns.pairplot,
    }
    plot_choice = (
        elements_dict["plot"]
        if elements_dict["plot"] in plot_types.keys()
        else "relplot"
    )
    elements_dict.pop("plot", None)
    return plot_types[plot_choice], elements_dict


def validate_format(input_string):
    # Count the number of '/' characters before '~'
    # extra logic - check if kind is in list of support kinds, if column names present check if all columns are in the first part of the string.

    slash_count = input_string.count("/")
    tilde_index = input_string.find("~")
    pattern = re.compile("^([A-Z][0-9]+)+$")
    check = pattern.match(input_string)
    # pattern = r"^[^/]*(?:/[^/]*){7}~"
    # if not bool(re.match(pattern, script_string)
    # Check if there are exactly 7 '/' characters before '~'
    if slash_count == 7 and tilde_index != -1 and tilde_index > 7:
        return True
    else:
        return False
