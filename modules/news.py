import VS
import random
import universe
import Director
def saveVal(str):
    return Director.getSaveData(VS.getMissionOwner(),str,0)

class NotZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'
        return saveVal(self.str)!=0
class IsZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'
        return saveVal(self.str)==0
class GreaterZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'        
        return saveVal(self.str)>0
class LessZero:
    def __init__ (self,str):
        self.str = str
    def __nonzero__ (self):
        print 'nonzeroing'        
        return saveVal(self.str)<0

    
news =( ( 'kinneas',(IsZero('kinneas'),),"TEENAGE BOY OUTSMARTS SYSTEM:  A teenager from the Draul Bisa Habitat was caught redhanded on New Poona Mining Base last week, as he was trying to sneak past security without proper identification. The young human male, identified as Kinneas Pinman, somehow managed to make it past spaceport security on Draul Bisa and stow away on a passanger transport bound for the mining base in the Celeste System. While the motives behind Pinman's actions remain unknown, redfaced spaceport officials are hard-pressed to explain how the cheeky computer whizkid managed to elude all their security precautions. Pinman was detained by police on New Poona and will be returned to Draul Bisa within the week."),
        ('congress_convenes',(IsZero('congress_convenes'),),"GREAT CONGRESS CONVENES:  The Great Congress of the Human Star Confederacy convened earlier today at the Confederate Center in Alpha Centauri. On their agenda was discussing possible military intervention against the Rlaan Star Force, because of the increased number of raids they have launched upon Confederate military positions across the border, with loss of human life as a direct result. A plan for a limited retaliatory strike against Rlaan targets on their side of the border was put before the Congress. No decisions were made in the heated debate that followed, with the representatives of Ukraine, Indonesia and Mastif VII leaving the Confederate Center in disgust."),
        ('slaver_guild',(IsZero('slaver_guild'),),"SLAVER GUILD EXPOSED:  An operation lead by the HCS Illustrious working in conjunction with Confederate Special Forces uncovered a Slaver Guild in the Rigel System last week. The slavers were based off an outpost inside an asteroid field, and though they had managed to avoid detection by Navy patrols up till now, they had no such luck this time thanks to intelligence forwarded by the local militia. After the Illustrious overcame the outpost's defenses, the Special Forces unit moved in and secured the station, liberating over a hundred slaves and killing close to forty slavers and capturing twice as many. A large number of Rlaan were discovered on the outpost, and while they will be turned over to Rlaan authorities, a formal complaint is expected to be issued by the General Secretary to the Rlaan government within the week."),
        ('california_missing',(IsZero('california_missing'),),"MISSING SHIP STILL MISSING:   The mysterious disappearance of the HCS California continues to puzzle naval investigators. The Confederate missile cruiser's last known position was in the Axis System, but all contact was lost with it two days ago. Fighter patrols dispatched to search the area, that was reported to be clear of pirates and other hostile elements after extensive sweeps by the military two months ago, came up with nothing. Mutiny or alien intervention cannot be ruled out, according to sources inside the Navy."),
        ('racene_star1',(IsZero('racene_star1'),),"RACENE STAR SOON SECURED:  The battle across the single continent of the habitable moon rages on, as the forces of the Confederate Army continue to push forward towards the 'Devil's Fort', the largest military outpost of the Aera in the entire system. Last month, relieved military human strategists could remove a significant Aera army from their battle maps, after its alien commander surrendered after having been boxed in by hovertanks under the command of General Sulimani Abdullah. The Army expresses hope that the moon, a strategic target in the push against Aera space, will be secured before the end of next month."),
        ('racene_star_tide',(NotZero('racene_star_intro'),IsZero('quest_racene'),IsZero('racene_star_progress'),IsZero('racene_star_tide'),),"TIDE TURNS ON RACENE STAR - FOR THE WORSE:   After a large battle in the space surrounding the moon of racene Star B, the human fleet in orbit was forced to surrender its position and flee back towards friendly space, taking heavy losses in the process and effectively stranding over 75,000 soldiers on the surface below. In the last couple of weeks, things were looking up as Confederate forces began advancing through the lines of the Aera, but military analysts are certain that the offensive will grind to a halt without space support. Scouts also reported that Aera capital ships immediately entered a close orbit around the moon and began bombarding the human positions below with heavy photon disruptor fire and space-to-surface missiles."),
        ('racene_star_victory',(NotZero('racene_star_intro'),NotZero('quest_racene'),IsZero('racene_star_defeat'),IsZero('racene_star_victory'),),"VICTORY AT RACENE STAR:   Troops have taken Devil's Fort after a number of privateers and other civilians heroically stopped a key recon wing that would other wise have discovered the Terran Relief Fleet.  With the cover of the far moon, the terran fleet swooped in and delivered a close range bombardment to the fort.  With the TRF support from the air, Terran Marines flattened the military outposts, causing remaining Aera civilians to abandon much of the planet and retreat to Aera Space"),
        ('racene_star_defeat',(NotZero('racene_star_intro'),NotZero('racene_star_tide'),IsZero('racene_star_quest'),IsZero('racene_star_progress'),IsZero('racene_star_defeat'),IsZero('racene_star_victory'),),"THE STAR CONFEDERATE ARMY LOSES RACENE STAR:   After days of intense fighting, the Terran marines failed to hold off an Aera advance drone army and lost their main command center.  It was not long before the scattered, disorganized band of remaining marines were singly tracked down and destroyed through coordination with the off world Devil's Fort.  Coordination between the offworld starbases and onworld establishments spelled disaster for these stranded marines in enemy turf."),
        ('shipyard_bomb', (IsZero('shipyard_bomb'),),"NAVAL SHIPYARDS HIT BY BOMB:   Disaster struck the Confederate Naval Shipyards orbiting Alpha Centauri two days ago, when a powerful explosive device detonated, crippling a fleet carrier that was nearing completion. At least a dozen casualties were reported with an unknown number of injured, and salvage crews are still working hard to clear the area of wreckage. A team from the CSP (Confederate Security Police) arrived at the shipyards mere hours after the incident, and an investigation has been launched to determine who the perpetrators of this attack were, whether they were human terrorists or agents of an alien power."),
        ('pirate_militia',(IsZero('pirate_militia'),),"ROGUE MILITIA CRUSHED:  With the bulk of the Confederate Navy deployed in the war against the Aera, the protection and defense of civilian trade lines have been left to local militias in many systems. Recent events have proven, though, that some of these militias walk a very fine line between enforcing the law and breaking it. In the Bradshaw System, the militia began charging outrageous toll fees for passage through the system. On those occasions when their demands weren't met, they opened fire. This prompted the Navy to dispatch the HCS Hangzhou to the system, and today the cruiser finally reported arresting the last member of the rogue militia."),
        ('rlaan_rescue',(IsZero('rlaan_rescue'),),"RLAAN RESCUE OPERATION ON HUMAN COLONY:   The human settlers on Keppler Colony experienced a strange incident three days ago, when two Rlaan fighters seemingly on a reconnaissance mission swept in low over the settlement. Then, as they started to gain altitude again, one of them suffered what seemed to be engine trouble and proceeded to crash into the ground, but not before its pilot managed to eject. Less than two hours later, just as the colonists were organizing a rescue party to search the dense forest for the survivor, a Rlaan assault shuttle appeared and dropped a heavily armed commando team equipped with hoverbelts. While six of the alien troopers kept the humans at bay by aiming their weapons at them, the others managed to extract the downed pilot and within fifteen minutes the Rlaan shuttle was on its way again. No shots were fired, and while the condition of the Rlaan pilot remains unknown, no one else was hurt."),
        ('abu_dhabi_return',(IsZero('abu_dhabi_return'),),"ABU DHABI EMERGES:   The HCS Abu Dhabi, presumed lost 89 years ago when it failed to emerge in Sirius after having jumped from Sol, baffled the galaxy yesterday by suddenly appearing again. The crew of the now-obsolete frigate were in perfect health, but were naturally shocked to learn that almost a century had passed since they entered jumpspace, in what they experienced as a perfectly normal instantaneous jump. They have been transfered over to facilities on Holton Station where the General Secretary will meet with them tomorrow. Scientists and engineers are currently busy studying the Abu Dhabi's jump drive in an attempt to figure out what went wrong. This is the only recorded incident of its kind in the history of the Star Confederacy."),
        ('iso_demonstration',(IsZero('iso_demonstration'),),"ISO DEMONSTRATION ON NEW BREMEN:  The ISO (Interplanetary Socialist Organization) organized a demonstration on New Bremen today in the Blake system, protesting against the planet's economic policies and for being 'an Earth puppet'. A large number of police monitored the demonstration which never escalated into violence. The ISO calls itself a political organization, but it has been branded as paramilitary by the CSP. Though it deploys a significant fleet of mostly civilian spacecraft, the ISO has never used them in any recorded assaults against Confederate military or civilian targets. The ISO enjoys a strong following primarily from students and workers on the frontier colonies."),
        ('skull_pirate_arrest',(IsZero('skull_pirate_arrest'),),"THE SKULL ARRESTED!  Christopher 'The Skull' Thorne was finally arrested today in the Draul Bisa Habitat after an interstellar manhunt spanning seven systems. For three years, Thorne was the leader of one of the cruelest and most vicious band of pirates on the frontier, charged with over a hundred counts of murder and space piracy. In light of the Navy's failure to capture Thorne and his lackeys, a group of wealthy merchants banded together and with the help of a powerful mercenary squadron, they were able to decimate Thorne's armada. Thorne himself managed to elude his hunters, until today. He will be transfered to a prison ship until a trial can be scheduled."),
        ('rlaan_mining_spy',(IsZero('rlaan_mining_spy'),),"MINERS EXPOSE RLAAN SPY:  Miners in the Novaya Kiev System were in for a surprise earlier today when they drilled their way into the core of a recently discovered asteroid. The rock wall collapsed only to reveal a small communications and sensor room and a lone Rlaan operating the controls inside it. Before the miners could react, the startled alien scrambled into a small escape pod and launched into space through a narrow tube. The slow mining ship was unable to intercept the pod before a Rlaan fighter uncloaked and retrieved it. The Navy has now invoked a policy to thoroughly scan all suspicious asteroids near military installations and important jump routes in the space adjacent to the Rlaan border, should they contain Rlaan sensor posts.  In addition a hefty price of 20,000 credits has been placed on this spy's head should he be discovered before escaping Confederate space."),
        ('calimanchus_disaster',(IsZero('calimanchus_disaster'),),"ASTEROID STRIKES CALIMANCHUS COLONY:  Disaster struck the Calimanchus colony yesterday when an asteroid the size of a space cruiser somehow managed to make it past the planet's satellite defenses. The asteroid hit ground not far from Port Bernard, the second largest settlement on the planet. Casualties are expected to be tallied in the thousands. The asteroid was large enough to have a profound impact on the enviroment of the entire planet, and as a result, a complete evacuation has been ordered by the local authorities. The Confederate Navy is diverting ships to assist in this endeavour.  The colonies in Calimanchus are relatively young, and it does not enjoy the same satellite protection from interstellar projectiles as the more heavily populated inner worlds do. Still, an investigation will be launched to determine why the two defense satellites in orbit did not react to the approaching danger."),
        ('bert_tribunal',(IsZero('bert_tribunal'),),"MARINE COLONEL TO FACE MILITARY TRIBUNAL:  Colonel Bert Thompson of the Confederate Marine Corps was detained by the CSP earlier this week. He is to stand before a military tribunal where he will be put to trial for his actions on the HCS Coral Sea two months ago. As stated in reports, the Coral Sea had managed to disable and tractor in an Aera transport after having destroyed its escorts. Colonel Thompson and his marines proceeded to board and secure the alien ship, encountering only light resistance. They took 22 prisoners, which Thompson himself interrogated. After Thompson had deemed the interrogations to be finished, he had the prisoners placed in one of the airlocks and then ejected them into space."),)
def newNews():
    newsitem = random.randrange (0,len(news))
    newsitem = news[newsitem]
    player = VS.getMissionOwner()
    for conditional in newsitem[1]:
        print 'conditioning'
        if (not conditional):
            return
    universe.setFirstSaveData(player,newsitem[0],1)
    VS.IOmessage(0,"game","news",newsitem[2])
    

    
