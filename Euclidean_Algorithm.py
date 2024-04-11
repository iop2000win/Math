# 유클리드 호제법
'''
두 수, A와 B가 있을 때 (A > B)
A와 B의 최대 공약수는, A를 B로 나눈 나머지와 B의 최대 공약수와 같다.

즉 A%B = r일 경우,
(A, B) = (B, r) <- ()는 최대 공약수를 의미하는 임의의 기호
'''

def euclidean_algorithm(a, b):
	if b > a:
		a, b = b, a

	if b == 0:
		'''
		0의 최대 공약수는 어떻게 될까?
		0은 어떤 수와 곱해도 0이 되기 때문에 0의 약수는 정의상 모든 정수가 된다.
		따라서 0과의 최대 공약수는 자기 자신이 된다.
		'''
		return b

	if a % b == 0:
		'''
		나누어 떨어지는 수라면 최대 공약수는 작은 수 자체이다.
		'''
		return b

	else:
		euclidean_algorithm(b, a%b)
  

# 최대공약수와 최소공배수의 관계
def lcm(a, b):
    
    return (a * b) / euclidean_algorithm(a, b)

# 파이썬의 경우 math 패키지를 통해 쉽게 구할 수 있다.
import math
gcd_ = math.gcd(a, b) # Greatest Common Measure
lcm_ = math.lcm(a, b) # Least Common Multiple