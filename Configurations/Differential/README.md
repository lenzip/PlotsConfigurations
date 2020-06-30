Steps involved
==============

(- Create gen-level histograms with mkShapes in directory `fiducial` (one-time))
- Create histograms with mkShapes.
- Merge the histograms into per-sample ROOT files.
- Preprocess the histograms for each differential observable.
  - Drop unused signal histograms (binned in different observables)
  - Merge categories
  - Create reduced-binning histograms
  - Merge processes and create new variation histograms accordingly
  - Renormalize signal uncertainties
- Make the per-category datacards with mkDatacard.
- Merge the datacards.
- Run various fits.

Creating histograms
===================

Because of the fine categorization + signal splitting, histogram files returned by mkShapes can be large (O(100) MB for signal samples). To not overflow your working directory, a good idea would be to create a symlink to an EOS directory with name `rootFile` under your configuration directory.

If some jobs fail, `tools/resubmit.py` can automatically find them and resubmit to condor. mkShapesMulti or batchTools should have similar features. Whatever works works.

Merging histograms
==================

Instead of `mkShapesMulti.py --doHadd=1`, use `tools/submit_merge_plots.py`. Because of the extreme number of histograms in the output root files, merging can be time consuming. This script submits a merge job (`tools/merge_plots.sh`) per sample. There is no need to merge the output files further; for one thing there is no space gain when merging two files containing entirely different set of histograms (as is the case when merging per-sample ROOT files). mkPlot.py and mkDatacard.py will work with one ROOT file per sample (we won't be using mkDatacard directly on these files though).

Because one ROOT file will be created per sample but the rest of the workflow (`restructure_input.py`, `mkDatacards.py`, and `mkPlot.py` if used) expects one file per *subsample*, you need to create symlinks representing subsamples in the `rootFile_merged` directory. The script `tools/mklinks.sh` takes care of this automatically.

Preprocessing
=============

From a configuration directory (in this example `ggH2018`), do
```
year=2018
obs=njet
card_tag=fullmodel

mkdir shapes

../tools/restructure_input.py --tag ggHDifferential${year} --signal-hww-only --signal-no-fiducial --aslnn-category-pool -j 8 rootFile_merged shapes/plots_${obs}_${card_tag}.root $obs
# for WW+ggWW merged input
#../tools/restructure_input.py --tag ggHDifferential${year} --signal-hww-only --signal-no-fiducial --aslnn-category-pool --background-merging WW=WW,ggWW minor=WWewk,Vg,VgS_L,VgS_H,VZ,VVV -j 8 rootFile_merged shapes/plots_${obs}_${card_tag}.root $obs
# for qqH_hww turned off / scaled up
#../tools/restructure_input.py --tag ggHDifferential${year} --signal-hww-only --signal-no-fiducial --aslnn-category-pool --custom-scale qqH_hww=0 -j 8 rootFile_merged shapes/plots_${obs}_${card_tag}.root $obs
#../tools/restructure_input.py --tag ggHDifferential${year} --signal-hww-only --signal-no-fiducial --aslnn-category-pool --custom-scale qqH_hww=2 -j 8 rootFile_merged shapes/plots_${obs}_${card_tag}.root $obs
```

This `restructure_input.py` is the most critical and most convoluted part of the differential analysis configuration. It sets up the sample and category merging schemes and executes merging, propagating systematic variations of individual samples / categories into the merged products. The script is mostly self-contained. The only external dependency is to the fiducial cross sections, for which you need to first run mkShapes on the `fiducial` configuration.

## Special hacks for 2017

Some samples are too small in the 2017 configuration, making the fit unstable. Fortunately it is acceptable to just copy the corresponding histograms from the 2018 configurations for all of the problematic samples. Do the following before running the preprocessing command:
```
python add_ps_variation.py rootFile_merged/plots_ggHDifferential2017_ALL_WW.root ../ggH2018/rootFile_merged/plots_ggHDifferential2018_ALL_WW.root WW UE_CP5
python add_ps_variation.py rootFile_merged/plots_ggHDifferential2017_ALL_ggH_hww.root ../ggH2018/rootFile_merged/plots_ggHDifferential2018_ALL_ggH_hww.root ggH_hww PS
python add_ps_variation.py rootFile_merged/plots_ggHDifferential2017_ALL_qqH_hww.root ../ggH2018/rootFile_merged/plots_ggHDifferential2018_ALL_qqH_hww.root qqH_hww PS
python copy_dy.py ../ggH2018/rootFile_merged/plots_ggHDifferential2018_ALL_DY.root rootFile_merged/plots_ggHDifferential2017_ALL_DY.root 59.74 41.53
```

Making datacards
================

Standard `mkDatacard.py` is used, but with the output of preprocessing (`shapes/plots_${obs}_${card_tag}.root`) and the special structure file in `tools`. From a configuration directory, do
```
mkdir unmerged_cards

mkDatacards.py --outputDirDatacard=unmerged_cards/${obs}_${card_tag} --inputFile=shapes/plots_${obs}_${card_tag}.root --structureFile=../tools/structure_${obs}.py
```

Then switch to a `combine` environment (i.e. do `cmsenv` in the Combine-installed CMSSW workspace) and combine the cards from different categories with
```
obs=njet
card_tag=fullmodel

mkdir merged_cards

../tools/fitting/combine_cards.py --in unmerged_cards/${obs}_${card_tag} --out merged_cards/${obs}_${card_tag} --only-fullmodel --float-background WW=WW top=top DY${year}=DY > combine_cards_${obs}_${card_tag}.log
```

The workspace root file will be saved at `merged_cards/${obs}_${card_tag}/fullmodel.root`.

Running the fits
================

Script `tools/fitting/dofit.sh` has the commands for various fit-related tasks.

```
cd merged_cards

../../tools/fitting/dofit.sh $PWD $obs $card_tag COMMAND [ARGS]
```

COMMANDs for fits that go into the AN:

`AsimovUnreg AsimovReg Reg Unreg "IntegratedUnreg "{0..5} GOFObs AsimovImpact Impact`

Also COMMANDs for the AN, but requiring some of the above commands to finish first:

`"GOFGen 4 "{1..250} IntegratedUnregStatOnly "IntegratedUnregUncert "{signal,theoretical,luminosity,experimental} IntegratedImpact RegStatOnly "RegUncert "{signal,theoretical,luminosity,experimental}`

Once GOFGen jobs are done, compute the goodness of fit:

`"GOFFreqToy 4 "{1..250}`

Creating the full combination workspace
=======================================

Constraint term is currently not supported by combineCards.py. Use the unregularized data cards and add the constraint term later:
```
cd combination
mkdir ${obs}_${card_tag}

combineCards.py hww2016=$PWD/../ggH2016/merged_cards/${obs}_${card_tag}/fullmodel_unreg.txt hww2017=$PWD/../ggH2017/merged_cards/${obs}_${card_tag}/fullmodel_unreg.txt hww2018=$PWD/../ggH2018/merged_cards/${obs}_${card_tag}/fullmodel_unreg.txt > ${obs}_${card_tag}/fullmodel_unreg.txt
sed 's/kmax [0-9]*/kmax */' ${obs}_${card_tag}/fullmodel_unreg.txt > ${obs}_${card_tag}/fullmodel.txt 
grep ' constr ' ../ggH2016/merged_cards/${obs}_${card_tag}/fullmodel.txt >> ${obs}_${card_tag}/fullmodel.txt

ulimit -s unlimited

cd ${obs}_${card_tag}
if [ $obs = ptH ]
then
  # Make sure you are using the actual binning in the datacard!!
  text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose --PO map=.*/.*H_hww_PTH_0_20:r_0[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_20_45:r_1[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_45_80:r_2[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_80_120:r_3[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_120_200:r_4[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_GT200:r_5[1.,-10.,10.] fullmodel.txt -o fullmodel.root
elif [ $obs = njet ]
then
  text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose --PO map=.*/.*H_hww_NJ_0:r_0[1.,-10.,10.] --PO map=.*/.*H_hww_NJ_1:r_1[1.,-10.,10.] --PO map=.*/.*H_hww_NJ_2:r_2[1.,-10.,10.] --PO map=.*/.*H_hww_NJ_3:r_3[1.,-10.,10.] --PO map=.*/.*H_hww_NJ_GE4:r_4[1.,-10.,10.] fullmodel.txt -o fullmodel.root
fi
```

Integrated mu measurement
=========================

Integrated (normalized) fit can be performed choosing which `f_i` to be made dependent on other `f`s. The last argument to dofit is the index of dependent `f`.
```
tools/fitting/dofit.sh combination ptH fullmodel IntegratedUnreg 0
```
Makes the datacard and workspace (if not yet made with `tools/fitting/make_integrated_cards.py`) and performs the fit. Results are stored in `combination/ptH_fullmodel/integrated`.

Inclusive mu measurement (ggH tag)
==================================

The differential configurations include NJ>=2 cuts, to be combined with NJ=0 and =1 to perform the inclusive mu measurement. For this fit, we skip the preprocessing step and use the standard Latinos framework steps:
```
python ../tools/merge_for_inclusive.py $year shapes/plots_ggHInclusive${year}.root rootFile_merged/plots_ggHDifferential${year}_ALL_*.root
mkDatacards.py --outputDirDatacard=unmerged_cards/inclusive --inputFile=shapes/plots_ggHInclusive${year}.root --structureFile=../tools/structure_inclusive.py
../tools/fitting/make_inclusive_card.sh (2016|2017|2018|combination)
```

Inclusive mu measurement (no tag)
==================================

An inclusive mu fit without overlap resolution against VH and VBF tags can be constructed simply by running `text2workspace.py` with no options to the `fullmodel_unreg.txt` data card.

Gen-only plots configuration
============================

For the cross section interpretation of the fit results and multiple other purposes, there is a `fiducial` plot configuration under this directory. The configuration is light-weight enough to not need batch splitting at all. Some of the plotting scripts below assume that this configuration has been run and there exists a ROOT file named `fiducial/rootFile/plots_Fiducial.root`.

Other fit-related tasks
=======================

Directory `tools/fitting` contains script for fit-related tasks:

- `bias_estimate.py`: Compute the regularization bias as dmu/dn (nu - n) where dmu/dn is the rate of change of mu wrt SR event yield n and nu is the postfit prediction of nu. Requires an postfit Asimov from unregularized best-fit model and the result of a regularized fit result on it (Both can be done with dofit.sh).

Making plots
============

Directory `tools/plotting` contains scripts for plotting:

- `dyreweight.py`: Draw the rather-obscure DY reweighting function.
- `selectionvars.py`: Draw the distributions of variables used for event selection. Used with `selectionvars` configuration subdirectory for Figure 3 of AN-2019/006.
- `plot_distributions.py`: Draw the prefit and postfit distributions of fit shapes and other variables.
- `responsematrix.py`: Draw the signal response matrix.
- `binyields.py`: (Not used) Draw and print the prefit yields of signal and background in all CR and SR bins.
- `plot_delta_scan.py`: Take the output of DeltaScan in dofit.sh and plot the mean of the global correlation coefficients as a function of the regularization strength delta.
- `diffNuisances_mlfit.py`: Do what the standard diffNuisances script does for MultiDimFit output.
- `plot_mu.py`: Take the regularized and unregularized fit outputs and plot the mu values.
- `plot_correlation_matrix.py`: Take a fit result and plot the signal strength correlation matrix.
- `plot_correlation_matrix_2.py`: Paper version of correlation matrix.
- `bias_estimate_vbfshift.py`: Use VBF0 and VBF2 shifted fits (see above) to assess the model dependency of unfolding.
- `plot_sigma.py`: Make the "money plot".
- `plot_postfit_sr.py`: Make post-fit mll distributions from a workspace with possibly different mll:mtH binning from the actual fit model. See below.

Making postfit SR plots
=======================

Use plot_postfit_sr.py to create "postfit" SR plots with template binning different from what was used in the fit (so certain postfit uncertainties are not propagated to the plots).
```
obs=ptH
source_card_tag=binrenorm
card_tag=fullbinning
for year in 201{6,7,8}
do
  cd ggH$year
  mkDatacards.py --outputDirDatacard=unmerged_cards/${obs}_${card_tag} --inputFile=shapes/plots_${obs}_${source_card_tag}.root --structureFile=../tools/structure_${obs}_fullbinning.py
  cd ../
done

# in combine environment
obs=ptH
card_tag=fullbinning
for year in 201{6,7,8}
do
  cd ggH$year
  ../tools/fitting/combine_cards.py --in unmerged_cards/${obs}_${card_tag} --out merged_cards/${obs}_${card_tag} --only-fullmodel --float-background WW=WW top=top DY${year}=DY --just-combine
  cd ../
done

cd combination
mkdir ${obs}_${card_tag}

combineCards.py hww2016=$PWD/../ggH2016/merged_cards/${obs}_${card_tag}/fullmodel_unreg.txt hww2017=$PWD/../ggH2017/merged_cards/${obs}_${card_tag}/fullmodel_unreg.txt hww2018=$PWD/../ggH2018/merged_cards/${obs}_${card_tag}/fullmodel_unreg.txt > ${obs}_${card_tag}/fullmodel_unreg.txt
sed 's/kmax [0-9]*/kmax */' ${obs}_${card_tag}/fullmodel_unreg.txt > ${obs}_${card_tag}/fullmodel.txt 
grep ' constr ' ../ggH2016/merged_cards/${obs}_${card_tag}/fullmodel.txt >> ${obs}_${card_tag}/fullmodel.txt

cd ${obs}_${card_tag}

# Make sure you are using the actual binning in the datacard!!
text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose --PO map=.*/.*H_hww_PTH_0_20:r_0[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_20_45:r_1[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_45_80:r_2[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_80_120:r_3[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_120_200:r_4[1.,-10.,10.] --PO map=.*/.*H_hww_PTH_GT200:r_5[1.,-10.,10.] fullmodel.txt -o fullmodel.root

cd ../../

python tools/plotting/plot_postfit_sr.py $obs --source combination/${obs}_${card_tag}/fullmodel.root --postfit combination/${obs}_${source_card_tag}/higgsCombineReg.MultiDimFit.mH120.root --rootfile combination/${obs}_${card_tag}/postfit_plots.root --reuse --out $PWD
```
