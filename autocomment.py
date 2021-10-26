# -- coding: UTF-8 --
import os
import shutil # shell utilities
import colorama #https://pypi.org/project/colorama/
import time
import argparse
import requests
import json
import datetime
from random import randrange
from colorama import Fore, Style
from InstagramAPI import InstagramAPI #https://github.com/LevPasha/Instagram-API-python

defaultAccount = ""	# Account the bot targets when there is no value given
username = ""		# Your IG account username
password = ""		# Your IG account password
maxTriesInSeconds = 20		# Stop sending requests in seconds after the post should have been uploaded
startrequests = 20			# Start to send requests in seconds before the post should get uploaded
listStrings = ["Cole. His name was Cole. And he had just turned 6 at the time of the accident. It wasn't your fault Lieutenant. A truck skidded on a sheet of ice and your car rolled over. Cole needed emergency surgery, but no human was available to do it. So an android had to take care of it. Cole didn't make it. That's why you hate androids. You think one of us is responsible for your son's death.",
"28 stab wounds, you didn’t want to leave him a chance, huh? Did you feel anger? Hate? He was bleeding, begging for mercy. but you stabbed him, again and again and again!…I know you killed him. Why don’t you say it? Just say “I killed him”! Is it that hard to say?! JUST SAY YOU KILLED HIM! JUST SAY IT!",
"“Sumo, attack!” WOOF “Good dog.“",
"“Why did they make you look so goofy and give you that weird voice?” Connor: “CyberLife androids are designed to work harmoniously with humans. Both my appearance and voice were specifically designed to facilitate my integration.” Hank: “Well, they fucked up.”",
"“I think working with an officer with personal issues is an added challenge, but adapting to human unpredictability is one of my features.” WINK.",
"“My instructions stipulate that I have to accompany you.” Hank: “You know where you can stick your instructions?” Connor: “No... where?”",
"“My name is Connor, im the adroid sent by Cyberlife”",
"“What if we're on the wrong side, Connor? What if we're fighting against people who just want to be free?”",
"🔊🔊🚨🚨WARNING🔊🚨🚨WARNING🚨🚨🔊THIS IS A 🐸DANK 👽MEME❗❗ 🐸ALERT. INCOMING 🐸DANK 👽MEME🐸 👐👌HEADING STRAIGHT 🚀🚀YOUR WAY. 🔜👆👆👆PLEASE TAKE ANY PRECAUTIONS🚧🚧 NECESSARY TO PREPARE YOURSELF FOR THIS 🐸DANK 👽MEME❗❗ 🐸 🌋🌋🌋 .BUCKLE UP♿♿♿ THEM SEATBELTS👮👮,PUT THEM CELLPHONES ON SILENT📵📵 AND LOOSEN THAT ANUS👅👅🍑🍑🍑🍩🍩💩💩 CUZ THIS MEME JUST CAME STRAIGHT OUT OF THE 🚬🚬 🍁🏭🍁🏭🍁🚬🚬DANK FACTORY.",
"😍Guys😍, I’m 😲shaking😲. I’m fucking😲 shaking😲. I never wanted to 👉👌🍆🍑breed 🍑🍆👉👌with anyone more than I want to with 🎃👻Halloween 👻✝️Mercy.✝️🎃️ That 💯perfect,💯 ⏳curvy ⏳😍body.😍 Those 😍bountiful😍 🍈breasts🍈. The 👪child 👪bearing😍 hips😍 of a 🖼️💐literal goddess💐🖼️. It honestly fucking 😳😳hurts😳😳 knowing that I’ll never❤👅💋mate ❤👅💋with her, ⬆pass⬆ my 👖genes👖 through her, and have her 👑birth👑 a set of 👪💯perfect offspring.💯👪 I’d dov fucking💰💰💰 ANYTHING 💰💰",
"Wow Guys 😂😂 being a dank XD memer is hard work so 🅱️🅱️ sorry I'm random XD this is a cool Meme guide 😂 first you neeed to be random!!!111 XD then you need to be a weirdo Looool :p I'm so not normal OMG XD you need to know memes and bring them into R E A L L I F E say to ur teacher u mad bro?? They will go 😜 it's so funny 😂 being a dank memer is hard work😴😴😴 you need the funniest memes to make people know that you! ☝️️☝️️☝️️ are a DANK memer Xd rawr xD",
"🆗 son, 🌞 there ain't❌❌a ☝single☝fucking☝person☝ with any intellect👓👓📖who gives a 🎮remote🎮fuck🎮about your extensive vaping💯😎💨 talent. 😂I happen to be quite🎩the🎩intellectual🎩myself, so I can confirm✔✔this fact💯as truth™.👌if👌you👌think👌 that your vape💯😎💨 is going↗to get you hoes👯👯, you are utterly🐄 mistaken❌, fam👪. my pa👨 once taught📖 me the 😏secret😏 of life👍💛, and it was not❌❌ your vape💯😎💨 🆗🆒now listen 👂👂here my chum✌✌, my pa👨 was a man who kept it 💯💯💯💯💯💯. ✋that✋is✋six✋fucking✋hundreds✋ and he never❌🙅🙅 once vaped💯😎💨. The man 🚬smoked🚬some🚬mad🚬cigars🚬 because he wasnt❌the pussy🐱🐱you are🆗⁉❗⁉ he lived to be 💯 because he kept it 💯💯💯💯💯💯 and killed🔫🔪 👌every👌vaping👌fucker👌he👌saw👌🆗🆒😂😂👀👀 so in the spirit👻of me good ol pa👨, I think💭you should kys🔫 they have 🆓 vapes💯😎💨 in hell🔥and🔥it's🔥lit🔥for😂 unintelligent vaping💯😎💨 hooligans like yourself👌😂😂",
"I'm Rick Harrison, and this is my pawn shop. I work here with my old man and my son, Big Hoss. Everything in here has a story and a price. One thing I've learned after 21 years - you never know what is gonna come through that door.",
"When my dad caught me sucking dick, he made me sit down and suck an entire carton of dicks thinking it would make me sick of sucking dick. Quite the opposite. It was the beginning of my isatiable dick sucking addiction. Every day is a struggle, but with love and support if my friends and wife, I'm doing just fine. Dick free for nine months next week.",
"Can you imagine getting shot on the battlefield, and it hits your can of silly string? Like, everyone thinks you're dead, as you drop to the ground sheerly from the impact. The can saved your life, but your team is unaware as they run up to what they believe to be your corpse, with some god-forsaken foam spilling out of your chest. \"Oh god! Is it chemical warfare?!\" they cry. Your entire crew passes out from panic, and you sit up, covered in silly string, wondering what the fuck just happened.",
"If my girl👧😍 and my beyblades💯🔥 are both drowning🌊😦 and I could only save one😄☝️️ you can Catch me letting it rip at my girls funeral😅👻💀 Cause it's beyblade before getting laid🙏👊 😠💯😭",
"Hillary Clinton TRIGGERS Liberal by SENDING them to NAZI DEATH CAMPS using pure CONSERVATIVE LOGIC and REASONING and then ANGERS SJW by GOING on a RAMPAGE literally RAPING and MURDERING every single MINORITY within a 200 MILE RADIUS then TROLLS Libtard with TRUMP DERANGEMENT SYNDROME by licking Donald Trumps MICROdelaynum of all the DRIED CUM from the CONCEPTION of Barron Trump and he ANGERS democrat by FEEDING upon the FLESH of ABORTED FETUSES and the BLOOD of EVERY single LIBTARD to literally BECOME a GOD AMONG MEN which TROLLS idiot COMMIES by OPENING the seals of HELL and CAUSING the APOCALYPSE in which the DEVIL RAPES CHILDREN and TEARS OFF the heads of Liberal TODDLERS and LITERALLY setting WOMEN's RIGHTS a THOUSAND YEARS and also Ben TRIGGERS the SOCIALISTS by RAPING the UNDEAD CORPSE of LEON TROTSKY and JOSEPH STALIN and he PISSES OFF the LEFTISTS by ESTABLISHING a NEW WORLD ORDER in which he is the SUPREME GOD EMPEROR OF ALL OF THE AMERICAS, CHINA, EUROPE, BRITAIN, TAIWAN, and THAT RANDOM ISLAND IN THE MIDDLE OF THE PACIFIC OCEAN and MURDERS all POLITICAL DISSIDENTS within the government and then he LITERALLY summons CTHULHU and have him and the DEVIL FUCK HIM IN THE ASS while he CUMS all OVER the BOTTLE of LIBERAL TEARS and then he PRANKS Chink Ugayer by IMITATING him and literally dying from the ANAL WOUNDS from Literally being FUCKED IN THE ASS by SATAN and CTHULHU and then ENRAGES the COMMIES by RAPING GOD and BECOMING the NEW ABSOLUTE RULER OF THE UNIVERSE!!! (LIBERALS TROLLED) (NOT CLICKBAIT) (SJWs and FEMINISTS OWNED)"
"⚠️⚠️ warning : you need an IQ of at least 200 to understand this comment ⚠️⚠️ Wa🅱🅱a lu🅱🅱a du🅱 du🅱 i'm pickle Rick 😄😂😂😂 Hit that mf like if you understood👌💯😜"
]
# Make your own list if you're not as stupid as I am
#listStrings = ["I won the giveaway", "Hi there"]

