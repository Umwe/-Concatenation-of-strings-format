# -Concatenation-of-strings-format

【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
Sample Source URL: https://github.com/techgymjp/techgym_python_en
Execution Environment of program: https//colab.research.google.com/
■ 5-1: Concatenation of strings (format()): R7qu.py
【Exercise】
To get same output, you can write as follows:
Update code below using ‘format()’.
【Executed outcome】
【Hints】
□ You can add parameter to ‘format()’.
□ No need to convert parameter to string.
■ Answer is V6vG.py
name1 = ‘Tom’
name2 = ‘Jane
print(name1 + ‘and’ + name2 + ‘are friends.’)
name1 = ‘Tom’
name2 = ‘Jane’
print(‘{} and {} are friends.’.format(name1,name2))
print(name + ‘ bet ’ + str(bet_coin) + ‘coin(s) to ’ + str(bet_cell) 
+ ‘.’
I bet 30 coin(s) to 3.
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-2: Concatenation of strings (Template literal): R7qu.py *Python 3.6 or later
【Exercise】
To get same output, you can write as follows:
Update code below using template literal. 
【Executed outcome】
【Hints】
□ No need to convert variables in {} to string.
■ Answer is Jp9q.py
name1 = ‘Tom’
name2 = ‘Jane
print(name1 + ‘and’ + name2 + ‘are friends.’)
name1 = ‘Tom’
name2 = ‘Jane’
print(f”{name1} and {name2} are friends”)
print(name + ‘ bet ’ + str(bet_coin) + ‘coin(s) to ’ + str(bet_cell) 
+ ‘.’
I bet 30 coin(s) to 3.
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-3: Index in for statement: X5gR.py
【Exercise】
To get same output, you can write as follows:
Update code below like sample code above.
【Executed outcome】
■ Answer is g5Hw.py
friends = [‘Tom’, ’Jane’, ’Brian’]
i = 0
for friend in friends:
print(f”{i}:{friend}”)
i += 1
friends = [‘Tom’, ’Jane’, ’Brian’]
for i, friend in enumerate(friends):
print(f”{i}:{friend}”)
friends = [‘Tom’, ’Jane’, ’Brian’, ‘Carol’, ’Jack’]
i = 0
for friend in friends:
print(f”{i}:{friend}”)
i += 1
1: Tom
2: Jane
3: Brian
4: Carol
5: Jack
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-4: Basic of web scraping: zP8u.py
【Exercise】
Send Request to ‘https://www.bbc.com/news/world’, get response body in text and display it.
【Executed outcome】(Example)
【Hints】
□ To send request, write as ‘requests.get(URL)’.
□ Return statement of ‘requests.get()’ is response body.
□ To get response body in text write as ‘response.text’.
<!DOCTYPE html>
<html lang="en-GB" class="b-pw-1280 no-touch b-reith-sans-font" 
id="responsive-news">
<head>
 <meta name="viewport" content="width=device-width, initialscale=1, user-scalable=1">
 <meta name="robots" content="NOODP,NOYDIR" />
 <meta charset="utf-8">
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
 <meta http-equiv="cleartype" content="on">
...omitted...
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-5: Basic of web scraping: Gu4t.py
【Exercise】
Scrape response body in task 5-4 and display title of news using BeautifulSoup library.
【Executed outcome】(Example)
【Hints】
□ Add ‘from bs4 import BeautifulSoup’ to second line for scraping.
□ You can get elements from response text by writing as follows: 
“BeautifulSoup(response, ‘lxml’)
□ You can get all elements from specific type of tag by writing as follows:
element.find_all(‘tag’)
□ You can get all elements from specific type of tag with class name by writing as follows: 
element.find_all(‘tag’, class_=classname)
□ See response text and find tag and class name to scrape.
□ In example above, tag to scrape is ‘h3’ and class is ‘gs-c-promo-heading__title gel-pica-bold nw-olink-split__text’.
[<h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-linksplit__text">Bots 'skewing the narrative' on Papua unrest</h3>, <h3 
c l a s s = " g s - c - p r o m o - h e a d i n g _ _ t i t l e g e l - p i c a - b o l d n w - o - l i n k -
split__text">Iran women attend first football match in decades</h3>, 
<h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-linksplit__text">German synagogue attack 'was far-right terror'</h3>, <h3 
c l a s s = " g s - c - p r o m o - h e a d i n g _ _ t i t l e g e l - p i c a - b o l d n w - o - l i n k -
split__text">'The Kurds have no friends but the mountains'</h3>, <h3 
c l a s s = " g s - c - p r o m o - h e a d i n g _ _ t i t l e g e l - p i c a - b o l d n w - o - l i n k -
split__text">Trump donors charged in campaign finance case</h3>, <h3 
c l a s s = " g s - c - p r o m o - h e a d i n g _ _ t i t l e g e l - p i c a - b o l d n w - o - l i n k -
split__text">Californians cope with mass power cuts</h3>, <h3 
class="gs-c-promo-heading__title gel- 
...omitted...
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-6: Basic of scraping: Ck8N.py
【Exercise】
Make news titles in 5-5 easy on the eyes.
【Executed outcome】
【Hints】
□ Iterate ‘titles’ with for statement.
□ Get title with ‘title.getText()’.
■ Answer is Wb7m.py
Bots 'skewing the narrative' on Papua unrest
Iran women attend first football match in decades
German synagogue attack 'was far-right terror'
'The Kurds have no friends but the mountains'
Trump donors charged in campaign finance case
Californians cope with mass power cuts
Bots 'skewing the narrative' on Papua unrest
...omitted...
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-7: List, array, numpy
【Introduction】
In previous chapters, list was used as array.
Now let’s study about array in Python.
N-dimensional array is not defined in Python. Numpy.array is alternative.
【Exercise】
Update the last program of chapter 1-4, change list to array.
friends = [‘Tom’, ’Jane’, ’Brian’, ‘Carol’, ’Jack’]
for I, friend in enumerate(friends):
print(f”{i+1}: {friend}”)
import numpy as np
friends = np.array([‘Tom’, ’Jane’, ’Brian’, ‘Carol’, ’Jack’])
for I, friend in enumerate(friends):
print(f”{i+1}: {friend}”)
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-8: Display and resize image file: z4Y2.py
Sample image file: https://github.com/techgymjp/techgym_python/blob/master/cat.jpg
【Introduction】
Execute sample code z4Y2.py and upload image file by clicking ‘Choose file’ button.
You can upload image file on your computer, or you can download sample image above and upload it.
【Exercise】
You’ll see outcome below when you execute z4Y2.py and upload image file.
Let’s reduce file size to 1/10.
【Executed outcome】(Example)
You’ll see scales of horizontal and vertical axis have changed to 1/10 of original ones and image is 
pixelated as it’s resized.
【Hints】
□ ‘Img’ is instance of image which is uploaded.
□ Use ‘cv2.resize(img, None, fx=percentage for horizontal size, fy= percentage for vertical size)’ to resize 
image.
【WiredInAcademy】Python Course Section 5 at「Advanced programming」
1st : min 2nd : min 3rd : min 4th : min 5th : min
■ 5-9: Image editing: Mosaic : D3is.py
【Exercise】
Enlarge image which was reduced in file size in task 5-8 to original file size. It will result in pixelated 
image.
【Executed outcome】(Example)
Image looks like same as outcome in task 5-8, but you’ll see pixelated image with original scale of 
horizontal and vertical axis.
【Hints】
□ Resize image in the same way as task 5-8.
□ Get size of original image before resizing it. (You can get vertical size: image.shape[0], horizontal 
size: img.shape[1])
□ To enlarge image to original file size, write as follow:
‘cv2.resize(img,(horizontal size, vertical size),interpolation=cv2.INTER_NEAREST)’
■ Answer is Qd5W.py
