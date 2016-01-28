# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:49:45 2016

@author: se415011
"""

import array
import csv
import numpy as np
from scipy.sparse import csr_matrix

def csv_to_csr(f):
    """Read content of CSV file f, return as CSR matrix."""
    data = array.array("f")
    indices = array.array("i")
    indptr = array.array("i", [0])

    for i, row in enumerate(csv.reader(f), 1):
        row = np.array(map(float, row))
        shape1 = len(row)
        nonzero = np.where(row)[0]
        data.extend(row[nonzero])
        indices.extend(nonzero)
        indptr.append(i)

    return csr_matrix((data, indices, indptr),
                      dtype=float, shape=(i, shape1))