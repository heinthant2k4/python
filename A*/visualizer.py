import pygame
from queue import PriorityQueue
import math
WIDTH = 800
window = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Visualizer")
#Just some colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)

#Node class to represent each spot in the grid
#We need to build the tool before implementing A* algorithm. This class is pretty vital for the program since it will contain everything related to start,end,barrier,node pos, neighbors, node color, drawing the node etc.
#Each node will be an object of this class. And we will have many methods to handle different operations. Operations like getters,setters and makers will be in here. Operations are get_pos() to get the pos of the node, is_barrier(),is_start(),is_end() to check the type of node, reset() to reset the node to default color, make_start(), make_end(), make_barrier() to set the type of node by changing color, make_open(), make_closed(), make_path() to change the color of the node during the algorithm execution, draw() to draw the node on the window, update_neighbors() to update the neighbors of the node based on the current grid.
class Node:
  def __init__(self,row,col,width,total_rows):
    self.row = row
    self.col = col
    self.x = col * width
    self.y = row * width
    self.color = WHITE
    self.neighbors = []
    self.width = width
    self.total_rows = total_rows
  
  #method to get position of the node
  def get_pos(self):
    return self.row, self.col

  #method to set a node as barrier
  def is_barrier(self):
    return self.color == BLACK
  
  #method to set a node as start node
  def is_start(self):
    return self.color == ORANGE
  
  #method to set a node as end node
  def is_end(self):
    return self.color == TURQUOISE
  
  #method to set a node to open node
  def is_open(self):
    return self.color == GREEN
  
  #method to set a node to closed node
  def is_closed(self):
    return self.color == RED
  
  #reset method
  def reset(self):
    self.color = WHITE

  #method to make a node as start node
  def make_start(self):
    self.color = ORANGE
  
  #method to make a node as end node
  def make_end(self):
    self.color = TURQUOISE
  
  #method to make a node as barrier
  def make_barrier(self):
    self.color = BLACK
  
  #method to make a node as open node
  def make_open(self):
    self.color = GREEN
  
  #method to make a node as closed node
  def make_closed(self):
    self.color = RED
  
  #method to make a node as path node
  def make_path(self):
    self.color = PURPLE
  
  #method to draw the node on the grid
  def draw(self,window):
    pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))#This draws a rectangle at (x,y) with width and height of width in the window with the color of the node.
  
  #method to update the neighbors of the node
  #This is a vital function, we should not think barriers as neighbors. Only up, down, left, right nodes are considered as neighbors if they are not barriers and within the grid bounds.
  #This works by checking each of the four possible directions (down, up, right, left) from the current node's position (self.row, self.col). For each direction, it checks if the new position is within the grid bounds and if the node at that position is not a barrier. If both conditions are met, it appends that neighbor node to the self.neighbors list.
  def update_neighbors(self,grid):
    self.neighbors = []
    #down
    #This checks if the row below the current node is within the grid bounds and if that node is not a barrier. If both conditions are met, it adds that node to the neighbors list.
    if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
      self.neighbors.append(grid[self.row + 1][self.col])
    #up
    #This checks if the row above the current node is within the grid bounds and if that node is not a barrier. If both conditions are met, it adds that node to the neighbors list.
    if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
      self.neighbors.append(grid[self.row - 1][self.col])
    #right
    #This checks if the column to the right of the current node is within the grid bounds and if that node is not a barrier. If both conditions are met, it adds that node to the neighbors list.
    if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
      self.neighbors.append(grid[self.row][self.col + 1])
    #left
    #This checks if the column to the left of the current node is within the grid bounds and if that node is not a barrier. If both conditions are met, it adds that node to the neighbors list.
    if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
      self.neighbors.append(grid[self.row][self.col - 1])

  #less than method for priority queue
  def __lt__(self,other):
    return False

