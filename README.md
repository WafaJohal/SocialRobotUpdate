# Dataset and Analysis for Systematic Review of Social Robots for Education

Code accompaninig Current Robotics Report from the Topical Collection on Service and Interactive Robotics. 
Paper link: [https://link.springer.com/article/10.1007/s43154-020-00008-3](https://link.springer.com/article/10.1007/s43154-020-00008-3)


![Field of Social Robotics for Education](https://media.springernature.com/full/springer-static/image/art%3A10.1007%2Fs43154-020-00008-3/MediaObjects/43154_2020_8_Fig1_HTML.png?as=webp)

--- 

## Introduction

Based on Belpaeme et al. 2018, we propose an updated and ovel analysis of the litterature of social robots for leanring. 
This repo contains the code used to generate the figures for the paper "Research Trends in Social Robots for Learning" as well as the annotated dataset used for the analysis. 


## Usage

The main notebook to reproduce the figures of the paper is ```Main.ipynb```. New data can be asserted in the social_robot4learning.xlsx file in order to generate the new plots.

### Prereqs

You will need to install jupyter-lab or to upload ```Main.ipynb``` on google collab  as well as the dataset.

### Data

The dataset is based on the dataset shared by Belpaeme et al. 2018 (here, [Data Belpame et al. 2018](https://tinyurl.com/ybuyz5vn)) as mentioned on their paper (see references below). The dataset was augmented by performing similarly a search for papers from 2017 till March 2020. The current dataset includes 160 papers (Belpame2018 contained 101 papers).

<img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Zotero_icon.png" width="60" height="60" >
The dataset is also stored as an open Zotero collection that is easy to search and to download as bibtex: https://www.zotero.org/groups/2419050/hri-unsw/collections/X6PKYLT6. 
The Zotero collection also contains some related review and some references that were excluded from the systematic analysis.


### Adding your data or report an issue

Please refer to the ISSUE_GUIDELINE.md

### Running the notebook for analysis

1. To run jupyter without poetry::
	```
	jupyter-lab
	```


2. To run jupyter with poetry::
	```
	poetry run jupyter-lab
	```
Enjoy!

## References

- Johal, W. Research Trends in Social Robots for Learning. Curr Robot Rep (2020). https://doi.org/10.1007/s43154-020-00008-3
- Belpaeme, T., Kennedy, J., Ramachandran, A., Scassellati, B., & Tanaka, F. (2018). Social robots for education: A review. Science robotics, 3(21). https://robotics.sciencemag.org/content/3/21/eaat5954
