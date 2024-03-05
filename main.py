import numpy as np

# Prison class
# Used to create the prison and manage all its functions, expecially to find loops
class Prison:

    def __init__(self, number):
        self.number = number
        self.prison_cells = self.create_prison_cells(number)
        #self.prison_cells = np.array([7,4,6,8,1,3,5,2])

    # Create Prison
    def create_prison_cells(self, number):
        base_array = np.arange(1, number+1,1,dtype=int)
        np.random.shuffle(base_array)
        return base_array
    # Finds loops
    # Returns true if it founds one, otherwise false
    def find_loops(self):
        loops = []
        for x in range(0,len(self.prison_cells)):
            loop = []
            steps = 0
            loop.append(x)
            next_number = self.prison_cells[x]
            loop.append(next_number)
            while (not next_number== x+1) and (not steps>= self.number/2):
                steps = steps+1
                next_number = self.prison_cells[next_number-1] 
                loop.append(next_number)
            if not steps>= self.number/2:
                #print(loop)
                loops.append(loop)
            else:
                #print(x, ":Not found;", loop)
                return False
        
        return True

    
    def print_prison(self):
        print(self.prison_cells)


# Function to get the probability to find loops
# Param: prision size
def test_prob(size):
    found_loop = 0
    for x in range(0,10000):
        print(x)
        prison = Prison(size)
        if prison.find_loops():
            found_loop = found_loop +1
    print(found_loop/10000)

if __name__ == "__main__":
    prison = Prison(100)
    prison.print_prison()
    prison.find_loops()

    test_prob(100)
