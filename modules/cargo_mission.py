from go_to_adjacent_systems import *
from go_somewhere_significant import *
import random
import launch
import faction_ships
import VS
import Briefing
import universe
import unit
import Director

class cargo_mission (Director.Mission):
	you=VS.Unit()
	faction=""
	base=VS.Unit()
	cargoname=""
	difficulty=1
	quantity=1
	cred=0
	capship=0
#	mission_time=0
	adjsys=0
	arrived=0
        mplay="all"
	def initbriefing(self):
		self.jump_ani=0
		self.rnd_y=0.0
		self.added_warp=1
		self.brief_stage=0
		self.begintime= VS.getGameTime()-6.0
		print "starting briefing"
		if (self.you.isNull()):
			VS.terminateMission(0)
			Briefing.terminate()
			return
		faction=you.getFaction()
		name=you.getName()
		self.brief_you=Briefing.addShip(name,faction,(0.0,0.0,80.0))
		VS.IOmessage (0,"cargo mission","briefing","Your mission for today will be to deliver some %s cargo to the %s system.\nIn order to get there, you must follow this route that we have planned out for you." % (cargoname,destination))
	
	def loopbriefing(self):
		size=len(jumps)
		time = VS.getGameTime()
		Briefing.setCamPosition((1.6*(time-self.begintime)*self.brief_stage,0.0,0.0))
		if (((time-self.begintime)>=5.0) and added_warp):
			self.jump_ani=Briefing.addShip("brief_warp",faction,(20.0*(brief_stage),rnd_y,79.5+rnd_y))
			self.added_warp=0
		if (((time-self.begintime)>=6.0)):
			if (self.jump_ani!=0):
				Briefing.removeShip(self.jump_ani)
				self.jump_ani=0
		if ((size==self.brief_stage) and ((time-self.begintime)>=6.0)):
			VS.IOmessage(0,"cargo mission","briefing","Once there, you must drop the cargo off at a specified unit")
			self.brief_stage=size+1
			self.added_warp=0
			self.time=0.0
		elif ((self.brief_stage>size) and ((time-self.begintime)>=11.0)):
			Briefing.terminate()
			return
		elif (((time-self.begintime)>=6.0) and (self.brief_stage<size)):
			self.added_warp=1
			self.rnd_y=(random.random()*40.0-20.0)
			Briefing.addShip("brief_jump",faction,(20.0*(self.brief_stage+1),self.rnd_y,79.6+self.rnd_y))
			Briefing.enqueueOrder (self.brief_you,(20.0*(self.brief_stage+1),self.rnd_y,80.0+self.rnd_y,5.0))
			self.begintime=time
			myname=self.jumps[self.brief_stage]
			VS.IOmessage (0,"cargo mission","briefing","You must go to the '%s' jump point" % (myname))
			self.brief_stage+=1
	
	def endbriefing(self):
		print "endinging briefing"
		del self.jump_ani
		del self.rnd_y
		del self.added_warp
		del self.brief_stage
		del self.begintime
	
	def __init__ (self,factionname, numsystemsaway, cargoquantity, missiondifficulty, creds, launchoncapship, time_to_complete, category):
	  Director.Mission.__init__(self);
#	  self.mission_time=VS.GetGameTime()+time_to_complete*100*float(1+numsystemsaway)
	  self.capship= launchoncapship
	  self.faction=factionname
	  self.cred=creds
	  self.difficulty=missiondifficulty
	  mysys=VS.getSystemFile()
	  self.adjsys=go_to_adjacent_systems(self.you,numsystemsaway)
	  self.quantity=cargoquantity
	  sysfile = mysys
	  self.you=VS.getPlayer()
	  mplay=universe.getMessagePlayer(self.you)
	  if (self.quantity<1):
	    self.quantity=1
	  carg=VS.getRandCargo(self.quantity,category)
	  if (carg.GetQuantity()==0):
	    carg = VS.getRandCargo(quantity,"") #oh no... could be starships...
	  tempquantity=self.quantity
	  self.cargoname=carg.GetContent()
	  name = self.you.getName ()
	  carg.SetMissionFlag(1)
	  if (self.you):
	    quantity = self.you.addCargo(carg)  #I add some cargo
	  else:
	    VS.IOmessage (2,"cargo mission",self.mplay,"#ff0000Unable to establish communications. Mission failed.")
	    VS.terminateMission (0)
	    return
#	  creds_deducted = (carg.GetPrice()*float(self.quantity)*random.random()+1)
#	  self.cred += creds_deducted
	  if (tempquantity>0):
	    self.cred*=float(quantity)/float(tempquantity)
	  else:
	    VS.IOmessage (2,"cargo mission",self.mplay,"#ff0000You do not have space to add our cargo to the mission. Mission failed.")
	    VS.terminateMission(0)
	    return
	  
	  if (quantity==0):
	    VS.IOmessage (2,"cargo mission",self.mplay,"#ff0000You do not have space to add our cargo to the mission. Mission failed.")
	    VS.terminateMission(0)
	    return
	  
	  VS.IOmessage (0,"cargo mission",self.mplay,"Good Day, %s. Your mission is as follows:" % (name))
	  self.adjsys.Print("You should start in the system named %s","Then jump to %s","Finally, jump to %s, your final destination","cargo mission",1)
	  VS.IOmessage (2,"cargo mission",self.mplay,"Give the cargo to a %s unit." % (self.faction))
	  VS.IOmessage (3,"cargo mission",self.mplay,"You will receive %d of the %s cargo" % (self.quantity,self.cargoname))
