#OPEN BROWSER
openApp("Chrome");
#type("s", Key.WIN);
#wait("1576247803951.png");
#type("Chrome");
#wait("chrome.png");
#type(Key.ENTER);
wait("1576248036385.png");

#GO TO MOCKAROO
type("l", Key.CTRL);
type("mockaroo.com/");
type(Key.ENTER);
wait("1576248104054.png");

#MAKE CONFIGURATIONS TO EXCEL FILE AND DOWNLOAD
click(Pattern("1576248714791.png").targetOffset(361,-5));
click(Pattern("1576247332090.png").targetOffset(353,56));
click(Pattern("1576247370707.png").targetOffset(358,83));
click(Pattern("1576247440235.png").targetOffset(-317,2));
type("a", Key.CTRL);
type("150");
type(Key.TAB);
type("e");
click(Pattern("1576247525481.png").targetOffset(-348,2));

#GO TO DOWNLOAD FOLDER AND CUT THE FILE
rightClick(Pattern("1576247639980.png").targetOffset(-248,4));
click(Pattern("1576247682118.png").targetOffset(-36,13));
wait("1576248442298.png");
type("x", Key.CTRL);

#FIND THE FOLDER AND FILE
type("e", Key.WIN);
wait("1576335822880.png");
type("l", Key.CTRL);
wait("1576338479163.png");
type("C:\Tahma\Work\Ailea");
type(Key.ENTER);
wait("1576249054845.png");
type("v", Key.CTRL);
wait("1576249098428.png");
doubleClick(Pattern("1576336580101.png").targetOffset(-252,29));

#MODIFY DATA
wait("1576248887483.png");
click(Pattern("1576248913394.png").targetOffset(322,-1));
wait(Pattern("1575993800116.png").targetOffset(-571,-30));
click(Pattern("1575993800116.png").targetOffset(-571,-30));
wait(Pattern("1575993854539.png").targetOffset(-130,13));

#FILTER ONLY ".com"-DATA
click(Pattern("1575993854539.png").targetOffset(-130,13));
wait(Pattern("1576338772776.png").exact());
rightClick(Pattern("1576339472907.png").exact())
wait("1576339504288.png");
click(Pattern("1576339504288.png").targetOffset(-4,86));
type("30");
type(Key.ENTER)
click(Pattern("1576339581050.png").targetOffset(113,0));
wait("1576338857238.png");
click(Pattern("1576338857238.png").targetOffset(-82,75));
type(".com" + Key.ENTER);

#SAVE THE FILE AS Ailea_python_exercise
#SELECT ALL, COPY, MAKE NEW FILE, PASTE, SAVE AS, EXCEL FILE TYPE
type("a", Key.CTRL);
type("c", Key.CTRL);
type("n", Key.CTRL);
wait("1576338037416.png");
type("v", Key.CTRL);
wait("1576339907979.png");
type(Key.F12);
wait("1576339955371.png");
type("l", Key.CTRL);
type("a", Key.CTRL);
type("C:\Tahma\Work\Ailea");
type(Key.ENTER);
wait("1576340143800.png");
click(Pattern("1576338154980.png").targetOffset(-140,-65));
type("a", Key.CTRL);
type("Ailea_python_exercise");
type(Key.TAB);
type("e");
type(Key.ENTER);



            