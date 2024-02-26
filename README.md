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
<br>
I plan to add a cipher puzzles section, a friends system, and a cipher creator, which would allow users to combine difference operations and preexisting ciphers together in a game-like way to create a 'supercipher' that can be saved and used for their messaging system. 
<br>
I also plan on deploying this website and growing this with a wider audience.

<details open>
  <summary><b>Demo Images</b></summary>
<br>
Login:
<img width="1278" alt="image" src="https://github.com/Vihaan314/Code-brew/assets/91592863/212267c6-dbde-4ec6-9cdc-1c85fc21639a">
Signup:
<img width="1275" alt="image" src="https://github.com/Vihaan314/Code-brew/assets/91592863/12b9a500-2ef5-4997-97cc-b0120d9d83e6">
Home screen (chat):
<img width="1154" alt="image" src="https://github.com/Vihaan314/Code-brew/assets/91592863/8ebfe03a-3bfe-4f28-ab19-5175d922b21a">
Learn:
<img width="1233" alt="image" src="https://github.com/Vihaan314/Code-brew/assets/91592863/5b3eab70-5a0c-44da-843e-5ecfdad83618">
Cipher playground:
<img width="1255" alt="image" src="https://github.com/Vihaan314/Code-brew/assets/91592863/ee44d796-1f3e-4215-b7a7-d310cf107e72">
<img width="1256" alt="image" src="https://github.com/Vihaan314/Code-brew/assets/91592863/261b4cb9-e18e-4b3e-a637-121d1aca8563">
