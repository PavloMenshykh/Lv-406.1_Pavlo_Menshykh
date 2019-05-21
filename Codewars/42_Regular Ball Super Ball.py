class Ball:
  
  def __init__(self, a=None):
      self.ball_type = "super"
      if a == None:
          self.ball_type = "regular"

#https://www.codewars.com/kata/53f0f358b9cb376eca001079
#Create a class Ball.
#Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
