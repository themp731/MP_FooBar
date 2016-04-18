from fractions import gcd
def answer(area):
	#[Ax(By-Cy) + Bx(Cy-Ay) + Cx(Ay-By)]*(1/2)
	#http://www.mathopenref.com/coordtrianglearea.html
	#tri1 = (area[0][0]-area[2][0])*(area[1][1]-area[0][1])
	#tri2 = (area[0][0]-area[1][0])*(area[2][1]-area[0][1])
	#triangle = 0.5*abs(tri1 - tri2)
	triangle = tri_area(area)

	#Get Boundy Points
	boundry_points = boundry(area)
	
	#Pick's Theorem
	#Area = Points + IntegersOnLine/2 - 1
	#Points = Area - IntegersOnLine/2 + 1
	#http://mathforum.org/library/drmath/view/54248.html
	#I would rather avoid Pick's theorem and use an intersection of rays
	#Iteration can carry over to other points not just integers on plane
	carrots = triangle - boundry_points/2 + 1
	print(carrots)
	return(carrots)

def tri_area(vs):
	tri_A = vs[0][0]*(vs[1][1]-vs[2][1])
	tri_B = vs[1][0]*(vs[2][1]-vs[0][1])
	tri_C = vs[2][0]*(vs[0][1]-vs[1][1])
	triangle = (abs(tri_A+tri_B+tri_C))/2
	return(triangle)

def boundry(vs):
	p1 = gcd(abs(vs[0][0]-vs[1][0]),abs(vs[0][1]-vs[1][1]))
	p2 = gcd(abs(vs[1][0]-vs[2][0]),abs(vs[1][1]-vs[2][1]))
	p3 = gcd(abs(vs[0][0]-vs[2][0]),abs(vs[0][1]-vs[2][1]))
	total = p1 + p2 +p3
	return(total)

answer([[2,3],[6,9],[10,160]])
answer([[91206,89566],[-88690,-83026],[67100,47194]])
