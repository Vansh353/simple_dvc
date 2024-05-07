import pytest
class NotinRange(Exception):
    def __init__(self,message="value not in range"):
        self.message=message
        super().__init__(self.message)
        
        

def test_genric():
    a=21
    with pytest.raises(NotinRange):
        if a not in range(1,20):
            raise NotinRange
       
