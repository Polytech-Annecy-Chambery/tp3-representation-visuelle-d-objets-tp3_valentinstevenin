# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
            
        # Objects list
        self.objects = []

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color'],
                                      'position': self.parameters['position']})
        self.objects.append(self.parentSection) 
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self                 

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
    
    
    # Adds an object    
    def add(self, x):    
        # A compléter en remplaçant pass par votre code
        for x in self.objects:
            x.draw()        
                    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        self.vertices = [ 
                self.parameters['position'], 
                [self.parameters['position'][0],self.parameters['position'][1], self.parameters['position'][2]+self.parameters['height']], 
                [self.parameters['position'][0]+self.parameters['width'], self.parameters['position'][1], self.parameters['position'][2]+self.parameters['height']],
                [self.parameters['position'][0]+self.parameters['width'], self.parameters['position'][1],self.parameters['position'][2]],
                [self.parameters['position'][0],self.parameters['position'][1]+self.parameters['thickness'], self.parameters['position'][2]],
                [self.parameters['position'][0]+self.parameters['width'],self.parameters['position'][1]+self.parameters['thickness'],self.parameters['position'][2]],
                [self.parameters['position'][0]+self.parameters['width'], self.parameters['position'][1]+self.parameters['thickness'], self.parameters['position'][2]+self.parameters['height']],
                [self.parameters['position'][0],self.parameters['position'][1]+self.parameters['thickness'], self.parameters['position'][2]+self.parameters['height']],

                # Définir ici les sommets
                ]
        
        for i in range(len(self.vertices)-1):
            for j in range(i):
                a=0.4
                gl.glPushMatrix()
                gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)
                gl.glBegin(gl.GL_QUADS)# Tracé d’une ligne
                gl.glColor3fv([0.5*a, 0.5*a, 0.5*a]) # Couleur gris moyen
                gl.glVertex3fv(self.vertices[j])
                gl.glEnd()
                gl.glPopMatrix()
                
                
        
        
        
    
  