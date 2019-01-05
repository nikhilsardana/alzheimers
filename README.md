# alzheimers
Convolutional Networks for Alzheimer's Classification

Read the paper [here](https://nikhilsardana.github.io/sts.pdf).

This work began in June 2017 as my project at the [Communications Engineering Branch](https://ceb.nlm.nih.gov/) of the [National Institutes of Health](https://www.nih.gov/). I finished this work in November 2017, a few months after I left the NIH at the end of Summer 2017.

## Overview
Using convolutional networks to classify subjects into five caregories of cognitive impairment, solely from [rs-fMRI](https://en.wikipedia.org/wiki/Resting_state_fMRI) data. The classes are listed below in order of increasing cognitive impairment:
- No cognitive impairment (Normal)
- Significant memory concern (SMC)
- Early Mild Cognitive Impairment (EMCI)
- Late Mild Cognitive Impairment (LMCI)
- Alzheimer's

All data used in this project is from the [Alzheimer's Disease Neuroimaging Initiative](http://adni.loni.usc.edu/). These five categories are defined more precisely [in documents on the ADNI website](http://adni.loni.usc.edu/wp-content/themes/freshnews-dev-v2/documents/clinical/ADNI-2_Protocol.pdf). 

This work uses a standard [Inception-ResNet-v2](https://arxiv.org/abs/1602.07261) model for classification.

This work is fairly straightforward, but took more time than initially allocated due to the sheer size of the ADNI dataset. The three main tasks were:
- Preprocessing and sanitizing the fMRI data
- Training and testing the CNN
- Visualizing CNN results using [Picasso](https://github.com/merantix/picasso) and calculating classification metrics.

See the `scripts/` folder for preprocessing and sanitization scripts, the `visualize/` folder for scripts to help with Picasso visualization, and the `results/` folder for a few classification metric scripts.

