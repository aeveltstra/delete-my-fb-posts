# delete-my-fb-posts
A python script that allows you to delete your own Facebook posts.

This runs on MacOSx 10.11.6 (El Capitan), in a terminal, using python 3.9, the latest selenium web driver, and Mozilla's latest geckodriver.

Use pip to install selenium. 
Download Mozilla's geckodriver from their own website. Copy the executable into /usr/local/bin: that puts it onto the executable PATH, which is where selenium needs it.

Edit the script main.py to set the authentication variables, and run the script.

Known issues:
Localization. Facebook goes through a lot of trouble to make their pages not automatable for scripts like this. So we have to select the post deletion button by its title. But Facebook renders that title in a language of your choosing. If that is French, the title is 'Supprimer'. That's what the script in main.py looks for. For other languages the title will differ and you will need to adjust the script accordingly.
