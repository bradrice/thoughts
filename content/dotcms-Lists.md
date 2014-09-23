Date: 09/24/2010 - 21:02
Author: Brad Rice
Email: brad@bradrice.com
Title: dotCMS - working with velocity and lists
Slug: dotcms-lists
Tags: dotcms, velocity, arrays
Category: Velocity

Scripting is a common activity for the web developer. dotCMS has a built in templating language called Velocity and it isn't really a full featured scripting language, but allows the web designer/developer a way to build dynamic webpages. Velocity is rather limited in scope if you look at the core macros it provides. However, standard viewtools expand it's basic functionality and dotCMS has even expanded that basic set of tools with their own viewtools.

One of the most common things one needs to do when building dynamic web pages is loop through a set of query results and display those results. dotCMS has some built in macros for pulling content and what it returns is a list of hash items. So you can iterate through the results and print the fields as needed. However, there are times you need more control over your results. Fortunately dotCMS provides a viewtool called "contents" that has two very helpful methods.

The Java Programming language has a standard framework for working with collections. There are two core collections specified (collections and maps) See [Java Collections](http://download.oracle.com/javase/tutorial/collections/interfaces/index.html) Interfaces. Of the collections core it is broken down. The one that dotcms exposes is List. dotcms also exposes Map through the contents viewtool.

The contents viewtool has two important methods for creating the list or map collection.

	:::velocity
	$contents.getEmptyList() and $contents.getEmptyMap()

You use these methods in a set statement. So if you want to create a new empty list use it like this:

	:::velocity
	#set($contentList = $contents.getEmptyList())

Now the unusual part that takes some getting used to for people coming from another script language is adding items to the list. You have to do it inside a set statement so it doesn't print to your screen. So you create an unnecessary variable in the process.

	:::velocity
	#set($_dummy = $contentList.add($item))
	$item is some element you are adding to the list.

If you have a list of [1, 2, 3] and you add 4 you will have a list of [1,2,3,4]. Using add is similar to push in Perl.

	:::velocity
	#set($contentList = [1,2,3])
	#set($_dummy = $contentList.add(4))
	$contentList is now [1,2,3,4]

You can add another list to a list, but the whole list is added as a single element.

	:::velocity
	#set($_dummy = $contentList.add(4,5,6))
	$contentList is now [1,2,3,[4,5,6]]

Pulling an element out of the list is simple using the get method.

	:::velocity
	$contentList.get(2)
	returns 3
	$contentList.get(3)
	returns [4,5,6]
	$contentList.get(3).get(1)
	returns 5

Velocity lists are java lists, so you can use the java list methods on the list.

	:::velocity
	$contentList.contains(2)
	returns true
	$contentList.isEmpty()
	returns false

Instead of adding the list as a single element you can add all the elements using the addAll() method.

	:::velocity
	$contentList.addAll([‘banana’, ‘apple’, ‘peach’])
	returns [1,2,3,[4,5,6],’banana’,’apple’,’peach’]

To remove an element:

	:::velocity
	$contentList.remove(5)
	returns [1,2,3,[4,5,6],banana,apple]

You may have a comma separated list you need to have as a list. Since that is a string you can use a string method to quickly create a list.

	:::velocity
	#set($string = "lemon,orange,kiwi,pomegranate")
	#set($listfromstring = $string.split(","))

There is a catch to this here. $listfromstring is actually an array rather than a list. That is what split returns. You can iterate through an array just like you can a list, but it you want to print it to the screen you will need to convert it to a list. dotCMS provides a method to do that.

	:::velocity
	#set($dummy = $UtilMethods.arrayToArrayList($listfromstring))

Now $listfromstring is [lemon, orange, kiwi, pomegranate]

dotCMS provides additional methods to use. If you want to pull a random element out of the list you can use:

	:::velocity
	$UtilMethods.randomList($listfromstring, 1)

returns [kiwi] - or one of the other 3 items
If you just want to shuffle up the list you can do:

	:::velocity
	$UtilMethods.randomList($listfromstring, $listfromstring.size())
	returns [lemon, kiwi, pomegranate, orange] - or some random iteration of that.

Velocity provides a sort viewtool. In dotCMS it is called $sorter. To sort the list:

	:::velocity`
	$sorter.sort($listfromstring)
	returns [kiwi, lemon, orange, pomegranate]

###Maps

dotCMS works nearly the same way with maps. However instead of add you use the method put to populate the map. I'll stop here and give some samples of map next time.
[Maplists](/thoughts/posts/dotcms-map-lists)