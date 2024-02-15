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
@click.argument("script", type=str)
@click.argument("input_file", type=click.File("r"), default="-")
@click.option("--output", "-o", type=str, help="Output file")
@click.option("--file", "-f", type=click.File("r"), help="Script file")
@click.option(
    "--separator", "-s", type=str, default=",", help="Separator for input file"
)
def seal(script, input_file, output, file, separator):
    """Terminal-based plotting with seaborn"""
    contents = input_file.read()
    df = pd.read_csv(StringIO(contents), sep=separator, names=["w", "x", "y", "z", "n"])
    fig = sns.relplot(data=df, x="x", y="y")
    # if an output file is present then write to it
    if output:
        fig.figure.savefig(output)
    else:
        plt.show()