def logShit(text):
	with open('botbeaterlogs.txt', 'w') as f:
		f.write(text)

def unixToDate(value):
	readable = datetime.datetime.fromtimestamp(
		int(value)
	).strftime('%Y-%m-%d %H:%M:%S')
	return readable

def comment(self, mediaId, commentText):
	data = json.dumps({'_uuid': self.uuid,
			'_uid': self.username_id,
			'_csrftoken': self.token,
			'comment_text': commentText})
	return self.SendRequest('media/' + str(mediaId) + '/comment/', self.generateSignature(data))

def getIDLastPost(insta, usuario, username_id):
	user_posts = InstagramAPI.getUserFeed(insta, username_id)
	info = insta.LastJson
	return info['items'][0]['id']

def getPostDate(insta, usuario, username_id, postnumb):
	user_posts = InstagramAPI.getUserFeed(insta, username_id)
	info = insta.LastJson
	return info['items'][postnumb]['taken_at']

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

clear()

cuenta = input("\n\n\n> Enter the name of the account (default: @"+defaultAccount+"): ")
if not cuenta:
	cuenta = defaultAccount
print(Fore.MAGENTA + "\n> Selected account "+cuenta)

autoCalculate = input("Should we automatically calculate the post upload frequency? (y/N)")
if str(autoCalculate) == "y":
	useAuto = True
	print(Fore.RESET + "\nAutomatic mode [ON]")