#algo timeeee
#A* algorithm works with a formula f(n) = g(n) + h(n)
#f(n) = total cost of node n
#g(n) = cost from start node to n node
#We will first create an empty priority queue called open_set to store the nodes to be explored. We will also create a dictionary called came_from to keep track of the best path to reach each node. We will initialize two dictionaries g_score and f_score to store the cost from start to each node and the total cost for each node respectively. We will set the g_score of the start node to 0 and the f_score of the start node to the heuristic estimate from start to end.
def a_star_algorithm(draw,grid,start,end):
  count = 0
  open_set = PriorityQueue()
  open_set.put((0,count,start))
  # Bidirectional A* (practical speedup on grids). Replace single-source A* with two simultaneous A* searches
  # from start and end; when they meet we reconstruct the path.
  came_from = { }  # keep for compatibility if something else expects it, but we will use came_from_f / came_from_b
  came_from_f = {}
  came_from_b = {}
  count_f = 0
  count_b = 0
  open_f = PriorityQueue()
  open_b = PriorityQueue()
  open_f.put((0, count_f, start))
  open_b.put((0, count_b, end))

  g_f = {node: float("inf") for row in grid for node in row}
  g_b = {node: float("inf") for row in grid for node in row}
  g_f[start] = 0
  g_b[end] = 0

  f_f = {node: float("inf") for row in grid for node in row}
  f_b = {node: float("inf") for row in grid for node in row}
  f_f[start] = h(start.get_pos(), end.get_pos())
  f_b[end] = h(end.get_pos(), start.get_pos())

  open_f_hash = {start}
  open_b_hash = {end}
  closed_f = set()
  closed_b = set()

  def build_bidirectional_path(meet):
    # walk back from meet to start (forward came_from)
    reconstruct_path(came_from_f, meet, draw)
    # walk from meet to end (backward came_from)
    reconstruct_path(came_from_b, meet, draw)

  # Expand the side with smaller current f-value each step.
  while not open_f.empty() and not open_b.empty():
    # peek at fronts
    front_f = open_f.queue[0][0] if open_f.queue else float("inf")
    front_b = open_b.queue[0][0] if open_b.queue else float("inf")
    if front_f <= front_b:
      current = open_f.get()[2]
      open_f_hash.remove(current)
      closed_f.add(current)

      if current in closed_b:
        build_bidirectional_path(current)
        start.make_start()
        end.make_end()
        return True

      for neighbor in current.neighbors:
        if neighbor in closed_f:
          continue
        tentative_g = g_f[current] + 1
        if tentative_g < g_f[neighbor]:
          came_from_f[neighbor] = current
          g_f[neighbor] = tentative_g
          f_f[neighbor] = tentative_g + h(neighbor.get_pos(), end.get_pos())
          if neighbor not in open_f_hash:
            count_f += 1
            open_f.put((f_f[neighbor], count_f, neighbor))
            open_f_hash.add(neighbor)
            neighbor.make_open()
      draw()
      if current != start:
        current.make_closed()
    else:
      current = open_b.get()[2]
      open_b_hash.remove(current)
      closed_b.add(current)

      if current in closed_f:
        build_bidirectional_path(current)
        start.make_start()
        end.make_end()
        return True

      for neighbor in current.neighbors:
        if neighbor in closed_b:
          continue
        tentative_g = g_b[current] + 1
        if tentative_g < g_b[neighbor]:
          came_from_b[neighbor] = current
          g_b[neighbor] = tentative_g
          f_b[neighbor] = tentative_g + h(neighbor.get_pos(), start.get_pos())
          if neighbor not in open_b_hash:
            count_b += 1
            open_b.put((f_b[neighbor], count_b, neighbor))
            open_b_hash.add(neighbor)
            neighbor.make_open()
      draw()
      if current != end:
        current.make_closed()
  return False
  g_score = {node: float("inf") for row in grid for node in row}
  g_score[start] = 0
  f_score = {node: float("inf") for row in grid for node in row}
  f_score[start] = 0
  open_set_hash = {start}
  while not open_set.empty():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      current = open_set.get()[2]
      open_set_hash.remove(current)
      if current == end:
        reconstruct_path(came_from,end,draw)
        end.make_end()
        return True
      for neighbor in current.neighbors:
        temp_g_score = g_score[current] + 1
        if temp_g_score < g_score[neighbor]:
          came_from[neighbor] = current
          g_score[neighbor] = temp_g_score
          f_score[neighbor] = temp_g_score + h(neighbor.get_pos(),end.get_pos())
          if neighbor not in open_set_hash:
            count += 1
            open_set.put((f_score[neighbor],count,neighbor))
            open_set_hash.add(neighbor)
            neighbor.make_open()
      draw()
      if current != start:
        current.make_closed()
  return False

