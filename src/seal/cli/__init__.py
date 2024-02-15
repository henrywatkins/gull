import re
from io import StringIO

import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from seal.__about__ import __version__

# sns.set_theme("whitegrid")


@click.command(
    context_settings={"help_option_names": ["-h", "--help"]}
)  # , invoke_without_command=True)
@click.version_option(version=__version__, prog_name="seal")
@click.argument("input_file", type=click.File("r"), default="-")
@click.option("--program", "-p", type=str, default="~", help="Script string")
@click.option("--output", "-o", type=str, help="Output file")
@click.option("--file", "-f", type=click.File("r"), help="Script file")
@click.option(
    "--separator", "-s", type=str, default=",", help="Separator for input file"
)
def seal(program, input_file, output, file, separator):
    """Terminal-based plotting with seaborn"""
    if file:
        program = file.read()
    plot_type, plot_args, column_names = parse_script(program)
    contents = input_file.read()
    name_dict = {"names": column_names} if len(column_names) > 0 else {}
    df = pd.read_csv(StringIO(contents), sep=separator, **name_dict)
    fig = plot_type(data=df, **plot_args)
    # if an output file is present then write to it
    if output:
        fig.figure.savefig(output)
    else:
        plt.show()


def parse_script(script_string):
    """Parse the script string and return the dictionary"""
    # sting of format plot/kind/x/y/hue/col/size/style~col1/col2/col3
    pattern = r"^[^/]*(?:/[^/]*){7}~"
    if not bool(re.match(pattern, script_string)):
        raise ValueError("Invalid script")
    elements, headers = script_string.strip().split("~")
    column_names = headers.split("/")
    elements = elements.split("/")
    plot_types = {
        "relplot": sns.relplot,
        "catplot": sns.catplot,
        "displot": sns.displot,
        "pairplot": sns.pairplot,
    }
    plot_choice = elements[0] if elements[0] in plot_types.keys() else "relplot"
    args = ["x", "y", "hue", "col", "size", "kind", "style"]
    script_data = {i: j for i, j in zip(args, elements[1:]) if j}

    # extra logic - check if kind is in list of support kinds, if column names present check if all columns are in the first part of the string.

    return plot_types[plot_choice], script_data, column_names


def validate_format(input_string):
    # Count the number of '/' characters before '~'
    slash_count = input_string.count("/")
    tilde_index = input_string.find("~")
    pattern = re.compile("^([A-Z][0-9]+)+$")
    check = pattern.match(input_string)
    print(check)
    # Check if there are exactly 7 '/' characters before '~'
    if slash_count == 7 and tilde_index != -1 and tilde_index > 7:
        return True
    else:
        return False
