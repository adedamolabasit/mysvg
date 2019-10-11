from math import sqrt,atan,cos,sin,degrees,tan,radians
print('YOU MUST NOT LEAVE ANY SPACE BLANK FILL IN ANY BLANK SPACES WITH (meaning none)')
class Computation1:
    def __init__(self,N1,E1,N2,E2,N3,E3,N4,E4,N5,E5,N6,E6):
        self.N1=N1
        self.N2=N2
        self.N3=N3
        self.N4=N4
        self.N5=N5
        self.N6=N6
        self.E1=E1
        self.E2=E2
        self.E3=E3
        self.E4=E4
        self.E5=E5
        self.E6=E6

    def bearing(self):
        print(f'bearing1={atan(self.E1/self.N1)}')
        print(f'BEARING2={atan(self.E2/self.N2)}')
        print(f'BEARING3={atan(self.E3/self.N3)}')
        print(f'BEARINGe={atan(self.E4/self.N4)}')
        print(f'BEARING5={atan(self.E5/self.N5)}')
        print(f'BEARING6={atan(self.E6/self.N6)}')


    def distance(self):
        print(f'distance1={sqrt(pow(self.N1,2))+pow(self.E1,2)}')
        print(f'distance2={sqrt(pow(self.N2,2))+pow(self.E2,2)}')
        print(f'distance3={sqrt(pow(self.N3,2))+pow(self.E3,2)}')
        print(f'distance4={sqrt(pow(self.N4,2))+pow(self.E4,2)}')
        print(f'distance5={sqrt(pow(self.N5,2))+pow(self.E5,2)}')
        print(f'distance6={sqrt(pow(self.N6,2))+pow(self.E6,2)}')

    def area(self):
        DA1=(self.N1*self.E2)+(self.N2*self.E3)+(self.N3*self.E4)+(self.N4*self.E5)+(self.N5*self.E6)
        DA2=(self.E1*self.N2)+(self.E2*self.N3)+(self.E3*self.N4)+(self.E4*self.N5)+(self.E5*self.N6)
        A=DA1-DA2
        print(A)

class Computation2:
    def __init__(self,N1,E1,brg1,dist1,brg2,dist2,brg3,dist3,brg4,dist4,brg5,dist5,brg6,dist6):
        self.brg1=degrees(brg1)
        self.brg2=degrees(brg2)
        self.brg3=degrees(brg3)
        self.brg4=degrees(brg4)
        self.brg5=degrees(brg5)
        self.brg6=degrees(brg6)
        self.dist1=dist1
        self.dist2=dist2
        self.dist3=dist3
        self.dist4=dist4
        self.dist5=dist5
        self.dist6=dist6
        self.N1=N1
        self.E1=E1

    def northings(self):
        N2=(self.N1)+self.dist1*(cos(self.brg1))
        N3=(self.dist2*(cos(self.brg2)))+N2
        N4=(self.dist3*(cos(self.brg3)))+N3
        N5=(self.dist4*(cos(self.brg4)))+N4
        N6=(self.dist5*(cos(self.brg5)))+N5
        print(f'(Northings1={self.N1}),(Northings2={N2}),(Northings3={N3}),(Northings4={N4}),(Northings5={N5}),(Northings6{N6})')

    def eastings(self):
        E2 = (self.E1) + self.dist1 * (cos(self.brg1))
        E3 = (self.dist2 * (cos(self.brg2))) + E2
        E4 = (self.dist3 * (cos(self.brg3))) + E3
        E5 = (self.dist4 * (cos(self.brg4))) + E4
        E6 = (self.dist5 * (cos(self.brg5))) + E5
        print(f'(Easthings1={self.E1}),(Easthings2={E2}),(Easthings3={E3}),(Easthings4={E4}),(Easthings5={E5}),(Easthings6{E6})')

class SimpleCurves:
    def __init__(self,Ang,Radius):
        self.Raduis=Radius
        self.Ang=Ang

    def tangentlenght(self):
        return (self.Raduis(tan(self.Ang/2)))

    def arclenght(self,lenght):
        self.lenght=lenght
        return self.Raduis*radians(self.Ang)

    def external_ang(self):
        return  self.radius((1/sin(self.Ang/2)-self.Raduis))



def Radius(D):
        c=5729.58/D
        return c

def verssine(Raduis,ang):
    v=Raduis-Raduis*cos(ang/2)
    print(v)


com=Computation1(450,470,320,390,490,410,520,415,5,42,55,55)
print(com.bearing(),com.distance(),com.area())
print(degrees(119))
a=Radius(6566)
print(a)