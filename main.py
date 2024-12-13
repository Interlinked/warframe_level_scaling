
#Imports certain commands needed to correctly manipulate the data values
import math
#This is used to help plot the scatterplot and create the line through it.
import scikit.learn
import matplotlib.pyplot as plt
#Imports r2_score to help me test data sets for compatability in a polynomial model. 
x = [8,9,10,13,15,20,25,30,35,40,45,50,55,60,65,70,75,80,82,85,87,90,93,97,100,105,110,115,116,120,125,130,135,140,145,150,165,] #The level values.
y = [800,814,856,1157,1320,3139,6166,11222,19090, 30697,47111,69537,99304,137869,186810,247822,322716,424807,485742,560216,587515,613696,639588,674405,700733,745011,789773,835003,844104,880686,926808,973356,1020320,1067687,1115447,1163591,1310232,]
y2=[62.5, 65.73, 74.04, 81.24, 86.29,89.69,92.01,93.65,95.55,96.21 ]
x2=[8, 15, 25, 35, 45,55,65,75,100,125 ]
y3=[800,814,856,1157,1320,3139,6166,11222,19090, 30697,47111,69537,99304,137869,186810,247822,322716,424807,485742,560216,587515,613696,639588,674405,700733,745011,789773,835003,844104,880686,926808,973356,1020320,1067687,1115447,1163591,1310232,]
x3=[8,9,10,13,15,20,25,30,35,40,45,50,55,60,65,70,75,80,82,85,87,90,93,97,100,105,110,115,116,120,125,130,135,140,145,150,165,] #x2 and y2 are the in progress armour values, x2 is level and y2 is the damage reduction as a percentage, following the same sibling-esque paring as before. 





test = input("Say Levels to get the ehp of a level.\nSay Armour to get the armour dr from a level. \nSay Graph to see the graph that the robot pulls values from. \nSay Health to get the estimated level for any given ehp value.\n\nNOTE:\nThis graph only remains closely accurate up to level 145.\nPast that, it loses accuracy\nEhp and armour do not scale linearly.")
if test == "Health":
	b = int(input("What amount of ehp do you want to test?\n An average health is in the ten thousands"))
	
	mymodel = numpy.poly1d(numpy.polyfit(x3, y3, 3))
	myline = numpy.linspace(800,1310232, 1000)
	LVL = numpy.interp(b, y3,x3)
	LVL = round(LVL,0)
	print(LVL, "is the estimated level based of health value you gave.")
if test == "Graph":

	fig, ax = plt.subplots()
	slope, intercept, r, p, std_err = stats.linregress(x, y)
	mymodel = numpy.poly1d(numpy.polyfit(x2, y2, 3))
	myline = numpy.linspace(62.5,93.5, 1000)
  #Creates a polynomial model
	
	plt.scatter(x, y)#plots the points
	ax.plot(x,y,linestyle='solid',color='blue')
	ax2 = ax.twinx()
	ax2.plot(x2,y2,color='yellow')
	ax2.tick_params(axis='y',labelcolor='yellow')
	ax2.scatter(x2,y2)
	plt.show()#shows all of the above.

if test == "Armour":
	b = int(input("What level do you want to test? (Integer)"))
	#Gets the requested level from the user and \eturns an error if it is not a number.
	mymodel = numpy.poly1d(numpy.polyfit(x2, y2, 3))
	myline = numpy.linspace(62.5,93.5, 1000)
#Defines the starting point of the line and the ending point, in Y.
	DR = numpy.interp(b, x2,y2)
	#gets the armour DR reduction from the y axis of the requested X. It esentially makes a sqaure by getting y from the x and continuing the lines forever.
	print(r2_score(y2, mymodel(x2)))
	print(DR, "percent damage reduction")
#This prints the percentage of damage reduction from the dr definition above


if test == "Levels":

	e = int(input("What level do you want to test? (Number)"))
	mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
	myline = numpy.linspace(1, 39, 1000)
	DMGTTL = numpy.interp(e, x,y)
	#This functions identically to the armour statement, with the exception that instead of pulling from the Armour values it pulls from the health.
	print(r2_score(y, mymodel(x)))
	#This score helps determine the relationship of x to y, is really only for testing purposes. it will look like 0.99...
	print(DMGTTL, "total effective health (armour, health and shields added total)")
#This is different than numbered health. While an enemy may have 1000 health, if it has 50 percent DR, that gives it 1500 effective health. The equation for effetive health is (Health * Damage Reducion) + (Shields * 1.25) As shields have innate 25 percent reduction.

#just tips for each of the groups of levels.
	if e <= 20:
		print("You don't need any special equipment for these levels.")

	if e > 20 and e < 40:
		print("Might need a simple viral status build but equipment still doesn't matter.")

	if e > 40 and e < 60:
		print("Typical mid-late star chart levels, you might need to upgrade your equipment now.")

	if e > 60 and e < 80:
		print("Your build may needs some upgrading, start thinking of status,crit, and more advanced combos.")

	if e > 80 and e < 100:
		print("typical sortie levels, you need to start getting decent guns and builds, certain arcanes and primer abilities and guns may need to start being used for armoured enemies.")

	if e > 100 and e < 150:
		print("Steel Path levels, start thinking slash procs, viral, corrosive, and crit, with good weopons. Armour is one of the biggest roadblocks at these levels.")

	if e > 150:
		print("If you even have access to these levels, that probably means that you don't need my help.")

