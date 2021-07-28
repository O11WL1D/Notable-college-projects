from binarytree import BinaryTree
from stack import Stack
import unittest
import random







class hh():

	#this little section stores global values used in this program.

	saved_input=[]
	saved_tree=[]

	parents=[]
	objects=[]

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

		self.currentTest=["1!(","1valEvl","logiEval1"]
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




















def buildMPLogicParseTree(s):
	"""This function uses a set of rules to create a parse tree for logic expressions. The rules are as follows:

		1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
		2.If the current token is in the list ["AND","OR"], set the root value of the current node to the operator represented by the current token.
		 Add a new node as the right child of the current node and descend to the right child.
		3.If the current token is a logic value, set the root value of the current node to the value and return to the parent.
		4.If the current token is a ')', go to the parent of the current node.

		Maybe and Prob probability values, reperesented by the syntax M_0.x , P_0.x  , are considered logic values, and are true in x cases.


	 """


	#this saves the input, which will correspond to a tree root value. With a root value, you can find the corresponding index of the saved input.
	h.saved_input.append(s)

	root=BinaryTree(None)
	currentNode=root
	currentNode.key=""


	h.parents.append(None)     																																      # =[None]
	h.objects.append(currentNode)     																														     #=[currentNode]
	#by saving the value of parent with the same index used in the object list, you can find one value's index if you know the other value's index.
	#this means that you can access the parent addr of any object.



	#below is the implementation of the four rules stated above.
	for x in range(len(s)):
			if(s[x]=='('):
				currentNode.insertLeft("None")

				h.objects.append(currentNode.getLeftChild())
				h.parents.append(currentNode)


																																											#currentNode.getLeftChild().parentNode=currentNode
				currentNode=currentNode.getLeftChild()
				h.p("!(","occurance"," ")



			if((s[x]=='A')or(s[x]=='O')):
					currentNode.key=s[x:x+3]

					#since the AND and or operators have different lengths, any OR operators will have an additional character of whitespace included.

					currentNode.insertRight(None)

					h.objects.append(currentNode.getRightChild())
					h.parents.append(currentNode)

																																											#currentNode.getRightChild().parentNode=currentNode

					currentNode=currentNode.getRightChild()




			#true false values.
			if( (s[x]=='T') or(s[x]=='F') ):
				currentNode.key=s[x]

																																														#currentNode=currentNode.parentNode
				index=h.objects.index(currentNode)
				currentNode=h.parents[index]



			#Maybe/prob  values
			if( (s[x]=='M') or(s[x]=='P')):
				currentNode.key=s[x:x+6]

																																																#currentNode=currentNode.parentNode

				index=h.objects.index(currentNode)
				currentNode=h.parents[index]







			if(s[x]==')'):

																																																		#currentNode=currentNode.parentNode
				index=h.objects.index(currentNode)
				currentNode=h.parents[index]









	#this stores the tree in parallel with the saved input, making the input retreval function very easy.
	h.saved_tree.append(root)
	#print(root.printTree(0))
	return root














def M_val(value):
		"""This function generates a true value X times.
		This function is implemented via the random number generator. Since probability is defined as the number of outcomes which something is true,
		there will be 0-x cases in which a 'true' outcome occurs, out of a total of 100 possible cases. To evaluate if a case occurs, the random number
		is compared to the probability.

		 """

		#print("M "+str(value))


		prob=(int(value[4:len(value)]))
		h.p("valEvl"," prob value ",prob )


		if((prob>75)or(prob<0)):
			print("invalid maybe value, try again")
			return(0)

		else:
			ran=random.randrange(100)
			h.p("valEvl","random value:",ran)
			if(ran>prob):
				return "F"
			else:
				return "T"









def P_val(value):
		"""same thing.   """
		#print("P "+str(value))


		prob=(int(value[4:len(value)]))
		h.p("valEvl"," prob value ",prob )

		if((prob>100)or(prob<75)):
			print("invalid prob value, try again")
			return 0

		else:
				ran=random.randrange(100)
				h.p("valEvl","random value:",ran)
				if(ran>prob):
					return "F"
				else:
					return "T"










def valueEval(value,op1=0,op2=0):
	"""This function takes in two logic values as operands, the desired operation and outputs the result of that operation.
	Any probability logic values are evalutated with the M_val and P_val functions.
	 """

	#values that should be 10%, i.e. .1, only register as .01 or 1%. input needs to be padded with an additional zero.

	value=str(value)





	#check for M and P probability values.

	if(op1[0]=="M"):
		op1=M_val(op1)

	if(op1[0]=="P"):
		op1=P_val(op1)


	if(op2[0]=="M"):
		op2=M_val(op2)

	if(op2[0]=="P"):
		op2=P_val(op2)







	if(value[0]=="A"):
		return str((op1=="T") and (op2=="T"))[0]


	if(value[0]=="O"):
		return str((op1=="T") or (op2=="T"))[0]





#print(valueEval("AND",True,True))

















