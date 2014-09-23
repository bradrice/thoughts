Date: 10/21/2010 - 03:13
Author: Brad Rice
Email: brad@bradrice.com
Title: dotcms map lists
Slug: dotcms-map-lists
Tags: dotcms, velocity, arrays, lists, maps
Category: Velocity

Using the array list in dotCMS is pretty straight forward and if you've used arrays in any other script language, you'll see the similarities of using the velocity tools. The power of lists comes when you use maps in dotCMS. Especially, when you use maps within an array list you'll become a velocity power user.

In my earlier article I showed a number of ways to use ArrayLists in dotCMS using velocity templating language. Lists are important to understand especially because the macro that pulls data from the Lucene index in dotCMS returns an array list. The really interesting thing about Array Lists are that they can have hash map members. And that is what #pullContent returns. That's why you can get a variable after calling #pullContent in the foreach statement.

	:::html+velocity
	#foreach($item in $list)
	<p>$item.title</p>
	#end

In this example, I have looped through the $list return variable and put the title field of each item into a p tag. The reason you can refer to the variable item in this way is the list looks something like this much truncated map list:

	:::java
	[{title=Akron's "Better Half"},{title=Along the Towpath}, {title=Ascending Order}, {title=Behind A Diplomatic Curtain}]

Actually if you used the pullContent macro there would be a lot of additional fields. I simplified it for the sake of understanding. The foreach iterates through the list and prints the elements each in a paragraph tag. This is pretty standard fare for working with velocity in dotCMS. (note: dotCMS 1.9.3 is being released with a new pull tool and pullContent will be deprecated, however the principles are the same).

dotCMS gives us two important tools to create lists. dotCMS exposes Map through the contents viewtool.

The contents viewtool has two important methods for creating the list or map collection.

	:::velocity
	$contents.getEmptyList() and $contents.getEmptyMap()

So you usually will want to start by creating an empty list using a set statement. I'll use an example of how to build a list of book titles that start with the letter A. Assume the book title is in the field text4.

First pull all the titles that have a word that starts with A (in this case I'm passing it in the url string so the variable $search_term contains the letter).

	:::velocity
	#set($query = "+text4:${search_term}*")
	#pullContent("+structureInode:1430164 +live:true +deleted:false $query", '0', "text4 asc")
	#set($book_list = $list)
	$booklist now contains my list of books, all of them have a word in the title that begins with A.

now before we iterate, lets make sure we got a list result.

	:::velocity
	#if($book_list.size() > 0)

If we did create the empty list to hold just the books that the first letter of the book is A.

	:::velocity
	#set($contentList = $contents.getEmptyList())

Now loop through the books and put the book into the empty list. I check if the first letter matches the $search_term which is the letter "A." In this case I am adding the book title, identifier, description and then adding it to the empty map $!contentList.

	#!velocity
	#foreach($book in $book_list)
	#set($word = $book.title.trim())
	#if ($word.substring(0,1) == "$search_term")
	#set($item = $contents.getEmptyMap())
	#set($dummy = $item.put('id', $book.identifier))
	#set($dummy = $item.put('title', $word))
	#set($dummy = $item.put('desc', $book.description))
	#set($_dummy = $contentList.add($item))
	#end
	#end

You'll notice that I created an empty map on each loop. The put statements adds each book element to the map. After running this loop you will have a list that looks like this.

	:::java
	[{title=Aim and Progress by Psychology and Other Sciences, desc=This volume is..., id=1463710}, {title=Akron's "Better Half", desc=While the men of Akron busied..., id=1463314}, {title=Along the Towpath, desc=Along the Towpath.., id=1462747}]

I've truncated the description field to save space. Now you can see I have a content list made up of only books that begin with the letter A.

I can now loop through that list to build my html display. You should be able to come up with all kinds of ways to use this combining lists and map lists.

	:::html+velocity
	#foreach($cont in $contentList)
	<div class="book">
	<h4><a href="https://www.uakron.edu/uapress2/book-lists/book-details/index.dot?id=$cont.id">$cont.title</a></h4>
	<p class="desc">$cont.desc.substring(0, 300)&nbsp;&gt;&gt;<a href="https://www.uakron.edu/uapress2/book-lists/book-details/index.dot?id=$cont.id">Read more</a></p>
	</div>
	#end

Note from 2014 after dotcms is now up to 2.5
>By the way, you can now use #set($list = []) and #set($map = {}) as a shortcut to $contents.getEmptyList() and $contents.getEmptyMap()