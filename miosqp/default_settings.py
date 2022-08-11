def get_miosqp_settings():
    return {
        # integer feasibility tolerance
        'eps_int_feas': 1e-03,
        # maximum number of iterations
        'max_iter_bb': 1000,
        # tree exploration rule
        #   [0] depth first
        #   [1] two-phase: depth first until first incumbent and then  best bound
        'tree_explor_rule': 1,
        # branching rule
        #   [0] max fractional part
        'branching_rule': 0,
        'verbose': False,
        'print_interval': 1
    }


def get_osqp_settings():
    return {
        'eps_abs': 1e-03,
        'eps_rel': 1e-06,
        'eps_prim_inf': 1e-04,
        'verbose': False
    }
