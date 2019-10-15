from tkinter import * 
energy = 50 
knowledge = 50
confidence = 50
win = Tk()
win.minsize(375,450)
startmessage1 = "You are in the last days of your first quarter in college. The dial is cranking up and it's a race to the finish line. " 
startmessage2= "Along with taking your final exams you need to raise money for an ambitious project through grants that you can get at a social mixer. "
startmessage3= "You also plan on competing in a triathalon after finals. Every decision you make from now to then will impact your performance for these 3 activities"
startmessage = startmessage1 + startmessage2 + startmessage3
st = StringVar()
st.set(startmessage)
synopsis = Message(win, textvariable=st, width=300)
synopsis.config(font=('times',18))
synopsis.pack()
label = Label(win)
finmessage = Message(win, textvariable="", width = 300)
trimessage = Message(win, textvariable="", width = 300)
socmessage = Message(win, textvariable="", width = 300)

def finframe():
	global knowledge
	global finmessage
	finvar = StringVar()
	if knowledge < 46:
		finvar.set("You've done poorly on your exams, so poorly in fact that you failed all your classes and you now plan on dropping out")
	if knowledge > 45 and knowledge < 71:
		finvar.set("You did ok on your exams and barely passed your classes, you're lucky that you barely got by and you need to work harder next quarter if you wish to excel")
	if knowledge > 70:
		finvar.set("You did very well on your exams and have a bright academic future ahead of you, keep up the good work")
	finmessage = Message(win, textvariable = finvar, width=300)
	finmessage.config(font=('times',18))
	finmessage.pack()

def triframe():
	global energy
	global trimessage
	global finmessage
	global nex17
	finmessage.destroy()
	nex17.destroy()
	trivar = StringVar()
	if energy < 26:
		trivar.set("Due to your poor stamina, you barely managed to successfully get through the biking and swimming portions. Halfway into the running portion you fell and couldn't get up due to exhaustion")
	if energy > 25 and energy < 51:
		trivar.set("You did the bare minimum when it comes to you health, so you finished the race but in last place")
	if energy > 50 and energy < 81:
		trivar.set("You really took care of yourself this quarter. Because of that you easily finished the race. You may have not gotten first place but you have nothing to be ashamed of")
	if energy > 80:
		trivar.set("You truly believe that health is wealth and because of that you finished in first!")
	trimessage = Message(win, textvariable = trivar, width=300)
	trimessage.config(font=('times',18))
	trimessage.pack()
	nex18.pack()

def socframe():
	global confidence
	global trimessage
	global socmessage
	global nex18
	trimessage.destroy()
	nex18.destroy()
	socvar = StringVar()
	if confidence < 46:
		socvar.set("You had a very off-putting prescence at the mixer and noone wanted to talk to you, therefore you raised no money")
	if confidence > 45 and confidence < 71:
		socvar.set("Although you were a bit awkward, you managed to strike a decent conversation with a few donors and got half the funding you needed. You will need a part time job to get the remaining funds")
	if confidence > 70:
		socvar.set("You were an absolute delight at the mixer! You got all the funding you needed and then some")
	socmessage = Message(win, textvariable = socvar, width=300)
	socmessage.config(font=('times',18))
	socmessage.pack()


nex18 = Button(win, text="Next", bd=5, width=10, command=socframe)

def frame1():
	win.minsize(375,225)
	synopsis.destroy()
	nex.destroy()
	promptQ1.pack()
	Q1A1.pack(anchor='w')
	Q1A2.pack(anchor='w')
	Q1A3.pack(anchor='w')
	Q1A4.pack(anchor='w')
	nex2.pack()

nex = Button(win, text="Next", bd=5, width=10, command=frame1) 
nex.pack()

def statchange(primary, secondary, inc):
	hold = []
	if inc == 1:
		primary+=9
		secondary-=7
		hold.append(primary)
		hold.append(secondary)
		return hold
	elif inc == 3:
		primary+=5
		secondary-=5
		hold.append(primary)
		hold.append(secondary)
		return hold
	elif inc == 5:
		primary+=3
		secondary+=5
		hold.append(primary)
		hold.append(secondary)
		return hold
	else:
		primary-=7
		secondary+=8
		hold.append(primary)
		hold.append(secondary)
		return hold

