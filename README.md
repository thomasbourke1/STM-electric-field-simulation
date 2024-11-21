# Scanning tunnelling microscropy pulsing

> "electricity is really just organized lightning" - George Carlin

## Table of Contents
- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contact](#contact)
- [References](#references)

## About the Project

During my Master's research project, we wished to model electric field pulses that could be applied to a semiconducting 2D material via a conducting STM tip . Previous work [1] [2] has shown that pulsing of this kind can change the magnetic domain structure of the material, leading the way for possible all-electrical manipulation of magnetic domains. This code plots data generated from COMSOL Multiphysics to show how the electric field intensity varies across the surface of the material.

### Built With
- [Python](https://www.python.org/)
- [COMSOL Multiphysics](https://www.comsol.com/)

## Features
- Plot in and out of plane electric field component as a function of distance across the substrate.
- Calculate tip-sample distance with feedback on using the STM equation.

### Screenshots

- Schematic of the model used in this simulation. The Au substrate was set as grounded and a bias of 7V applied uniformly throughout the tip. A small distance (<5$\r{A}$) is set between the tip and sample. \\[ augh \\]
![STM geometry](/readme_scs/setup.jpg)
- Heat map of voltage applied.
![Tip-surface bias applied](/readme_scs/SCR-20241121-ohlm.jpeg)
- Out of plane electric field component as function of distance across the monolayer ReS$_2$ sample
![Electric field plotted](/readme_scs/E_z.jpeg)

## Contact
Your Name - [tb944@bath.ac.uk](mailto:tb944@bath.ac.uk)

## References

[1] Zhang, Fan, Zhe Wang, Lixuan Liu, Anmin Nie, Yanxing Li, Yongji Gong, Wenguang Zhu, and Chenggang Tao. ‘Atomic-Scale Manipulation of Polar Domain Boundaries in Monolayer Ferroelectric In2Se3’. Nature Communications 15, no. 1 (24 January 2024): 718. https://doi.org/10.1038/s41467-023-44642-9.

[2] Chang, Kai, Felix Küster, Brandon J. Miller, Jing-Rong Ji, Jia-Lu Zhang, Paolo Sessi, Salvador Barraza-Lopez, and Stuart S. P. Parkin. ‘Microscopic Manipulation of Ferroelectric Domains in SnSe Monolayers at Room Temperature’. Nano Letters 20, no. 9 (9 September 2020): 6590–97. https://doi.org/10.1021/acs.nanolett.0c02357.