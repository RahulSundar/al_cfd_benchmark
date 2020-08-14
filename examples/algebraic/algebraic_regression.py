import numpy as np
from active_learning_cfd.cfd_regressor import active_learner_regressor
from active_learning_cfd.custom_sampling import (
    probabilistic_std_sampling,
    random_sampling,
)
from active_learning_cfd.basic_regressors import regressor_list

from algebraic_runner import TwoParameterFunction

function = TwoParameterFunction()

features_ranges = np.array(
    [[0, 2], [0, 1]]
)  # List of maximum and minimum values for each parameter
query_minimum_spacing = np.array(
    [0.01, 0.01]
)  # List of minimum spacing for each parameter
n_initial = 9  # Number of initial samples
n_queries = 30  # Number of queries
plot_regression = True
plot_brute_force = True

regressor_constructor = regressor_list["gaussian_process_rbf"]
regressor = regressor_constructor()

query_strategy = probabilistic_std_sampling

active_learner_regressor(
    function,
    features_ranges,
    regressor,
    query_minimum_spacing,
    n_queries,
    query_strategy,
    n_initial,
    plot_regression=plot_regression,
    plot_brute_force=plot_brute_force,
    save_path="figs",
    save_name="algebraic",
)
