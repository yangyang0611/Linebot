from transitions.extensions import GraphMachine

from utils import *  # send_text_message, send_IP12_carousel, send_fsm, send_go_to_menu_button,send_Apple_carousel, send_Menu_carousel, send_info, send_IP12_Pro_carousel, send_IP12_Mini_carousel, send_IP12_Pro_Max_carousel

import requests
from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup


class TocMachine(GraphMachine):
    def __init__(self):
        self.machine = GraphMachine(
            model=self,
            **{
                "states": [
                    'start',
                    'Menu',
                    'place',
                    'themepark',
                    'genting',
                    'genting_introduce',
                    'genting_ticket',
                    'genting_video',
                    'legoland',
                    'legoland_introduce',
                    'legoland_ticket',
                    'legoland_video',
                    'historical',
                    'famosa',
                    'famosa_introduce',
                    'famosa_ticket',
                    'famosa_video',
                    'Kcastle',
                    'Kcastle_introduce',
                    'Kcastle_ticket',
                    'Kcastle_video',

                    'festival',
                    'chinese',
                    'new_year',
                    'new_year_introduce',
                    'new_year_food',
                    'dragon_boat',
                    'dragon_boat_introduce',
                    'dragon_boat_food',
                    'malay',
                    'haji',
                    'haji_introduce',
                    'haji_food',
                    'raya',
                    'raya_introduce',
                    'raya_food',
                    'indian',
                    'deepa',
                    'deepa_introduce',
                    'deepa_food',
                    'thai',
                    'thai_introduce',
                    'thai_food',
                    'fsm'
                ],
                "transitions": [
                    {
                        'trigger': 'advance',
                        'source': '*',
                        'dest': 'fsm',
                        'conditions': 'is_going_to_fsm'
                    },
                    {
                        'trigger': 'advance',
                        'source': '*',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # menu_place

                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'place',
                        'conditions': 'is_going_to_place'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'place',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # place
                    {
                        'trigger': 'advance',
                        'source': 'place',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'place',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'place',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # themepark
                    {
                        'trigger': 'advance',
                        'source': 'themepark',
                        'dest': 'genting',
                        'conditions': 'is_going_to_genting'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'themepark',
                        'dest': 'legoland',
                        'conditions': 'is_going_to_legoland'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'themepark',
                        'dest': 'place',
                        'conditions': 'is_going_to_place'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'themepark',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # genting
                    {
                        'trigger': 'advance',
                        'source': 'genting',
                        'dest': 'genting_introduce',
                        'conditions': 'is_going_to_genting_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting',
                        'dest': 'genting_ticket',
                        'conditions': 'is_going_to_genting_ticket'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting',
                        'dest': 'genting_video',
                        'conditions': 'is_going_to_genting_video'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # genting_introduce
                    {
                        'trigger': 'advance',
                        'source': 'genting_introduce',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting_introduce',
                        'dest': 'genting',
                        'conditions': 'is_going_to_genting'
                    }, {
                        'trigger': 'advance',
                        'source': 'genting_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # genting_ticket
                    {
                        'trigger': 'advance',
                        'source': 'genting_ticket',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting_ticket',
                        'dest': 'genting',
                        'conditions': 'is_going_to_genting'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting_ticket',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # genting_video
                    {
                        'trigger': 'advance',
                        'source': 'genting_video',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting_video',
                        'dest': 'genting',
                        'conditions': 'is_going_to_genting'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'genting_video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # legoland
                    {
                        'trigger': 'advance',
                        'source': 'legoland',
                        'dest': 'legoland_introduce',
                        'conditions': 'is_going_to_legoland_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland',
                        'dest': 'legoland_ticket',
                        'conditions': 'is_going_to_legoland_ticket'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland',
                        'dest': 'legoland_video',
                        'conditions': 'is_going_to_legoland_video'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # legoland_introduce
                    {
                        'trigger': 'advance',
                        'source': 'legoland_introduce',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland_introduce',
                        'dest': 'legoland',
                        'conditions': 'is_going_to_legoland'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # legoland_ticket
                    {
                        'trigger': 'advance',
                        'source': 'legoland_ticket',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland_ticket',
                        'dest': 'legoland',
                        'conditions': 'is_going_to_legoland'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland_ticket',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # legoland_video
                    {
                        'trigger': 'advance',
                        'source': 'legoland_video',
                        'dest': 'themepark',
                        'conditions': 'is_going_to_themepark'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland_video',
                        'dest': 'legoland',
                        'conditions': 'is_going_to_legoland'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'legoland_video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # historical
                    {
                        'trigger': 'advance',
                        'source': 'historical',
                        'dest': 'famosa',
                        'conditions': 'is_going_to_famosa'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'historical',
                        'dest': 'Kcastle',
                        'conditions': 'is_going_to_Kcastle'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'historical',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # famosa
                    {
                        'trigger': 'advance',
                        'source': 'famosa',
                        'dest': 'famosa_introduce',
                        'conditions': 'is_going_to_famosa_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa',
                        'dest': 'famosa_ticket',
                        'conditions': 'is_going_to_famosa_ticket'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa',
                        'dest': 'famosa_video',
                        'conditions': 'is_going_to_famosa_video'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # famosa_introduce
                    {
                        'trigger': 'advance',
                        'source': 'famosa_introduce',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa_introduce',
                        'dest': 'famosa',
                        'conditions': 'is_going_to_famosa'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # famosa_ticket
                    {
                        'trigger': 'advance',
                        'source': 'famosa_ticket',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa_ticket',
                        'dest': 'famosa',
                        'conditions': 'is_going_to_famosa'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa_ticket',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # famosa_video
                    {
                        'trigger': 'advance',
                        'source': 'famosa_video',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa_video',
                        'dest': 'famosa',
                        'conditions': 'is_going_to_famosa'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'famosa_video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # Kcastle
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle',
                        'dest': 'Kcastle_introduce',
                        'conditions': 'is_going_to_Kcastle_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle',
                        'dest': 'Kcastle_ticket',
                        'conditions': 'is_going_to_Kcastle_ticket'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle',
                        'dest': 'Kcastle_video',
                        'conditions': 'is_going_to_Kcastle_video'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # Kcastle_introduce
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_introduce',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_introduce',
                        'dest': 'Kcastle',
                        'conditions': 'is_going_to_Kcastle'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # Kcastle_ticket
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_ticket',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_ticket',
                        'dest': 'Kcastle',
                        'conditions': 'is_going_to_Kcastle'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_ticket',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # Kcastle_video
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_video',
                        'dest': 'historical',
                        'conditions': 'is_going_to_historical'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_video',
                        'dest': 'Kcastle',
                        'conditions': 'is_going_to_Kcastle'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'Kcastle_video',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # menu_festival
                    {
                        'trigger': 'advance',
                        'source': 'Menu',
                        'dest': 'festival',
                        'conditions': 'is_going_to_festival'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'festival',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_festival'
                    },

                    # festival
                    {
                        'trigger': 'advance',
                        'source': 'festival',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'festival',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'festival',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'festival',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },


                    ###
                    # chinese
                    {
                        'trigger': 'advance',
                        'source': 'chinese',
                        'dest': 'new_year',
                        'conditions': 'is_going_to_new_year'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'chinese',
                        'dest': 'dragon_boat',
                        'conditions': 'is_going_to_dragon_boat'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'chinese',
                        'dest': 'festival',
                        'conditions': 'is_going_to_festival'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'chinese',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # new_year
                    {
                        'trigger': 'advance',
                        'source': 'new_year',
                        'dest': 'new_year_introduce',
                        'conditions': 'is_going_to_new_year_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'new_year',
                        'dest': 'new_year_food',
                        'conditions': 'is_going_to_new_year_food'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'new_year',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'new_year',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # new_year_introduce
                    {
                        'trigger': 'advance',
                        'source': 'new_year_introduce',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'new_year_introduce',
                        'dest': 'new_year',
                        'conditions': 'is_going_to_new_year'
                    }, {
                        'trigger': 'advance',
                        'source': 'genting_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # new_year_food
                    {
                        'trigger': 'advance',
                        'source': 'new_year_food',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'new_year_food',
                        'dest': 'new_year',
                        'conditions': 'is_going_to_new_year'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'new_year_food',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # dragon_boat
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat',
                        'dest': 'dragon_boat_introduce',
                        'conditions': 'is_going_to_dragon_boat_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat',
                        'dest': 'dragon_boat_food',
                        'conditions': 'is_going_to_dragon_boat_food'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # dragon_boat_introduce
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat_introduce',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat_introduce',
                        'dest': 'dragon_boat',
                        'conditions': 'is_going_to_dragon_boat'
                    }, {
                        'trigger': 'advance',
                        'source': 'dragon_boat_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # dragon_boat_food
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat_food',
                        'dest': 'chinese',
                        'conditions': 'is_going_to_chinese'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat_food',
                        'dest': 'dragon_boat',
                        'conditions': 'is_going_to_dragon_boat'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'dragon_boat_food',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # malay
                    {
                        'trigger': 'advance',
                        'source': 'malay',
                        'dest': 'haji',
                        'conditions': 'is_going_to_haji'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'malay',
                        'dest': 'raya',
                        'conditions': 'is_going_to_raya'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'malay',
                        'dest': 'festival',
                        'conditions': 'is_going_to_festival'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'malay',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # haji
                    {
                        'trigger': 'advance',
                        'source': 'haji',
                        'dest': 'haji_introduce',
                        'conditions': 'is_going_to_haji_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'haji',
                        'dest': 'haji_food',
                        'conditions': 'is_going_to_haji_food'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'haji',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'haji',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # haji_introduce
                    {
                        'trigger': 'advance',
                        'source': 'haji_introduce',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'haji_introduce',
                        'dest': 'haji',
                        'conditions': 'is_going_to_haji'
                    }, {
                        'trigger': 'advance',
                        'source': 'haji_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # haji_food
                    {
                        'trigger': 'advance',
                        'source': 'haji_food',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'haji_food',
                        'dest': 'haji',
                        'conditions': 'is_going_to_haji'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'haji_food',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # raya
                    {
                        'trigger': 'advance',
                        'source': 'raya',
                        'dest': 'raya_introduce',
                        'conditions': 'is_going_to_raya_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'raya',
                        'dest': 'raya_food',
                        'conditions': 'is_going_to_raya_food'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'raya',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'raya',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # raya_introduce
                    {
                        'trigger': 'advance',
                        'source': 'raya_introduce',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'raya_introduce',
                        'dest': 'raya',
                        'conditions': 'is_going_to_raya'
                    }, {
                        'trigger': 'advance',
                        'source': 'raya_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # raya_food
                    {
                        'trigger': 'advance',
                        'source': 'raya_food',
                        'dest': 'malay',
                        'conditions': 'is_going_to_malay'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'raya_food',
                        'dest': 'raya',
                        'conditions': 'is_going_to_raya'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'raya_food',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # indian
                    {
                        'trigger': 'advance',
                        'source': 'indian',
                        'dest': 'deepa',
                        'conditions': 'is_going_to_deepa'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'indian',
                        'dest': 'thai',
                        'conditions': 'is_going_to_thai'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'indian',
                        'dest': 'festival',
                        'conditions': 'is_going_to_festival'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'indian',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # deepa
                    {
                        'trigger': 'advance',
                        'source': 'deepa',
                        'dest': 'deepa_introduce',
                        'conditions': 'is_going_to_deepa_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'deepa',
                        'dest': 'deepa_food',
                        'conditions': 'is_going_to_deepa_food'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'deepa',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'deepa',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # deepa_introduce
                    {
                        'trigger': 'advance',
                        'source': 'deepa_introduce',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'deepa_introduce',
                        'dest': 'deepa',
                        'conditions': 'is_going_to_deepa'
                    }, {
                        'trigger': 'advance',
                        'source': 'deepa_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # deepa_food
                    {
                        'trigger': 'advance',
                        'source': 'deepa_food',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'deepa_food',
                        'dest': 'deepa',
                        'conditions': 'is_going_to_deepa'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'deepa_food',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # thai
                    {
                        'trigger': 'advance',
                        'source': 'thai',
                        'dest': 'thai_introduce',
                        'conditions': 'is_going_to_thai_introduce'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'thai',
                        'dest': 'thai_food',
                        'conditions': 'is_going_to_thai_food'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'thai',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'thai',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # thai_introduce
                    {
                        'trigger': 'advance',
                        'source': 'thai_introduce',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'thai_introduce',
                        'dest': 'thai',
                        'conditions': 'is_going_to_thai'
                    }, {
                        'trigger': 'advance',
                        'source': 'thai_introduce',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },

                    # thai_food
                    {
                        'trigger': 'advance',
                        'source': 'thai_food',
                        'dest': 'indian',
                        'conditions': 'is_going_to_indian'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'thai_food',
                        'dest': 'thai',
                        'conditions': 'is_going_to_thai'
                    },
                    {
                        'trigger': 'advance',
                        'source': 'thai_food',
                        'dest': 'Menu',
                        'conditions': 'is_going_to_Menu'
                    },
                ],
                "initial": 'start',
                "auto_transitions": False,
                "show_conditions": True,
            },
        )

    def is_going_to_Menu(self, event):
        text = event.message.text
        return "Menu" in text or "menu" in text

    def go_back_Menu(self, event):
        text = event.message.text
        return "Menu" in text or "menu" in text

    # menu_place
    def is_going_to_place(self, event):
        text = event.message.text
        return '觀光景點' in text

    def go_back_place(self, event):
        text = event.message.text
        return "觀光景點" in text

    # themepark
    def is_going_to_themepark(self, event):
        text = event.message.text
        return "游樂園" in text

    def go_back_themepark(self, event):
        text = event.message.text
        return "游樂園" in text

    # genting
    def is_going_to_genting(self, event):
        text = event.message.text
        return "雲頂高原" in text

    def is_going_to_genting_introduce(self, event):
        text = event.message.text
        return "景點介紹" in text

    def is_going_to_genting_ticket(self, event):
        text = event.message.text
        return "門票及規定" in text

    def is_going_to_genting_video(self, event):
        text = event.message.text
        return "雲頂高原影片介紹" in text

    def go_back_genting(self, event):
        text = event.message.text
        return "雲頂高原" in text

    # legoland
    def is_going_to_legoland(self, event):
        text = event.message.text
        return "樂高主題樂園" in text

    def is_going_to_legoland_introduce(self, event):
        text = event.message.text
        return "景點介紹" in text

    def is_going_to_legoland_ticket(self, event):
        text = event.message.text
        return "門票及規定" in text

    def is_going_to_legoland_video(self, event):
        text = event.message.text
        return "樂高主題樂園影片介紹" in text

    def go_back_legoland(self, event):
        text = event.message.text
        return "樂高主題樂園" in text

    # historical
    def is_going_to_historical(self, event):
        text = event.message.text
        return "歷史古跡" in text

    def go_back_historical(self, event):
        text = event.message.text
        return "歷史古跡" in text

    # famosa
    def is_going_to_famosa(self, event):
        text = event.message.text
        return "法摩沙堡" in text

    def is_going_to_famosa_introduce(self, event):
        text = event.message.text
        return "景點介紹" in text

    def is_going_to_famosa_ticket(self, event):
        text = event.message.text
        return "門票及規定" in text

    def is_going_to_famosa_video(self, event):
        text = event.message.text
        return "法摩沙堡影片介紹" in text

    def go_back_famosa(self, event):
        text = event.message.text
        return "法摩沙堡" in text

    # Kcastle
    def is_going_to_Kcastle(self, event):
        text = event.message.text
        return "凱莉古堡" in text

    def is_going_to_Kcastle_introduce(self, event):
        text = event.message.text
        return "景點介紹" in text

    def is_going_to_Kcastle_ticket(self, event):
        text = event.message.text
        return "門票及規定" in text

    def is_going_to_Kcastle_video(self, event):
        text = event.message.text
        return "凱莉古堡影片介紹" in text

    def go_back_Kcastle(self, event):
        text = event.message.text
        return "凱莉古堡" in text

    # menu_festival
    def is_going_to_festival(self, event):
        text = event.message.text
        return "節日" in text

    def go_back_festival(self, event):
        text = event.message.text
        return "節日" in text

    # chinese
    def is_going_to_chinese(self, event):
        text = event.message.text
        return "華人" in text

    def go_back_chinese(self, event):
        text = event.message.text
        return "華人" in text

    # new_year
    def is_going_to_new_year(self, event):
        text = event.message.text
        return "農曆新年" in text

    def is_going_to_new_year_introduce(self, event):
        text = event.message.text
        return "農曆新年由來" in text

    def is_going_to_new_year_food(self, event):
        text = event.message.text
        return "農曆新年食物" in text

    def go_back_new_year(self, event):
        text = event.message.text
        return "農曆新年" in text

    # dragon_boat
    def is_going_to_dragon_boat(self, event):
        text = event.message.text
        return "端午節" in text

    def is_going_to_dragon_boat_introduce(self, event):
        text = event.message.text
        return "端午節由來" in text

    def is_going_to_dragon_boat_food(self, event):
        text = event.message.text
        return "端午節食物" in text

    def go_back_dragon_boat(self, event):
        text = event.message.text
        return "端午節" in text

    # malay
    def is_going_to_malay(self, event):
        text = event.message.text
        return "馬來人" in text

    def go_back_malay(self, event):
        text = event.message.text
        return "馬來人" in text

    # raya
    def is_going_to_raya(self, event):
        text = event.message.text
        return "開齋節" in text

    def is_going_to_raya_introduce(self, event):
        text = event.message.text
        return "開齋節由來" in text

    def is_going_to_raya_food(self, event):
        text = event.message.text
        return "開齋節食物" in text

    def go_back_raya(self, event):
        text = event.message.text
        return "開齋節" in text

    # haji
    def is_going_to_haji(self, event):
        text = event.message.text
        return "哈芝節" in text

    def is_going_to_haji_introduce(self, event):
        text = event.message.text
        return "哈芝節由來" in text

    def is_going_to_haji_food(self, event):
        text = event.message.text
        return "哈芝節食物" in text

    def go_back_haji(self, event):
        text = event.message.text
        return "哈芝節" in text

    # indian
    def is_going_to_indian(self, event):
        text = event.message.text
        return "印度人" in text

    def go_back_indian(self, event):
        text = event.message.text
        return "印度人" in text

    # deepa
    def is_going_to_deepa(self, event):
        text = event.message.text
        return "屠妖節" in text

    def is_going_to_deepa_introduce(self, event):
        text = event.message.text
        return "屠妖節由來" in text

    def is_going_to_deepa_food(self, event):
        text = event.message.text
        return "屠妖節食物" in text

    def go_back_deepa(self, event):
        text = event.message.text
        return "屠妖節" in text

    # thai
    def is_going_to_thai(self, event):
        text = event.message.text
        return "大寶森節" in text

    def is_going_to_thai_introduce(self, event):
        text = event.message.text
        return "大寶森節由來" in text

    def is_going_to_thai_food(self, event):
        text = event.message.text
        return "大寶森節食物" in text

    def go_back_thai(self, event):
        text = event.message.text
        return "大寶森節" in text

    # fsm

    def is_going_to_fsm(self, event):
        text = event.message.text
        return "fsm" in str(text).lower()

    # on enter
    def on_enter_Menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_Menu_carousel(reply_token)

    # place 他是屬於menu的部分，不需要back
    def on_enter_place(self, event):
        print("I'm entering place")
        reply_token = event.reply_token
        send_place_carousel(reply_token)

    # themepark
    def on_enter_Back_themepark(self, event):
        print("I'm entering themepark")
        reply_token = event.reply_token
        send_themepark_carousel(reply_token)

    def on_enter_themepark(self, event):
        print("I'm entering themepark")
        reply_token = event.reply_token
        send_themepark_carousel(reply_token)

    # genting
    def on_enter_Back_genting(self, event):
        print("I'm entering genting")
        reply_token = event.reply_token
        send_genting_carousel(reply_token)

    def on_enter_genting(self, event):
        print("I'm entering genting")
        reply_token = event.reply_token
        send_genting_carousel(reply_token)

    def on_enter_genting_introduce(self, event):
        print("I'm entering genting_introduce")
        reply_token = event.reply_token
        word = "景點介紹"
        information = "雲頂高原是馬來西亞最大、最著名的一座建立在高原上的旅游勝地。\n高山海拔2000公尺，全年氣溫22度左右。\n這裏山巒重叠，視野遼闊，夜間西觀可欣賞吉隆坡輝煌的燈火。這裏是當地人周末休閒娛樂的熱門去處。遊客需要先乘坐纜車到達山頂，或者自行開車上山頂也行。\n\n遊樂園分為室外場及室內場，在室外場可以體驗過山車、跳樓機、超人飛等驚險刺激的遊樂項目。\n\n室內場則有適合親子遊玩的迷你火車、航天船以及小朋友專屬的馬戲團乘騎、熱帶雨林樂園等設施。"
        current = "雲頂高原"
        brand = "游樂園"
        send_info(reply_token, word, information, current, brand)

    def on_enter_genting_ticket(self, event):
        print("I'm entering genting_ticket")
        reply_token = event.reply_token
        word = "門票"
        information = "雲頂高原的SnowWorld門票是RM45。\n在這裏你可以天體驗零下的環境，包括栩栩如生的降雪，冰屋及古代羅馬的遺跡。更不用説，雪橇滑梯提供了成人和兒童數小時的娛樂！"
        current = "雲頂高原"
        brand = "游樂園"
        send_info(reply_token, word, information, current, brand)

    def on_enter_genting_video(self, event):
        print("I'm entering genting Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=l0-F1MUisNk'
        send_text_message(reply_token, url)

    # legoland
    def on_enter_Back_legoland(self, event):
        print("I'm entering legoland")
        reply_token = event.reply_token
        send_legoland_carousel(reply_token)

    def on_enter_legoland(self, event):
        print("I'm entering legoland")
        reply_token = event.reply_token
        send_legoland_carousel(reply_token)

    def on_enter_legoland_introduce(self, event):
        print("I'm entering legoland_introduce")
        reply_token = event.reply_token
        word = "景點介紹"
        information = "樂高主題樂園有7和園區，共70個游樂設施，分別是有樂高積木堆積而成。\n包含亞洲18個國家景點組成【迷你樂園】。\n\n最受歡迎的是以中世紀為背景的【樂高王國】，以及法老和恐龍為主題的【探險之地】。"
        current = "樂高主題樂園"
        brand = "游樂園"
        send_info(reply_token, word, information, current, brand)

    def on_enter_legoland_ticket(self, event):
        print("I'm entering legoland_ticket")
        reply_token = event.reply_token
        word = "門票"
        information = "樂高主題樂園門票如下：\n主題樂園：成人：RM189  小孩：RM149\n主題樂園+海底世界：成人：RM249  小孩：RM200\n主題樂園+海底世界+水上樂園：成人：RM313  小孩：RM249"
        current = "樂高主題樂園"
        brand = "游樂園"
        send_info(reply_token, word, information, current, brand)

    def on_enter_legoland_video(self, event):
        print("I'm entering legoland Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=G3K_2qb7rIc'
        send_text_message(reply_token, url)

    # historical
    def on_enter_Back_historical(self, event):
        print("I'm entering historical")
        reply_token = event.reply_token
        send_historical_carousel(reply_token)

    def on_enter_historical(self, event):
        print("I'm entering historical")
        reply_token = event.reply_token
        send_historical_carousel(reply_token)

    # famosa
    def on_enter_Back_famosa(self, event):
        print("I'm entering famosa")
        reply_token = event.reply_token
        send_famosa_carousel(reply_token)

    def on_enter_famosa(self, event):
        print("I'm entering famosa")
        reply_token = event.reply_token
        send_famosa_carousel(reply_token)

    def on_enter_famosa_introduce(self, event):
        print("I'm entering famosa_introduce")
        reply_token = event.reply_token
        word = "景點介紹"
        information = "法摩沙城堡是葡萄牙人在1511年为了防止荷兰人入侵所见的堡垒。后来遭英国人炸毁，现在只剩城门和城门前的大炮。"
        current = "法摩沙堡"
        brand = "歷史古跡"
        send_info(reply_token, word, information, current, brand)

    def on_enter_famosa_ticket(self, event):
        print("I'm entering genting_ticket")
        reply_token = event.reply_token
        word = "門票"
        information = "法摩沙堡是戶外參觀空間，不需要任何入門票，但不准破壞公物哦！"
        current = "法摩沙堡"
        brand = "歷史古跡"
        send_info(reply_token, word, information, current, brand)

    def on_enter_famosa_video(self, event):
        print("I'm entering famosa Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=jzPXPoYfG2A'
        send_text_message(reply_token, url)

    # Kcastle

    def on_enter_Back_Kcastle(self, event):
        print("I'm entering Kcastle")
        reply_token = event.reply_token
        send_Kcastle_carousel(reply_token)

    def on_enter_Kcastle(self, event):
        print("I'm entering Kcastle")
        reply_token = event.reply_token
        send_Kcastle_carousel(reply_token)

    def on_enter_Kcastle_introduce(self, event):
        print("I'm entering Kcastle_introduce")
        reply_token = event.reply_token
        word = "景點介紹"
        information = "凱莉古堡是一棟為完工的建築，是凱莉先生爲了獻給其未婚妻的禮物。可惜在工程接近尾聲，凱莉忽然逝世而宣告工程停止。這是一棟歐式建築，包括馬棚、升降梯、天臺網球場、地下酒窖和密道。"
        current = "凱莉古堡"
        brand = "歷史古跡"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Kcastle_ticket(self, event):
        print("I'm entering Kcastle_ticket")
        reply_token = event.reply_token
        word = "門票"
        information = "凱莉古堡門票如下：\n成人：RM5\n小孩：RM3"
        current = "凱莉古堡"
        brand = "歷史古跡"
        send_info(reply_token, word, information, current, brand)

    def on_enter_Kcastle_video(self, event):
        print("I'm entering Kcastle Video")
        reply_token = event.reply_token
        url = 'https://www.youtube.com/watch?v=3Th0XQ3OTiY'
        send_text_message(reply_token, url)

    # festival

    def on_enter_festival(self, event):
        print("I'm entering festival")
        reply_token = event.reply_token
        send_festival_carousel(reply_token)

    # chinese
    def on_enter_Back_chinese(self, event):
        print("I'm entering chinese")
        reply_token = event.reply_token
        send_chinese_carousel(reply_token)

    def on_enter_chinese(self, event):
        print("I'm entering chinese")
        reply_token = event.reply_token
        send_chinese_carousel(reply_token)

    # new_year
    def on_enter_Back_new_year(self, event):
        print("I'm entering new_year")
        reply_token = event.reply_token
        send_new_year_carousel(reply_token)

    def on_enter_new_year(self, event):
        print("I'm entering Kcastle")
        reply_token = event.reply_token
        send_new_year_carousel(reply_token)

    def on_enter_new_year_introduce(self, event):
        print("I'm entering new_year_introduce")
        reply_token = event.reply_token
        word = "節日介紹"
        information = "傳説有一隻凶猛的野獸【年獸】會在除夕夜出來吃人。\n它害怕紅色、火光及嘈雜的聲音。\n於是人們在門口貼紅紙，燃放炮竹來避開【年獸】。\n第二天【恭喜】之聲不絕於耳，空氣中彌漫著打敗【年獸】的喜悅。"
        current = "農曆新年"
        brand = "華人"
        send_info(reply_token, word, information, current, brand)

    def on_enter_new_year_food(self, event):
        print("I'm entering new_year_food")
        reply_token = event.reply_token
        myTuple = (
            "魚：魚🐟象征着“盈余”，我们看到一年下来赚取和节省下来的钱，自然是开心的。而且吃不同品种的鱼，代表的吉祥意思也不同呢！",
            "餃子：饺子的形状很像银锭，所以也有吃的饺子越多，新年积累的财富越多的意思。",
            "春捲：由于春卷金黄的外表，所以吃春卷时说的吉祥话有：黄金万两，寓意大富大贵。",
            "年糕：年糕主要由糯米、糖、栗子、枣、荷叶等组成。有“年年高”的意思，即象征着生活、学业、事业越来越好。",
            "湯圓：我们一般在元宵节才会吃汤圆，但在南方的很多地方，人们在春节也会吃汤圆，就像北方人吃饺子一样。“汤圆”和“团圆”发音相似，所以这也是汤圆受到人们青睐的原因。",
            "長壽麵：长寿面的长度比一般的面条要长，象征着“长寿”，除了生日的时候会吃，在春节也有人会吃长寿面。",
            "好運果：橘子、橙子、柚子是我们经常在春节期间吃到的水果，而且因为它们长得又圆，颜色又是金黄色，象征着圆满和财富，因而受到人们的喜爱。橙子的“橙”与“成”谐音，寓意成功。橘子的“橘”与“吉”谐音，象征吉祥。柚子的“柚”与“有”谐音，寓意富足。"
        )
        x = "\n\n".join(myTuple)

        word = "食物介紹"
        information = x
        current = "農曆新年"
        brand = "華人"
        send_info(reply_token, word, information, current, brand)

    # dragon_boat
    def on_enter_Back_dragon_boat(self, event):
        print("I'm entering dragon_boat")
        reply_token = event.reply_token
        send_new_year_carousel(reply_token)

    def on_enter_dragon_boat(self, event):
        print("I'm entering dragon_boat")
        reply_token = event.reply_token
        send_dragon_boat_carousel(reply_token)

    def on_enter_dragon_boat_introduce(self, event):
        print("I'm entering dragon_boat_introduce")
        reply_token = event.reply_token
        word = "節日介紹"
        information = "春秋時期，屈原是楚國大臣.當時楚國被秦軍攻下，屈原不忍捨棄祖國，於是在5月5日跳江自盡。百姓很哀痛，爲了不讓魚蝦食飽身軀，用樹葉包飯丟入江中。從此有了划龍舟、吃粽子、喝黃酒的習俗。."
        current = "端午節"
        brand = "華人"
        send_info(reply_token, word, information, current, brand)

    def on_enter_dragon_boat_food(self, event):
        print("I'm entering dragon_boat_food")
        reply_token = event.reply_token
        myTuple = (
            "粽子：端午節習俗必吃的就是粽子啦！大家應該都知道屈原的故事，在古代荊楚地區，端午時大家會煮糯米飯或蒸粽糕投入江中，以祭祀屈原。所以到端午的時候家家戶戶都會吃粽子。",
            "黃酒：有一個古老傳說端午節時白素貞不慎喝下雄黃酒，現出白蛇原形嚇死許仙的故事，所以古代人就認為雄黃可以剋制蛇、蠍等百蟲！古人不但把雄黃粉末撒在蚊蟲孳生的地方，還飲用雄黃酒來祈望能夠避邪，讓自己不生病。",
            "菜豆：臺灣有端午節應景俗諺曰：「食菜豆食至老老，食茄人較會超騰。」所以在古時候端午節習俗大家都會吃菜豆。"
        )

        x = "\n\n".join(myTuple)
        word = "食物介紹"
        information = x
        current = "端午節"
        brand = "華人"
        send_info(reply_token, word, information, current, brand)

    # malay
    def on_enter_Back_malay(self, event):
        print("I'm entering malay")
        reply_token = event.reply_token
        send_malay_carousel(reply_token)

    def on_enter_malay(self, event):
        print("I'm entering malay")
        reply_token = event.reply_token
        send_malay_carousel(reply_token)

    # haji
    def on_enter_Back_haji(self, event):
        print("I'm entering haji")
        reply_token = event.reply_token
        send_haji_carousel(reply_token)

    def on_enter_haji(self, event):
        print("I'm entering haji")
        reply_token = event.reply_token
        send_haji_carousel(reply_token)

    def on_enter_haji_introduce(self, event):
        print("I'm entering haji_introduce")
        reply_token = event.reply_token
        word = "節日介紹"
        information = "哈芝節是爲了紀念預言者伊布拉辛犧牲自己兒子作爲上蒼的供奉品。其實上蒼並沒有要他真正犧牲兒子，只是要考驗他對自己的忠誠。最後上蒼給了伊布拉辛一頭羊取代兒子作爲犧牲品。"
        current = "哈芝節"
        brand = "馬來人"
        send_info(reply_token, word, information, current, brand)

    def on_enter_haji_food(self, event):
        print("I'm entering haji_food")
        reply_token = event.reply_token
        myTuple = (
            "哈芝節不會特別吃什麽。",
            "但哈芝節最重要的三件事就是祈禱、獻祭和分享。在哈芝節期間，穆斯林們要穿上他們最好的衣服，到清真寺里聆聽布道並虔誠祈禱。",
            "上午的禱告會之後，下午就要舉行儀式屠宰牛、羊和駱駝。這些作為「獻牲」的牲畜要預先買好，好吃好喝要把它們餵養的壯壯的。一般經濟條件較好的男性穆斯林，每人要宰一隻羊，七人合宰一頭牛或一峰駱駝。"
        )

        x = "\n\n".join(myTuple)
        word = "食物介紹"
        information = x
        current = "哈芝節"
        brand = "馬來人"
        send_info(reply_token, word, information, current, brand)

    # raya
    def on_enter_Back_raya(self, event):
        print("I'm entering raya")
        reply_token = event.reply_token
        send_raya_carousel(reply_token)

    def on_enter_raya(self, event):
        print("I'm entering raya")
        reply_token = event.reply_token
        send_raya_carousel(reply_token)

    def on_enter_raya_introduce(self, event):
        print("I'm entering raya_introduce")
        reply_token = event.reply_token
        word = "節日介紹"
        information = "穆罕默德在傳教前，會定期到山上沉思默禱。這天沉思時突然接到安拉（神明）的啓示，命他以【使者】身份傳教。因此把這個月定爲齋戒月，以示紀念。"
        current = "開齋節"
        brand = "馬來人"
        send_info(reply_token, word, information, current, brand)

    def on_enter_raya_food(self, event):
        print("I'm entering raya_food")
        reply_token = event.reply_token
        myTuple = (
            "马来粽：類似華人的粽子，他們會把米飯包在葉子裏，然後封口煮沸。\n比較不同的是，葉子裏包的是存米飯，沒有別的配菜\n（作者認爲：蠻..蠻難吃的0_0)。",
            "仁儅：全世界的食客都应当感谢印尼的米南卡堡族部落，因为他们发明了这道浓郁的椰香干酱美食。作为节日大餐的常客，通常仁当会搭配牛肉或者鸡肉烹制。",
            "馬來粥：在斋戒月，这道清淡且浓稠的斋戒月肉粥非常常见，而且由于其配方可以随意调整，因此相对来说也非常受欢迎。"
        )

        x = "\n\n".join(myTuple)
        word = "食物介紹"
        information = x
        current = "開齋節"
        brand = "馬來人"
        send_info(reply_token, word, information, current, brand)

    # indian
    def on_enter_Back_indian(self, event):
        print("I'm entering indian")
        reply_token = event.reply_token
        send_indian_carousel(reply_token)

    def on_enter_indian(self, event):
        print("I'm entering indian")
        reply_token = event.reply_token
        send_indian_carousel(reply_token)

    # deepa
    def on_enter_Back_deepa(self, event):
        print("I'm entering deepa")
        reply_token = event.reply_token
        send_deepa_carousel(reply_token)

    def on_enter_deepa(self, event):
        print("I'm entering deepa")
        reply_token = event.reply_token
        send_deepa_carousel(reply_token)

    def on_enter_deepa_introduce(self, event):
        print("I'm entering deepa_introduce")
        reply_token = event.reply_token
        word = "節日介紹"
        information = "屠妖節起源有不同説法。\n南印度：歡慶光明守護神克里斯南爲他們鏟除惡魔之王那拉卡。\n北印度：是作爲慶祝英雄羅摩神殺死魔王羅波那的節日。"
        current = "屠妖節"
        brand = "印度人"
        send_info(reply_token, word, information, current, brand)

    def on_enter_deepa_food(self, event):
        print("I'm entering deepa_food")
        reply_token = event.reply_token

        myTuple = (
            "椰糖：椰糖是一种味道浓郁，以椰奶为主的糖果。它是一种mithai甜点，令人难以抗拒的经典的印度开胃菜。\n(作者認爲：這超級好吃啊啊啊(╹ڡ╹ )",
            "Ladoo：Ladoo是屠妖节里最重要的甜点。Ladoo是一种高尔夫球般大小的糕点，有多种口味，最常见的是酥油Ladoo、坚果Ladoo、以及用玫瑰水和糖浆所调成的Ladoo，这些甜点会为您的味蕾带来天堂般的享受。",
            "Murukku：“Murukku”在泰米尔语的意思是“卷曲”，是一个几乎可在所有印度家庭里都可以找到的美食，它的来源与屠妖节有关。它由黑扁豆、米粉制成，再以辣椒以及Carom种子调味。最令人惊讶的是，尽管这个松脆的饼干是油炸而成的，但它不会油腻！"
        )

        x = "\n\n".join(myTuple)

        word = "食物介紹"
        information = x
        current = "屠妖節"
        brand = "印度人"
        send_info(reply_token, word, information, current, brand)

    # thai
    def on_enter_Back_thai(self, event):
        print("I'm entering thai")
        reply_token = event.reply_token
        send_thai_carousel(reply_token)

    def on_enter_thai(self, event):
        print("I'm entering thai")
        reply_token = event.reply_token
        send_thai_carousel(reply_token)

    def on_enter_thai_introduce(self, event):
        print("I'm entering thai_introduce")
        reply_token = event.reply_token
        word = "節日介紹"
        information = "大寶森節是在淡米爾曆10月，他們俗稱的“泰月”。\n而這個月在恰逢滿月便是“寶森”時分，所以叫做大寳森節。"
        current = "大寶森節"
        brand = "印度人"
        send_info(reply_token, word, information, current, brand)

    def on_enter_thai_food(self, event):
        print("I'm entering thai_food")
        reply_token = event.reply_token
        myTuple = (
            "Pongal：這是一種用米和奶在陶罐中烹煮成與節日同名的食物。",
            "大寳森節不會特別吃什麽，但人們還會舉行敬牛儀式，給牛洗澡、染牛角、以好食款待牛隻、牽牛遊行或舉辦賽牛會等",
            "另外，這天信徒會以針和鉤子刺穿自己的身體，把敬神物品鈎在皮肉之上，一路爬完黑風洞（馬來西亞的一個山洞）的272級階梯，抵達石灰岩洞穴內的印度教神廟參拜。"
        )

        x = "\n\n".join(myTuple)
        word = "食物介紹"
        information = x
        current = "大寶森節"
        brand = "印度人"
        send_info(reply_token, word, information, current, brand)

    # FSM

    def on_enter_fsm(self, event):
        print("I'm entering fsm")
        reply_token = event.reply_token
        send_fsm(reply_token)
