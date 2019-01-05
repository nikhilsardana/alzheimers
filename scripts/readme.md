These files are scripts used for:

- Preprocessing data
- Splitting and merging 4d/3d nii files
- Moving and renaming data to make it easier for ingestion into a keras model

Many of these scripts simply create text files, where each line is a command (gzip, fslsplit, etc.), which can then be run in a standard terminal environment.

The software used for preprocessing the NII data is [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/).

All data is from the [ADNI](http://adni.loni.usc.edu/) dataset.
