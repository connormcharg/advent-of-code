import sys

def solve():
    # Parse Input
    try:
        input_data = sys.stdin.read().splitlines()
    except Exception:
        return

    points = []
    for line in input_data:
        if not line.strip():
            continue
        parts = line.split(',')
        points.append((int(parts[0]), int(parts[1])))

    if not points:
        return

    N = len(points)
    
    # Precompute polygon edges
    # Each edge is ((x1, y1), (x2, y2))
    edges = []
    for i in range(N):
        p1 = points[i]
        p2 = points[(i + 1) % N]
        edges.append((p1, p2))

    # Generate all candidate rectangles
    # Stored as (Area, index1, index2)
    candidates = []
    for i in range(N):
        for j in range(i + 1, N):
            p1 = points[i]
            p2 = points[j]
            
            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            area = w * h
            candidates.append((area, i, j))

    # Sort by Area Descending to find the largest valid one first
    candidates.sort(key=lambda x: x[0], reverse=True)

    # Helper function for Point-in-Polygon (Ray Casting)
    def is_inside_or_on_boundary(cx, cy):
        # 1. Check if strictly on an edge (Boundary)
        for (ex1, ey1), (ex2, ey2) in edges:
            if ex1 == ex2: # Vertical edge
                if ex1 == cx and min(ey1, ey2) <= cy <= max(ey1, ey2):
                    return True
            else: # Horizontal edge
                if ey1 == cy and min(ex1, ex2) <= cx <= max(ex1, ex2):
                    return True

        # 2. Ray Casting (Ray to the right)
        inside = False
        for (ex1, ey1), (ex2, ey2) in edges:
            # Check if edge intersects the horizontal ray from (cx, cy)
            # Use strict inequalities for y to avoid double-counting vertices
            if (ey1 > cy) != (ey2 > cy):
                # Calculate x-coordinate of intersection
                intersect_x = (ex2 - ex1) * (cy - ey1) / (ey2 - ey1) + ex1
                if cx < intersect_x:
                    inside = not inside
        return inside

    for area, i, j in candidates:
        p1 = points[i]
        p2 = points[j]
        
        rx_min = min(p1[0], p2[0])
        rx_max = max(p1[0], p2[0])
        ry_min = min(p1[1], p2[1])
        ry_max = max(p1[1], p2[1])

        # --- CHECK 1: No Polygon Vertex Strictly Inside ---
        # If a vertex is inside, the polygon folds into the rectangle.
        vertex_fail = False
        for k in range(N):
            if k == i or k == j: continue
            px, py = points[k]
            if rx_min < px < rx_max and ry_min < py < ry_max:
                vertex_fail = True
                break
        if vertex_fail:
            continue

        # --- CHECK 2: No Polygon Edge Strictly Crosses ---
        # If an edge passes completely through the rectangle, it splits it into In/Out.
        # This catches the case (2,5) <-> (7,1) in the example.
        edge_fail = False
        for (ex1, ey1), (ex2, ey2) in edges:
            # Check Vertical Edge Crossing
            if ex1 == ex2: 
                # Edge x is strictly between rect x bounds
                if rx_min < ex1 < rx_max:
                    # Edge covers the entire height of the rectangle
                    if min(ey1, ey2) <= ry_min and max(ey1, ey2) >= ry_max:
                        edge_fail = True
                        break
            
            # Check Horizontal Edge Crossing
            else:
                # Edge y is strictly between rect y bounds
                if ry_min < ey1 < ry_max:
                    # Edge covers the entire width of the rectangle
                    if min(ex1, ex2) <= rx_min and max(ex1, ex2) >= rx_max:
                        edge_fail = True
                        break
        
        if edge_fail:
            continue

        # --- CHECK 3: Center Point is Inside/On Boundary ---
        # Ensures we didn't pick a rectangle in the "hole" of a shape
        mid_x = (rx_min + rx_max) / 2
        mid_y = (ry_min + ry_max) / 2
        
        if is_inside_or_on_boundary(mid_x, mid_y):
            print(area)
            return

if __name__ == "__main__":
    solve()