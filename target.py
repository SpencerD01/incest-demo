class Target:
  def __init__(self, initial_position, velocity):
    self.position = initial_position
    self.velocity = velocity

  def update(self, time_step):
    self.position += self.velocity * time_step