import quest
import quest_drone
import random
import quest_racene
import quest_disappear
import quest_rlaan_spy
import quest_slaver
import quest_shipyard_bomb
import quest_abu_dhabi
import quest_rogue_militia
import quest_teleport
adventures = {"gemini_sector/delta_prime":quest_drone.quest_drone_factory(),
              "enigma_sector/racene":quest_racene.quest_racene_factory(),
              "enigma_sector/axis":quest_disappear.quest_disappear_factory(),
              "enigma_sector/novaya_kiev":quest_rlaan_spy.quest_rlaan_spy_factory(),
              "enigma_sector/rigel":quest_slaver.quest_slaver_factory(),
              "sol_sector/sirius":quest_abu_dhabi.quest_abu_dhabi_factory(),
              "sol_sector/alpha_centauri":quest_shipyard_bomb.quest_shipyard_bomb_factory(),
              "enigma_sector/heinlein":quest_rogue_militia.quest_rogue_militia_factory(),
              "enigma_sector/enigma":quest_teleport.quest_teleport_factory()}

persistent_adventures = [quest_drone.quest_drone_factory()]

def removePersistentAdventure(newq):
    mylen = len(persistent_adventures)
    if (mylen):
        for x in range (mylen):
            if (persistent_adventures[x]==newq):
                del persistent_adventures[x]
                return
            
def newAdventure(playernum,oldsys,newsys):
    newfac=adventures.get (newsys)
    if (newfac):
        newq = newfac.factory(playernum)
        if (newq):#only remove it if that player hasn't done it before
            del adventures[newsys]
            removePersistentAdventure(newfac)
        return newq
    return
#that returns false

def persistentAdventure(playernum):
    for index in range (len(persistent_adventures)):
        ret = persistent_adventures[index].persistent_factory(playernum)
        if (ret):
            del persistent_adventures[index]            
            return ret
    return
