import random

class Target:
  def __init__(self, initial_position, velocity, process_variance, measurement_variance, seed=None):
    if seed is not None:
      random.seed(seed)
    self.position = initial_position
    self.velocity = velocity
    self.process_stdev = process_variance ** 0.5
    self.measurement_stderv = measurement_variance ** 0.5

  def update(self, time_step):
    self.position += self.velocity * time_step + random.gauss(sigma=self.process_stdev)

  def get_position(self):
    return self.position

  def get_measurement(self):
    return self.position + random.gauss(sigma=self.measurement_stderv)