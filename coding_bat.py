#warm_up_1
def sleep_in(weekday, vacation):
	return not weekday or vacation

#warm_up_2
def monkey_trouble(a_smile, b_smile):
    return not(a_smile^b_smile)

#warm_up_3
def sum_double(a, b):
	if (a==b): return 2*(a+b)
	else: return (a+b)

#warm_up_4
def diff21(n):
	if n < 21: return (21 - n)
	else: return (2*(n - 21))

#warm_up_5
def parrot_trouble(talking, hour):
	return talking and ( hour < 7 or hour > 20)

#warm_up_6
def makes10(a, b):
	return (a==10 or b==10 or a+b==10)

#warm_up_7
def near_hundred(n):
	return abs(100-n)<=10 or abs(200-n)<=10

#warm_up_8
def pos_neg(a, b, negative):
	return (negative and a<0 and b<0) or (not negative and (a<0)^(b<0))

'''
#another "easy to read" way to 8
#    if negative and a<0 and b<0 :
#        return True
#    elif not negative and ((a<0 and b>0) or (a>0 and b<0)):
#        return True
#    else:
#        return False
'''

#warm_up_9
def not_string(str):
	if str[:3]=='not': return str
	else: return 'not '+str

#warm_up_10
def missing_char(str, n):
	assert(len(str)>0 and n<len(str))
	return str[:n]+str[n+1:]

#warm_up_11
def front_back(str):
    if len(str)<=1: return str
    else: return str[-1]+str[1:-1]+str[0]

#warm_up_12
def front3(str):
  return str[:3]*3

'''
#should assert len(str)>0
#another solution
#if len(str)<3: return str*3
#else: return str[:3]*3
'''

#warm_up_13
def string_times(str, n):
    return str*n

#warm_up_14
def front_times(str, n):
     return str[:3]*n

'''
#should assert n is +ve, len(str)>0
'''

#warm_up_15
def string_bits(str):
	res=''
	for ind in xrange(0,len(str),2):
		res+=str[ind]
	return res

#warm_up_16
def string_splosion(str):
	res=''
	for ind in xrange(len(str)+1):
		res+=str[:ind]
	return res

#warm_up_17
def last2(str):
	if len(str)<=2: return 0
	else:
		c=0
		for ind in xrange(len(str)-2):
			if str[ind:ind+2]==str[-2:]: c+=1
	return c

#warm_up_18
def array_count9(nums):
	return nums.count(9)

#warm_up_19
def array_front9(nums):
	return nums[0:4].count(9)>0

#war_up_20
def array123(nums):
	return (1 in nums) and (2 in nums) and (3 in nums)

'''
#another solution
#    for i in range(len(nums)-2):
#        if [1,2,3] == nums[i:i+3]: return True
#    return False
'''

#warm_up_21
def string_match(a, b):
	c=0
	l = min(len(a),len(b))
	for i in xrange(l-1):
		if a[i:i+2] == b[i:i+2]:
			c+=1
	return c

#----------------------------------------- sting ------------------------------------------


#string_1
def hello_name(name):
	return 'Hello '+name+'!'

#string_2
def make_abba(a, b):
	return a+b*2+a

#string_3
def make_tags(a,b):
	return '<%s>%s</%s>'%(a,b,a)

#string_4
def make_out_word(a,b):
	return '%s%s%s'%(a[0:2],b,a[2:])

#string_5
def extra_end(str):
	return str[-2:]*3

#string_6
def first_two(str):
	if len(str)<2: return str
	else: return str[:2]

#string_7
def first_half(str):
	return str[:len(str)/2]

#string_8
def without_end(str):
	return str[1:-1]

#string_9
def combo_string(a, b):
	if len(a) < len(b): return a+b+a
	elif len(b) < len(a): return b+a+b

#string_10
def non_start(a, b):
	return a[1:]+b[1:]

#string_11
def left2(str):
	return str[2:]+str[:2]

#string_12 ---- string_2_start
def double_char(str):
	return ''.join(''.join(i) for i in zip(str,str))

'''
another solution:
	res=''
	for i in str:
		res+= 2*i
	return res
'''

#string_13
def count_hi(str):
	return str.count('hi')

'''
c=0
	for i in xrange(len(str)):
		if str[i:i+2]=='hi': c+=1
	return c
'''

#string_14
def cat_dog(str):
	return str.count('cat')==str.count('dog')

#string_15
def count_code(str):
	c=0
	for i in xrange(len(str)-3):
		if str[i:i+2]=='co' and str[i+3]=='e': c+=1
	return c

'''
import re
def count_code(str):
	return len(re.findall('co[a-z]e',str))
'''

#string_16
def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

'''
def end_other(a, b):
	l=min(len(a),len(b))
	return a.lower()==b.lower()[-l:] or a.lower()[-l:]==b.lower()
'''

#string_17
def xyz_there(str):
	for i in xrange(len(str)-2):
		if str[i-1]!= '.' and str[i:i+3]=='xyz': return True
	else: return False


#------------------------------------------------ list ----------------------------------------

#list_1
def first_last6(nums):
	return nums[0]==6 or nums[-1]==6

#list_2
def same_first_last(nums):
	return len(nums)>=1 and nums[0]==nums[-1]

#list_3
def make_pi():
	return [3,1,4]

#list_4
def common_end(a, b):
	return a[0]==b[0] or a[-1]==b[-1]

#list_5
def sum3(nums):
	return sum(nums)

'''
another sol:
retun sum[i for i in nums]

or

ttl=0
for i in nums: ttl+= i
return ttl

'''

