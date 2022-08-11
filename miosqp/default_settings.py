MIOSQP_SETTINGS = {
    'eps_int_feas': 1e-02,   # integer feasibility tolerance
    'max_iter_bb': 2000,     # maximum number of iterations
    'tree_explor_rule': 1,   # tree exploration rule
                             #   [0] depth first
                             #   [1] two-phase: depth first  until first incumbent and then  best bound
    'branching_rule': 0,     # branching rule
                             #   [0] max fractional part
    'verbose': False,
    'print_interval': 1
}

OSQP_SETTINGS = {
    'eps_abs': 1e-03,
    'eps_rel': 1e-03,
    'eps_prim_inf': 1e-04,
    'verbose': False
}