def frame2():
	global energy
	global knowledge
	if var2.get() > 0:
		temp = statchange(energy, knowledge, var2.get())
		energy = temp[0]
		knowledge = temp[1]
		promptQ1.destroy()
		Q1A1.destroy()
		Q1A2.destroy()
		Q1A3.destroy()
		Q1A4.destroy()
		nex2.destroy()
		promptQ2.pack()
		Q2A1.pack(anchor='w')
		Q2A2.pack(anchor='w')
		Q2A3.pack(anchor='w')
		Q2A4.pack(anchor='w')
		nex3.pack()

var2 = IntVar()
tvar1 = StringVar()
tvar1.set("Day 1: You woke up late this morning but can still get to class on time if you hurry. Do you:")
promptQ1 = Message(win, textvariable=tvar1, width=400, font=('times',16))
Q1A1 = Radiobutton(win, text="Have a balanced breakfast and prepare a healthy lunch before leaving", variable=var2, value=1, font=('times',16))
Q1A2 = Radiobutton(win, text="Have a balanced breakfast and plan to eat out for lunch", variable=var2, value=3, font=('times',16))
Q1A3 = Radiobutton(win, text="Grab a banana and get going", variable=var2, value=5, font=('times',16))
Q1A4 = Radiobutton(win, text="Skip breakfast altogether to guarantee that you show up on time", variable=var2, value=8, font=('times',16))
nex2 = Button(win, text="Next", bd=5, width=10, command=frame2)

def frame3():
	global knowledge
	global confidence
	if var3.get() > 0:
		temp1 = statchange(knowledge, confidence, var3.get())
		knowledge=temp1[0]
		confidence=temp1[1]
		promptQ2.destroy()
		Q2A1.destroy()
		Q2A2.destroy()
		Q2A3.destroy()
		Q2A4.destroy()
		nex3.destroy()
		promptQ3.pack()
		Q3A1.pack(anchor='w')
		Q3A2.pack(anchor='w')
		Q3A3.pack(anchor='w')
		Q3A4.pack(anchor='w')
		nex4.pack()

var3 = IntVar()
tvar2 = StringVar()
tvar2.set("Class just started and you didn't read the chapter like you were supposed to. Do you:")
promptQ2 = Message(win, textvariable=tvar2, width=400, font=('times',16))
Q2A1 = Radiobutton(win, text="Annoy the professor with questions that imply you didn't read", variable=var3, value=1, font=('times',16))
Q2A2 = Radiobutton(win, text="Annoy a classmate with questions that imply you didnt read", variable=var3, value=3, font=('times',16))
Q2A3 = Radiobutton(win, text="Take a picture of your classmate's notes", variable=var3, value=5, font=('times',16))
Q2A4 = Radiobutton(win, text="Quietly sit through class and catch up on it later", variable=var3, value=8, font=('times',16))
nex3 = Button(win, text="Next", bd=5, width=10, command=frame3)

def frame4():
	global knowledge
	global confidence
	if var4.get() > 0:
		temp2 = statchange(knowledge, confidence, var4.get())
		knowledge = temp2[0]
		confidence = temp2[1]
		promptQ3.destroy()
		Q3A1.destroy()
		Q3A2.destroy()
		Q3A3.destroy()
		Q3A4.destroy()
		nex4.destroy()
		promptQ4.pack()
		Q4A1.pack(anchor='w')
		Q4A2.pack(anchor='w')
		Q4A3.pack(anchor='w')
		Q4A4.pack(anchor='w')
		nex5.pack()

var4 = IntVar()
tvar3 = StringVar()
tvar3.set("After back to back classes you catch a 2 hour break. Do you:")
promptQ3 = Message(win, textvariable=tvar3, width=400, font=('times',16))
Q3A1 = Radiobutton(win, text="Catch up on material by yourself", variable=var4, value=1, font=('times',16))
Q3A2 = Radiobutton(win, text="Attend professor office hours", variable=var4, value=3, font=('times',16))
Q3A3 = Radiobutton(win, text="Catch up on material with a classmate", variable=var4, value=5, font=('times',16))
Q3A4 = Radiobutton(win, text="Enjoy lunch with a friend and socialize", variable=var4, value=8, font=('times',16))
nex4 = Button(win, text="Next", bd=5, width=10, command=frame4)

