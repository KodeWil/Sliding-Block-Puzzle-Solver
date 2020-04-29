# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:21:41 2020

@author: William
"""
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            min = 999999
            for i in range(len(self.queue)): 
                if self.queue[i] < self.queue[min]: 
                    min = i 
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError: 
            print() 
            exit() 
    # for get the next element based on Priority        
    def get(self): 
        try: 
            min = 999999
            for i in range(len(self.queue)): 
                if self.queue[i] < self.queue[min]: 
                    min = i 
            item = self.queue[min]  
            return item 
        except IndexError: 
            print() 
            exit()
            
def heur(a,b):
    (x1, y1) = a
    (x2, y2) = b
    if(x1!=x2 and y1!=y2):
        return 1
    else:
        return 1.414
        
def lookOb(obArray,dot):
    for objs in obArray:
        if (objs==dot):
            return 1
    return 0
def neighborhood(dot,obs):
    neighbors = []
    [dotX,dotY] = dot
    ran = range(-1,2,1)
    for i in ran:
        for j in ran:
            if (i and j != 0):
                if (lookOb([dotX+i,dotY+j],obs) !=1):
                    neighbors.append([dotX+i,dotY+j])
                    
            
import numpy as np
xn = np.random.randint(0,80,15)
yn = np.random.randint(0,80,15)
points = []
for i in range(15):
  points.append([xn[i],yn[i]])

#A*
start = [0,5]
goal = [40,40]
neighbors = PriorityQueue()
neighbors.insert(start)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not neighbors.empty():
   current = neighbors.delete()

   if current == goal:
      break
   dotNeighbors =  neighborhood(current,points)
   
   for next in dotNeighbors:
       new_cost = cost_so_far[current] + heur(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + heuristic(goal, next)
         frontier.put(next, priority)
         came_from[next] = current
  
   
  




