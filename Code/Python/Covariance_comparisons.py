# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Covariance between $c$ and $\mathbf{p}$ over time
# ### By William Du

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
from HARK.ConsumptionSaving.ConsIndShockModel import IndShockConsumerType

# %%
Harmenberg_Dict={
    # Parameters shared with the perfect foresight model
    "CRRA":2,                             # Coefficient of relative risk aversion
    "Rfree": 1.02**.25,                  # Interest factor on assets
    "DiscFac": 0.9935,                    # Intertemporal discount factor
    "LivPrb" : [1.00],                    # Survival probability
    "PermGroFac" :[1.00],                 # Permanent income growth factor

    # Parameters that specify the income distribution over the lifecycle
   
    "PermShkStd" :  [.06],     # Standard deviation of log permanent shocks to income
    "PermShkCount" : 5,                    # Number of points in discrete approximation to permanent income shocks
    "TranShkStd" : [.3],                   # Standard deviation of log transitory shocks to income
    "TranShkCount" : 5,                    # Number of points in discrete approximation to transitory income shocks
    "UnempPrb" : 0.07,                     # Probability of unemployment while working
    "IncUnemp" : 0.3,      # Unemployment benefits replacement rate
    "UnempPrbRet" : 0.0005,                # Probability of "unemployment" while retired
    "IncUnempRet" : 0.0,                   # "Unemployment" benefits when retired
    "T_retire" : 0,                        # Period of retirement (0 --> no retirement)
    "tax_rate" : 0.18,      # Flat income tax rate (legacy parameter, will be removed in future)

    # Parameters for constructing the "assets above minimum" grid
    "aXtraMin" : 0.001,                    # Minimum end-of-period "assets above minimum" value
    "aXtraMax" : 2000,                       # Maximum end-of-period "assets above minimum" value
    "aXtraCount" : 90,                     # Number of points in the base grid of "assets above minimum"
    "aXtraNestFac" : 4,                    # Exponential nesting factor when constructing "assets above minimum" grid
    "aXtraExtra" : [None],                 # Additional values to add to aXtraGrid

    # A few other parameters
    "BoroCnstArt" : 0.0,                   # Artificial borrowing constraint; imposed minimum level of end-of period assets
    "vFuncBool" : False,                    # Whether to calculate the value function during solution
    "CubicBool" : False,                   # Preference shocks currently only compatible with linear cFunc
    "T_cycle" : 1,                         # Number of periods in the cycle for this agent type

    # Parameters only used in simulation
    "AgentCount" : 2000000,                 # Number of agents of this type
    "T_sim" : 2500,                         # Number of periods to simulate
    "aNrmInitMean" : np.log(1.25)-(.5**2)/2,# Mean of log initial assets
    "aNrmInitStd"  : .5,                   # Standard deviation of log initial assets
    "pLvlInitMean" : 0,                    # Mean of log initial permanent income
    "pLvlInitStd"  : 0,                    # Standard deviation of log initial permanent income
    "PermGroFacAgg" : 1.0,                 # Aggregate permanent income growth factor
    "T_age" : None,                        # Age after which simulated agents are automatically killed

}

# %% [markdown]
# # Run with PermGroFac = 1.0

# %%
fast = IndShockConsumerType(**Harmenberg_Dict, verbose = 1 )
fast.cycles = 0
GIC = ((fast.Rfree*fast.DiscFac)**(1/fast.CRRA))/fast.PermGroFac[0] # Make harmenberg but not szcheidle

print( 'RB**(1/rho) ' +str(GIC))
print('szeidl upper bound :' +str(np.exp((-fast.PermShkStd[0]**2) / 2) ))

fast.track_vars = ['cNrm','pLvl'] 
fast.solve()

fast.initialize_sim()
fast.simulate()

# Compute paths of aggregate consumption, assets and market resources

Asset_list = [] # path of aggregate assets
Consumption_list = [] # Path of aggregate consumption
M_list =[] # path of aggregate market resources

covariances =[]

for i in range (fast.T_sim):
    covariances.append(np.cov( fast.history['cNrm'][i] , fast.history['pLvl'][i] )[1][0]   )
    #Assetagg =  np.mean(fast.history['aNrm'][i]) # compute aggregate assets for period i
    #Asset_list.append(Assetagg)
    ConsAgg =  np.mean(fast.history['cNrm'][i] )# compute aggregate consumption for period i
    Consumption_list.append(ConsAgg)
    #Magg = np.mean(fast.history['mNrm'][i])# compute aggregate market resources for period i
   # M_list.append(Magg)


# %% [markdown]
# # Plot of $C_{t}$ 

# %%
plt.plot(Consumption_list[25:])
plt.title('Aggregate Consumption')
plt.show()

# %% [markdown]
# # Plot of $Cov_{t}(c_{t},p_{t})$ over time

# %%
plt.plot(covariances[25:])# only consider period t=25 to t=200
plt.plot(np.mean(covariances[25:])*np.ones(len(covariances[25:])))
plt.title('covariance between consumption and permanent income level')
plt.show()

print('mean covariance between consumption and permanent income ' + str(np.mean(covariances)))


# %% [markdown]
# # Plot of $ \frac{Cov_{t+1}(c_{t+1},p_{t+1})}{ Cov_{t}(c_{t}, p_{t})}$ over time

# %%
growth_diff = []
for i in range(len(covariances) -1):
    growth_diff.append( covariances[i+1]/covariances[i])
    
