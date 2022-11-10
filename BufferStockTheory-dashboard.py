#!/usr/bin/env python
# coding: utf-8

# # [Theoretical Foundations of Buffer Stock Saving](https://econ-ark.github.io/BufferStockTheory)
# ## Interactive Figures
# 
# [![econ-ark.org](https://img.shields.io/badge/Powered%20by-Econ--ARK-3e8acc.svg)](https://econ-ark.org/materials/bufferstocktheory)
# 
# (Execute the cells below one at a time to activate the corresponding interactive tools)

# In[1]:


# Make sure we have things set up correctly

# Get others' tools
import os.path

# Make sure requirements have been satisfied
if os.path.isdir('binder'):  # Folder defining requirements exists
    # File requirements.out should be created first time notebook is run
    if not os.path.isfile('./binder/requirements.out'):  
        get_ipython().system('(pip install -r ./binder/requirements.txt > ./binder/requirements.out)')

from ipywidgets import interact, interactive, fixed, interact_manual

# Get HARK modeling tool
from HARK.ConsumptionSaving.ConsIndShockModel import IndShockConsumerType

# Get BufferStockTheory dashboard tools
import Dashboard.dashboard_widget as BST


# ## Convergence of the Consumption Rules
# \begin{align}
# \newcommand\maththorn{\mathord{\pmb{\text{\TH}}}}
# \newcommand{\aLvl}{\mathbf{a}}
# \newcommand{\aNrm}{{a}}
# \newcommand{\BalGroRte}{\tilde}
# \newcommand{\Bal}{\check}
# \newcommand{\bLvl}{{\mathbf{b}}}
# \newcommand{\bNrm}{{b}}
# \newcommand{\cFunc}{\mathrm{c}}
# \newcommand{\cLvl}{{\mathbf{c}}}
# \newcommand{\cNrm}{{c}}
# \newcommand{\CRRA}{\rho}
# \newcommand{\DiscFac}{\beta}
# \newcommand{\dLvl}{{\mathbf{d}}}
# \newcommand{\dNrm}{{d}}
# \newcommand{\Ex}{\mathbb{E}}
# \newcommand{\hLvl}{{\mathbf{h}}}
# \newcommand{\hNrm}{{h}}
# \newcommand{\IncUnemp}{\mu}
# \newcommand{\mLvl}{{\mathbf{m}}}
# \newcommand{\mNrm}{{m}}
# \newcommand{\MPC}{\kappa}
# \newcommand{\PatFac}{\pmb{\unicode[0.55,0.05]{0x00DE}}}
# \newcommand{\PatRte}{\pmb{\unicode[0.55,0.05]{0x00FE}}}
# \newcommand{\PermGroFacAdj}{\underline{\Phi}}
# \newcommand{\PermGroFac}{\pmb{\Phi}}
# \newcommand{\PermShkStd}{\sigma_{\PermShk}}
# \newcommand{\PermShk}{\pmb{\psi}} % New
# \newcommand{\pLvl}{{\mathbf{p}}}
# \newcommand{\Rfree}{\mathsf{R}}
# \newcommand{\RNrm}{\mathcal{R}}
# \newcommand{\RPFac}{\APFac_{\Rfree}}
# \newcommand{\Thorn}{\pmb{\TH}}
# \newcommand{\TranShkAll}{\pmb{\xi}}
# \newcommand{\TranShkStd}{\sigma_{\TranShk}}
# \newcommand{\TranShk}{\pmb{\theta}}
# \newcommand{\Trg}{\hat}
# \newcommand{\uFunc}{\mathrm{u}}
# \newcommand{\UnempPrb}{\wp}
# \newcommand{\vLvl}{{\mathbf{v}}}
# \newcommand{\vNrm}{{v}}
# \renewcommand{\APFac}{\pmb{\unicode[0.55,0.05]{0x00DE}}}
# \end{align}
# Under the given parameter values,
# 
# 
# | Parameter | Description | Python Variable | Value |
# |:---:      | :---:       | :---:  | :---: |
# | $\PermGroFac$ | Permanent Income Growth Factor | $\texttt{PermGroFac}$ | 1.03 |
# | $\Rfree$ | Interest Factor | $\texttt{Rfree}$ | 1.04 |
# | $\DiscFac$ | Time Preference Factor | $\texttt{DiscFac}$ | 0.96 |
# | $\CRRA$ | Coeﬃcient of Relative Risk Aversion| $\texttt{CRRA}$ | 2 |
# | $\UnempPrb$ | Probability of Unemployment | $\texttt{UnempPrb}$ | 0.005 |
# | $\TranShk^{\large u}$ | Income when Unemployed | $\texttt{IncUnemp}$ | 0. |
# | $\PermShkStd$ | Std Dev of Log Permanent Shock| $\texttt{PermShkStd}$ | 0.1 |
# | $\TranShkStd$ | Std Dev of Log Transitory Shock| $\texttt{TranShkStd}$ | 0.1 |
# 
# [the paper's first figure](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#Convergence-of-the-Consumption-Rules) depicts the successive consumption rules that apply in the last period of life $(\cFunc_{T}(\mNrm))$, the second-to-last period, and earlier periods $(\cFunc_{T-n})$.  $\cFunc(\mNrm)$ is the consumption function to which these converge:
# 
# \begin{align}
#  \cFunc(\mNrm) & = \lim_{n \uparrow \infty} \cFunc_{T-n}(\mNrm)
# \end{align}
# 

