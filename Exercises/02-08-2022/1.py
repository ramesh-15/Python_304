=>definitiono Programmer / User-Defined Functions:
    
    Programmer / User-Defined Functions are those which are  defined  by Python Programmer
    and Available in the Project and use for performing Common Operations and Provided Code-Re-usability.

Examples:-    sumop()   divop()    expoop()...etc

Parts of Functions:
----------------------------------
=>At the time of dealing  with Functions concept, we have two parts. They are
	a) Function Definition
	b) Function Call
=>For Every Function Call, there must exists a Function Definition otherwise we get NameError.
=>Programatically, Function Definition Exists Only Once and we may have one or more Function calls to Coresponding Function Definition.
=>Function Definition will be executed when we call the Function Definition by using Function Call(s).


		=============================================
			Syntax  for Defining the Function
		=============================================

def     functionname(list of formal params ):
		"""doc String"""
		----------------------------------
		Statement-1
		statement-2
		--------------------
		statement-n
		----------------------------------

=============================================X=============================================
		
                -----------------------
                    Explanation:
                ----------------------
1) "def" is a keyword use for defining Programmer-defined functions.
2)"functionname" is one of the valid variable name and treated as name of the 
     function.
3) "list of formal params" represents Variables List used in Function Heading 
     and whose purpose is that to store Input values coming from Function Calls.
4) """doc String""" stands for Documentation String. Writing the
     """doc  String""" is optional and whose purpose is that to describe the
    function ality of the Function.
5) Here "statement-1,statement-2,........statement-n" represents Set / Block of executable statement which provides Solution for Given Problem Statement. This logic is called Problem solving / Business Logic.
6) we are using Some variables inside of Function Body for storing Temporary    results and such variables are called "Local Variables".

7) The values of Local Variable and Formal parameters can be accessed within the corresponding Function Definition but not possible to access from Other Function Definitions.



#Exmaple:

def   sumop(a,b):  # here 'a' and 'b' are called Formal Params
	print("i am inside sumop()")
	c=a+b # here 'c' is called Local variable
	return c   # here return statement is used for returning the value

#main program

x1=float(input("Enter First value:"))
x2=float(input("Enter Second value:"))
c = sumop(x1,x2) # Function Call--Sending Input--
print("sum in main program={}".format(c))    """
