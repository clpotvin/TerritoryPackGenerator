# Territory Pack Generator v1.0

This is a Python script that automatically generates a resource pack for territories
in the territory management menu in the Wynncraft MMORPG server.

Please report any bugs or issues you encounter to me through Discord.
Discord Tag: cam_zzz

## Instructions

1. Go into BaseTextures and replace any textures you might want to replace
	- Note: All textures (except HQ) must be 32x PNG files with a Bit Depth of 32.
	- To check Bit Depth, open the properties of an image and find Bit Depth in the details tab. 
	- If you need to change the Bit Depth, find instructions in Changing Bit Depth section.
2. Open main.py in PyCharm.
	- Hopefully it will work out of the box since I included the venv, otherwise you will need to setup a venv.
3. Run the script.
4. When asked to input your guild tag, input the 3 or 4 letter tag of your guild.
5. When asked to input your HQ location, input the name of the territory that your hq will be located on, make sure it is capitalized how it is in-game, as I was too lazy to make it accept improper capitalization.
6. The territory pack should be generated, now just copy it into you resource packs.

## Changing Bit Depth

There are 2 ways to change Bit Depth, one you can do if you have GIMP, otherwise you can use an online image converter. 

### Method 1 - Online Image Converter:
1. Go to https://online-converting.com/image/
2. Change the "Convert to:" option to "PNG"
3. Change the "Depth color:" option to "32 (True color, RGBA, transparent)"
4. Upload image(s)
5. Download image(s) and place in BaseTextures folder

### Method 2 - GIMP:
1. Open the image in GIMP
2. Do File > Export As...
3. Click the Export button in the pop-up
4. Click the Replace button in the next pop-up
5. Above "Compression level", select "8bpc RGBA" from the dropdown menu
6. Click Export
