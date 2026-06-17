# InfoTracer
This is a prototype of paper "Robust Anchor-driven Attack Investigation Method Based on Information Flow", which is a tool for attack investiagtion based on dependency graphs.
## Dataset
Datasets used in this prototype is public dataset DARPA TC and the ATLAS dataset. Their url is following:

https://github.com/darpa-i2o/Transparent-Computing

https://github.com/purseclab/ATLAS.

## Dictionary

files in DependencyGraphConstruction are used to prase audit logs and construct corresponding dependency graphs.

files in AttackNarrativeReconstruction are used to extract attack graph based on given POIs.

files in Result are narratives shown by graph, the script ShowGraph.ipynb is used to visualize them.
