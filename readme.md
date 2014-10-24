##:Web Scraper:

This is a python program to download a webpage given a webpage link or a group of webpage links. A group of webpage links can be passed to it using a txt file or a html file with the links in it (<ahref></ahref>). This is somewhat similar to what wget does but i just wanted to try coding it myself.

####:Options

-p      :  Expects a single webpage link. 
-g      :  Expects a group of webpage links
-t      :  Used only if -g option is used. Expects a text file containg 
           group of webpage links
-h      :  Used only if -g option is used. Expects a html page with the 
           links
-o      :  To set the destination folder of the downloads.(_Optional_)


####:Usage

If you want to download a single webpage.

**python webscrape.py -p http://www.google.com**

If you want to download a group of links. There are two methods.
1.Either you input a txt file containing the links on separate lines.
For example:
~links.txt
http://www.google.com
http://www.geeksforgeeks.com
In this case the command is
**python webscrape.py -g -t links.txt**

2. Or you can input a html file with all the links you want to download. The program will search for all the <ahref> tags and then download the list of links obtained from there.
In this case the command is
**python webscrape.py -g -h http://www.geeksforgeeks.org/data-structures/**

You can also specify the destination folder of the downloaded webpages by appending the -o option as such
**python webscrape.py -p www.google.com -o ~/Google**

