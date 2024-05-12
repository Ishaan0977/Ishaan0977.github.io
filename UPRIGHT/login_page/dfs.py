
def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
           

    start = (0, 0)
    end = (7, 6)

    path = dfs(maze, start, end)
    print(path)
    
    
    
def dfs(maze,start,end):
    
        