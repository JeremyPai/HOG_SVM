def non_maximum_suppression(boxes, overlapThresh=0.3):

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Non-Maximum Suppression (Malisiewicz et al.)
        
        The only difference compared to Felzenszwalb's method
        is that the inner loop is eliminated to speed up the 
        algorithm.
    
        Return value
            boxes[pick]     Remaining bounding boxes
    
        Arguments
            boxes           Detection bounding boxes
            overlapThresh   Overlap threshold for suppression
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    # If there is no bounding box, then return an empty list
    if len(boxes) == 0:
        return []
        
    # Initialize the list of picked indexes
    pick = []
    
    # Coordinates of bounding boxes
    x1 = boxes[:,0].astype("float")
    y1 = boxes[:,1].astype("float")
    x2 = boxes[:,2].astype("float")
    y2 = boxes[:,3].astype("float")
    
    # Calculate the area of bounding boxes
    bound_area = (x2-x1+1) * (y2-y1+1)
    
    # Sort the bounding boxes by the bottom-right y-coordinate of the bounding box
    sort_index = np.argsort(y2)
    
    # Looping until nothing left in sort_index
    while sort_index.shape[0] > 0:
        # Get the last index of sort_index
        # i.e. the index of bounding box having the biggest y2
        last = sort_index.shape[0]-1
        i = sort_index[last]
        
        # Add the index to the pick list
        pick.append(i)
        
        # Compared to every bounding box in one sitting
        xx1 = np.maximum(x1[i], x1[sort_index[:last]])
        yy1 = np.maximum(y1[i], y1[sort_index[:last]])
        xx2 = np.minimum(x2[i], x2[sort_index[:last]])
        yy2 = np.minimum(y2[i], y2[sort_index[:last]])        

        # Calculate the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        # Compute the ratio of overlapping
        overlap = (w*h) / bound_area[sort_index[:last]]
        
        # Delete the bounding box with the ratio bigger than overlapThresh
        sort_index = np.delete(sort_index, 
                               np.concatenate(([last], np.where(overlap > overlapThresh)[0])))
        
    # return only the bounding boxes in pick list        
    return boxes[pick]
