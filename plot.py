from math import floor

from trigger import Trigger


plot_lib={
    22:([(5,1),(7,1)],[(4,4),(4,7),(4,10),(8,4),(8,7),(8,10)]),
    81:([(8,4),(10,4)],[(9,3)]),
    101:([],[(1,2),(9, 3),(9, 2), (8, 2),(2,2),(10,2),(1,3),(0,2)],[((6, 4), 'skeleton_trigger'), ((5, 0), 'skeleton_captain_trigger'), ((5, 5), 'skeleton_soldier_trigger'), ((4, 5), 'skeleton_trigger'), ((4, 4), 'skeleton_trigger'),  ((6, 3), 'skeleton_trigger'), ((5, 6), 'special_door') ,((4, 3), 'skeleton_trigger'), ((5, 2), 'special_door'), ((6, 5), 'skeleton_trigger'), ((5, 3), 'skeleton_soldier_trigger')]),
    102:([(4,3),(5,3),(6,3),(4,4),(4,5),(5,5),(6,5),(6,4)],[(5,2)]),
    103:([],[(3,3),(7,3),(5,6)],[((0,2),'red_gem'),((1,2),'red_gem'),((2,2),'red_gem'),((0,3),'blue_blood'),((1,3),'blue_blood'),((2,3),'blue_blood'),((8,2),'blue_gem'),((9,2),'blue_gem'),((10,2),'blue_gem'),((8,3),'yellow_key'),((9,3),'yellow_key'),((10,3),'yellow_key'),((5,10),'upstairs')]),
    111:([(0,4),(2,4)],[(1,3)]),
    144:([(0,0),(1,1),(2,0)],[(0,2)],[((0,2), 'red_key')]),
    151:([],[],[((5,8),'special_door')]),
    152:([(5,4)],[(5,8),(5,2)],[((5,3),'pickaxe')]),
    171:([(0,7),(2,7)],[(1,6)]),
    172:([(0,4),(2,4)],[(1,3)]),
    173:([(8,7),(10,7)],[(9,6)]),
    174:([(8,4),(10,4)],[(9,3)]),
    201:([],[(4,4),(4,5),(4,6),(5,4),(5,6),(6,4),(6,5),(6,6)],[((5,5), 'vampire_trigger'),((5,8),'special_door')]),
    202:([(5,5)],[(5,8),(5,2)],[((5,0),'upstairs'),((4,3),'yellow_key'),((5,3),'yellow_key'),((6,3),'yellow_key'),((3,4),'red_gem'),((3,5),'red_gem'),((3,6),'red_gem'),((7,4),'blue_gem'),((7,5),'blue_gem'),((7,6),'blue_gem'),((4,7),'blue_blood'),((5,7),'blue_blood'),((6,7),'blue_blood')]),
    301:([],[],[((5,3),'special_door'),((5,6),'special_door')]),
    302:([(2,4),(3,4),(4,4),(6,4),(7,4),(8,4)],[(5,3),(5,6)],[((5,0),'upstairs')]),
    321:(),
    322:([(0,9),(2,9)],[(1,8)]),
    331:([],[],[((9,3),'special_door'),((9,7),'special_door')]),
    332:([(8,4),(8,6),(10,4),(10,6)],[(9,3),(9,7)]),
    342:([(4,3),(6,3),(8,3),(10,3),(4,7),(6,7),(8,7),(10,7)],[],[((0, 4), 'yellow_key'),((2, 4), 'yellow_key'),((0, 6), 'yellow_key'),((2, 6), 'yellow_key'),((1, 5), 'red_key')]),
    381:([],[],[((1,4),'wall')]),
    382:([(0,9),(2,9)],[],[((1,8),'hidden_door')]),
    392:([(3,1),(5,3)],[],[((3,3),'red_key')])
          }
class Plot:
    def __init__(self,i,j,floor,case):
        self._i=i
        self._j=j
        self._floor=floor
        self._case=self._floor._num*10+case

        print(self.__dict__)
        self.run(self._case)
        
        
    def run(self,case):
        if isinstance(plot_lib[case], tuple):
            if self.detect(plot_lib[case][0]):
                for i,j in plot_lib[case][1]:
                    self._floor.del_floor(i,j)
                if len(plot_lib[case])>2:
                    for (i, j),item in plot_lib[case][2]:
                        self._floor.set_floor(i,j,item)

        
    def detect(self,positions):
        print('detecting!!!')
        return all([not isinstance(self._floor.get_floor(i,j),Trigger) for i,j in positions])
