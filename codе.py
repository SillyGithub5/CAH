import random
import Quotes
import time
languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}languages = {
  "HTML":"html",
  "CSS":"css",
  "JavaScript":"js",
  "Python":"py",
  "Java":"java",
  "C":"c",
  "C++":"cpp",
  "C#":"cs",
  "JSON":"json",
  "SVG":"svg",
  "CSV":"csv",
  "Plain Text":"txt"
}

modes = {
  "html":"html",
  "css":"css",
  "js":"javascript",
  "py":"python",
  "java":"java",
  "c":"c_cpp",
  "cpp":"c_cpp",
  "cs":"csharp",
  "json":"json",
  "svg":"html",
  "csv":"text",
  "txt":"text"
}

filetypes = {
  "html":"text/html",
  "css":"text/css",
  "js":"text/javascript",
  "py":"text/x-python-script",
  "java":"text/plain",
  "c":"text/plain",
  "cpp":"text/plain",
  "cs":"text/plain",
  "json":"application/json",
  "svg":"image/svg+xml",
  "csv":"text/csv",
  "txt":"text/plain"
}

filestarts = {
  "html":"""<!DOCTYPE html>
<html>
	<head></head>
	<body></body>
</html>""",
  "css":"""body {
}""",
  "js":"",
  "py":"",
  "java":"""public class FILENAME {
	public static void main(String[] args) {
		System.out.println("Hello World!");
	}
}""",
  "c":"""#include <stdio.h>

int main(void) {
  printf("Hello World");
  return 0;
}""",
  "cpp":"""#include <iostream>

int main() {
  std::cout << "Hello World!";
}""",
  "cs":"""using System;

class MainClass {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  }
}""",
  "json":"{}",
  "svg":"""<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" xml:space="preserve"></svg>""",
  "csv":"",
  "txt":""
}
BRIND=("Windows", "Apple", "Sony", "Tesla", "Doritos", "Google", "Mojang Studios", "Tesco", "BBC", "Facebook")
brind=random.choice(BRIND)
#cards against humanity 
def CAH():
	STRC= ("a", "b", "c", "d", "e", "f", "g", "h")
	PROD=("iPhone", "Crisp", "OS", "car", "playstation", "bike", "type of cheese", "video game", "gaming console", "CPU", "US flag", "glasses", "Desktop fan", "horror movie", "book", "fruit", "TV Box")
	WHAT=("scams you", "makes money", "is losing money", "Is run by terrorists", "could end the world", "is linked", "lost $1,000,000,000,000", "breaks loads of UK laws", "owns a zoo", "treats its employees", "is selling your info")
	BRAND=("Windows", "Apple", "Sony", "Tesla", "Doritos", "Google", "Mojang Studios", "Tesco", "BBC", "Facebook", "Adidas", "Netflix", "TikTok", "Samsung", "intel", "Amazon", "Sky", "WWF")
	brand=random.choice(BRAND)
	strc=random.choice(STRC)
	prod=random.choice(PROD)
	what=random.choice(WHAT)
	if strc=="a":
		print("How", brand, what)
	elif strc=="b":
		print("Why", brand, "could make the next", prod)
	elif strc=="c":
		print("Why", brand, "never made a", prod)
	elif strc=="d":
		print("Is", brand, "better than", brind)
	elif strc=="e":
		print("Will", brand, "get taken over by", brind)
	elif strc=="f":
		print("Reviewing the new", brand, prod)
	elif strc=="g":
		print("How", brand, "could become the next US state")
	elif strc=="h":
		print("What it's like to work at", brand)
	
def challenge():
	STRC=("a", "b", "c","d")
	CURR=("£100", "£10,000", "£100,000", "1,000,000", "100,000,000", "annual")
	CHAL=("Chilli eating", "art", "coding", "Doritos eating", "Drag", "singing")
	PLCE=("prison", "pizzeria", "school", "police station", "shed", "diner", "factory", "construction site", "McDonalds", "Bank", "random persons house")
	TIME=("30 days", "24hr", "one night", "a year", "some time")
	BRAND=("Windows", "Apple", "Sony", "Tesla", "Doritos", "Google", "Mojang Studios", "Tesco", "BBC", "Facebook", "Adidas", "Netflix", "TikTok", "Samsung", "intel", "Amazon", "Sky", "WWF")
	brand=random.choice(BRAND)
	strc=random.choice(STRC)
	curr=random.choice(CURR)
	chal=random.choice(CHAL)
	plce=random.choice(PLCE)
	time=random.choice(TIME)
	if strc=="a":
		print("Beating the", curr, chal, "challenge")
	elif strc=="b":
		print("Spending", time, "in a", plce)
	elif strc=="c":
		print("Who does the best", chal)
	elif strc=="d":
		print("The", brand, chal, "challenge")
