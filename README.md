Auto Youtube to MP3
===================
Auto convert list of music name to mp3 via selenium and ytmp3.cc

Requirements
---------
  * `Python 3.7` or higher
  * `Chrome driver` (Require the same version as your chrome browser)
  * Other packages in [requirements.txt](requirements.txt)
  * Edit [song_names.txt](music/song_names.txt) with your songs (Format for song_names.txt wil be explain in the following section)
   
 Writing format
 --------
 - **Folder name** must end with **;**
 - **Singer or Band** must end with **}** 
 - Song names  
 
 #### Example:
    Internation music; <-- Folder name
    Bruno Mars} <-- Singer or Band
    24kMagic <-- Song name
    Nothing on you <-- Song name
  
 How to run
 --------
 - Install require packages by running the following cmd
    ```
    pip install -r requirements.txt
    ```
 - Run collectlink.py
     