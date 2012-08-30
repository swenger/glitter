import numpy as np
from math import cos, sin, acos

class Quaternion:

  # Create rotational quaternion to represent a rotation around the axis given by the first parameter and
  #  the angle given by the second. (angle: 2Pi = 360)
  def __init__(self):
    self.vals = np.zeros((4,),dtype=np.double)

  @staticmethod
  def make_from_axis_angle(axis, angle, angle_in_degree=False):
    if angle_in_degree:
      angle = angle * 2 * np.pi / 360.
    q = Quaternion()
    axis = np.array(axis) / np.linalg.norm(axis)
    q.vals = np.array([cos(angle / 2), axis[0] * sin(angle / 2), axis[1] * sin(angle / 2), axis[2] * sin(angle / 2)], dtype=np.double)
    return q
    
  @staticmethod
  def make_from_position(position):
    q = Quaternion()
    q.vals[1:] = position
    return q

  @staticmethod
  def make_from_wxyz(w,x,y,z):
    q = Quaternion()
    q.vals = np.array([w,x,y,z], dtype=np.double)
    return q

  def __str__(self):
    return self.vals.__str__()

  #Quaternion multiplication is _NOT_ commutative!
  def __mul__(self, other):
    return Quaternion.make_from_wxyz(
    self.vals[0] * other.vals[0] - self.vals[1] * other.vals[1] - self.vals[2] * other.vals[2] - self.vals[3] * other.vals[3],
    self.vals[0] * other.vals[1] + self.vals[1] * other.vals[0] + self.vals[2] * other.vals[3] - self.vals[3] * other.vals[2],
    self.vals[0] * other.vals[2] - self.vals[1] * other.vals[3] + self.vals[2] * other.vals[0] + self.vals[3] * other.vals[1],
    self.vals[0] * other.vals[3] + self.vals[1] * other.vals[2] - self.vals[2] * other.vals[1] + self.vals[3] * other.vals[0])

  def __imul__(self, other):
    self.vals = self.__mul__(other)
    

  def angle(self):
    return 2 * acos(self.vals[0])

  def angle_degree(self):
    return 2 * acos(self.vals[0]) * 360 / 2. / np.pi

  def axis(self):
    denom = np.dot(self.vals[1:4], self.vals[1:4])
    return self.vals[1:4] / denom

  def conjugate(self):
    q = Quaternion()
    q.vals = self.vals * [1, -1, -1, -1]
    return q
        
  def rotate(self, vector):
    p = Quaternion.make_from_position(vector[:3])
    q1 = self * p
    q2 = q1 * self.conjugate()
    return q2.vals[1:]

  def normalize(self):
    denom = np.linalg.norm(self.vals)
    self.vals /= denom
    
  #TODO: Convert this:
  #Quaternion interpolate(Quaternion qb, double t) {
  #  Quaternion qa = *this;
  #  Quaternion qm(0,0,0,0);
  #  // Calculate angle between them.
  #  double cosHalfTheta = qa.mW * qb.mW + qa.mX * qb.mX + qa.mY * qb.mY + qa.mZ * qb.mZ;
  #  // if qa=qb or qa=-qb then theta = 0 and we can return qa
  #  if (abs(cosHalfTheta) >= 1.0){
  #    qm.mW = qa.mW;qm.mX = qa.mX;qm.mY = qa.mY;qm.mZ = qa.mZ;
  #    return qm;
  #  }
  #  // Calculate temporary values.
  #  double halfTheta = acos(cosHalfTheta);
  #  double sinHalfTheta = sqrt(1.0 - cosHalfTheta*cosHalfTheta);
  #  // if theta = 180 degrees then result is not fully defined
  #  // we could rotate around any axis normal to qa or qb
  #  if (fabs(sinHalfTheta) < 0.001){ // fabs is floating point absolute
  #    qm.mW = (qa.mW * 0.5 + qb.mW * 0.5);
  #    qm.mX = (qa.mX * 0.5 + qb.mX * 0.5);
  #    qm.mY = (qa.mY * 0.5 + qb.mY * 0.5);
  #    qm.mZ = (qa.mZ * 0.5 + qb.mZ * 0.5);
  #    return qm;
  #  }
  #  double ratioA = sin((1 - t) * halfTheta) / sinHalfTheta;
  #  double ratioB = sin(t * halfTheta) / sinHalfTheta; 
  #  //calculate Quaternion.
  #  qm.mW = (qa.mW * ratioA + qb.mW * ratioB);
  #  qm.mX = (qa.mX * ratioA + qb.mX * ratioB);
  #  qm.mY = (qa.mY * ratioA + qb.mY * ratioB);
  #  qm.mZ = (qa.mZ * ratioA + qb.mZ * ratioB);
  #  return qm;
  #}

if __name__ == "__main__":
  q = Quaternion()
  assert((q.vals == [0, 0, 0, 0]).all())
  q2 = Quaternion.make_from_position([4,5,6])
  assert((q2.vals == [0, 4, 5, 6]).all())
  q3 = Quaternion.make_from_wxyz(10,1,3,5)
  assert((q3.vals == [10,1,3,5]).all())

  q = Quaternion.make_from_wxyz(1,2,3,4)
  assert((q.conjugate().vals == [1,-2,-3,-4]).all())

  q  = Quaternion.make_from_axis_angle(axis=[1,0,0], angle=90, angle_in_degree=True)
  p = [0,1,0]
  assert((np.round(q.rotate(p), decimals=2) == [0.00, 0.00, 1.00]).all())
  assert((np.round((q * q).rotate(p), decimals=2) == [0.00, -1.00, 0.00]).all())
  assert((np.round((q * q * q).rotate(p), decimals=2) == [0.00, 0.00,-1.00]).all())
  assert((np.round((q * q * q * q).rotate(p), decimals=2) == [0.00, 1.00, 0.00]).all())

  q  = Quaternion.make_from_axis_angle(axis=[0.1,0.2,4], angle=79, angle_in_degree=True)
  assert(abs(q.angle_degree() - 79) < 0.01)
  q  = Quaternion.make_from_axis_angle(axis=[0,0,1], angle=90, angle_in_degree=True)
  assert(abs(q.angle() - np.pi / 2) < 0.01)

  q = Quaternion.make_from_wxyz(7,8,9,10)
  q.normalize()
  assert((np.round(q.vals, decimals=3) == [ 0.408,  0.467,  0.525,  0.583]).all())