def frame5():
	global knowledge
	global confidence
	if var5.get() > 0:
		temp3 = statchange(confidence, knowledge, var5.get())
		knowledge = temp3[0]
		confidence = temp3[1]
		promptQ4.destroy()
		Q4A1.destroy()
		Q4A2.destroy()
		Q4A3.destroy()
		Q4A4.destroy()
		nex5.destroy()
		promptQ5.pack()
		Q5A1.pack(anchor='w')
		Q5A2.pack(anchor='w')
		Q5A3.pack(anchor='w')
		Q5A4.pack(anchor='w')
		nex6.pack()

var5 = IntVar()
tvar4 = StringVar()
tvar4.set("Day 2: During lecture the professor asks that you get into pairs for the assignment today. Do you:")
promptQ4 = Message(win, textvariable=tvar4, width=400, font=('times',16))
Q4A1 = Radiobutton(win, text="Team up with your friend who doesn't care about their grade", variable=var5, value=1, font=('times',16))
Q4A2 = Radiobutton(win, text="Team up with your friend who always hogs all the work", variable=var5, value=3, font=('times',16))
Q4A3 = Radiobutton(win, text="Team up with someone you've been getting to know this quarter", variable=var5, value=5, font=('times',16))
Q4A4 = Radiobutton(win, text="Team up with the smart, but really awkward kid", variable=var5, value=8, font=('times',16))
nex5 = Button(win, text="Next", bd=5, width=10, command=frame5)

def frame6():
	global energy
	global confidence
	if var6.get() > 0:
		temp4 = statchange(energy, confidence, var6.get())
		energy = temp4[0]
		confidence = temp4[1]
		promptQ5.destroy()
		Q5A1.destroy()
		Q5A2.destroy()
		Q5A3.destroy()
		Q5A4.destroy()
		nex6.destroy()
		promptQ6.pack()
		Q6A1.pack(anchor='w')
		Q6A2.pack(anchor='w')
		Q6A3.pack(anchor='w')
		Q6A4.pack(anchor='w')
		nex7.pack()

var6 = IntVar()
tvar5 = StringVar()
tvar5.set("Your last class got cancelled for the day. You get home and you:")
promptQ5 = Message(win, textvariable=tvar5, width=400, font=('times',16))
Q5A1 = Radiobutton(win, text="Catch up on some sleep", variable=var6, value=1, font=('times',16))
Q5A2 = Radiobutton(win, text="Go to the gym", variable=var6, value=3, font=('times',16))
Q5A3 = Radiobutton(win, text="Invite a friend over for a healthy meal", variable=var6, value=5, font=('times',16))
Q5A4 = Radiobutton(win, text="Go out to eat with a friend", variable=var6, value=8, font=('times',16))
nex6 = Button(win, text="Next", bd=5, width=10, command=frame6)

def frame7():
	global confidence
	global knowledge
	if var7.get() > 0:
		temp5 = statchange(confidence, knowledge, var7.get())
		confidence = temp5[0]
		knowledge = temp5[1]
		promptQ6.destroy()
		Q6A1.destroy()
		Q6A2.destroy()
		Q6A3.destroy()
		Q6A4.destroy()
		nex7.destroy()
		promptQ7.pack()
		Q7A1.pack(anchor='w')
		Q7A2.pack(anchor='w')
		Q7A3.pack(anchor='w')
		Q7A4.pack(anchor='w')
		nex8.pack()

var7 = IntVar()
tvar6 = StringVar()
tvar6.set("Your relatives invite your family over at the last minute for dinner but you need to study for class tomorrow. Do you:")
promptQ6 = Message(win, textvariable=tvar6, width=400, font=('times',16))
Q6A1 = Radiobutton(win, text="Come over anyways", variable=var7, value=1, font=('times',16))
Q6A2 = Radiobutton(win, text="Come over and bring your books", variable=var7, value=3, font=('times',16))
Q6A3 = Radiobutton(win, text="Show up late to dinner so you can study", variable=var7, value=5, font=('times',16))
Q6A4 = Radiobutton(win, text="Not show up at all to secure plenty of study time", variable=var7, value=8, font=('times',16))
nex7 = Button(win, text="Next", bd=5, width=10, command=frame7)

