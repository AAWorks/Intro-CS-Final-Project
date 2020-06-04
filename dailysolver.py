#!/usr/bin/python3

import cgi
from urllib.request import urlopen

class wordscapes:
    total_matches=[]
    def wordtodict(self, word):
        letterdict={}
        for i in range(len(word)):
            if word[i] != '-':
                if type(word[i])==int:
                        letterdict[i]=chr(word[i])
                else:
                    letterdict[i]=word[i]
        return letterdict
    def solve_daily(self, available_letters, myword):
        posletters=available_letters.replace(',','',available_letters.count(','))
        posletters=posletters.replace(' ','',available_letters.count(' '))
        posletters=posletters.lower()
        worddict=wordscapes().wordtodict(myword)
        with urlopen(url='http://www.mieliestronk.com/corncob_lowercase.txt') as dict_file:
            for line in dict_file.readlines():
                tempdict=wordscapes().wordtodict(line)
                match1, match2, match3=(True, True, True)
                templetters=list(tempdict.values())
                templetters=templetters[:-2]
                if len(myword) != len(templetters):
                    match1=False
                for num, letter in worddict.items():
                    try:
                        if tempdict[num] != letter:
                            match2=False
                    except:
                        pass
                for templetter in templetters:
                    if templetters.count(templetter) > posletters.count(templetter):
                        match3=False
                if match1==True and match2==True and match3==True:
                    match=''.join(templetters)
                    match=match[0].upper()+match[1:]
                    wordscapes().total_matches.append(match)
        matches=' '.join(map(str, wordscapes().total_matches))
        matches=matches.replace(' ', ', ')
        if bool(wordscapes().total_matches):
            return matches
        else:
            return 'None - Check Submission Values'

class GUI:
    def htmlTop(self):
        print('''
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
        <p>Alejandro Alonso - <a href='mailto:aalonso20@stuy.edu'>aalonso20@stuy.edu</a> - <a href='https://www.facebook.com/profile.php?id=100026727005426' target='blank_'>Facebook</a> - <a href='https://www.instagram.com/axalonso_/?hl=en' target='blank_'>Instagram</a> - Copyrights &copy; 2020 All Rights Reserved - Last Update: Jun 2020</p>
      </div>  
    </body>
  </html>
              ''')
    def getdata(self):
        formData=cgi.FieldStorage()
        available_letters = formData.getvalue('available_letters')
        myword = formData.getvalue('partial_word')
        return [available_letters, myword]
    def maincode(self):
        varlist=GUI().getdata()
        print('Content-type:text/html\n')
        GUI().htmlTop()
        print('''
      <h1 class='filler'>dsf</h1>
      <h1 class="heading">Possible words are: {}</h1>
              '''.format(wordscapes().solve_daily(varlist[0], varlist[1])))
        GUI().htmlTail()

if __name__=='__main__':
    try:
        GUI().maincode()
    except:
        cgi.print_exception()
