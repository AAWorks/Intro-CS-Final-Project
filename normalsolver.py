#!/usr/bin/python3

import cgi

class wordscapes:
    total_matches=[]
    def wordtodict(self, word):
        letterdict={}
        for i in range(len(word)):
            if word[i] != '-':
                letterdict[i]=word[i]
        return letterdict
    def solve_normal(self, available_letters):
        posletters=available_letters.replace(',','',available_letters.count(','))
        posletters=posletters.replace(' ','',available_letters.count(' '))
        posletters=posletters.lower()
        with open('http://moe.stuy.edu/~aalonso20/dictionary.txt', 'r') as dict_file:
            for line in dict_file.readlines():
                tempdict=wordscapes().wordtodict(line)
                match1, match2=(True, True)
                templetters=list(tempdict.values())
                templetters=templetters[:-1]
                lengths=list(range(4, len(available_letters)+1))
                if not len(line) in lengths:
                    match1=False
                for templetter in templetters:
                    if templetters.count(templetter) > posletters.count(templetter):
                        match2=False
                if match1==True and match2==True:
                    wordscapes.total_matches.append(line[:-1])

class GUI:
    formData=cgi.FieldStorage()
    def htmlTop(self):
        print('''
Content-type: text/html\n
<!DOCTYPE html>
  <html lang="en-US">
    <head>
      <meta charset="utf-8">
      <title>server-side-script</title>
      <style>
html { 
  background: url(https://www.wordscapescheat.com/resources/images/bgs/bg06.png) no-repeat center fixed; 
  background-size: cover;
}
.heading {
  display: inline-block;
  width: 100%;
  margins: auto;
  border: 2px solid black;
  text-align: center;
  color: white;
  background-color: rgba(0,0,0,0.5);
  font-family: Copperplate; 
  font-style: normal; 
  font-variant: small-caps; 
  font-weight: 700; 
}
#footer {
  background-color: rgba(30, 30, 30, 0.9);
  text-align: center;
  padding: 10px;
  font-size: 10px;
  color: white;
  position:fixed;
  bottom:0;
  left:0;
  right:0;
  height:30px;
}
.filler{
  padding: 5% 0;
  color: Transparent;
}
a:link{
  color: blue;
}
a:visited{
  color: dodgerblue;
}
a:hover{
  color: cyan;
}
a:active{
  color: cyan;
}          
      </style>
    </head>
    <body>''')
    def htmlTail(self):
        print('''
      <div id="footer">
        <p>Alejandro Alonso - <a href='mailto:aalonso20@stuy.edu'>aalonso20@stuy.edu</a> - <a href='https://www.facebook.com/profile.php?id=100026727005426' target='blank_'>Facebook</a> - <a href='https://www.instagram.com/axalonso_/?hl=en' target='blank_'>Instagram</a> - New York City, NY - Jun 2020</p>
      </div>  
    </body>
  </html>
              ''')
    def getletters(self):
        available_letters = GUI().formData.getvalue('available_letters')
        return available_letters
    def getword(self):
        myword = GUI().formData.getvalue('partial_word')
        return myword
    def maincode(self):
        GUI().htmlTop()
        print('''
      <h1 class="heading">Possible words are: {}</h1>
              '''.format(wordscapes().solve_normal(GUI().getword(), GUI().getletters())))
        GUI().htmlTail()

if __name__=='__main__':
    try:
        GUI().maincode()
    except:
        cgi.print_exception()