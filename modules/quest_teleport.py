import quest
import Vector
import VS
import unit
import universe
import random
class quest_teleport (quest.quest):
    def __init__ (self):
        self.sysfile = VS.getSystemFile()
        self.timer = VS.GetGameTime();
    def teleportNPC (self,un):
        pos=un.Position()
        rsiz = un.rSize()
        size=4*rsiz
        sig = unit.getSignificant (random.randrange(0,50),0,0)
        if (not sig):
            return
        nam = sig.getName()
        if (nam.find ("lackhole")!=-1):
            return
        targetpos = sig.Position()
        arad = sig.rSize()*2+size
        targetpos = Vector.Add(targetpos,(random.uniform(arad,arad*1.5),
                                          random.uniform(arad,arad*1.5),
                                          random.uniform(arad,arad*1.5)))
        targetpos = VS.SafeEntrancePoint (targetpos,rsiz)
        if (size<1000):
            size=1000
        print "kill"
        print un.getName()
        un.SetCurPosition(targetpos)
        VS.playAnimation("warp.ani",pos,size)
        VS.playSound("cloak.wav",pos,(1,0,0))
        VS.playAnimation("warp.ani",targetpos,size)        
        VS.playSound("cloak.wav",targetpos,(1,0,0))
    def teleportPlayer(self,un):
        if (random.randrange(0,20)==0):
            (adj,test) = universe.getAdjacentSystems(self.sysfile,1)
            un.JumpTo(adj)
        else:
            self.teleportNPC (un)
    def teleportUnit (self,un):
        nam = un.getName()
        if ((nam.find ("lackhole")!=-1) or  un.isSun()):
            return
        if (un.isPlayerStarship()==-1):
            self.teleportNPC(un)
        else:
            self.teleportPlayer(un)
    def Execute (self):
        if (VS.getSystemFile()==self.sysfile):
            mytime = VS.GetGameTime();
            if (mytime-self.timer>.5):
                self.timer=mytime
                numunits=VS.getNumUnits()
                if (numunits>0):
                    self.teleportUnit(VS.getUnit(random.randrange(0,numunits)))
        return 1

class quest_teleport_factory (quest.quest_factory):
    def __init__ (self):
        quest.quest_factory.__init__ (self,"quest_teleport")
    def create (self):
        return quest_teleport()



