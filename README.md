#### Install the required modules by navigating to this directory in the console and running 

```git
pip install --force-reinstall discord==0.16.12
```

There are two components to this discord bot. 
### 1. The Interactions script:
	
The Interactions script uses the API to connect to the bot user. 
This is where custom commands are created, and their responses.

### 2. The LinkBlock script:

This script has to be run seperatly from the Interactions script. This is where the actual link-block code is.
The original purpose of this bot was to block explicit links on a discord server of over 3500 people [https://discord.gg/HpkCFHR]. 
There were many troubles when first designing this bot. 
- How would I detect user input?
- How would the bot know it is a link?
- How would I predefine the blocked websites?

I gradually overcame each of these obstacles as I built the bot (on and off, took about 3-4 months)
I wrote my own function (checkLink.py) to load the linkcheck list, and compare the user input to the defined list.
I also made the bot responses a bit prettier (because why not :P) by using the Embed function.

The code itself still contains redundant code from previous ideas not working. And I may just comment them out.

The bot itself is deployed on two public server and a few private ones, although, I have not found cheap hosting for it yet so it just runs locally on my PC.