# In[2]:


# Risk aversion ρ and σ_ψ have the most interesting effects

cFuncsConverge_widget=interactive(
    BST.makeConvergencePlot,
    DiscFac=BST.DiscFac_widget[0],
    CRRA=BST.CRRA_widget[0],
    Rfree=BST.Rfree_widget[0],
    PermShkStd=BST.PermShkStd_widget[0],
)
cFuncsConverge_widget


# ## [Growth Impatience, and Pseudo-Steady-State versus Target Wealth](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#The-GIC)
# 
# [A figure](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#GICModFailsButGICRawHolds) in the paper depicts a solution when:
# 
#    - the **FVAC** [(Finite Value of Autarky Condition)](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#FVAC) and **WRIC** [(Weak Return Impatience Condition)](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#WRIC) hold 
#        - so that [the model has a solution](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#Conditions-Under-Which-the-Problem-Defines-a-Contraction-Mapping), 
#    - and the raw **GIC** [(Growth Impatience Condition)](https://econark.github.io/BufferStockTheory/BufferStockTheory3.html#GICRaw) holds
#        - so that there is an [aggregate balanced-growth equilibrium](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#Growth-Rates-of-Aggregate-Income-and-Consumption) and an individual [Pseudo-Steady-State](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#pseudo-steady-state),
#    - but the impatience condition normalized by the permanent shock (the [Normalized Growth Impatience Condition **GIC-Nrm**](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#GICMod) fails
#        - so that there is no [individual target wealth ratio](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#TheoremTarget)
# 

# \begin{align}
# \texttt{GICRaw-Holds:    }\phantom{\Ex}\left[\frac{(\Rfree \DiscFac)^{1/\CRRA}}{\PermGroFac\phantom{\PermShk}}\right] & <  1 \\
# \texttt{GICMod-Fails:    }\Ex\left[\frac{(\Rfree \DiscFac)^{1/\CRRA}}{\PermGroFac\PermShk}\right] & >  1
# \end{align}

# Use the slider to see what happens as you move $\sigma_{\PermShk}$ from below to above the value that makes the GIC-Nrm condition fail.  
# 
# | Param | Description | Code | Value |
# | :---: | ---         | ---  | :---: |
# | $\sigma_{\PermShk}$ | Std Dev Perm Shk | `PermShkStd` | 0.2 |

# In[3]:


# Make consumer more patient by doubling uncertainty
BST.base_params['PermShkStd'] = [2 * 0.1]

# Give solution a bit more precision by increasing density of shocks
BST.base_params['PermShkCount'] = BST.PermShkCount = 7  #  extra points for accuracy

# Construct an instance, and unquietly describe it
GICModFailsButGICRawHolds =     IndShockConsumerType(**BST.base_params,
                         quietly=False,
                         messaging_level=10) # level 10 is all messages; increase for less output


# In[4]:


# Under starting parameters, this example has a pseudo-steady-state m where there
# is balanced growth in the levels of market resources and consumption, BalLvl,
# but does not have a (finite) "target" value of m where the ratio of individual
# market resources to permanent income is expected to be stable
# (the consumption function intersects with the expected MLvl growth but not the mNrm change locus)
# If permanent shock std is reduced, it will have both steady state m and target m

GICFailsExample_widget = interactive(
    BST.makeGICFailExample,
    DiscFac=BST.DiscFac_widget[1],
    PermShkStd=BST.PermShkStd_alt_start_widget[1],
    UnempPrb=BST.UnempPrb_widget[1],
)
GICFailsExample_widget


# ### [Balanced Growth "Steady State Equilibrium" $\check{m}$, "Target" $\hat{m}$, Expected Consumption Growth, and Permanent Income Growth](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#AnalysisoftheConvergedConsumptionFunction)
# 
# The next figure is shown in  [Analysis of the Converged Consumption Function](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#cNrmTargetFig), and depicts the expected consumption growth factor $\Ex_{t}[\cLvl_{t+1}/\cLvl_{t}]$ for a consumer behaving according to the converged consumption rule, along with the expected growth factor for market resources $\Ex_{t}[\pmb{\mathrm{m}}_{t+1}/\pmb{\mathrm{m}}_{t}]$, and the expected growth factor for the ratio of market resources to permanent income, $\Ex_{t}[\mNrm_{t+1}/\mNrm_{t}]$.
# 
# Manipulate the time preference and income growth factors to show the effects on target and pseudo-steady-state ("balanced growth") wealth, whose numerical values appear above the figure.

# In[5]:


# Explore what happens as you make the consumer more patient in two ways: β ↑ and Γ ↓

BST.base_params['PermShkStd'] = [0.1]  #  Restore the original default uncertainty
cNrmTargetFig_widget = interactive(
    BST.cNrmTargetFig_make,
    PermGroFac=BST.PermGroFac_growth_widget[2],
    DiscFac=BST.DiscFac_growth_widget[2]
)
cNrmTargetFig_widget


# ### [Consumption Function Bounds](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#AnalysisoftheConvergedConsumptionFunction)
# [The next figure](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#cFuncBounds)
# illustrates theoretical bounds for the consumption function.
# 
# The numerator in the ratios in the growth impatience conditions above is a central object in the paper, which we call the Absolute Patience Factor, [APF](https://econark.github.io/BufferStockTheory/BufferStockTheory3.html#APFacDefn):
# \begin{align}
# \texttt{APF:   } \APFac & = \left(\Rfree \DiscFac\right)^{1/\CRRA}
# \end{align}
# and by analogy to the Growth Impatience Conditions we define a [Return Patience Factor](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#RPFacDefn) as:
# \begin{align}
# \\ \RPFac & = \APFac/\Rfree
# \end{align}
# because this leads to a definition of a [Return Impatience Condition](https://econ-ark.github.io/BufferStockTheory/BufferStockTheory3.html#RIC) as:
# \begin{align}
# \\ \RPFac & < 1
# \end{align}
# which makes sense because, in the perfect foresight model, the marginal propensity to consume is $\kappa = 1-\RPFac$ which must be positive.
# 
# In the figure below, we set $\Rfree$ and $\Phi$ to fixed values of 1.0.  Explore what happens to the consumption function as you move the parameters as far as you can toward the perfect foresight model and the time preference factor up toward 1 (warning: the model takes longer to solve if the RIC is close to failing; be patient).  What would you expect to see if the upper boundary of the figure were extended far enough?  
# 
# Notice that the model with uncertainty gets very close to the perfect foresight model only when the uncertainty is tuned down to the very lowest possible levels, relative risk aversion is at its lowest allowed value, and the time preference rate is set to a high number.  Uncertainty has powerful effects!

# In[6]:


cFuncBounds_widget = interactive(
    BST.makeBoundsFigure,
    UnempPrb=BST.UnempPrb_widget[3],
    PermShkStd=BST.PermShkStd_widget[3],
    TranShkStd=BST.TranShkStd_widget[3],
    DiscFac=BST.DiscFac_widget[3],
    CRRA=BST.CRRA_widget[3]
)
cFuncBounds_widget