def frame8():
	global energy
	global knowledge
	if var8.get() > 0:
		temp6 = statchange(energy, knowledge, var8.get())
		energy = temp6[0]
		knowledge = temp6[1]
		promptQ7.destroy()
		Q7A1.destroy()
		Q7A2.destroy()
		Q7A3.destroy()
		Q7A4.destroy()
		nex8.destroy()
		promptQ8.pack()
		Q8A1.pack(anchor='w')
		Q8A2.pack(anchor='w')
		Q8A3.pack(anchor='w')
		Q8A4.pack(anchor='w')
		nex9.pack()

var8 = IntVar()
tvar7 = StringVar()
tvar7.set("Day 3: You get up an hour earlier than usual. What do you want to do with this extra hour?")
promptQ7 = Message(win, textvariable=tvar7, width=400, font=('times',16))
Q7A1 = Radiobutton(win, text="Force yourself back to sleep", variable=var8, value=1, font=('times',16))
Q7A2 = Radiobutton(win, text="Go on a run", variable=var8, value=3, font=('times',16))
Q7A3 = Radiobutton(win, text="Prepare all your food for the day and do a little reading", variable=var8, value=5, font=('times',16))
Q7A4 = Radiobutton(win, text="Get your classwork done early", variable=var8, value=8, font=('times',16))
nex8 = Button(win, text="Next", bd=5, width=10, command=frame8)

def frame9():
	global knowledge
	global energy
	if var9.get() > 0:
		temp7 = statchange(knowledge, energy, var9.get())
		knowledge = temp7[0]
		energy = temp7[1]
		promptQ8.destroy()
		Q8A1.destroy()
		Q8A2.destroy()
		Q8A3.destroy()
		Q8A4.destroy()
		nex9.destroy()
		promptQ9.pack()
		Q9A1.pack(anchor='w')
		Q9A2.pack(anchor='w')
		Q9A3.pack(anchor='w')
		Q9A4.pack(anchor='w')
		nex10.pack()

var9 = IntVar()
tvar8 = StringVar()
tvar8.set("The college is holding drop-ins for tutoring on a class you're struggling in but its during your lunch break. Do you:")
promptQ8 = Message(win, textvariable=tvar8, width=400, font=('times',16))
Q8A1 = Radiobutton(win, text="Go to the drop-in and ignore your hunger", variable=var9, value=1, font=('times',16))
Q8A2 = Radiobutton(win, text="Bring a bit of your food to eat during the drop-in", variable=var9, value=3, font=('times',16))
Q8A3 = Radiobutton(win, text="Eat really quick and show up at the last 30 minutes of the drop-in", variable=var9, value=5, font=('times',16))
Q8A4 = Radiobutton(win, text="Skip drop-ins altogether", variable=var9, value=8, font=('times',16))
nex9 = Button(win, text="Next", bd=5, width=10, command=frame9)

def frame10():
	global confidence
	global energy
	if var10.get() > 0:
		temp8 = statchange(confidence, energy, var10.get())
		confidence = temp8[0]
		energy = temp8[1]
		promptQ9.destroy()
		Q9A1.destroy()
		Q9A2.destroy()
		Q9A3.destroy()
		Q9A4.destroy()
		nex10.destroy()
		promptQ10.pack()
		Q10A1.pack(anchor='w')
		Q10A2.pack(anchor='w')
		Q10A3.pack(anchor='w')
		Q10A4.pack(anchor='w')
		nex11.pack()

var10 = IntVar()
tvar9 = StringVar()
tvar9.set("A new game that you've been very excited for comes out at midnight tonight and your friends are picking it up as well. Do you:")
promptQ9 = Message(win, textvariable=tvar9, width=400, font=('times',16))
Q9A1 = Radiobutton(win, text="Spend all night playing the new game", variable=var10, value=1, font=('times',16))
Q9A2 = Radiobutton(win, text="Spend an hour playing the new game", variable=var10, value=3, font=('times',16))
Q9A3 = Radiobutton(win, text="Go to the midnight release but not play till after finals", variable=var10, value=5, font=('times',16))
Q9A4 = Radiobutton(win, text="Not go to the midnight release", variable=var10, value=8, font=('times',16))
nex10 = Button(win, text="Next", bd=5, width=10, command=frame10)

