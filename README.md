# Code-brew
The ultimate website for learning and using ciphers with a place to talk with other coders.
<br>
Features:
<ul>
  <li>Public messaging system</li>
  <li>Friends system (beta)</li>
  <li>Codebreaker</li>
  <li>Puzzles (beta)</li>
  <li>Learn</li>
  <li>Playground</li>
  <li>Cipher creator (beta)</li>
  <li>Settings panel - customize website appearance and choose ciphers for the messaging system</li>
</ul>

Public messaging system - in this feature you can communicate with all users that are registered on code brew. The messages that you send will be indicated with your username and the time you sent it. When you hover one somebodies profile, you will be able to see their email as well as a larger profile view which contains information such as 
<ol>
  <li>Your username</li>
  <li>Your email</li>
  <li>Your username</li>
  <li>Your about me</li>
  <li>Your programming langauges</li>
  <li>Your message count</li>
</ol>
You will also have the option to see a users' cipher statistics page, which will show a that users' proficiency in the six ciphers that you can train on the website.
<br>
Friends system - You would be able to add friends that are registered on code brew and send one to one private messages to them.
<br>
Codebreaker - This has three separate tools - <ol><li><b>A shift cipher cracker</b>.</li> <li><b>A vigenere cipher cracker</b>.</li> <li><b>A frequency analysis tool</b>.</li></ol>.
<br>
The <b>shift cipher cracker</b> will allow you to crack messages that have been encrypted with shift ciphers such as the caeser cipher. As shift ciphers only have 26 possibilties for a shifted message, this tool will check all 26 possibilities of a decrypted message and then use a formula utilizing the standard letter distributions to get the optimal shift for the text. 
<br>
The <b>Vigenere cipher cracker</b> will allow you to get the key and the decrypted text for a passage that is encrypted with the Vigenere cipher. This performs two tests that are designed for Vigenere cryptanalysis - the <b>Kasiski Test</b> and the <b>Friedman Test</b>. The Kasiski test will give you the most probable key length for the passage and the Friedman Test uses this output to break up the passage into blocks of the key length and treat every repeat of the key length as an individual caeser cipher (as the shift will repeat) giving you the decrypted passage.
<br>
The puzzles section
<br>
The learn section
<br>
The playground page.
<br>
The cipher creator page.
<br>
The settings page.


The ciphers that I implemented include the:
Caeser cipher, Rot13 cipher (variation of the Caeser cipher)
Vigenere cipher
Trithemius cipher
Atbash cipher
Monoalphabetic cipher
Transposition cipher
Affine cipher
Hill cipher
Playfair cipher
The Hill cipher and Playfair cipher were the most challenging as they required a lot of work with matrices and linear algebra - modular inverse of matrix, etc.
I also enjoying learning about cryptanalysis techniques to create code breakers that include: 
A frequency analysis tool which provides all useful information about an encrypted passage that would be useful to decrypt it, by providing things like the letter distribution compared to the standard letter distributions, digraph information, and more. 
A shift cipher cracker, that uses a mathematical formula to return the most likely decrypted text
A Vigenere cipher cracker that uses the Kasiski test to determine the key length and then the Friedman's test, which use a variety of mathematical formulas and frequency analysis-like techniques to deduce the alphabetical key from the result of the Kasiski test and other analysis.
However, this also includes a user and messaging system, where the user can choose from a variety of appearance options, ciphers to use for messaging (even though users don't see the difference), and more. The information that the user provides in the sign-up page are displayed in the user cards. This is also being stored safely in an SQLite database.
There is also a learn section, where you can go through a mini-course to learn about each of the ciphers.
I plan to add a cipher puzzles section, a friends system, and a cipher creator, which would allow users to combine difference operations and preexisting ciphers together in a game-like way to create a 'supercipher' that can be saved and used for their messaging system. I also plan on deploying this website and growing this with a wider audience.

