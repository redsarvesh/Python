#cmd line search engine :->


import webbrowser


import time



print 'This is my search engine'

time.sleep(2)



print 'lets go'
print '_________________________________________________________________'
print '_________________________________________________________________'


x='''
	
        press 1.search about anything
	press 2.search for news
	press 3.search for maps 
	press 4.search for images 
	press 5.search for videos 
	 '''
	 
print x

y=raw_input('Option : ')

if y=='1':
	print 'you have choosen option 1'
	about=raw_input('what do you want to search  :')
	webbrowser.open('https://www.google.com/search?q=%s'%about)
	
	
if y=='2':
	print 'you have choosen option 2'
	news=raw_input('what do you want to search :')
	webbrowser.open('https://www.google.com/search?q=news of %s'%news)
	
	
if y=='3':
	print 'you have choosen option 3'
	maps=raw_input('what do you want to search  :')
	webbrowser.open('https://www.google.com/maps?q=%s'%maps)
	
if y=='4':
	print 'you have choosen option 4'
	images=raw_input('what do you want to search  :')
	webbrowser.open('https://www.google.com/images?q=%s'%images)
	
if y=='5':
	print 'you have choosen option 5'
	videos=raw_input('what do you want to search  :')
	webbrowser.open('https://www.google.com/search?q=videos of %s'%videos)
	
	
if y>'5':
	print 'oops :-< wrong option choosen'