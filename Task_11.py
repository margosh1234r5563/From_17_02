a = int(input())
b = int(input())
c = int(input())
import math

angle_A = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * 180 / math.pi
angle_B = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * 180 / math.pi
angle_C = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * c * b)) * 180 / math.pi

print(angle_A, angle_B, angle_C)
