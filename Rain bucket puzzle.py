import math
import unittest





class hh():

	#this little section stores global values used in this program.

	# global values end.

	"""This class contains code nessicary to implement the conditional output function, p.
		The syntax of the function is as follows:    h.p("groupValue","message","data")
		grouping value indicates group of different messages, group output for individual groups can be
		enabled/disabled in the currentTest list, by appending/removing a one from the name of each group.

		message describes the meaning or name of the data passed. For formatting purposes, the groupvalue can be set to whitespace
		by adding a ^ character at the start of the data field. Upon printing, this chacter is removed from the datafield. This group-nullification
		allows users to create empty print statements which have formatting characters such as the newline character, or possibly titles/descriptions of
		output sets.

		All output is printed upon calling the h.d() function. This output is formatted so that each group message is sorted into sections.


	"""

	def __init__(self):

		self.currentTest=["test1","checkAmt1","main1"]
				#remove the 1 from groups you wish to test.  When done testing a section, add a one to the string to disable it. keep groupingValue names descriptive.

				#Items will be printed according to how they are ordered in the currentTest list. The first item is printed first.

		self.output=[]

	def d(self):
		"""Since group output is stored in an alternating manner, i.e. (group1, group2,group3,group1,none,group3),
			This function runs a counter which increments the starting position of each group, and then prints out all input
			on indexes incremented by (len(currentTest)). Either encountering None, or an invalid position will reset the inner while loop.
			The outer while loop is terminated when an invalid group starting position is reached.

		  """

		#print ALL function.

		startPos=0

		while(True):
			x=startPos
			while(True):
				if(x>len(self.output)-1):
					break
				if(self.output[x]==None):
					break


				print(self.output[x])

				x+=len(self.currentTest)


			startPos+=1
			print("\n")
			if(startPos>len(self.currentTest)-1):
				return 0

	def p(self,groupingValue,indicator,x0):
		""" yeah
		"""
		x0=str(x0)

		for y in range(len(self.currentTest)):
			if(groupingValue==self.currentTest[y]):
				x0=str(x0)
				gv=str(groupingValue)
				if(x0[0:1]=="^"):
					gv="      "
					x0=x0[1:len(x0)]


				string_1=("     "+gv+"     " +str(indicator))

				#format output string
				if(len(string_1)<40):

					for zz in range(40-len(string_1)):
						string_1=string_1+" "

				string_1=string_1+" "+str(x0)


				megaIndex=len(self.currentTest)
				startPos=self.currentTest.index(groupingValue)

				#create items to fill.
				#print(megaIndex)
				for x in range(megaIndex):
					self.output.append(None)

				if(self.output[startPos]==None):
					self.output[startPos]=string_1
					return 0


				x=startPos
				while(True):
					if(self.output[x]==None):
						self.output[x]=string_1
						return 0
					x+=megaIndex
h=hh()









