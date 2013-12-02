Title: Game - Tic-Tac-Toe
Date: 2013-12-01 07:00
Comments: true
Slug: Fun with Games

<!-- PELICAN_BEGIN_SUMMARY -->
Hacker School application is done.  I am glad they suggested to submit a game of Tic-Tac-Toe and not some implementation of fourier transformation.  That would be Rocket Science to me.  I had fun playing around with various data structures to make the game.  It's not perfect and doesn't make the best choice possible, but it allows my son to win the game and be happy that he beat daddy's program.

Now, his Christmas wish list is for daddy to write more games for him.  Nothing wrong with that :-)
<!-- PELICAN_END_SUMMARY -->

When I saw that Hacker School suggested writing a Tic-Tac-Toe for their application process.  I thought how hard can that really be.  Its a 3X3 matrix and has only a finite set of winning combinations.  But when I had to make the program choose the best possible slot to win and block any paths, it stopped being a silly game.  I had to think about appropriate data structures and how I keep track of the player positions.

I initally wrote it using Python, my favorite language.  It works well.  But only I could play and couldn't get my three year son interested in entering keys at terminal.

So, I decided to port it to JavaScript.  I like that both Python and JavaScript treat functions as first class objects.  Also, I prefer composition over inheritence, so the lack of defined classes in JavaScript didn't bother me.  I used to use JavaScript / JQuery because I had to.  But now that I have tried Node.JS and Express (similar to Python Flask), I am starting to like it more.

The trickiest part was in finding out a way to lay the buttons in a row and experimenting with CSS styles.  But it' all done now.  My son had fun playing with it and winning a few times.

If you want to give it a try, play [Tic-Tac-Toe](http://sampathweb.com/game_toe).  The code for it is at my [Github Account](http://github.com/sampathweb/game_toe)

My kids are making their Christmas wish list -

* Memory Game
* Still thinking of other things daddy can do.

Daddy got his Christmas wish.

Suggestions?
------------

Any suggestions on what games kids age 3 or 9 will be interested in that daddy can do?