#	  VS.IOmessage (4,"cargo mission",self.mplay,"We will deduct %.2f credits from your account for the cargo needed." % (creds_deducted))
	  VS.IOmessage (4,"cargo mission",self.mplay,"You will earn %.2f credits when you deliver our cargo." % (creds))
	  VS.IOmessage (4,"game","all","#00ff00Good luck!")
#	  self.you.addCredits (-creds_deducted)
	
	def takeCargoAndTerminate (self,you, remove):
	  removenum=0 #if you terminate without remove, you are SKREWED
	  if (remove):
	    removenum=you.removeCargo(self.cargoname,self.quantity,1)
	    mpart=VS.GetMasterPartList()
	    newcarg=mpart.GetCargo(self.cargoname)
	    newcarg.SetQuantity(removenum)
	    self.base.addCargo(newcarg)
	    has=self.you.hasCargo(self.cargoname)
	    if (has):
	      has=self.you.removeCargo(self.cargoname,has,0)
	      newcarg.SetMissionFlag(0)
	      newcarg.SetQuantity(has)
	      self.you.addCargo(newcarg) #It seems that removing and then adding it again is the only way...
	  if ((removenum>=self.quantity) or (self.quantity==0)):
	    VS.IOmessage (0,"cargo mission",self.mplay,"#00ff00Excellent work pilot.")
	    VS.IOmessage (0,"cargo mission",self.mplay,"#00ff00You have been rewarded for your effort as agreed.")
	    VS.IOmessage (0,"cargo mission",self.mplay,"#00ff00Your excellent work will be remembered.")
	    you.addCredits(self.cred)
	    VS.terminateMission(1)
	    return
	  else:
	    VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000You did not follow through on your end of the deal.")
	    if (self.difficulty<1):
	      VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000Your pay will be reduced")
	      VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000And we will consider if we will accept you on future missions.")
	      addcred=(float(removenum)/(float(self.quantity*(1+self.difficulty))))*self.cred
	      you.addCredits(addcred)
	    else:
	      VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000You will not be paid!")
	      if (self.difficulty>=2):
		VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000And your idiocy will be punished.")
		VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000You had better run for what little life you have left.")
		for i in range(self.difficulty):
		  un=faction_ships.getRandomFighter(self.faction)
		  newunit=launch.launch_wave_around_unit("shadow", self.faction, un, "default", 1, 200.0,400.0,you)
		  newunit.setFgDirective("B")
		  newunit.setTarget(you)
	    VS.terminateMission(0)
	    return
	  
	
	def Execute (self):
##	  if (VS.getGameTime()>mission_time):
##	    VS.IOmessage (0,"cargo mission",self.mplay,"You Have failed to deliver your cargo in a timely manner.")
##	    VS.IOmessage (0,"cargo mission",self.mplay,"The cargo is no longer of need to us.")
##	    if (you):
##	      takeCargoAndTerminate(you,0)
##	    return
	  if (self.you.isNull() or (self.arrived and self.base.isNull())):
	    VS.IOmessage (0,"cargo mission",self.mplay,"#ff0000You were unable to deliver cargo. Mission failed.")
	    VS.terminateMission(0)
	    return
	  if (not self.adjsys.Execute()):
	    return
	  print "Won a section; class name:"
#	  print self.adjsys
	  if (self.arrived):
	    self.adjsys.Execute=self.adjsys.HaveArrived
	    if (self.base.isDocked(self.you)):
	      self.takeCargoAndTerminate(self.you,1)		
	      return
	  else:
	    self.arrived=1
	    self.adjsys=go_somewhere_significant(self.you,1,100,self.capship,self.faction)
	    capstr="planet"
	    dockstr="land"
	    if (self.capship):
	      dockstr="dock"
	      capstr="ship"
	    self.adjsys.Print("You must visit the %%s %s" % (capstr),"cargo mission",", docked around the %s",0)
	    VS.IOmessage(0,"cargo mission",self.mplay,"Once there, %s and we will transport the cargo off of your ship." % (dockstr))
	    self.base=self.adjsys.SignificantUnit()

def initrandom (factionname, missiondifficulty,creds_per_jump, launchoncapship, sysmin, sysmax, time_to_complete, category):
	numsys=random.randrange(sysmin,sysmax)
	return cargo_mission(factionname,numsys, random.randrange(4,15), missiondifficulty,creds_per_jump*float(1+numsys),launchoncapship, 10.0, category)