def findWaterContainerPath(a, b, c,inputState):
	""" This function generates possible states, connections between said states, and returns the first path to a target value.

	Generation//connection:

		To generate possible states, for every state is the STATES list the program will create a list of state objects, each created by performing one of the three possible state operations. After generating states,
		The program will evaluate every state previously generated to see if they are the same. If so, this means that the current state evaluated in the STATES list connects to the other evaluated, or the current state
		can form the other state via one if its operations. If A generated state is not found in the state list, that means that it was never generated prior to that evaluation and that it must be added to the STATES list.





	 """





	""" DOCUMENTATION FOR THIS FUNCTION """
	starting_state = (0, 0)  #cap a, cap b
	final_path = list()
	final_path.append(starting_state)



	""" THIS IS WHERE THE REAL WORK FOR THIS ASSIGNMENT WILL BE """



	start=state(a,b)
	#where all states will be stored,
	states=[start]
	currentState=None



	x=0
	y=len(states)
	while(1):


		currentState=states[x]
		#print("---------CURRENT STATE 0, 1 amt  :: "+str(currentState.amt[0])+" "+str(currentState.amt[1]) )

		#generate possible States, cycle through possible operations.
		for h in range(2):
			for q in range(3):
				tempState=state(a,b,currentState.amt[0],currentState.amt[1])
				tempState.operation(h,q)
				#print("h,q value : " +str(h)+"  "+str(q))
				#print("\n TEMP STATE 0 and 1 amt ::"+ str(tempState.amt[0]) +"  " +str(tempState.amt[1])  )

				connected=0
				for z in range(len(states)):
					if(states[z].compare(tempState)):
						currentState.connections.append(states[z])
						#print("--CONNECTED TO::"+str(states[z].amt[0])+" "+str(states[z].amt[1]))
						connected=1

				if(not(connected)):
					states.append(tempState)
					currentState.connections.append(tempState)
					#print("--CONNECTED TO::"+str(tempState.amt[0])+" "+str(tempState.amt[1]))
					y+=1





		x+=1
		#print("\n X VALUE:: " + str(x))
		if(x==y):
			break







	#code needed to remove duplicate items.   ->> i.e. connected to self
	# this just goes through and annihilates all self referring states

	for l in range(len(states)):
		#print("----CURRENT STATE ::" + str(states[l].amt[0])+ str(states[l].amt[1]) )

		index=0
		while(not(index==len(states[l].connections))):

			#print("index: "+str(index))
			if(states[l].connections[index].compare(states[l])):
				#print("is same")


				states[l].connections.pop(index)
				index-=1




			index+=1





	print("------------------CONNECTED TO")



	for l in range(len(states)):
		#print("----CURRENT STATE ::" + str(states[l].amt[0])+ str(states[l].amt[1]) )

		index=0
		while(not(index==len(states[l].connections))):

			#print("connection: "+str(states[l].connections[index].amt[0])+str(states[l].connections[index].amt[1]))

			#print("index: "+str(index))
			#if(states[l].connections[index].compare(states[l])):
				##print("is same")


				#states[l].connections.pop(index)





			index+=1



	#print()

	#print("SELECTED STATE: "+ str(states[8].amt[0])+ str(states[8].amt[1])  )
	for x in bfs(states[inputState],c):
		print("PATH: "+str(x.amt[0])+"  :  "+str(x.amt[1]))




	return 0



"""
	print("SEARCH")

"""





""" ADD ANY OTHER (HELPER) FUNCTIONS THAT ARE NEEDED HERE """


def bfs(start,c):
	"""
This functions performs a breadth first search on any provided state object, stopping when a state is found with either bucket being the target quantity. A breadth first search searches for a target vertex one connection level out at a time,
meaning that it will only add the (N+1)th set of vertex connections to the evaluate queue when all (N) connections are added; resulting in an explored tree which is more baleneced than its counterpart the depth first search.
To find the path leading back up to the starting vertex the function has another multi-dimensional queue list which does not pop the values added, and also saves a pointer to each state's parent; so that starting from the target value its possible to trace a path to the starting vertex"""


#takes in any vertex and seeks out a valid path.
	#where the list of nodes which lead to a valid solution are stored.

	#to handle situation where start is the end path.
	if((start.amt[0]==c)or(start.amt[1]==c)):
		return [start]


	Savedpath=[[]]
	path=[]


	twoIndex=-1

	start.color="g"
	queue=[start]

	#the saved que saves every addition to the que, and also the parent state of each queue addition.



	while(len(queue)>0):


		twoIndex+=1
		#print("TWOS INDEX :" +str(twoIndex))
		curState=queue.pop(0)


		#print("--------current State : " + str(curState.amt[0]) + str(curState.amt[1]))



		if((curState.amt[0]==c)or(curState.amt[1]==c)):
			break




		yy=len(curState.connections)-1

		for xx in curState.connections:


			#print("yy value : "+str(yy))
			#print("current connection: "+str(curState.connections[yy].amt[0])+str(curState.connections[yy].amt[1]) )
			#print("COLOR : "+str(curState.connections[yy].color))




			if((curState.connections[yy].color=="w")):


				curState.connections[yy].color="g"


				queue.append(curState.connections[yy])
				Savedpath.append([curState.connections[yy],curState])





			yy-=1






		#print("Que--->")
		#for x in queue:
			#print(" "+str(x.amt[0])+str(x.amt[1]))



		#THIS IS WHERE THE PATH IS TRACED


	CURRENTValue=Savedpath[twoIndex][0]
	while(1):



		path.append(CURRENTValue)
		if(CURRENTValue==start):
			break

		#print("Path --> ")
		#for x in path:
			#print(" "+str(x.amt[0])+str(x.amt[1]))
		#set the current value to the parent of the current value.


		for ll in range(len(Savedpath)):
			#print("ll val"+str(ll))
			if(Savedpath[ll+1][0]==CURRENTValue):
				CURRENTValue=Savedpath[ll+1][1]
				break



	return path






