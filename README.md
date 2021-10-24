# Plate-Reader
---
Repository for analysing microplate reader data to find biomass, growth rate, and gene expression rate (fluorescence intensity) using omniplate software. 


This repository is to analyse microplate reader data produced by a microbial cell culture. Biomass (OD600) and growth rates can be found for yeast or bacteria cultures. OD correction can be applied for haploid yeast cells grown in 2% glucose media using _**ODcorrection_Glucose_Haploid.txt**_. Autofluorescence correction can be applied for yeast cells. In this way, fluorescence intensities and time-derived fluorescences produced by a reporter gene can be also found.


The microplate reader data and its content should be in should be in specific formats as found in _**ExampleData.xlsx**_ and _**ExampleDataContents.xlsx**_, respectively. 


## To install the omniplate:

Type:\
git clone https://git.ecdf.ed.ac.uk/pswain/omniplate.git \
and in the omniplate directory created\
pip install -e .\
where the . means the current directory.

## Documentation:

https://swainlab.bio.ed.ac.uk/software/platereader/omniplate.html