plt.plot(growth_diff[25:]) # only consider period t=25 to t=200
plt.plot(np.mean(growth_diff[400:])*np.ones(len(growth_diff[25:])))
plt.title('Cov_{t+1}(c_{t+1},p_{t+1}) / Cov_{t}(c_{t}, p_{t})')
plt.show()
    
    
print('mean growth diff ' + str(np.mean(growth_diff[400:])))

# %% [markdown]
# # Check If Equation 43 (in HTML) holds. (IF THEY HAVE CONSTANT GROWTH)

# %%
C_growth_diff = []
for i in range(len(Consumption_list) -1):
    C_growth_diff.append( Consumption_list[i+1]/Consumption_list[i])
    
sim_period_show_starting=25
plt.plot(C_growth_diff[sim_period_show_starting:])
plt.plot(np.mean(C_growth_diff[400:])*np.ones(len(C_growth_diff[sim_period_show_starting:])))
plt.title('C_{t+1} / C_{t}')
plt.show()

print('C_{t+1}/C_{t} = ' + str(np.mean(C_growth_diff[sim_period_show_starting:])))
#Equation 43 in HTML

omega_c = np.mean(C_growth_diff[1000:])

omega_cov = np.mean(growth_diff[1000:])

print('omega_cov :' + str(omega_cov))
print('omega_cov / omega_c: ' + str(omega_cov / omega_c ))

# %% [markdown]
# # Run with PermGroFac = 1.02

# %%
fast = IndShockConsumerType(**Harmenberg_Dict, verbose = 1 )
fast.cycles = 0
fast.Rfree = 1.2**.25
fast.PermGroFac = [1.02]

GIC = ((fast.Rfree*fast.DiscFac)**(1/fast.CRRA))/fast.PermGroFac[0] # Make harmenberg but not szcheidle

print( 'RB**(1/rho)  / PermGroFac ' +str(GIC))
print('szeidl upper bound :' +str(np.exp((-fast.PermShkStd[0]**2) / 2) ))
fast.track_vars = ['cNrm','pLvl'] 
fast.solve()

fast.initialize_sim()
fast.simulate()

# Compute paths of aggregate consumption, assets and market resources

Asset_list = [] # path of aggregate assets
Consumption_list = [] # Path of aggregate consumption
M_list =[] # path of aggregate market resources

covariances =[]

for i in range (fast.T_sim):
    
    covariances.append(np.cov( fast.history['cNrm'][i] , fast.history['pLvl'][i] )[1][0]   )
    #Assetagg =  np.mean(fast.history['aNrm'][i]) # compute aggregate assets for period i
    #Asset_list.append(Assetagg)
    ConsAgg =  np.mean(fast.history['cNrm'][i] )# compute aggregate consumption for period i
    Consumption_list.append(ConsAgg)
    #Magg = np.mean(fast.history['mNrm'][i])# compute aggregate market resources for period i
    #M_list.append(Magg)
    

# %%
var_cNrm = []

for i in range(fast.T_sim):
    var_cNrm.append(np.std(fast.history['cNrm'][i])**2)
    
plt.plot(var_cNrm)
plt.show()

# %%
fast.check_conditions(verbose=True)

# %% [markdown]
# # Plot of $C_{t}$

# %%
plt.plot(Consumption_list[25:])
plt.title('Aggregate Normalized Consumption')
plt.show()

# %% [markdown]
# # Plot of $Cov_{t}(c_{t},p_{t})$ over time

# %%
plt.plot(covariances[25:])# only consider period t=25 to t=200
plt.plot(np.mean(covariances[200:800])*np.ones(len(covariances[25:])), '--')
plt.title('covariance between consumption and permanent income level')
plt.show()
print(' covariance between consumption and permanent income ' + str(np.mean(covariances)))

# %%
plt.plot(np.log(covariances[300:1000]))
plt.show()

# %% [markdown]
# # Plot of $ \frac{Cov_{t+1}(c_{t+1},p_{t+1})}{ Cov_{t}(c_{t}, p_{t})}$ over time

# %%
growth_diff = []
for i in range(len(covariances) -1):
    growth_diff.append( covariances[i+1]/covariances[i])
    
plt.plot(growth_diff[25:])# only consider period t=25 to t=200
plt.plot(np.mean(growth_diff[400:])*np.ones(len(growth_diff[25:])))
plt.title('Cov_{t+1}(c_{t+1},p_{t+1}) / Cov_{t}(c_{t}, p_{t})')
plt.show()
    
print('mean growth diff ' + str(np.mean(growth_diff[400:])))

# %% [markdown]
# # Check If Equation 43 (in HTML) holds.

# %%
C_growth_diff = []
for i in range(len(Consumption_list) -1):
    C_growth_diff.append( Consumption_list[i+1]/Consumption_list[i])
    
plt.plot(C_growth_diff[25:])
plt.plot(np.mean(C_growth_diff[400:])*np.ones(len(C_growth_diff[25:])))
plt.title('C_{t+1} / C_{t}')
plt.show()

print('omega_c =' + str(np.mean(C_growth_diff[400:])))

#Equation 43 in HTML

omega_c = np.mean(C_growth_diff[400:])
omega_cov = np.mean(growth_diff[400:])

print('omega_cov ' + str(omega_cov))
print('omega_cov / omega_c = ' + str(omega_cov/ omega_c ))

# %%
omega_c

# %%
omega_cov