else:
	useAuto = False
	print(Fore.GREEN + "\nAutomatic mode [OFF]")

# Log into IG
insta = InstagramAPI(username, password)
try:
	print(Fore.MAGENTA + "\n> Logging into IG: "+username+"\n")
	insta.login()
except:
	print(Fore.RED + "[ERR] Instagram Login has failed.")
time.sleep(2)

clear()

InstagramAPI.searchUsername(insta, cuenta)
info = insta.LastJson
username_id = info['user']['pk']

theonebefore = getIDLastPost(insta, cuenta, username_id)	# Get last post ID
if not useAuto:
	selectedComment = listStrings[randrange(0, len(listStrings))]
	lastPost = time.time()
	delaynum = 5
	print("\n\n")
	delaynum = input("Type the delay between each check (IG can ban you if it's too small): ")
	print("\n\n")
	while True:
		if lastPost+int(delaynum) <= time.time():
				lastPost = time.time()
				lastmediaid = getIDLastPost(insta, cuenta, username_id)
				if str(lastmediaid) == theonebefore:	# If no new post is uploaded
					print(Fore.RED + "[ERR] No new posts.")
				else:
					comment(insta, lastmediaid, selectedComment)
					print(Fore.YELLOW + "> New post detected, new media ID: "+str(lastmediaid))
					print(Fore.GREEN + "> Commented on "+str(lastmediaid))
					theonebefore = lastmediaid

else:
	unix1 = getPostDate(insta, cuenta, username_id, 0)
	unix2 = getPostDate(insta, cuenta, username_id, 1)
	delaybetweenposts = unix1 - unix2
	lasttimesincelastpost = time.time()
	attemptingToPost = False

	selectedComment = listStrings[randrange(0, len(listStrings))]


	while True:
		ourtime = time.time()
		timesincelastpost = ourtime - unix1
		if lasttimesincelastpost+1 <= ourtime and not attemptingToPost:
			clear()
			print(Fore.CYAN + "\n\n> Time since last post: "+Fore.GREEN+str(round(timesincelastpost)))
			print(Fore.CYAN + "> Current delay between posts: "+Fore.GREEN+str(delaybetweenposts))
			print(Fore.CYAN + "> Current account selected: "+Fore.GREEN+"@"+str(cuenta))
			print(Fore.CYAN + "> Current selected comment: "+Fore.GREEN+str(selectedComment)+"\n")
			lasttimesincelastpost = ourtime
		if timesincelastpost+startrequests >= delaybetweenposts:
			try:
				attemptingToPost = True
				if delaybetweenposts+maxTriesInSeconds <= timesincelastpost:
					print(Fore.RED + "[ERR] Couldn't find a specific upload pattern, retrying in 15 seconds...")
					unix1 = getPostDate(insta, cuenta, username_id, 0)
					unix2 = getPostDate(insta, cuenta, username_id, 1)
					delaybetweenposts = unix1 - unix2
					print(Fore.RESET + "> Current delay calculated between posts: "+str(delaybetweenposts))
					time.sleep(15)
					attemptingToPost = False
					continue
				lastmediaid = getIDLastPost(insta, cuenta, username_id)
				if str(lastmediaid) == theonebefore:	# If no new post is uploaded
					print(Fore.RED + "[ERR] No new posts.")
					continue
				else:
					print(Fore.YELLOW + "> New post detected, new media ID: "+str(lastmediaid))
					comment(insta, lastmediaid, selectedComment)
					print(Fore.GREEN + "> Commented on "+str(lastmediaid))
					unix1 = getPostDate(insta, cuenta, username_id, 0)
					unix2 = getPostDate(insta, cuenta, username_id, 1)
					timetaken = time.time()-unix1
					delaybetweenposts = unix1 - unix2
					logShit(str(unixToDate(time.time()))+" -> Commented on the account: "+str(cuenta)+" with media ID: "+str(lastmediaid)+". Took "+str(timetaken)+" seconds.")
					theonebefore = lastmediaid
					time.sleep(5)
					attemptingToPost = False
					selectedComment = listStrings[randrange(0, len(listStrings))]
					continue
			except Exception as e:
				print(Fore.RED + "[ERR] Error requesting the last post's ID.")
				print(e)
