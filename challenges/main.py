def same_point(point1, point2):
    # TODO: return True if point1 and point2 represent the same location
    if point1 == (point2) and point2 == (point1):
        return True
    else:
        return False    

print(same_point((1, 2), (1, 2)))