def CAH():
	wait=time.sleep
	print("Welcome to the unofficial")
	print("Cards agains")
	print("Game")
	print(" ")
	NO=[1,11]
	no=chose(NO)
	WLITE=['The blood of christ.', 'A 	middle aged man on roller skates','Being able to talk to elephants.', 'Diversity.', 'Vladimir Putin.','Having chips for eyes','the man who stole my wife', 'Poor life choices.', 'Multiple stab wounds.', 'Some punk kid who stole my turkey sandwich.', 'Getting married, having a few kids, buying some stuff,retiring to Florida, and dying.', 'Pictures of boobs.', 'Old-people smell.','Not wearing pants.', 'Racism.', 'World peace.', 'Having big dreams but no realistic way to achieve them.', 'An AR-15 assault rifle.', 'Former President George W. Bush.','Her Majesty, Queen Elizabeth II.', 'Wondering if it’s possible to get some of that salsa to go.', 'All-you-can-eat  this week. Nothing but kale    juice and','The J.K. Rowling book Harry Potter and the chamber of','When I am President, I will create the Department of', 'Hey guys, welcome to Chili’s! Would you like to start the night off right with?', 'When I am a billionaire, I shall erect a 50-foot statue to commemorate', 'I’m sorry, Professor, but I couldn’t complete my       homework because of', 'This is the way the world ends This is the way the    world ends Not with a bang but with', 'Just saw this upsetting video! Please retweet!! #stop', 'The class field trip was completely ruined by', 'But before I kill you, Mr. Bond I must show you', 'Here is the church Here is the steeple Open the doors And there is','What is George W. Bush thinking about right now?', 'What ended my last relationship?','When Pharaoh remained unmoved, Moses called down a Plague of', 'No matter what people tell me I will never believe    that God created', 'Can i have some money for', 'I`m no doctor but im pretty sure what your suffering from is called', 'My fellow Americans: Before this decade is out, we will have', 'This year i gave the children', 'Yesterday I saw a very wet', '50% of all marriages end in']
	KCALB=['Betcha cant have just one']
	w=int(input("How many card draws?"))
	if w==69 or w==69:
		a1=input("Do you think you're funny?")
		if a1=="Yes" or a1=="yes":
			print("Nobody's laughing")
			print("At all."
			exit()
		elif a1=="No" or a1=="no":
			print("Liar.")
			exit()
		else:
			print("Whats funny is you dont know how to answer a yes or no question"
			exit()
	for q in range(w):
		white=choose(WHITE)
		black=choose(BLACK)
		wait(1)
		print(black,white,"\n","\n")
		now=black+" "+white+"\n"+"\n"
		text=".txt"
		x = "text"
		x=str(x)
		loc2="/storage/emulated/0/.*Python/"
		rando=random.randint(1,827733834883)
		texto=loc2+x+text
		str(now
		text_file = open("*log.txt","a")
		n = text_file.write(now)
		text_file.close()
def mine():
	STRC=("a", "b")
	BRAND=("Windows", "Apple", "Sony", "Tesla", "Doritos", "Google", "Mojang Studios", "Tesco", "BBC", "Facebook", "Adidas", "Netflix", "TikTok", "Samsung", "intel", "Amazon", "Sky", "WWF")
	BLOCK=("dirt", "stone", "random", "explosive", "alive", "hard to break", "edible", "glass", "coal ore")
	brand=random.choice(BRAND)
	strc=random.choice(STRC)
	brandi=brand+"'s"
	block=random.choice(BLOCK)
	if strc=="a":
		print(brandi, "CEO has a minecraft world")
	elif strc=="b":
		print("Minecraft but every block is", block)
	
	
	
O=8
o=1
while 1+1==2:
	tech()
	time.sleep(0.5)
	mine()
	time.sleep(0.5)
	challenge
	time.sleep(0.5)
	