#list_6
def rotate_left3(nums):
	return nums[1:]+[nums[0]]

#list_7
def reverse3(nums):
	nums.reverse(); return nums

#list_8
def max_end3(nums):
	return [max(nums[0],nums[-1]) for i in nums]

'''
another solution
a=max(nums[0],nums[-1])
for i in xrange(len(nums)): nums[i]=a
return nums

'''

#list_9
def sum2(nums):
	return sum(nums[:2])

#list_10
def middle_way(a, b):
	return [a[len(a)/2],b[len(b)/2]]

#list_11
def make_ends(nums):
	return [nums[0],nums[-1]]

#list_12
def has23(nums):
	return (2 in nums) or (3 in nums)

#list_13 ----- lists_2_start
def count_evens(nums):
	c=0
	for i in nums:
		if not i%2: c+=1
	return c

#list_14
def big_diff(nums):
	return max(nums)-min(nums)

'''
def big_diff(nums):
	mini=None;maxi=None
	for i in nums:
		if mini is None or maxi is None: mini=maxi=i
		else:
			if i<mini: mini = i
			if i>maxi: maxi = i
	return maxi-mini
'''

#list_15
def centered_average(nums):
	a=min(nums);b=max(nums)
	nums.remove(a);nums.remove(b)
	return sum(nums)/len(nums)

#list_16
def sum13(nums):
	if len(nums)<1: return 0
	elif 13 not in nums: return sum(nums)
	else:
		s=0
		for i in xrange(1,len(nums)):
			if nums[i-1]==13 or nums[i]==13: continue
			else: s+= nums[i]
		if nums[0]!=13: s+= nums[0]
	return s

#list_17
def sum67(nums):
	if len(nums)<1: return 0
	elif 6 not in nums: return sum(nums)
	else:
		s=0;six=0
		for i in xrange(len(nums)):
		if nums[i]==6: six=1; continue
		elif nums[i]==7 and six==1: six=0;s-=7
		if not six: s+= nums[i]
	return s

#list_18
def has22(nums):
	for i in xrange(len(nums)-1):
		if nums[i]== nums[i+1]==2: return True
	return False

#--------------------------------------------Logic -------------------------------------------------

#logic_1
def cigar_party(cigars, is_weekend):
	return (is_weekend and cigars>=40) or (not is_weekend and((cigars>=40) and(cigars<=60)))
'''
another solution
	if not is_weekend:
		return cigars>=40 and cigars<=60
	else:
		return cigars>=40
'''

#logic_2
def date_fashion(you, date):
	if (you>=2 or date>=2): return 0
	elif (you >=8 or date>=8): return 2
	else: return 1

#logic_3
def squirrel_play(temp, is_summer):
	return (is_summer and(temp>=60 and temp<=100))or(not is_summer and(temp>=60 and temp<=90))

#logic_4
def caught_speeding(speed, is_birthday):
	if not is_birthday:
		if speed<=60: return 0
		elif speed>80: return 2
		else: return 1
	else:
		if speed<=65: return 0
		elif speed>85: return 2
		else: return 1

#logic_5
def sorta_sum(a, b):
	if a+b<10 or a+b>20: return a+b
	else: return 20

#logic_6
def alarm_clock(day, vacation):
	if vacation:
		if not day or day==6: return 'off'
		else: return '10:00'
	else:
		if not day or day==6: return '10:00'
		else: return '7:00'

#logic_7
def love6(a, b):
	return (a == 6 or b == 6) or (a+b == 6) or (abs(a-b)== 6)

#logic_8
def in1to10(n, outside_mode):
	return (outside_mode and(n<=1 or n>=10))or(not outside_mode and (n>=1 and n<=10))

#logic_9
def near_ten(num):
	return num%10 <=2 or num%10>=8

#logic_10 ---- logic_2_start
def make_bricks(small, big, goal):
	return (goal/5 <= big and goal%5<= small) or ( goal/5>big and goal-5*big <= small)

'''
	if (goal/5 <= big) and (goal%5 <= small): return True
	elif (goal/5 > big and (goal-5*big)<=small): return True
	else: return False
'''

#logic_11
def lone_sum(a, b, c):
	if a==b==c: return 0
	if b==c: return a
	elif a==b: return c
	elif a==c: return b
	else: return sum((a,b,c))

#logic_12
def lucky_sum(a, b, c):
	if 13 in [a,b,c]: return sum([a,b,c][:[a,b,c].index(13)])
	else: return sum((a,b,c))

'''
#	if a==13: return c
#	elif b== 13: return a
#	elif c==13: return a+b
#	else: return sum((a,b,c))
'''

#logic_13
def no_teen_sum(a, b, c):
	return sum([fix_teen(i) for i in [a,b,c]])

def fix_teen(n):
	if n==15 or n==16: return n
	elif n>=13 and n<=19: return 0
	else: return n

#logic_14
def round_sum(a, b, c):
	return sum(round10(i) for i in [a,b,c])

def round10(n):
	if n%10<5: return n-(n%10)
	else: return (10-(n%10))+n

#logic_15
f close_far(a, b, c):
	return (abs(a-b)<=1 and (abs(a-c)>=2 and abs(b-c)>=2)) or\
	(abs(a-c)<=1 and (abs(a-b)>=2 and abs(b-c)>=2))

#logic_16
def make_chocolate(small, big, goal):
	if (goal/5 <= big) and (goal%5 <= small): return goal%5
	elif (goal/5 > big) and (goal-5*big <=small): return goal-5*big
	else: return -1

