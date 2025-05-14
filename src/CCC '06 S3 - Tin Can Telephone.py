def gaussian_elimination(A, B):
    n = len(B)
    # Augmenting A with B to form the augmented matrix [A|B]
    augmented_matrix = [A[i] + [B[i]] for i in range(n)]

    # Forward Elimination
    for i in range(n):
        # Search for maximum in this column (pivoting)
        max_row = max(range(i, n), key=lambda r: abs(augmented_matrix[r][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        # Make the diagonal element 1 and eliminate the column below
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(i, n + 1):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Back Substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i][n] / augmented_matrix[i][i]
        for j in range(i - 1, -1, -1):
            augmented_matrix[j][n] -= augmented_matrix[j][i] * x[i]

    return x

def line_equation(x1, y1, x2, y2):
    # Calculate coefficients
    a = y2 - y1
    b = -(x2 - x1)
    c = -(a * x1 + b * y1)

    # Return the equation in ax + by + c = 0 form
    return [a,b,c]


def solve(a1,b1,c1,a2,b2,c2):
    if 0 in [a1,b1,a2,b2]:
        # print(1)
        if a1==b1==0 or a2==b2==0:
            return 'infinite'

        if a1 == 0 and a2 == 0:
            if c1 == c2:
                return 'infinite'
            else:
                return'none'
        if 0 in [a2,b2]:
            A = [[a1, b1], [a2, b2]]
            B = [c1 * -1, c2 * -1]
            # print(A, B)
            try:
                return gaussian_elimination(A, B)
            except:
                if c1/a1 == c2/a2:
                    return 'infinite'
                else:
                    return 'none'


    elif a1/b1 == a2/b2:
        if c1 ==0 and c2==0:
            return 'infinite'
        elif c1==0 or c2==0:
            return "none"
        elif a1/c1 == a2/c2:
            return 'infinite'
        else:
            return 'none'


    A = [[a1,b1],[a2,b2]]
    B =[c1*-1,c2*-1]
    # print(A,B)
    return gaussian_elimination(A, B)



def check_intersection(x1,y1,x2,y2):
    coef1 = line_equation(xr,yr,xj,yj)
    coef2 = line_equation(x1,y1,x2,y2)
    print(coef1,coef2)
    intersection = solve(coef1[0],coef1[1],coef1[2],coef2[0],coef2[1],coef2[2])
    # print(intersection)
    # print(intersection)
    if intersection=='infinite':
        if min(xr,xj)<=x1<=max(xr,xj) and min(yr,yj)<=y1<=max(yr,yj) or min(xr,xj)<=x2<=max(xr,xj) and min(yr,yj)<=y2<=max(yr,yj):
            return True
        else:
            return False
    elif intersection == 'none':
        return False
    elif min(xr,xj)<=intersection[0]<=max(xr,xj) and min(yj,yr)<=intersection[1]<=max(yr,yj) and min(x2,x1)<=intersection[0]<=max(x1,x2) and min(y2,y1)<=intersection[1]<=max(y1,y2):
        # print(xr,xj,yr,yj)
        return True
    else:
        return False

xr,yr,xj,yj = map(int,input().split())
counter = 0
for i in range(int(input())):
    inp = list(map(int,input().split()))
    corners = inp.pop(0)
    edges = []
    # print(inp)
    if len(inp) == 2:
        coef = line_equation(xr,yr,xj,yj)
        a,b,c,x,y = coef[0],coef[1],coef[2],inp[0],inp[1]
        if a*x+b*y+c==0:
            if min(xr, xj) <= inp[0] <= max(xr, xj) and min(yj, yr) <= inp[1] <= max(yr, yj):
                counter+=1
                continue

    else:
        for i in range(corners):
            edges.append((inp[(i*2)%(corners*2)],inp[(i*2+1)%(corners*2)],inp[(i*2+2)%(corners*2)],inp[(i*2+3)%(corners*2)]))

        for i in edges:
            if check_intersection(i[0],i[1],i[2],i[3]):
                # print(i)
                counter+=1
                break
print(counter)