def frame11():
	global confidence
	global energy
	if var11.get() > 0:
		temp9 = statchange(confidence, energy, var11.get())
		confidence = temp9[0]
		energy = temp9[1]
		promptQ10.destroy()
		Q10A1.destroy()
		Q10A2.destroy()
		Q10A3.destroy()
		Q10A4.destroy()
		nex11.destroy()
		promptQ11.pack()
		Q11A1.pack(anchor='w')
		Q11A2.pack(anchor='w')
		Q11A3.pack(anchor='w')
		Q11A4.pack(anchor='w')
		nex12.pack()

var11 = IntVar()
tvar10 = StringVar()
tvar10.set("Day 4: Your friends want to hold a pool tournament after classes but you've been wanting to rest. Do you:")
promptQ10 = Message(win, textvariable=tvar10, width=400, font=('times',16))
Q10A1 = Radiobutton(win, text="Go to the tournament", variable=var11, value=1, font=('times',16))
Q10A2 = Radiobutton(win, text="Play a few games then forfeit", variable=var11, value=3, font=('times',16))
Q10A3 = Radiobutton(win, text="Watch a few games and not participate", variable=var11, value=5, font=('times',16))
Q10A4 = Radiobutton(win, text="Not go at all", variable=var11, value=8, font=('times',16))
nex11 = Button(win, text="Next", bd=5, width=10, command=frame11)

def frame12():
	global energy
	global confidence
	if var12.get() > 0:
		temp10 = statchange(energy, confidence, var12.get())
		energy = temp10[0]
		confidence = temp10[1]
		promptQ11.destroy()
		Q11A1.destroy()
		Q11A2.destroy()
		Q11A3.destroy()
		Q11A4.destroy()
		nex12.destroy()
		promptQ12.pack()
		Q12A1.pack(anchor='w')
		Q12A2.pack(anchor='w')
		Q12A3.pack(anchor='w')
		Q12A4.pack(anchor='w')
		nex13.pack()

var12 = IntVar()
tvar11 = StringVar()
tvar11.set("You've been meaning to grab groceries all week but you cousin is having a party at his place and needs help. Do you:")
promptQ11 = Message(win, textvariable=tvar11, width=400, font=('times',16))
Q11A1 = Radiobutton(win, text="Grab groceries and head home instead", variable=var12, value=1, font=('times',16))
Q11A2 = Radiobutton(win, text="Grab groceries then go to the party", variable=var12, value=3, font=('times',16))
Q11A3 = Radiobutton(win, text="Show up to the party on time and leave early to get groceries", variable=var12, value=5, font=('times',16))
Q11A4 = Radiobutton(win, text="Show up to the party and leave after you've finished helping", variable=var12, value=8, font=('times',16))
nex12 = Button(win, text="Next", bd=5, width=10, command=frame12)

def frame13():
	global knowledge
	global energy
	if var13.get() > 0:
		temp11 = statchange(knowledge, energy, var13.get())
		knowledge = temp11[0]
		energy = temp11[1]
		promptQ12.destroy()
		Q12A1.destroy()
		Q12A2.destroy()
		Q12A3.destroy()
		Q12A4.destroy()
		nex13.destroy()
		promptQ13.pack()
		Q13A1.pack(anchor='w')
		Q13A2.pack(anchor='w')
		Q13A3.pack(anchor='w')
		Q13A4.pack(anchor='w')
		nex14.pack()

var13 = IntVar()
tvar12 = StringVar()
tvar12.set("It's late at night and you're struggling to sleep, what do you do?")
promptQ12 = Message(win, textvariable=tvar12, width=400, font=('times',16))
Q12A1 = Radiobutton(win, text="Get some studying done", variable=var13, value=1, font=('times',16))
Q12A2 = Radiobutton(win, text="Read a book", variable=var13, value=3, font=('times',16))
Q12A3 = Radiobutton(win, text="Force yourself back to sleep", variable=var13, value=5, font=('times',16))
Q12A4 = Radiobutton(win, text="Go on a late night run", variable=var13, value=8, font=('times',16))
nex13 = Button(win, text="Next", bd=5, width=10, command=frame13)

