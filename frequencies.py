"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
 if not items:
   return{}
 frequencies = {}
 for item in items:
  item_str = str(item)  
  if item_str in frequencies:
     frequencies[item_str] += 1
  else:
     frequencies[item_str] = 1
      
 return frequencies

