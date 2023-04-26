#!/usr/bin/env python3

import unittest
import numpy as np

def get_batch(vectorized_songs, seq_length, batch_size):
  # the length of the vectorized songs string
  n = vectorized_songs.shape[0] - 1
  # randomly choose the starting indices for the examples in the training batch
  idx = np.random.choice(n-seq_length, batch_size)

  '''TODO: construct a list of input sequences for the training batch'''
  input_batch = [vectorized_songs[i : i + seq_length] for i in idx]
  '''TODO: construct a list of output sequences for the training batch'''
  output_batch = [vectorized_songs[i+1 : i + seq_length + 1] for i in idx]

  # x_batch, y_batch provide the true inputs and targets for network training
  x_batch = np.reshape(input_batch, [batch_size, seq_length])
  y_batch = np.reshape(output_batch, [batch_size, seq_length])
  return x_batch, y_batch

sample_vectorized_songs = np.array(range(0, 500))

class TestGetBatch(unittest.TestCase):
    def test_function(self):
        x, y = get_batch(sample_vectorized_songs, 3, 10)
        self.assertEqual(x, 'words')

if __name__ == '__main__':
    unittest.main()