# NPCParam-SpEffect-Reorganizer
For overhaul makers of Elden Ring to easily reconfigure their NPCParam csv exports so that massediting spEffects without overriding random very important IDs can be possible.

So imagine your NPCParam's SpEffects as a plate with sand on it. You want to draw a straight line on the plate from point A to point B, but without touching any sand. If you try and draw a straight line on the plate as-is, chances are, you will color over some sand and break random things in your game, because the plate is actually your NPCParam and your sand is pre-existing SpEffect IDs in said NPCParam.

However, this script, all it does is tilt the plate to one side. Thus, the sand is gathered but unharmed and you can proceed to draw lines on the metaphorical plate.

You need Python 3.1 to run this.

To run, either

a) Open the program with your IDE, like IntelliJ or whatever, and run from there.

b (recommended)) Open CMD, and type (without the single quotes) 'start python.exe -i "YOURPATHHERE"' so for most people it'd be something like 

start python.exe -i "Downloads\npcSpefferUpper.py"

This way of running the script was found by Pear (https://github.com/Pear0533). Directly running the script won't really work because Windows thinks the console is closed and closes it when it really isn't closed.

If you use this tool and are making an anime-styled ER overhaul, please sacrifice your firstborn unto me. Otherwise, go ham, no credits necessary lololol.
