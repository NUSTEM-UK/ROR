songdict = {
    "The First Noel":"thefirstnoel:d=4,o=6,b=100:8e5,8d5,c.5,8d5,8e5,8f5,2g5,8a5,8b5,c,b5,a5,2g5,8a5,8b5,c,b5,a5,g5,a5,b5,c,g5,f5,2e5,8e5,8d5,c.5,8d5,8e5,8f5,2g5,8c,8b5,2a5,a5,2g.5,c,b5,a5,g5,a5,b5,c,g5,f5,2e5",
    "Hark the Herald Angels Sing":"Christmas:d=4,o=6,b=112:c5,8p,8f5,f.5,8e5,f5,a5,a5,g5,c,c,c.,8a_5,a5,g5,2a5,c5,f5,f.5,8e5,f5,a5,a5,g5,8c,8g5,8p,g.5,8p,8f5,8e5,8d5,8p,2c5,8p,c,c,c,f5,a_5,a5,a5,g5,c,8p,8c,c,f5,a_5,a5,a5,g5,d,d,d,c,a_5,a5,2a_5,g5,8a5,8a_5,c,8p,8f5,f.5,8g5,2a5,d.,8d,d,c,a_5,a5,2a_5,g5,8a5,8a_5,c.,8f5,2f5,2g5,2f.5",
    "Frosty the Snowman":"Christmas:d=4,o=6,b=112:2g5,e.5,8f5,g5,2c,8b5,8c,d,c,b5,a5,2g.5,8b5,8c,d,c,b5,a5,8g5,c,e.5,8g5,8a5,g5,f5,e5,d5,2g.5,2g5,e.5,8f5,g5,2c,8b5,8c,d,c,b5,a5,2g.5,8b5,8c,d,c,b5,a5,8g5,c,e.5,8g5",
    "We Wish You a Merry Christmas":"WeWishYo:d=4,o=5,b=140:d,g,8g,8a,8g,8f#,e,c,e,a,8a,8b,8a,8g,f#,d,f#,b,8b,8c6,8b,8a,g,e,8d,8d,e,a,f#,2g.",
    "Oh Little Town of Bethlehem":"Oh Little Town of Bethlehem:d=8,o=5,b=120:16c.,16p,f,p,f,p,4f,4g,a,g,a,a#,c.6,16p,4a,4a#,a,16f.,g.,16p.,g,p,2f.,16c.,16p,f,p,f,p,4f,4g,a,g,a,a#,c.6,16p,4a,4a#,a,16f.,g.,16p,32p,g,p,2f",
    "On Ilkley Moor":"On Ilckley Moor:d=8,o=5,b=100:d,g.,16g,g,d,4g,p,a,b.,16b,b,a,4b,p,b,4a,4g,4g,4f#,2g",
    "The 12 Days of Christmas":"12DaysOf:d=8,o=5,b=140:d,d,4d,g,g,4g,f#,g,a,b,c6,a,4b,p,c6,4d6,e6,c6,b,g,4a,2g,d6,d6,4d6,g6,g6,4g6,f#6,g6,a6,b6,c7,a6,2b6,4d7,a,b,4c6,b6,c7,4d7,e7,c7,b6,g6,4a6,2g.6",
    "Rudolph the Red-Nosed Reindeer":"RudolphT:d=16,o=6,b=100:32p,g#5,8a#5,g#5,8f5,8c#,8a#5,4g#.5,g#5,a#5,g#5,a#5,8g#5,8c#,2c,f#5,8g#5,f#5,8d#5,8c,8a#5,4g#.5,g#5,a#5,g#5,a#5,8g#5,8a#5,2f5,g#5,8a#5,a#5,8f5,8c#,8a#5,4g#.5,g#5,a#5,g#5,a#5,8g#5,8c#,2c,f#5,8g#5,f#5,8d#5,8c,8a#5,4g#.5,g#5,a#5,g#5,a#5,8g#5,8d#,2c#",
    "Santa Claus is Coming To Town":"Santa Clause is Coming Tonight:d=4,o=5,b=200:g,8e,8f,g,g.,8g,8a,8b,c6,2c6,8e,8f,g,g,g,8a,8g,f,2f,e,g,c,e,d,2f,b4,1c,p,g,8e,8f,g,g.,8g,8a,8b,c6,2c6,8e,8f,g,g,g,8a,8g,f,f,e,g,c,e,d,2f,b4,1c,p,c6,d6,c6,b,c6,a,2a,c6,d6,c6,b,c6,2a.,d6,e6,d6,c#6,d6,b,b,b,8b,8c6,d6,c6,b,a,g,p,g.,8g,8e,8f,g,g.,8g,8a,8b,c6,2c6,8e,8f,g,g,g,8a,8g,8f,2f,e,g,c,e,d,2f,d6,1c6.",
    "Walking in the Air":"Walkingi:d=4,o=5,b=90:8a#6, 8d#7, 8d#7, 8c#7, 8c#7, 1a#6, 8a#6, 8d#7, 8d#7, 8c#7, 8c#7, 4.a#6, 8f#6, 2g#6, 8g#6, 8a#6, 8a#6, 4.g#6, 8d#6, 8f#6, 8f#6, 8f6, 8f6, 2d#6, 8a#6, 8d#7, 8d#7, 8c#7, 8c#7, 1a#6",
    "Take On Me":"TakeOnMe:d=16,o=5,b=100:8p,a#,a#,a#,8f#,8d#,8g#,8g#,g#,c6,c6,c#6,d#6,c#6,c#6,c#6,8g#,8f#,8a#,8a#,a#,g#,g#,a#,g#,a#,a#,a#,8f#,8d#,8g#,8g#,g#,c6,c6,c#6,d#6,c#6,c#6,c#6,8g#,8f#,8a#,8a#",
    "Airwolf Theme":"Airwolf:d=16,o=6,b=140:a#5,d#,f,g#,c#7,g#,a#,f,g#,d#,f,g#,a#5,d#,f,g#,c#7,g#,a#,f,g#,d#,f,g#,32p,4a#5,d#,f,g#,4a#,c#7,c7,g#,4a#,c#7,c7,g#,4a#,8g#.,c7,4f,4d#,8c#.,d#,8c.,g#5,4a#5,d#,f,g#,4a#,c#7,c7,g#,4a#,c#7,c7,g#,4a#,8g#.,c7,4f,4d#,8c#.,d#,8c.,g#5,4c#,f#,g#,b,4c#7,f#7,f7,b,4c#7,f#7,f7,b,4c#7,b7,a#7,f#7,1g#7",
    "All I Want for Christmas":"AllIWant:d=4,o=6,b=160:c5,e5,g5,8b5,c,b.5,8a5,g.5,d,c,8c,b5,c,b5,8a5,2g5,a5,c,8d,e,d,c,a.5,f5,8g#5,c.,8d,d#,d,a#5,g#.5,c,d,b5,8c,a5,b5,2g#5,c,d,b5,8c,a5,b5,2g#5,g5,a5,8c,g,f,8g,2f,e,d,c,a5,g#5,2d,e,8d.,2c.",
    "Do They Know It's Christmas":"DoTheyKn:d=4,o=5,b=112:2g,c.,8p,2f,e.,8p,a,c6,g,c,f,e,d,c,2g,c.,8p,2f,e.,8p,a,c6,g,c,f,e,d,c,2g,c.,8p,2f,e.,8p,a,c6,g,c,f,e,d,c,2g,c.,8p,2f,e.,8p,a,c6,g,c,f,e,d,c",
    "I'm Dreaming of a White Christmas":"I'mDream:d=4,o=6,b=125:2e,f,e,d_,e,2f,8p,f_,g.,8p,a,b,c7,d7,c7,b,a,2g,c,d,2e,2e,e,2a,g,2c.7,c,d,2e,2e,a,8c,8b5,b5,b5,2c,f,a,2c7",
    "Amazing Grace":"AmazingG:d=8,o=5,b=80:c,f,2f,a,g,f,2a,a,g,2f,4d,2c,c,f,2f,a,g,f,2a,g,a,2c.6",
    "Deck the Halls":"DeckTheH:d=8,o=6,b=140:4g.,f,4e,4d,4c,4d,4e,4c,d,e,f,d,4e.,d,4c,4b5,2c,4g.,f,4e,4d,4c,4d,e,b5,c,g5,d,e,f,d,4e,c,d,c,a5,b5,f5,2c,4d.,e,4f,4d,4e.,f,4g,4d,e,f#,g,d5,a,b,4c7,4b,a,c,g,a5,g5,f5,4g.,f,4e,4d,4c,4d,4e,4c,a,a,a,a,4g.,f,4e,4d,2c",
    "God Rest Ye Merry Gentlemen":"GodRestY:d=8,o=6,b=112:d.,d.,a.,a.,g.,f.,e.,d.,c.,d.,e.,f.,g.,2a,p,d.,d.,a.,a.,g.,f.,e.,d.,c.,d.,e.,f.,g.,2a,p,a.,a#.,g.,a.,a#.,c.7,d.7,a.,g.,f.,d.,e.,f.,4g.,f.,g.,4a.,a#.,a.,a.,g.,f.,e.,4d.,16f.,16e.,d.,4g.,f.,g.,a.,a#.,c.7,d.7,a.,g.,f.,e.,2d.",
    "Joy to the World":"JoyToThe:d=8,o=5,b=112:4d6,c#.6,16b,4a.,g,4f#,4e,4d,p,a,4b,p,b,4c#6,p,c#6,2d.6,p,d6,d6,c#6,b,a,a.,16g,f#,d6,d6,c#6,b,a,a.,16g,f#,f#,f#,f#,f#,16f#,16g,4a.,16g,16f#,e,e,e,16e,16f#,4g,p,16f#,16e,d,d6,p,b,a.,16g,f#,g,4f#,4e,2d",
    "Last Christmas":"LastChri:d=4,o=6,b=112:g,16f5,16p,8g,16f5,16p,8f,16f5,16p,8c,8g,8g,8a,f,16f5,16p,16f5,16p,8c,8g,8g,8a,16d5,16p,f,16d5,16p,8f,8e,8f,8e,d,16d5,16p,16d5,16p,16d5,16p,a,16g5,16p,8a,16g5,16p,g,8d,8a,8a,8a_,g,16g5,16p,16g5,16p,8f,8e,8f,16c5,16p,8e,16c5,16p,8f,16c5,16p,8e,16c5,16p,c,16c5,16p,16c5,16p,16c5,16p,16c5,16p,16d5,16p,8f5,8p,p,2p",
    "Let it Snow":"LetItSno:d=8,o=5,b=125:c,c,c6,c6,4a#,4a,4g,4f,2c,c,c,4g.,f,4g.,f,4e,2c,4d,d6,d6,4c6,4a#,4a,2g.,e.6,16d6,4c6,c.6,16a#,4a,a#.,16a,2f.",
    "Oh Christmas Tree":"OhChrist:d=4,o=5,b=140:c,8f.,16f,f,g,8a.,16a,a.,8p,8a,8g,8a,a#,e,g,f",
    "Oh Come All Ye Faithful":"OhComeAl:d=4,o=5,b=160:g,2g,d,g,2a,2d,b,a,b,c6,2b,a,g,2g,f#,e,f#,g,a,b,2f#,e.,8d,2d.",
    "Silent Night":"SilentNi:d=4,o=5,b=112:g.,8a,g,2e.,g.,8a,g,2e.,2d6,d6,2b.,2c6,c6,2g.,2a,a,c6.,8b,a,g.,8a,g,2e.,2a,a,c6.,8b,a,g.,8a,g,2e.,2d6,d6,f6.,8d6,b,2c6.,2e6.,c6,g,e,g.,8f,d,2c.",
    "We Three Kings":"WeThreeK:d=8,o=6,b=112:4g,f,4d#,c,d,d#,d,4c.,4g,f,4d#,c,d,d#,d,4c.",
    "Winter Wonderland":"WinterWo:d=16,o=5,b=112:8a#.,a#,2a#.,8a#.,a#,4g,2a#,8a#.,a#,2a#.,8a#.,a#,4g#,2a#,8p,a#,8d.6,d6,8d.6,4c.6,8p,c6,8a#.,a#,8a#.,4g#.,8p,g#,8g.,g,8g.,g,8f.,f,8f.,f,2d#,4p,8a#.,a#,2a#.,8a#.,a#,4g,2a#,8a#.,a#,2a#.,8a#.,a#,4g#,2a#,8p,a#,8d.6,d6,8d.6,4c.6,8p,c6,8a#.,a#,8a#.,4g#.,8p,g#,8g.,g,8g.,g,8f.,f,8f.,f,2d#,4p,8d.,d,8b.,b,8e.,e,8c.6,c6,4b,2g,4p,8d.,d,8b.,b,8e.,e,8c.6,c6,2b.,4p",
    "Away in a Manger":"AwayInAM:d=4,o=5,b=140:c,f,f,8g,8a,f,f,8a,8a#,c6,c6,d6,2a#,8g,8a,a#,a#,c6,a,a,8f,8a,g,d,f,2e",
    "Good King Wenceslas":"GoodKing:d=4,o=5,b=100:8f,8f,8f,8g,8f,8f,c,8d,8c,8d,8e,f,f,8f,8f,8f,8g,8f,8f,c,8d,8c,8d,8e,f,f",
    "Jingle Bells Rock":"JingleBe:d=8,o=6,b=125:g5,e,d,c,2g5,g5,e,d,c,2a5,a5,f,e,d,b5,g5,b5,d,g.,16g,f,d,2e,g5,e,d,c,2g5,16f#5,g5,e,d,c,2a5,a5,f,e,d,g,16g,16f#,16g,16f#,16g,16g#,a.,16g,e,d,4c,4g,e,e,e.,16d#,e,e,e.,16d#,e,g,c.,16d,2e,f,f,f.,16f,f,e,e,16e,16e,e,d,d,e,2d",
    "Jingle Bells":"JingleBe:d=2,o=5,b=350:b,b,b,p,b,b,b,p,b,d6,g,a,1b,c6,c6,1c6,b,b,1b,b,a,a,b,1a,d6",
    "Little Drummer Boy":"LittleDr:d=8,o=5,b=140:2c,4p,d,p,e,10p,e,p,e,p,e,p,f,e,16f,5p,2e,4p,d,p,e,p,f,p,g,p,g,p,g,p,a,p,g,f,16e,5p,4d,5p,e,32p,d,e,10p,4c",
    "Oh Christmas Tree":"OhChrist:d=4,o=5,b=100:c,8f.,16f,f.,8g,8a.,16a,a.,8a,8g,8a,a#,e,g,f,8p,8c6,8c6,8a,d.6,8c6,8c6,8a#,a#.,8a#,8a#,8g,c.6,8a#,8a#,8a,a,8p,8c,8f.,8f,f,8g,8a.,16a,a.,8a,8g,8a,a#,e,g,f",
    "I Wish it Could be Christmas Every Day":"IWishItC:d=8,o=6,b=120:16g,a,16g,b.,c.7,b.,a,g.,4a.,16g,f,4a.,16g,1e,g,16g,f#.,g,f#.,16f#,e,16e,d.,e,4d,c.,e.,f#,2d,16d5,d5,d.5,16g,a,16g,b.,c.7,b.,a,g.,4a.,16g,f,4a.,16g,1e,g,16a,2b,16p,b.,2a,16p,b.,a.,g.,b.5,a.5,g.5",
    "It's Beginning to Look a Lot Like Christmas":"It'sBegi:d=16,o=5,b=160:8c,32p,c#.,d#.,f,d#.,d.,p,d#.,4f,4g#,4c6,2d#.,4c.6,32p,c.6,4a#,4g#,2f,4p,f.,p,g.,g#.,a#,g#.,g.,p,g#.,8g.,p,f.,p,e.,8d#,32p,f.,g#.,p,c.6,4d#6,8e,32p,f.,2c#6,2g,2g#",
    "So This is Christmas":"SoThisIs:d=8,o=5,b=80:32p,a,b,c#6,a,e,4p,e,a,b,c#6,4b,4p,16f#,b,c#6,d6,c#6,4b,16e,16e,c#6,e6,16c#6,16b,4a",
    "Have Yourself a Merry Little Christmas":"HaveYour:d=16,o=5,b=100:b,8c,8e.,4g.,b,8c6,8g,4f,p,8e,d,4c,c,4d.,8p,b,8c,8e,4g.,b,8c.6,2g,4p,4e,4g,4c6,d6,8e.6,8d.6,8c6,8b,8a,4g,e,4f,2e,p,8f,g,d,d,8c,8d,a,4c.,4e,4g,b,8c.6,8g,4f.,p,8e,d,8c,d,e,8d.,8e,8p,c,8e,4g.,b,8c6,2g,4p,4e,4g,4c6,4d6,8d.6,c6,p,8b,a,4g#.,8b.,b,2c.6,p",
    "So Here it is Merry Christmas":"SoHereIt:d=4,o=5,b=180:d,e,f#,2g,8a.,b,a,f#.,d,8b.4,f.,d,8c.,a#4,1d,8p,2g,8a.,b,a,f#,d.,b4,f,f,f,f,f.,16e,16d#,d.,16e,16f,1f#",
    "The Prisoner":"ThePriso:d=4,o=6,b=160:8c#7,8b,2c#.,8b,8a,2b.,8a,g#,8a#,8f#,8d,8c#,f#,d,8c#,8f#,8d,8c#,f#,8c#,8b,c#7,b,a,g#,c#,8e,8c#,d#,8a,8b,c#7,b,a,g#,c#,8e,8c#,8d#,8a,b,2c#7,b,8a,8g#,c#,8e,8c#,d#,8e,8f#,g#.,g#.,g#,8g#,8p,8g#,8f#,8g#,8p,8d#,8c#,8d#,8p,8g#,8f#,8g#,8p,8g#7,8f#7,g#7,8f#7,8e7,f#7,8e7,8d#7,8c#7,8g#,f#,c#,8g#7,8f#7,g#7,8f#7,8e7,f#7,8e7,8d#7,8c#7,8e,b5,2a5",
    "Never Going To Give You Up":"rickastley:d=4,o=5,b=120:8f,a#3,g,8c4,8c,8c4,8g,a3,a,8d4,16c6,16a#,8a,8f,a#3,g,8c4,8c,8c4,8a2,a3,d3,16c,16c,16d,16f,16d4,16f,8f,a#3,g,8c4,8c,8c4,8g,a3,a,8d4,16c6,16a#,8a,8f,a#3,g,8c4,8c,8c4,8e,8f,8f,8a3,d4,16f,8f,16f,8a#2,8f3,8d,8e,8f,8f,8g,8e.,16d,c,8c4,c4,b3,8a#2,8d,8d,8e,8f,8d,8a#3,8c,16c6,8p,16p,8c6,8g,8c7,8g6,8c8,8g7,8a#2,8d,8d,8e,8f,8d,8f,8g,8c4,8e,8d,8c,c4,b3,8a#2,8d,8d,8e,8f,8d,c,8g,8g,8g,8a,g,b3,8f,8a#3,8a#2,8a#3,8a#2,8g,8a,8f,8g,8g,8g,8a,8g,8c4,8c,8c4,8a#2,8a#3,8a#2,8a#3,8d,8e,8f,8d,16c4,16p,8g,8a,g.,16c,16d,16f,16d,16a.,16p,32p,8a,16p,g.,16c,16d,16f,16d,16g.,16p,32p,8g,16p,8f.,16e,8d,16c,16d,16f,16d,f,8g,8e.,16d,8c,8c4,8c,8g,8p,2f,16c,16d,16f,16d,16a.,16p,32p,8a,16p,g.,16c,16d,16f,16d,c6,8e,8f.,16e,8d,16c,16d,16f,16d,f,8g,8e.,16d,8c,8c4,8c,8g,8p,2f"
}

eggs = {
    "Airwolf Theme":"airwolf.gif"
    "The Prisoner":"prisoner.gif",
    "Never Going To Give You Up":"rick.gif"
}

