#!/usr/bin/python

## @dataset_iterator.py
#  This file iterates a given dataset, and returns a list of dict records, of earthquakes
#      within the supplied parameters (i.e. radius, timeframe).

## Class: Data_Iterator
class Data_Iterator:

  ## constructor:
  def __init__(self, dataset, longitude, latitude, radius, daysBack):
    self.target   = []
    self.dataset  = dataset
    self.origin_longitude = longitude
    self.origin_latitude  = latitude
    self.radius   = radius
    self.daysBack = daysBack

  ## iterator: iterate a given dataset, and store earthquakes within the specified radius,
  #            and timeframe.
  def iterator(self):

  ## validator: validate subset(s) of given the dataset. The above 'iterator' method,
  #             implements this method.
  def validator(self):

  ## get_target: return a list of earthquakes within the supplied parameters.
  def get_target(self):
    return self.target
