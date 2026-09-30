# Information Visualization (CS-E4840), Aalto University, 2026

Coursework for Aalto University's Information Visualization course. Every assignment
explores **UN Sustainable Development Goal 9: Industry, Innovation and Infrastructure**,
mainly through UNIDO's Competitive Industrial Performance (CIP) data. The same dataset
is viewed from many angles, from simple time series to maps, clustermaps,
dimensionality reduction and networks.

Every notebook shows the iterative process that leads to a finished visualization. Rough drafts are shown too, to explain how the final visualisation is obtained. 

## Assignments

| Notebook | Assignment | Contents |
|---|---|---|
| `assignment1.ipynb` | 1: Visualization principles | CIP scores of the Nordic countries as a line chart, redesigned step by step along Tufte's principles (less non-data ink, direct labelling). |
| `assignment2.ipynb` | 2: Distributions, time series and high-dimensional data | Box plots of manufacturing value added (MVA) per capita by continent (log scale, labelled outliers). Box plots over time of the manufactured-export share in Asia and South America (2010–2023). Parallel coordinates, CIP heatmaps and scatter-plot matrices across several industrial indicators. |
| `assignment3.ipynb` | 2.1: Human factors | The industrialization intensity index across the EU in two choropleth maps: a sequential map (binned `YlGnBu`) and a diverging map centred on the EU mean (`RdYlGn`). A heatmap of 19 countries over 2010–2023, and a row-clustered clustermap (Euclidean metric) that shows three groups of countries. |
| `assignment4.ipynb` | 2.2: Advanced topics | Dimensionality reduction of six CIP indicators for 2023, with countries coloured by CIP quintile or continent: PCA with and without standardization, MDS with two seeds, and t-SNE with perplexity 5, 18 and 91 × two seeds. A hand-built network of connections between the 17 SDGs, drawn with radial, Kamada-Kawai and Fruchterman-Reingold layouts, with node size set by the number of connections. |
| `pca.ipynb` | Warm-up | PCA on the Iris dataset. |

## Tools

- **pandas / NumPy** for data loading, filtering and reshaping (long ↔ wide)
- **Matplotlib and seaborn** for all charts (line charts, box plots, heatmaps, clustermaps, scatter plots)
- **GeoPandas** with Natural Earth country borders for choropleth maps
- **scikit-learn** for PCA, MDS, t-SNE and standardization
- **NetworkX** for the SDG network
- **colorcet / cmasher** for additional colormaps
  

## Structure

```
data/        UNIDO CIP extracts, Natural Earth country borders, SDG edge list
figures/     Exported figures (PNG, 300 dpi)
notebooks/   One notebook per assignment
src/infoviz/ Small package with shared plotting settings (rcParams)
helper.py    Common imports and plot styling, loaded in each notebook with "%run ../helper.py"
```

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Then open a notebook and select the project's `.venv` as the kernel.

## Data sources

- [UNIDO Statistics Data Portal](https://stat.unido.org/data/download?dataset=cip): Competitive Industrial Performance (CIP) database
- [Natural Earth](https://www.naturalearthdata.com/): Admin 0 countries, 1:10m