def frame14():
	global confidence
	global knowledge
	if var14.get() > 0:
		temp12 = statchange(confidence, knowledge, var14.get())
		confidence = temp12[0]
		knowledge = temp12[1]
		promptQ13.destroy()
		Q13A1.destroy()
		Q13A2.destroy()
		Q13A3.destroy()
		Q13A4.destroy()
		nex14.destroy()
		promptQ14.pack()
		Q14A1.pack(anchor='w')
		Q14A2.pack(anchor='w')
		Q14A3.pack(anchor='w')
		Q14A4.pack(anchor='w')
		nex15.pack()


var14 = IntVar()
tvar13 = StringVar()
tvar13.set("Day 5: You have a friend coming over to your place for breakfast but you realize that you've made some mistakes in your homework that's due in an hour. Do you:")
promptQ13 = Message(win, textvariable=tvar13, width=400, font=('times',16))
Q13A1 = Radiobutton(win, text="Submit your homework as is", variable=var14, value=1, font=('times',16))
Q13A2 = Radiobutton(win, text="Fix as many errors as you can until your friend arrives", variable=var14, value=3, font=('times',16))
Q13A3 = Radiobutton(win, text="Fix your errors while your friend is over", variable=var14, value=5, font=('times',16))
Q13A4 = Radiobutton(win, text="Tell them that they can't come", variable=var14, value=8, font=('times',16))
nex14 = Button(win, text="Next", bd=5, width=10, command=frame14)

def frame15():
	global knowledge
	global energy
	if var15.get() > 0:
		temp13 = statchange(knowledge, energy, var15.get())
		knowledge = temp13[0]
		energy = temp13[1]
		promptQ14.destroy()
		Q14A1.destroy()
		Q14A2.destroy()
		Q14A3.destroy()
		Q14A4.destroy()
		nex15.destroy()
		promptQ15.pack()
		Q15A1.pack(anchor='w')
		Q15A2.pack(anchor='w')
		Q15A3.pack(anchor='w')
		Q15A4.pack(anchor='w')
		nex16.pack()

var15 = IntVar()
tvar14 = StringVar()
tvar14.set("You're in the middle of class and you are starving. Do you:")
promptQ14 = Message(win, textvariable=tvar14, width=400, font=('times',16))
Q14A1 = Radiobutton(win, text="Ignore your hunger and continue", variable=var15, value=1, font=('times',16))
Q14A2 = Radiobutton(win, text="Grab a quick snack out of the vending machine", variable=var15, value=3, font=('times',16))
Q14A3 = Radiobutton(win, text="Grab and meal and bring it into class", variable=var15, value=5, font=('times',16))
Q14A4 = Radiobutton(win, text="Leave class early for food", variable=var15, value=8, font=('times',16))
nex15 = Button(win, text="Next", bd=5, width=10, command=frame15)

def frame16():
	global energy
	global confidence
	global knowledge
	if var16.get() > 0:
		temp14 = statchange(energy, confidence, var16.get())
		energy = temp14[0]
		confidence = temp14[1]
		promptQ15.destroy()
		Q15A1.destroy()
		Q15A2.destroy()
		Q15A3.destroy()
		Q15A4.destroy()
		nex16.destroy()
		finframe()
		nex17.pack()

var16 = IntVar()
tvar15 = StringVar()
tvar15.set("You are on a run to tire yourself out so you can go to bed early. In the middle of the run you get a text from your parents saying that some relatives have come over. Do you:")
promptQ15 = Message(win, textvariable=tvar15, width=400, font=('times',16))
Q15A1 = Radiobutton(win, text="Finish your entire run then go", variable=var16, value=1, font=('times',16))
Q15A2 = Radiobutton(win, text="Shorten your run a little bit", variable=var16, value=3, font=('times',16))
Q15A3 = Radiobutton(win, text="Head home and continue your run when the relatives have left", variable=var16, value=5, font=('times',16))
Q15A4 = Radiobutton(win, text="Head home and right away and cancel your run", variable=var16, value=8, font=('times',16))
nex16 = Button(win, text="Next", bd=5, width=10, command=frame16)
nex17 = Button(win, text="Next", bd=5, width=10, command=triframe)

win.mainloop()