def evaluateMPLogicParseTree(t):
	"""This function processes a logic parse tree to identify the resulting logic.

	The method starts at the root node, and runs through the following conditionals in the order listed:

		1. If the current node's children are logic values, evaluate the resulting logic and replace the current nodes key with said logic value.
			Afterwards, move up to the parent node.

		2. If another unevaluated subtree exists on the left (i.e. there is a AND or OR operation node on the left), then move down to the left node.
		3. same as 2 but with the right nodes

		Once the currentnode is found to have returned to the root node, the method returns the current nodes value, or the resulting logic.

	"""

	boOl=["T","F","M","P"]
	root=t
	currentNode=root



	level=0


	while(True):

		if(currentNode==None):
			break

		leftKey=currentNode.getLeftChild().key
		rightKey=currentNode.getRightChild().key
		curKey=currentNode.key



		while(True):




			#print("\ncurrentKey :"+str(curKey)+"  level : "+str(level))
			#print("leftKey :"+str(leftKey))
			#print("rightKey :"+str(rightKey))



			if(((leftKey[0] in boOl)and(rightKey[0] in boOl))and( not(curKey[0] in boOl)) ):


				currentNode.key=valueEval(curKey,leftKey,rightKey)

				index=h.objects.index(currentNode)
				currentNode=h.parents[index]
				level=level-1

				break


			if(not(leftKey in boOl)):
				currentNode=currentNode.getLeftChild()
				level=level+1

				break


			if(not(rightKey in boOl)):
				currentNode=currentNode.getRightChild()
				level=level+1

				break



	#honestly recursion is just a fancy while loop that wastes stack memory. Please convince me otherwise.

	return(root.key)




















def printMPLogicExpression(t):
	"""As explained before, every tree value is saved along with its input in two seperate lists, so that one value's index can be used to indentify the other value's index.  """

	index=h.saved_tree.index(t)
	return h.saved_input[index]










class TestParseTree(unittest.TestCase):
	"""class for testing the other functions. """
	#buildMPLogicParseTree("( ( ( ( T AND F ) AND ( T OR F ) ) AND ( T OR F ) ) OR F )")
	#buildMPLogicParseTree("( ( T AND F ) OR (T OR F) )")



	#print(  evaluateMPLogicParseTree(  input  ))



	def test1(self):
		"""Evaluate if main functionality works. This includes construction of a tree, evaluation, and input fetching."""


		input=buildMPLogicParseTree("( ( ( ( T AND F ) AND ( T OR F ) ) AND ( T OR F ) ) OR F )")
		#print(  evaluateMPLogicParseTree(  input  ))
		#print( printMPLogicExpression(input) )
		self.assertEqual(evaluateMPLogicParseTree(  input  ),"F")
		self.assertEqual(printMPLogicExpression(input),"( ( ( ( T AND F ) AND ( T OR F ) ) AND ( T OR F ) ) OR F )")



	def test2(self):
		"""#evaluate is main functionality + maybe/prob logic values work.  """


		input=buildMPLogicParseTree("( W_0.34 AND P_0.98 )")
		self.assertEqual(evaluateMPLogicParseTree(  input  ),"T")





	def test3(self):
			"""--------------EDGE CASE-------------------:
			This tests to see if prob/maybe logic values with only one decimal place work as expected.
			 """
			input=buildMPLogicParseTree("( M_0.9 AND T )")
			self.assertEqual(evaluateMPLogicParseTree(  input  ),"T")
			#wow, looks like having only one decimal place does not work.




	def test4(self):
		"""----------------EDGE CASE------------------------
		This tests the outcome of setting the tree contructor methods operators as all lowercase
		"""
		input=buildMPLogicParseTree("( M_0.9 and T )")
		#print(evaluateMPLogicParseTree(  input  ))
		self.assertEqual(evaluateMPLogicParseTree(  input  ),"T")

		#as expected, it fails in this regard.


	def test5(self):
		"""------------------------------------EDGE CASE----------------------------------
		This determines what happens when you provide an input that has no spacing inbetween the tokens.
		"""

		input=buildMPLogicParseTree("((TORF)ANDT)")
		#print(evaluateMPLogicParseTree(  input  ))
		self.assertEqual(evaluateMPLogicParseTree(  input  ),"T")
		#suprisingly this does work, maybe with a more complicated input string I could
		#break the code.














#input=buildMPLogicParseTree("( M_0.9 and T )")




#input=buildMPLogicParseTree("((TORF)ANDT)")
#	print(evaluateMPLogicParseTree(  input  ))





#-----------------------------------------------------------TESTING ---------------------------------------------------------------------------


print("------Tree construction, evaluation and input test------")

input=buildMPLogicParseTree("( ( ( ( T AND F ) AND ( T OR F ) ) AND ( T OR F ) ) OR F )")
#print(  evaluateMPLogicParseTree(  input  ))
#print( printMPLogicExpression(input) )
if(evaluateMPLogicParseTree(  input  )=="F"):
	print("tree evaluation and construction successful")
else:
	print("Tree evaluation or construction failed.")


print("-------------input retreval testing------------------------")
if(printMPLogicExpression(input)=="( ( ( ( T AND F ) AND ( T OR F ) ) AND ( T OR F ) ) OR F )"):
	print("input fetch succeeded")
else:
	print("input fetch fail.")


print("\n\n\n !--------------------------- To see the results of unit test, go into the code and uncomment the unit test call. ")


#unittest.main()









h.d()