#recontruction func
def reconstruct_path(came_from,current,draw):
  while current in came_from:
    current = came_from[current]
    current.make_path()
    draw()

#h(n) implementation using Manhattan distance since this is a grid
def h(p1,p2):
  x1,y1 = p1
  x2,y2 = p2
  return abs(x2-x1) + abs(y2-y1)

#Lets build grids and draw grid spots
#Making a grid with rows and cols(width), returning a 2D list of node objects. We first create an empty list called grid. Then we calculate the gap which is the width of each rect spot by integer division of width by rows. Then we loop through each row and column to create a node object for each spot in the grid by appending each into the 2D grid.
def make_grid(rows,width):
  grid = []
  gap = width // rows #width of each rect spot
  for i in range(rows):
    grid.append([]) #creating 2D list
    for j in range(rows):
      node = Node(i,j,gap,rows)#creating node obj
      grid[i].append(node)#adding node obj to grid
  return grid

#Drawing grid
#Drawing the grid lines to separate each nodes. We iterate through the rows of the grid and draw each horizontal and vertical lines using pygame.draw.line() method.
def draw_grid(window,rows,width):
  gap = width // rows
  for i in range(rows):
    pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap)) #horizontal lines
  for j in range(rows):
    pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width)) #vertical lines

#Drawing the entire window
#We first fill the window with white color. Then we iterate through each node in the grid and call its draw() method to draw it on the window. Finally, we call draw_grid() to draw the grid lines and pygame.display.update() to update the display.
def draw(window,grid,rows,width):
  window.fill(WHITE)#initial is white
  for row in grid:
    for node in row:
      node.draw(window)
  draw_grid(window,rows,width)
  pygame.display.update()

#function to get clicked position in grid
def get_clicked_pos(pos,rows,width):
  gap = width // rows
  x, y = pos
  col = x // gap
  row = y // gap
  return row, col

def main(window,width):
  ROWS = 50
  grid = make_grid(ROWS,width)#creating a grid
  start = None
  end = None
  run = True
  while run:
    draw(window,grid,ROWS,width)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if pygame.mouse.get_pressed()[0]:#leftbtn
        pos = pygame.mouse.get_pos()
        row,col = get_clicked_pos(pos,ROWS,width)
        if 0 <= row < ROWS and 0 <= col < ROWS:
          node = grid[row][col]#accessing the node
          if not start and node != end:
            start = node  
            start.make_start()
          elif not end and node != start:
            end = node
            end.make_end()
          elif node != end and node != start:
            node.make_barrier()
      if pygame.mouse.get_pressed()[2]:#rightbtn
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos,ROWS,width)
        if 0 <= row < ROWS and 0 <= col < ROWS:
          node = grid[row][col]
          node.reset()
          if node == start:
            start = None
          elif node == end:
            end = None

      # start / keyboard events
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and start and end:
          for r in grid:
            for node in r:
              node.update_neighbors(grid)
          a_star_algorithm(lambda: draw(window,grid,ROWS,width),grid,start,end)
        if event.key == pygame.K_c:
          start = None
          end = None
          grid = make_grid(ROWS,width)
  pygame.quit()

main(window,WIDTH)
