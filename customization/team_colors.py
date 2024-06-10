class TeamColors:
    def __init__(self, team):
        team_data = self._get_team_data(team)
        if team_data:
            self.team = team_data['team']
            self.img = team_data['img']
            self.team_id = team_data['id']
            self.page_name = team_data['pageName']
            self.colors = team_data['colors']
            self.retrocolors = team_data.get('retrocolors', [])
        else:
            raise ValueError(f"Team '{team}' not found.")

    @staticmethod
    def _get_team_data(team_name):
        for team in team_colors:
            if team['team'] == team_name:
                return team
        return None

    def __repr__(self):
        return f"<TeamColors team={self.team}>"


team_colors = [
    {
      "team": "Miami Heat",
      "img": "Southeast Division 2/Heat_Logo.svg",
      "id": "1",
      "pageName": "miami-heat-colors",
      "colors": [
        {
          "colorName": "Miami Heat Red",
          "HEX": "#98002E",
          "RGB": "(152,0,46)",
          "CMYK": "(0,100,61,43)",
          "Pantone": "PMS 202 C"
        },
        {
          "colorName": "Miami Heat Yellow",
          "HEX": "#F9A01B",
          "RGB": "(249,160,27)",
          "CMYK": "(0,43,100,0)",
          "Pantone": "PMS 137 C"
        },
        {
          "colorName": "Miami Heat Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Miami Heat Retro Red",
          "retroHEX": "#BA0C2F",
          "retroRGB": "(186,12,47)",
          "retroCMYK": "(0,100,90,6)"
        },
        {
          "retrocolorName": "Miami Heat Retro Yellow",
          "retroHEX": "#FEDD00",
          "retroRGB": "(254,221,0)",
          "retroCMYK": "(0,1,100,0)"
        }
      ]
    },
    {
      "team": "Los Angeles Lakers",
      "img": "Los-Angeles-Lakers-logo.svg",
      "pageName": "Los-Angeles-Lakers-colors",
      "id": "2",
      "colors": [
        {
          "colorName": "Los Angeles Lakers Purple",
          "HEX": "#552583",
          "RGB": "(85,37,130)",
          "CMYK": "(79,100,0,12)",
          "Pantone": "526"
        },
        {
          "colorName": "Los Angeles Lakers Gold",
          "HEX": "#F9A01B",
          "RGB": "(253,185,39)",
          "CMYK": "(0,30,94,0)",
          "Pantone": "123 C"
        },
        {
          "colorName": "Los Angeles Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK"
        }
      ]
    },
    {
      "team": "Boston Celtics",
      "img": "Boston-Celtics-logo.svg",
      "id": "3",
      "pageName": "Boston-Celtics-colors",
      "colors": [
        {
          "colorName": "Celtics Green",
          "HEX": "#007A33",
          "RGB": "(0,122,51)",
          "CMYK": "(100,0,91,27)",
          "Pantone": "356 C"
        },
        {
          "colorName": "Celtics Gold",
          "HEX": "#BA9653",
          "RGB": "(139,111,78)",
          "CMYK": "(30,40,80,0)",
          "Pantone": "874 C"
        },
        {
          "colorName": "Celtics Brown",
          "HEX": "#963821",
          "RGB": "(150,56,33)",
          "CMYK": "(40,95,100,0)",
          "Pantone": "174 C"
        }
      ]
    },
    {
      "team": "Los Angeles Clippers",
      "id": "",
      "pageName": "Los-Angeles-Clippers-colors",
      "img": "Los-Angeles-Clippers-logos.svg",
      "colors": [
        {
          "colorName": "Red",
          "HEX": "#C8102E",
          "RGB": "(200,16,46)",
          "CMYK": "(2,100,85,6)",
          "Pantone": "186"
        },
        {
          "colorName": "Blue",
          "HEX": "#1D428A",
          "RGB": "(29,66,148)",
          "CMYK": "(100,78,0,18)",
          "Pantone": "7687"
        },
        {
          "colorName": "Silver",
          "HEX": "#BEC0C2",
          "RGB": "(190,192,194)",
          "CMYK": "(0,0,0,29)",
          "Pantone": "COOL GRAY 5"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(0,0,0)",
          "CMYK": "(75,68,67,90)",
          "HSB": "(204,100,0)"
        }
      ]
    },
    {
      "team": "Brooklyn Nets",
      "img": "Brooklyn-Nets-logo.svg",
      "id": "3",
      "pageName": "Brooklyn-Nets-colors",
      "colors": [
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(0,0,0)",
          "CMYK": "(75,68,67,90)",
          "Pantone": "BLACK"
        },
        {
          "colorName": "White",
          "HEX": "#FFFFFF",
          "RGB": "(255,255,255)",
          "CMYK": "(0,0,0,0)",
          "Pantone": "WHITE"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Navy Blue",
          "retroHEX": "#002A60",
          "retroRGB": "(0,42,96)",
          "retroCMYK": "(100,90,33,27)"
        },
        {
          "retrocolorName": "Red",
          "retroHEX": "#CD1041",
          "retroRGB": "(205,16,65)",
          "retroCMYK": "(13,100,73,3)"
        },
        {
          "retrocolorName": "Gray",
          "retroHEX": "#777D84",
          "retroRGB": "(119,125,132)",
          "retroCMYK": "(56,44,40,7)"
        },
        {
          "retrocolorName": "Silver",
          "retroHEX": "#C6CFD4",
          "retroRGB": "(198,207,212)",
          "retroCMYK": "(22,12,12,0)"
        },
        {
          "retrocolorName": "White",
          "retroHEX": "#ffffff",
          "retroRGB": "(255,255,255)",
          "retroCMYK": "(0,0,0,0)"
        }
      ]
    },
    {
      "team": "Charlotte Hornets",
      "img": "Charlotte-Hornets-logo.svg",
      "id": "3",
      "pageName": "Charlotte-Hornets-colors",
      "colors": [
        {
          "colorName": "Hornets Purple",
          "HEX": "#1D1160",
          "RGB": "(29,17,96)",
          "CMYK": "(96,98,38,44)",
          "Pantone": "275 C"
        },
        {
          "colorName": "Teal",
          "HEX": "#00788C",
          "RGB": "(0,120,140)",
          "CMYK": "(100,38,39,7)",
          "Pantone": "3145 C"
        },
        {
          "colorName": "Gray",
          "HEX": "#A1A1A4",
          "RGB": "(161,161,164)",
          "CMYK": "(0,1,0,43)",
          "Pantone": "COOL GRAY 8 C"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Retro Teal",
          "retroHEX": "#00778B",
          "retroRGB": "(0,119,139)",
          "retroCMYK": "(100,0,18,18)"
        },
        {
          "retrocolorName": "Retro Purple",
          "retroHEX": "#280071",
          "retroRGB": "(40,0,113)",
          "retroCMYK": "(100,94,0,0)"
        },
        {
          "retrocolorName": "Retro Orange",
          "retroHEX": "#F9423A",
          "retroRGB": "(249,66,58)",
          "retroCMYK": "(0,79,91,0)"
        }
      ]
    },
    {
      "team": "Chicago Bulls",
      "img": "Chicago-Bulls-logo.svg",
      "id": "3",
      "pageName": "Chicago-Bulls-colors",
      "colors": [
        {
          "colorName": "Bulls Red",
          "HEX": "#CE1141",
          "RGB": "(206,17,65)",
          "CMYK": "(0,100,65,15)",
          "Pantone": "200 C"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(0,0,0)",
          "CMYK": "(75,68,67,90)",
          "Pantone": "BLACK"
        }
      ]
    },
    {
      "team": "Atlanta Hawks",
      "img": "Atlanta-Hawks-Logo.svg",
      "id": "3",
      "pageName": "Atlanta-Hawks-colors",
      "colors": [
        {
          "colorName": "Hawks Red",
          "HEX": "#E03A3E",
          "RGB": "(225,68,52)",
          "CMYK": "(0,91,76,6)",
          "Pantone": "186 C"
        },
        {
          "colorName": "Volt Green",
          "HEX": "#C1D32F",
          "RGB": "(196,214,0)",
          "CMYK": "(29,2,100,0)",
          "Pantone": "PMS 382"
        },
        {
          "colorName": "Hawks Charcoal",
          "HEX": "#26282A",
          "RGB": "(38,40,42)",
          "CMYK": "(73,65,62,67)",
          "Pantone": "PMS 426"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Retro Hawks Red",
          "retroHEX": "#C8102E",
          "retroRGB": "(200,16,46)",
          "retroCMYK": "(100,0,18,18)"
        },
        {
          "retrocolorName": "Retro Hawks Yellow",
          "retroHEX": "#FFCD00",
          "retroRGB": "(255, 205, 0)",
          "retroCMYK": "(0,15,94,0)"
        },
        {
          "retrocolorName": "Retro Hawks Gold",
          "retroHEX": "#87674F",
          "retroRGB": "(135,103,79)",
          "retroCMYK": "(35, 60, 90, 0)"
        }
      ]
    },
    {
      "team": "Phoenix Suns",
      "id": "4",
      "pageName": "phoenix-suns-colors",
      "img": "Northwest Division 2/Phoenix Suns.svg",
      "colors": [
        {
          "colorName": "Phoenix Suns purple",
          "HEX": "#1d1160",
          "RGB": "(29,17,96)",
          "CMYK": "(98,100,0,43)",
          "Pantone": "PMS 275"
        },
        {
          "colorName": "Phoenix Suns orange",
          "HEX": "#E56020",
          "RGB": "(229,95,32)",
          "CMYK": "(0,75,100,5)",
          "Pantone": "PMS 159"
        },
        {
          "colorName": "Phoenix Suns black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK"
        },
        {
          "colorName": "Phoenix Suns gray",
          "HEX": "#63727A",
          "RGB": "(99,113,122)",
          "CMYK": "(15,0,0,65)",
          "Pantone": "PMS 431"
        },
        {
          "colorName": "Phoenix Suns yellow",
          "HEX": "#000000",
          "RGB": "(249,160,27)",
          "CMYK": "(0,43,100,0)",
          "Pantone": "PMS 137"
        },
        {
          "colorName": "Phoenix Suns dark orange",
          "HEX": "#B95915",
          "RGB": "(185,89,21)",
          "CMYK": "(0,67,100,28)",
          "Pantone": "PMS 1675"
        },
        {
          "colorName": "Phoenix Suns light gray",
          "HEX": "#BEC0C2",
          "RGB": "(190,192,194)",
          "CMYK": "(0,0,0,29)",
          "Pantone": "PMS COOL GRAY 5"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Yellow",
          "retroHEX": "#FF6900",
          "retroRGB": "(255,105,0)",
          "retroCMYK": "(0,45,100,0)"
        },
        {
          "retrocolorName": "Orange",
          "retroHEX": "#FFCD00",
          "retroRGB": "(254,80,0)",
          "retroCMYK": "(0,70,100,0)"
        },
        {
          "retrocolorName": "Red",
          "retroHEX": "#EF3340",
          "retroRGB": "(239,51,64)",
          "retroCMYK": "(0,100,100,0)"
        },
        {
          "retrocolorName": "Purple",
          "retroHEX": "#5F259F",
          "retroRGB": "(95,37,159)",
          "retroCMYK": "(95,95,0,0)"
        }
      ]
    },
    {
      "team": "Dallas Mavericks",
      "id": "",
      "pageName": "Dallas-Mavericks-colors",
      "img": "Dallas-Mavericks-logo.svg",
      "colors": [
        {
          "colorName": "Royal blue",
          "HEX": "#00538C",
          "RGB": "(0,83,188)",
          "CMYK": "(100,62,0,0)",
          "Pantone": "PMS 2388"
        },
        {
          "colorName": "Navy blue",
          "HEX": "#002B5e",
          "RGB": "(0,43,92)",
          "CMYK": "(100,64,0,60)",
          "Pantone": "289 C"
        },
        {
          "colorName": "Silver",
          "HEX": "#B8C4CA",
          "RGB": "(187,196,202)",
          "CMYK": "(5,25,0,0)",
          "Pantone": "877 C"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK C"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Blue",
          "retroHEX": "#002855",
          "retroRGB": "(0,40,85)",
          "retroCMYK": "(100,55,0,35)"
        },
        {
          "retrocolorName": "Green",
          "retroHEX": "#00843D",
          "retroRGB": "(0,132,61)",
          "retroCMYK": "(100,0,53,48)"
        }
      ]
    },
    {
      "team": "Denver Nuggets",
      "id": "",
      "pageName": "Denver-Nugget-colors",
      "img": "Denver-Nuggets-logo.svg",
      "colors": [
        {
          "colorName": "Midnight Blue",
          "HEX": "#0E2240",
          "RGB": "(13,34,64)",
          "CMYK": "(100,76,12,70)",
          "Pantone": "289"
        },
        {
          "colorName": "Sunshine Yellow",
          "HEX": "#FEC524",
          "RGB": "(255,198,39)",
          "CMYK": "(0,24,91,0)",
          "Pantone": "123"
        },
        {
          "colorName": "Flatirons Red",
          "HEX": "#8B2131",
          "RGB": "(139, 35, 50)",
          "CMYK": "(29,96,76,29)",
          "Pantone": "202"
        },
        {
          "colorName": "Skyline Blue",
          "HEX": "#1D428A",
          "RGB": "(29,66,138)",
          "CMYK": "(100,86,15,3)",
          "Pantone": "7687"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Navy Blue",
          "retroHEX": "#00285E",
          "retroRGB": "(0,45,98)",
          "retroCMYK": "(100,68,0,54)"
        },
        {
          "retrocolorName": "Powder Blue",
          "retroHEX": "#418FDE",
          "retroRGB": "(81,145,205)",
          "retroCMYK": "(68,34,0,0)"
        },
        {
          "retrocolorName": "Yellow",
          "retroHEX": "#FDB927",
          "retroRGB": "(253,185,39)",
          "retroCMYK": "(0,30,94,0)"
        }
      ]
    },
    {
      "team": "Detroit Pistons",
      "id": "",
      "pageName": "Detriot-Pistons-colors",
      "img": "Detriot-Pistons-logo.svg",
      "colors": [
        {
          "colorName": "Red",
          "HEX": "#C8102E",
          "RGB": "(200,16,46)",
          "CMYK": "(2,100,85,6)",
          "Pantone": "186"
        },
        {
          "colorName": "Royal",
          "HEX": "#1D42BA",
          "RGB": "(29,66,138)",
          "CMYK": "(100,78,0,18)",
          "Pantone": "7687"
        },
        {
          "colorName": "Gray",
          "HEX": "#BEC0C2",
          "RGB": "(181,179,179)",
          "CMYK": "(30,25,25,0)",
          "Pantone": "PMS COOL GRAY 5"
        },
        {
          "colorName": "Navy",
          "HEX": "#002D62",
          "RGB": "(0,45,98)",
          "CMYK": "(100,68,0,54)",
          "Pantone": "PMS 282"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Red",
          "retroHEX": "#ED174C",
          "retroRGB": "(237,23,76)",
          "retroCMYK": "(0,100,65,0)"
        },
        {
          "retrocolorName": "Royal",
          "retroHEX": "#006BB6",
          "retroRGB": "(0,107,182)",
          "retroCMYK": "(100,56,0,0)"
        },
        {
          "retrocolorName": "Navy",
          "retroHEX": "#002D62",
          "retroRGB": "(0,45,98)",
          "retroCMYK": "(100,68,0,54)"
        }
      ]
    },
    {
      "team": "Golden State Warriors",
      "id": "",
      "pageName": "Golden-State-Warriors-colors",
      "img": "Golden-State-Warriors-logo.svg",
      "colors": [
        {
          "colorName": "Warriors Blue",
          "HEX": "#1D428A",
          "RGB": "(29,66,138)",
          "CMYK": "(100 78 0 18)",
          "Pantone": "7687 C"
        },
        {
          "colorName": "Golden yellow",
          "HEX": "#FFC72C",
          "RGB": "(255,199,44)",
          "CMYK": "(0,19,89,0)",
          "Pantone": "123"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Blue",
          "retroHEX": "#041E42",
          "retroRGB": "(4,30,66)",
          "retroCMYK": "(100,90,13,68)"
        },
        {
          "retrocolorName": "Red",
          "retroHEX": "#BE3A34",
          "retroRGB": "(190,58,52)",
          "retroCMYK": "(3,91,86,12)"
        },
        {
          "retrocolorName": "Yellow",
          "retroHEX": "#FFA300",
          "retroRGB": "(255,163,0)",
          "retroCMYK": "(0,41,100,0)"
        },
        {
          "retrocolorName": "Light Blue",
          "retroHEX": "#00A9E0",
          "retroRGB": "(0,169,224)",
          "retroCMYK": "(83,1,0,0)"
        }
      ]
    },
    {
      "team": "Houston Rockets",
      "id": "",
      "pageName": "Houston-Rockets-colors",
      "img": "Houston-Rockets-logo.svg",
      "colors": [
        {
          "colorName": "Red",
          "HEX": "#CE1141",
          "RGB": "(206,17,65)",
          "CMYK": "(0,100,65,15)",
          "Pantone": "200"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK"
        },
        {
          "colorName": "Silver",
          "HEX": "#C4CED4",
          "RGB": "(196,206,211)",
          "CMYK": "(5,0,0,20)",
          "Pantone": "877"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Red",
          "retroHEX": "#BA0C2F",
          "retroRGB": "(186,12,47)",
          "retroCMYK": "(3,100,70,12)"
        },
        {
          "retrocolorName": "Yellow",
          "retroHEX": "#FFC72C",
          "retroRGB": "(255,199,44)",
          "retroCMYK": "(0,19,98,0)"
        }
      ]
    },
    {
      "team": "Indiana Pacers",
      "id": "",
      "pageName": "indiana-pacers-colors",
      "img": "Indiana-Pacers-logo.svg",
      "colors": [
        {
          "colorName": "Pacers blue",
          "HEX": "#002D62",
          "RGB": "(0,45,98)",
          "CMYK": "(100,68,0,54)",
          "Pantone": "282 C"
        },
        {
          "colorName": "Yellow",
          "HEX": "#FDBB30",
          "RGB": "(253,187,48)",
          "CMYK": "(0,15,94,0)",
          "Pantone": "123"
        },
        {
          "colorName": "Silver",
          "HEX": "#BEC0C2",
          "RGB": "(190,192,194)",
          "CMYK": "(0,0,0,29)",
          "Pantone": "COOL GRAY 5 C"
        }
      ]
    },
    {
      "team": "Memphis Grizzlies",
      "id": "",
      "pageName": "Memphis-Grizzlies-colors",
      "img": "Memphis-Grizzlies-logo.svg",
      "colors": [
        {
          "colorName": "Blue",
          "HEX": "#5D76A9",
          "RGB": "(93,118,169)",
          "CMYK": "(64,38,7,2)",
          "Pantone": "652"
        },
        {
          "colorName": "Navy",
          "HEX": "#12173F",
          "RGB": "(18,23,63)",
          "CMYK": "(100,84,45,50)",
          "Pantone": "PMS 289"
        },
        {
          "colorName": "Yellow",
          "HEX": "#F5B112",
          "RGB": "(255,187,34)",
          "CMYK": "(0,23,91,0)",
          "Pantone": "123"
        },
        {
          "colorName": "Gray",
          "HEX": "#707271",
          "RGB": "(112,114,113)",
          "CMYK": "(30,20,19,58)",
          "Pantone": "424"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Teal",
          "retroHEX": "#00B2A9",
          "retroRGB": "(0,178,169)",
          "retroCMYK": "(81,0,39,0)"
        },
        {
          "retrocolorName": "Orange",
          "retroHEX": "#E43C40",
          "retroRGB": "(228,60,64)",
          "retroCMYK": "(5,91,78,0)"
        },
        {
          "retrocolorName": "Brown",
          "retroHEX": "#BC7844",
          "retroRGB": "(188,120,68)",
          "retroCMYK": "(22,57,82,6)"
        }
      ]
    },
    {
      "team": "Milwaukee Bucks",
      "id": "",
      "pageName": "Milwaukee-Bucks-colors",
      "img": "Milwaukee-Bucks-logo.svg",
      "colors": [
        {
          "colorName": "Good land green",
          "HEX": "#00471B",
          "RGB": "(0,71,27)",
          "CMYK": "(80,0,90,75)",
          "Pantone": "PMS 350 C"
        },
        {
          "colorName": "Cream city cream",
          "HEX": "#EEE1C6",
          "RGB": "(240,235,210)",
          "CMYK": "(6,9,23,0)",
          "Pantone": "PMS 468 C"
        },
        {
          "colorName": "Great lakes blue",
          "HEX": "#0077C0",
          "RGB": "(0,125,197)",
          "CMYK": "(100,40,0,0)",
          "Pantone": "2935"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(20,20,20,100)"
        }
      ]
    },
    {
      "team": "Minnesota Timberwolves",
      "id": "",
      "pageName": "Minnesota-Timberwolves-colors",
      "img": "Minnesota-Timberwolves-logo.svg",
      "colors": [
        {
          "colorName": "Midnight blue",
          "HEX": "#0C2340",
          "RGB": "(12,35,64)",
          "CMYK": "(100,76,12,70)",
          "Pantone": "289"
        },
        {
          "colorName": "Lake blue",
          "HEX": "#236192",
          "RGB": "(35,97,146)",
          "CMYK": "(96,54,5,27)",
          "Pantone": "647"
        },
        {
          "colorName": "Moonlight grey",
          "HEX": "#9EA2A2",
          "RGB": "(158,162,162)",
          "CMYK": "(19,12,13,34)",
          "Pantone": "PMS 422"
        },
        {
          "colorName": "Aurora green",
          "HEX": "#78BE20",
          "RGB": "(120,190,32)",
          "CMYK": "(65,0,100,0)",
          "Pantone": "368"
        }
      ]
    },
    {
      "team": "New Orleans Pelicans",
      "id": "",
      "pageName": "New-Orleans-Pelicans-colors",
      "img": "New-Orleans-Pelicans-logo.svg",
      "colors": [
        {
          "colorName": "Pelicans navy",
          "HEX": "#0C2340",
          "RGB": "(0,22,65)",
          "CMYK": "(100,76,12,70)",
          "Pantone": "289 C"
        },
        {
          "colorName": "Pelicans red",
          "HEX": "#C8102E",
          "RGB": "(225,58,62)",
          "CMYK": "(0,91,76,6)",
          "Pantone": "186"
        },
        {
          "colorName": "Pelicans gold",
          "HEX": "#85714D",
          "RGB": "(180,151,90)",
          "CMYK": "(40,48,76,16)",
          "Pantone": "872"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Teal",
          "retroHEX": "#17BFDD",
          "retroRGB": "(0,119,139)",
          "retroCMYK": "(100,0,18,18)"
        },
        {
          "retrocolorName": "Purple",
          "retroHEX": "#280071",
          "retroRGB": "(40,0,113)",
          "retroCMYK": "(100,94,0,0)"
        },
        {
          "retrocolorName": "Orange",
          "retroHEX": "#F9423A",
          "retroRGB": "(249,66,58)",
          "retroCMYK": "(0,79,91,0)"
        }
      ]
    },
    {
      "team": "New York Knicks",
      "id": "",
      "pageName": "New-York-Knicks-colors",
      "img": "New-York-Knicks-logo.svg",
      "colors": [
        {
          "colorName": "Knicks blue",
          "HEX": "#006BB6",
          "RGB": "(0,107,182)",
          "CMYK": "(100,56,0,0)",
          "Pantone": "293 C"
        },
        {
          "colorName": "Knicks orange",
          "HEX": "#F58426",
          "RGB": "(245,132,38)",
          "CMYK": "(0,59,96,0)",
          "Pantone": "165 C"
        },
        {
          "colorName": "Knicks silver",
          "HEX": "#BEC0C2",
          "RGB": "(190,192,194)",
          "CMYK": "(0,0,0,29)",
          "Pantone": "COOL GRAY 5"
        },
        {
          "colorName": "Knicks black",
          "HEX": "#000000",
          "RGB": "(35,31,32)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK"
        }
      ]
    },
    {
      "team": "Oklahoma City Thunder",
      "id": "",
      "pageName": "Oklahoma-City-Thunder-colors",
      "img": "Oklahoma-City-Thunder-logo.svg",
      "colors": [
        {
          "colorName": "Thunder blue",
          "HEX": "#007AC1",
          "RGB": "(0,125,195)",
          "CMYK": "(89,43,0,0)",
          "Pantone": "PMS 285 C"
        },
        {
          "colorName": "Sunset",
          "HEX": "#EF3B24",
          "RGB": "(239,59,36)",
          "CMYK": "(0,92,100,0)",
          "Pantone": "PMS WARM RED C"
        },
        {
          "colorName": "Blue",
          "HEX": "#002D62",
          "RGB": "(0,45,98)",
          "CMYK": "(100,68,54,0)",
          "Pantone": "PMS 282 C"
        },
        {
          "colorName": "Yellow",
          "HEX": "#FDBB30",
          "RGB": "(253,187,48)",
          "CMYK": "(0,29,91,0)",
          "Pantone": "PMS 1235 C"
        }
      ]
    },
    {
      "team": "Orlando Magic",
      "id": "",
      "pageName": "Orlando-Magic-colors",
      "img": "Orlando-Magic-logo.svg",
      "colors": [
        {
          "colorName": "Magic blue",
          "HEX": "#0077C0",
          "RGB": "(0,125,197)",
          "CMYK": "(100,45,0,0)",
          "Pantone": "PMS 2935"
        },
        {
          "colorName": "Silver",
          "HEX": "#C4CED4",
          "RGB": "(196,206,211)",
          "CMYK": "(5,0,0,25)",
          "Pantone": "PMS 877"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(20,20,20,100)",
          "Pantone": "PMS BLACK"
        }
      ]
    },
    {
      "team": "Philadelphia 76ers",
      "id": "",
      "pageName": "Philadelphia-76ers-colors",
      "img": "Philadelphia-76ers-logo.svg",
      "colors": [
        {
          "colorName": "Blue",
          "HEX": "#006BB6",
          "RGB": "(0,107,182)",
          "CMYK": "(100,56,0,0)",
          "Pantone": "PMS 293"
        },
        {
          "colorName": "Red",
          "HEX": "#ED174C",
          "RGB": "(237,23,76)",
          "CMYK": "(0,100,65,0)",
          "Pantone": "PMS 199"
        },
        {
          "colorName": "Navy",
          "HEX": "#002B5C",
          "RGB": "(0,43,92)",
          "CMYK": "(100,64,0,60)",
          "Pantone": "PMS 289"
        },
        {
          "colorName": "Silver",
          "HEX": "#C4CED4",
          "RGB": "(196,206,211)",
          "CMYK": "(5,0,0,20)",
          "Pantone": "PMS 877"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Blue",
          "retroHEX": "#006BB6",
          "retroRGB": "(0,107,182)",
          "retroCMYK": "(100,56,0,0)"
        },
        {
          "retrocolorName": "Red",
          "retroHEX": "#D50032",
          "retroRGB": "(213,0,50)",
          "retroCMYK": "(0,100,65,0)"
        },
        {
          "retrocolorName": "Gold",
          "retroHEX": "#BB9754",
          "retroRGB": "(187,151,84)",
          "retroCMYK": "(27,38,78,3)"
        }
      ]
    },
    {
      "team": "Portland Trail Blazers",
      "id": "",
      "pageName": "Portland-Trailblazers-colors",
      "img": "Portland-Trailblazers-logo.svg",
      "colors": [
        {
          "colorName": "Red",
          "HEX": "#E03A3E",
          "RGB": "(224,58,62)",
          "CMYK": "(0,91,76,6)",
          "Pantone": "PMS 186"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "PMS BLACK"
        }
      ]
    },
    {
      "team": "Sacramento Kings",
      "id": "",
      "pageName": "Sacremento-Kings-colors",
      "img": "Sacremento-Kings-logo.svg",
      "colors": [
        {
          "colorName": "Purple",
          "HEX": "#5A2D81",
          "RGB": "(91,43,130)",
          "CMYK": "(81,100,12,2)",
          "Pantone": "PMS 268"
        },
        {
          "colorName": "Gray",
          "HEX": "#63727A",
          "RGB": "(99,113,122)",
          "CMYK": "(15,0,0,65)",
          "Pantone": "PMS 431"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "PMS BLACK"
        }
      ]
    },
    {
      "team": "San Antonio Spurs",
      "id": "",
      "pageName": "San-Antonio-Spurs-colors",
      "img": "San-Antonio-logo.svg",
      "colors": [
        {
          "colorName": "Silver",
          "HEX": "#C4CED4",
          "RGB": "(196,206,211)",
          "CMYK": "(5,0,0,20)",
          "Pantone": "877"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "PMS BLACK"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Silver",
          "retroHEX": "#8A8D8F",
          "retroRGB": "(138,141,143)",
          "retroCMYK": "(5,0,0,20)"
        },
        {
          "retrocolorName": "Black",
          "retroHEX": "#000000",
          "retroRGB": "(0,0,0)",
          "retroCMYK": "(0,0,0,100)"
        },
        {
          "retrocolorName": "Fuschia",
          "retroHEX": "#EF426F",
          "retroRGB": "(239,66,111)",
          "retroCMYK": "(0,76,38,0)"
        },
        {
          "retrocolorName": "Blue",
          "retroHEX": "#00B2A9",
          "retroRGB": "(0,178,169)",
          "retroCMYK": "(94,0,34,0)"
        },
        {
          "retrocolorName": "Orange",
          "retroHEX": "#FF8200",
          "retroRGB": "(255,130,0)",
          "retroCMYK": "(0,43,87,0)"
        }
      ]
    },
    {
      "team": "Toronto Raptors",
      "id": "",
      "pageName": "Toronto-Raptors-colors",
      "img": "Toronto-Raptors-logo.svg",
      "colors": [
        {
          "colorName": "Red",
          "HEX": "#CE1141",
          "RGB": "(206,17,65)",
          "CMYK": "(0,100,65,15)",
          "Pantone": "PMS 200"
        },
        {
          "colorName": "Black",
          "HEX": "#000000",
          "RGB": "(6,25,34)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "PMS BLACK"
        },
        {
          "colorName": "Silver",
          "HEX": "#A1A1A4",
          "RGB": "(161,161,164)",
          "CMYK": "(0,1,0,43)",
          "Pantone": "PMS COOL GRAY 8"
        },
        {
          "colorName": "Gold",
          "HEX": "#B4975A",
          "RGB": "(180,151,90)",
          "CMYK": "(20,30,70,15)",
          "Pantone": "PMS 872"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Purple",
          "retroHEX": "#753BBD",
          "retroRGB": "(117,59,189)",
          "retroCMYK": "(94,94,0,0)"
        },
        {
          "retrocolorName": "Red",
          "retroHEX": "#BA0C2F",
          "retroRGB": "(186,12,47)",
          "retroCMYK": "(0,100,65,15)"
        },
        {
          "retrocolorName": "Metallic Silver",
          "retroHEX": "#8A8D8F",
          "retroRGB": "(138,141,143)",
          "retroCMYK": "(5,0,0,20)"
        }
      ]
    },
    {
      "team": "Utah Jazz",
      "id": "",
      "pageName": "Utah-Jazz-colors",
      "img": "Utah-Jazz-logo.svg",
      "colors": [
        {
          "colorName": "Navy",
          "HEX": "#002B5C",
          "RGB": "(0,43,92)",
          "CMYK": "(100,64,0,60)",
          "Pantone": "PMS 289"
        },
        {
          "colorName": "Green",
          "HEX": "#00471B",
          "RGB": "(0,71,27)",
          "CMYK": "(80,0,90,75)",
          "Pantone": "350"
        },
        {
          "colorName": "Yellow",
          "HEX": "#F9A01B",
          "RGB": "(249,160,27)",
          "CMYK": "(0,43,100,0)",
          "Pantone": "137"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Purple",
          "retroHEX": "#753BBD",
          "retroRGB": "(117,59,189)",
          "retroCMYK": "(94,94,0,0)"
        },
        {
          "retrocolorName": "Light Blue",
          "retroHEX": "#00A9E0",
          "retroRGB": "(0 169,224)",
          "retroCMYK": "(94,94,0,0)"
        },
        {
          "retrocolorName": "Green",
          "retroHEX": "#006272",
          "retroRGB": "(0,98,114)",
          "retroCMYK": "(100,0,30,30)"
        },
        {
          "retrocolorName": "Cooper",
          "retroHEX": "#954E4C",
          "retroRGB": "(149,78,76)",
          "retroCMYK": "(25,70,70,0)"
        }
      ]
    },
    {
      "team": "Cleveland Cavaliers",
      "id": "Cleveland-Cavaliers-logo.svg",
      "pageName": "Cleveland-Cavaliers-colors",
      "img": "Cleveland-Cavaliers-logo.svg",
      "colors": [
        {
          "colorName": "Cavaliers wine",
          "HEX": "#860038",
          "RGB": "(134,0,56)",
          "CMYK": "(0,100,34,53)",
          "Pantone": "209 C"
        },
        {
          "colorName": "Cavaliers navy",
          "HEX": "#041E42",
          "RGB": "(4,30,66)",
          "CMYK": "(100,90,13,68)",
          "Pantone": "282 C"
        },
        {
          "colorName": "Cavaliers gold",
          "HEX": "#FDBB30",
          "RGB": "(253,187,48)",
          "CMYK": "(0,29,91,0)",
          "Pantone": "1235 C"
        },
        {
          "colorName": "Cavaliers black",
          "HEX": "#000000",
          "RGB": "(0,0,0)",
          "CMYK": "(30,0,0,100)",
          "Pantone": "BLACK"
        }
      ],
      "retrocolors": [
        {
          "retrocolorName": "Orange",
          "retroHEX": "#E35205",
          "retroRGB": "(227,82,5)",
          "retroCMYK": "(0,65,100,0)"
        },
        {
          "retrocolorName": "Blue",
          "retroHEX": "#5C88DA",
          "retroRGB": "(92,136,218)",
          "retroCMYK": "(72,43,0,0)"
        },
        {
          "retrocolorName": "Black",
          "retroHEX": "#27251F",
          "retroRGB": "(39,37,31)",
          "retroCMYK": "(0,0,0,100)"
        }
      ]
    },
    {
      "team": "Washington Wizards",
      "id": "",
      "pageName": "Washington-Wizards-color",
      "img": "Washington-Wizards-Logo.svg",
      "colors": [
        {
          "colorName": "Navy blue",
          "HEX": "#002B5C",
          "RGB": "(0,43,92)",
          "CMYK": "(100,64,0,60)",
          "Pantone": "PMS 289 C"
        },
        {
          "colorName": "Red",
          "HEX": "#E31837",
          "RGB": "(227,24,55)",
          "CMYK": "(0,100,81,4)",
          "Pantone": "PMS 186 C"
        },
        {
          "colorName": "Silver",
          "HEX": "#C4CED4",
          "RGB": "(196,206,212)",
          "CMYK": "(5,0,0,20)",
          "Pantone": "PMS 877"
        }
      ]
    }
  ]