class state():
	"""Each possible bucket state is represented as a class, which has each bucket's capacity and amount. The connections attribute represents other possible states a current state can
		become through a bucket fill, empty or transfer operation.
	"""

	def __init__(self,a,b,state1=0,state2=0):
		self.capacities=[a,b]
		#these keep track of the bucket's current contents
		self.amt=[state1,state2]
		#other states in which an operation can turn a state into
		self.connections=[]
		self.color="w"



	def checkAmt(self,bucket):
		"""This function checks how much liquid can be added to a bucket, this is accomplished by comparing a bucket's limit with how much liquid the bucket currently holds"""

		out=self.capacities[bucket]-self.amt[bucket]

		h.p("checkAmt", " bucket and amt: ", str(bucket)+" "+str(out) )

		return(out)


	def compare(self,state):
		"""This function compares two states and returns true if they are the same. """
		return ((state.amt[0]==self.amt[0]) and (state.amt[1]==self.amt[1]))



	def operation(self,bucket,op):
		"""This function contains all of the possible operations in which a state can undergoe. They are all wrapped into one super function so that each operation can be easily indexed later in the program's combinatorial segment.
		The fill operation fills a bucket as needed, stopping at its limit. This is accomplished by adding the amount of empty space in a bucket, determined by the check function.
		  The transfer operation overfills a beighbors bucket and puts excess fluid back into the orgin bucket. First the entire amount of water in a bucket is added to its neighbors amount. If the amount exceedes the capacity of the neighbors
		  bucket, the difference is subtracted off and added back into the orgin bucket.  The empty operation sets the amount of water in bucket to zero.
		 """


		#fill bucket operation
		if(op==0):
			#This function fills a bucket as needed."""
			self.amt[bucket]+=self.checkAmt(bucket)



		#transfer operation:
		if(op==1):
			#"""this function overfills a neightbors bucket and puts excess back into orgin bucket.."""

			self.amt[abs(bucket-1)]+=self.amt[bucket]
			diff=self.amt[abs(bucket-1)]-self.capacities[abs(bucket-1)]
			self.amt[bucket]=0

			if(diff>0):
				self.amt[bucket]=diff
				self.amt[abs(bucket-1)]-=diff


		#empty operation:
		if(op==2):
		#"""This function sets the amount of water in a bucket to zero."""
			self.amt[bucket]=0







def main():
	"""main"""

	try:
	#-------------------------------------------------------------------------------------------ALTERATION!
		capacity_a = input("Enter the capacity of container A: ")
		capacity_b = input("Enter the capacity of container B: ")
		goal_amount = input("Enter the goal quantity: ")
		inputState = input("Please enter the state index you wish to start with.   This is typically at 0")

		# ADD SOME TYPE/VALUE CHECKING FOR THE INPUTS (OR INSIDE YOUR FUNCTION)

		if int(goal_amount) % math.gcd(int(capacity_a), int(capacity_b)) == 0:
			path = findWaterContainerPath(int(capacity_a), int(capacity_b), int(goal_amount),int(inputState))
			print(path)
			print("!-----the path starts at the bottom.----!")
		else:
			print("\n\n\n!-----------No solution for containers with these sizes and with this final goal amount")





	except:
		print("\n\n\n\nwhoops, looks like you entered an invalid input. ")




#-------------------------------------------------------------------------TEST CODE TO ADD INTO UNTI TEST FUNCTION


class testbrSEARCH(unittest.TestCase):
#--------------------------------------------!!! EDGE CASES !!!!---------------------------------------------------

	def test1(self):
		"""Test what happens when a negative value is entered into the A capacity """
		#self.assertEqual(findWaterContainerPath(-3,-4,2,0),1)
		# Result: infinite loop,

	def test2(self):
		""" A test to see what happens when letters and ascii are entered as input for the target value"""
		x=findWaterContainerPath(3,4,2,0)
		self.assertEqual(findWaterContainerPath(3,4,"&&SDA2SDADW",0),0)










"""

# unittest_main() - run all of TestWaterContainerGraphSearch's methods (i.e. test cases)
def unittest_main():
	unittest.main()

"""








# evaluates to true if run as standalone program
if __name__ == '__main__':
	main()
	"""
	unittest_main()
	"""

h.d()
