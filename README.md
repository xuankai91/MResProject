# MResProject

files related to 2018-19 MRes Cognitive Neuroscience thesis project under the Gilbert lab

Authors: Xuan Kai Lee, Annika Boldt

# Preregistration

url: https://osf.io/748fe

# Files
## Main folder

*Files* 
* `AllFullData.csv` - Raw collected data, including stim/border colours, PM target responses, and lapses. 
* `tofit_HDDM.csv` - Preprocessed data, to be compatible with HDDM fitting, e.g. removal of lapses (unfittable), generation of conditional flags, rearrangement. 
* `multiprocessing_unittest.py` - unit test for multiprocessing module on User's computer; parallel run time should be significantly less than sequential run time. 


## Reanalysis2020

Reanalyzing the data using updated Python version (3.6.8) and HDDM package version (0.8.0; dependencies: PyMC 2.3.7, Kabuki 0.6.3)

*Files*
* `bs_modelling.py` - Script to run all 4 models under comparison. Change the variable `cores_to_use` to however many is necessary, dependent on User hardware.
* `gelman_rubin.py` - Script to generate 5 winning models, to check convergence stats (R_hat). Change the variable `cores_to_use` to however many is necessary, dependent on User hardware.
* `ppc_parallel.py` - Generate 100 samples from posterior predictive distributions of winning model 5 times in parallel . Change the variable `cores_to_use` to however many is necessary, dependent on User hardware.
* `ppc_summary.py` - Compile the generated posterior predictive samples, and calculate group/individual stats in comparison to actual collected data.

*Subfolders* 
* ### figures
  save folder for all figure plots

* ### gelman_rubin
  save folder for 5 repeated fits of the winning model <m_all>, for calculating gelman-rubin convergence stats.

* ### models
  save folder for all fitted models under consideration

* ### ppc
  save folder for posterior predictive checks generated from the winning model <m_all>

* ### stats
  save folder for statistics associated with each of the fitted models under consideration

* ### traces
  save folder for raw traces of each parameter for all fitted models under consideration


