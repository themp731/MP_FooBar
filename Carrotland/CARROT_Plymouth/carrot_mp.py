from fractions import gcd
def answer(area):
	#[Ax(By-Cy) + Bx(Cy-Ay) + Cx(Ay-By)]*(1/2)
	#http://www.mathopenref.com/coordtrianglearea.html
	#tri1 = (area[0][0]-area[2][0])*(area[1][1]-area[0][1])
	#tri2 = (area[0][0]-area[1][0])*(area[2][1]-area[0][1])
	#triangle = 0.5*abs(tri1 - tri2)
	triangle = tri_area(area)

	#Get number of integer points
	int_a = gcd(abs(area[0][0]-area[1][0]),abs(area[0][1]-area[1][1])) 
	int_b = gcd(abs(area[1][0]-area[2][0]),abs(area[1][1]-area[2][1]))
	int_c = gcd(abs(area[2][0]-area[0][0]),abs(area[2][1]-area[0][1]))
	integers = int_a + int_c + int_c
	
	#Pick's Theorem
	#Area = Points + IntegersOnLine/2 - 1
	#Points = Area - IntegersOnLine/2 + 1
	#http://mathforum.org/library/drmath/view/54248.html
	#I would rather avoid Pick's theorem and use an intersection of rays
	#Iteration can carry over to other points not just integers on plane
	carrots = triangle - integers/2 + 1
	print(carrots)
	return(int(carrots))

def tri_area(vs):
	tri_A = vs[0][0]*(vs[1][1]-vs[2][1])
	tri_B = vs[1][0]*(vs[2][1]-vs[0][1])
	tri_C = vs[2][0]*(vs[0][1]-vs[1][1])
	triangle = (abs(tri_A+tri_B+tri_C))/2
	return(triangle)

def tri_area2(vs):
	xs = []
	ys = []
	for x in vs:
		xs.append(x[0])
	for y in vs:
		ys.append(y[1])
	ys.sort()
	xs.sort()	
	box = abs(xs[2]-xs[0])*abs(ys[2]-ys[0])
	#Triangle with longest base
	tri1 = (abs(xs[2]-xs[0])*abs(ys[1]-ys[0]))/2
	#Triangle with longest height
	tri2 = (abs(xs[2]-xs[1])*abs(ys[2]-ys[0]))/2
	#Small Triangle
	tri3 = (abs(xs[1]-xs[0])*abs(ys[2]-ys[1]))/2
	triangle = box - (tri1 + tri2 + tri3)
	print("area: %d" % triangle)
	return triangle

answer([[2,3],[6,9],[10,160]])
answer([[91206,89566],[-88690,-83026],[67100,47194]])