Date: 2014-10-04 09:35
Author: Brad Rice
Email: brad@bradrice.com
Title:ssh for windows 8
Slug:ssh_windows_8
Tags:windows, ssh, pelican, git 
Category: Pelican 

I have been trying my best to get Pelican to work on my Windows laptop
so I can use it to post to my blog as well as my various mac
workstations. I have python running, cygwin, putty and git. Installing
git ended up being the main fix for getting it to work. I would like to
be able to use Windows Powershell as well as cygwin if possible. The
problem I kept running into was ssh. Apparently getting ssh to run on
Windows 8 is more problematic that I would have ever thought.

A collegue suggested I just run a virtual box using a vagrant setup.
That sounded great to me so I went through those steps, but when you run
the box headless from the command line, it requires ssh, too. I'm still
working on getting vagrant working as I could use that for much more
than just posting to my Pelican blog.

So the solution ended up being adding the provided git ssh app to my
path. After installing git, I noticed that ssh was working fine for git,
so why isn't it working elsewhere. I did some googling and found this
[post](http://www.robertpate.net/blog/2013/getting-the-vagrant-ssh-command-to-work-on-windows/) by Robert Pate.

Not only did adding the path C:\Program Files (x86)\Git\bin to my path
fix Windows Powershell, but the cygwin command line started working,
too. So now I can choose a Powershell or Cygwin and I can ssh.
