import pytest
class NotinRange(Exception):
    def __init__(self,message="value not in range"):
        self.message=message
        super().__init__(self.message)
        
        
 
