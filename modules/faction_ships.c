module faction_ships {
  import random;

  object confed_ships;
  object aera_ships;

  object confed(){
    return confed_ships;
  };

  object aera(){
    return aera_ships;
  };

  void make_ships_list(){
    confed_ships=_olist.new();

    _olist.push_back(confed_ships,"firefly");
    _olist.push_back(confed_ships,"ferret");
    _olist.push_back(confed_ships,"headhunter");
    _olist.push_back(confed_ships,"hellcat");
    _olist.push_back(confed_ships,"hornet");
    _olist.push_back(confed_ships,"rapier");
    _olist.push_back(confed_ships,"centurion");

    aera_ships=_olist.new();

    _olist.push_back(aera_ships,"dagger");
    _olist.push_back(aera_ships,"aeon");
    _olist.push_back(aera_ships,"aevant");
    _olist.push_back(aera_ships,"dralthi");
    _olist.push_back(aera_ships,"jalthi");
    _olist.push_back(aera_ships,"kyta");
    _olist.push_back(aera_ships,"lekra");
  };

  object getRandomShipType(object ship_list){
    int size=_olist.size(ship_list);

    int index=random.randomint(0,size-1);

    object ship_type=_olist.at(ship_list,index);
   
    return ship_type;
  };

}
