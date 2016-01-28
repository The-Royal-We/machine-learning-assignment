# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:38:44 2016

@author: se415011
"""
import array
import csv

import numpy as np
import scipy.sparse as sp
import theano

from theano import sparse
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

inputFile = open("sparse-rating-matrix.csv", 'r')

dataMat = csv_to_csr(inputFile)            

"""
mat = sparse.csc_matrix(name='mat', dtype='float32')

inputFile = open("sparse-rating-matrix", 'r')

dataMat = {}

for line in inputFile:
    elements = line.split()
    rater = elements[0]    
    ratee = elements[1]
    score = float(elements[2])
    
    if not dataMat.has_key(rater):
        dataMat[rater] = {ratee: score}
    else:
        dataMat[rater].update({ratee: score})

y = sparse.structured_add(mat, dataMat['abc4efcd']['8b5463fb'])
print y.toarray()
"""
