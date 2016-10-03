"""
The :mod:`sklearn.cross_validation` module includes utilities for cross-
validation and performance evaluation.
"""

# Author: jbsilva <@>
# License: BSD 3 clause


import warnings;
import pandas as pd;
import numpy as np;

def parti_set(data,part_percents,time_shuffle=None):
    """S.

    Parameters
    ----------
    X : Input data array.
    part_percents :
    Returns
    -------
    splitting : list of partitioned data
            Output type is the same as the input type.
    Examples
    --------
    """

    # shuffle data and make a data frame
    if not time_shuffle is None:
        data.sort_values([time_shuffle], inplace=True);
        X = data.values.copy();
    else:
        X = data.values.copy();
        np.random.shuffle(X);
    dat = pd.DataFrame(X, columns=data.columns)

    # calculate partitions
    part_percents_arr = np.array(part_percents)
    parti_indexes = np.round(np.multiply( X.shape[0] , np.true_divide( part_percents_arr, np.sum(part_percents_arr) ) )).astype(np.int);

    # split into partitions
    parti_out = []; curr_l = 0;
    for ind_end in parti_indexes:
        parti_out.append( dat[curr_l:curr_l+ind_end] )
        curr_l = ind_end + curr_l

    return parti_out

def parti_by(data,part_percents,by_col,time_partitions=None,time_col=None):
    """S.

    Parameters
    ----------
    X : Input data array.
    part_percents :
    Returns
    -------
    splitting : list of partitioned data
            Output type is the same as the input type.
    Examples
    --------
    """
    parti_list=data[by_col].unique()

    # split by variable values into partitions
    part_percents_arr = np.array(part_percents)
    parti_steps = np.round(np.multiply(len(parti_list), np.true_divide(part_percents_arr, np.sum(part_percents_arr)))).astype(np.int);
    parti_indexes=[];curr=0
    for stp in parti_steps:
        parti_indexes.append(stp+curr)
        curr=stp+curr

    # create hash map of partition destinations
    parti_map={}; curr = 0;
    for ind in range( len( parti_list ) ):
        if ind >= parti_indexes[curr]:
            curr = 1 + curr
        parti_map[ parti_list[ind] ] = curr

    # partion out data into partitions
    parti_out=[ [] for x in parti_indexes ]
    by_ind=data.columns.tolist().index(by_col);
    for curr_row in data.values.copy():
        by_val=curr_row[by_ind]
        parti_out[parti_map[by_val]].append(curr_row);

    # post process partitions
    for ind in range( len(parti_out) ):
        parti_out[ind]=pd.DataFrame(data=parti_out[ind],columns=data.columns.tolist())
        # if necessary further partition out data by time
        if not time_partitions is None:
            parti_out[ind] = parti_set(parti_out[ind],time_partitions,time_shuffle=time_col);

    return parti_out

