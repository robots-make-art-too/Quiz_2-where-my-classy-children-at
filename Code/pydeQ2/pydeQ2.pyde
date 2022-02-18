# Quiz 2 - PUT YOUR NAME HERE -- AND BE SURE TO ERASE ALL MY EXTRA COMMENTS WHEN YOU SUBMIT - INCLUDE __ONLY__ YOUR OWN, AND ONLY IF THEY ARE RELEVANT (or hilarious)

###
# what do we need for our concept?
# we list 4 main components: variables, setup, interactivity(? it could be our robot flare?), the class ClassyRobot(object):
###

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# THE VARIABLES
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 1. My variables, and what I need them to do:
#
# a way to count the robots
numRobots # = ?;

# a way to store the robots
robots = [0]*numRobots;

# a way to keep track of which robots
currentRobot = 0; # arrays start at a value of 0 so we will too

# a way to change the robot's flare?
# do they have colour?
# colour = None;
# do they have sound?
# what else? (we know they have shapes!)

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# THE STANDARD SETUP, DRAW
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 2. how to setup: setup(), draw() - like always
def setup():
  size(600,600); # bigger? smaller?
  smooth();
  global numRobots, robots;

  for i in range(numRobots):
    colour = color(random(255), random(255), random(255)); # I don't think the robots want to cycle through random colours though
    robots[i] = ClassyRobot(0, 0, 0, False, 'abcdef', ...); # Create each object with initial parameters (but how many are there?)

def draw():
  global numRobots, robots;
  background(251,128,114); # that pinkish background colour
  # hmm.. what *is* a good photo colour for the background of a robot family photo?
  # or did you want to take it outside? infront of a tree?

  for i in range(numRobots):
    # so we check for each robot object that could possibly exist
    # and this is why we scan the whole array from 0 to numRobots
    # at each element of the array we check if there are any conditions
    # or attributes
    # robots[i].?? # maybe you defined some other conditions in your class ClassyRobot()
    robots[i].display(); # the draw conditions _I_ defined in class ClassyRobot()

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# FLARE? INTERACTION? SAVING A PICTURE?
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 3a. do you want some interactivity?
# I'm not sure you'll want to use anything like this function but maybe you find it interesting?
def mousePressed():
  global ?;
  robots[currentRobot].gogogadget(mouseX, mouseY); # gogogadget is an activation _I_ defined in class ClassyRobot(object)
  currentRobot += 1;
  if (currentRobot >= numRobots):
    currentRobot = 0;

# 3b. do we need to save a file?
def save():
  global ?;
  with open('myfile.txt', 'w+') as textFile:
    textFile.write("\nThe robot name is : " + robot.name) # ? how are you storing the robot's attributes?
    textFile.write("\nThe profile_use_background_image is : " + str(robot.profile_use_background_image)) # do you need a str(ing)?
    # maybe you should make a list of the attributes you should keep track of first, then build the class...?

# what about just print to screen? Is there a way to do that _encapsulated_ into the class ClassyRobot()? hmmm ....
robot.name = 'shh' # I am just a placeholder
print('My name is: ' + robot.name);

#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
# THE CLASS
#----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

# 4. OOP setup for a python class
class ClassyRobot(object...):
  # we need to ask ourselve: what attributes, or characteristics do we want our robots to have?

  # 4a. initialize -> think of me as a 1-to-1 with def setup()
  # I am needed for an instance of class to exist ( I self, therefore I am )
  def __init__(self, param, param, shbam, ...):
    self.param = param;
    ...;

  # 4b. an example of giving a class some activation
  # gogogadget -> think of me as a 1-to-1 with the interaction - def mousePressed()
  def gogogadget(self, xpos, ypos):
    self.x = xpos;
    self.y = ypos;
    self.? = ?;
    ...

  # 4c. display -> think of me as a 1-to-1 with def draw():
  # I do need that family photo afterall...
  def display(self):
    if (self.on == True):
      noFill();
      strokeWeight(4);
      stroke(self.colour); #stroke(255, 153)
      ellipse(self.x, self.y, self.diameter, self.diameter);

  # 4d. assigning some flare?
  # randomly? specifically? inherited?
  # are we passing in any parameters?

  #def gimmeFlare(self, flare):
    #self.flare = flare; # you can use this method or try another way if you want to use this

  # did you want to add sound? try it here and follow the pattern from Week 04
  # maybe you want to initialize something in def __init__(): ?
  def sound():
    pass # place holder until you think of something to add or not
