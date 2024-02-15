# seal

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install seal
```

## License

`seal` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


## Design
- stdin is main input method or use file
- input comes from awk
- output in the form of gui, file or interactive dash (possible with plotly?)
- cli should follow awk/sed style
- use relplot,displot,catplot,pairplot as basic types
- f for file input for complicated processing
- main parameters to seaborn plot - x, y, col ,hue, style, size, kind

kinds of catplot
Categorical scatterplots:

    stripplot() (with kind="strip"; the default)

    swarmplot() (with kind="swarm")

Categorical distribution plots:

    boxplot() (with kind="box")

    violinplot() (with kind="violin")

    boxenplot() (with kind="boxen")

Categorical estimate plots:

    pointplot() (with kind="point")

    barplot() (with kind="bar")

    countplot() (with kind="count")

displot types

    histplot() (with kind="hist"; the default)

    kdeplot() (with kind="kde")

    ecdfplot() (with kind="ecdf"; univariate-only)

relplot types



    scatterplot() (with kind="scatter"; the default)

    lineplot() (with kind="line")
