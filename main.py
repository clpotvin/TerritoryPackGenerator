import json
import os
import shutil

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# GLOBAL VARIABLES
base_dir = os.getcwd()  # get current directory for paths
base_dir = base_dir.replace('\\', '/')
base_textures_dir = base_dir + '/BaseTextures/'  # define location of base textures
pack_dir = ''
assets_dir = ''
cit_dir = ''
models_dir = ''
textures_dir = ''
pack_png = ''
guild_tag = 'TAq'  # Guild Name - default to TAq
HQ = 'Path to Talor'  # HQ location - default to Path to Talor
font = ImageFont.truetype('smallfont.ttf', 5)  # define font to be used if generating with text
terr_arr = []  # instantiate empty array

# load json with territory production data
terr_f = open('TerrData.json')
terr_data = json.load(terr_f)

#load json with claim data
map_f = open('Map.json')
map_data = json.load(map_f)


class Territory:
    name = 'NA'
    acronym = 'NA'
    production = 'NA'
    owner = 'none'

    # constructor
    def __init__(self, nm, acr, prod, own):
        self.name = nm
        self.acronym = acr
        self.production = prod
        self.owner = own

    # create file name
    def get_file_name(self):
        file_name = self.production + '_' + self.name.replace(' ', '_').lower()
        return file_name

    # return file pointer for the base image
    def get_base_file(self):
        base_file = base_textures_dir + self.owner + '_' + self.production
        if self.production == 'city':
            base_file = base_textures_dir + self.production
        return base_file

    # print function for debug purposes
    def print(self):
        print('Name:', self.name, ', Acronym:', self.acronym, ', Production:',
              self.production, ', Owner:', self.owner)


# generate the empty pack file structure
def generate_empty_pack():
    global guild_tag, pack_dir, assets_dir, cit_dir, models_dir, textures_dir, pack_png
    guild_tag = input("Input Guild Tag (ex: TAq): ")  # receive input of guild tag

    # create variables for the various paths and directories
    pack_dir = base_dir + '/' + guild_tag + 'TerrPack'
    assets_dir = pack_dir + '/assets/minecraft'
    cit_dir = assets_dir + '/mcpatcher/cit/gmap'
    models_dir = assets_dir + '/models/item/favorites/'
    textures_dir = assets_dir + '/textures/favorites/'
    pack_png = base_textures_dir + '/pack.png'

    # check if the folders already exist, and if they don't then create them
    if not os.path.exists(pack_dir):
        os.makedirs(pack_dir)
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    if not os.path.exists(cit_dir):
        os.makedirs(cit_dir)
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    if not os.path.exists(textures_dir):
        os.makedirs(textures_dir)

    # check for pack.png file and copy it to the pack
    if os.path.exists(pack_png):
        shutil.copy(pack_png, pack_dir)

    # create pack.mcmeta file
    fp = open(pack_dir + '/pack.mcmeta', 'w')
    fp.write("{\n" +
             "  \"pack\": {\n" +
             "    \"pack_format\": 3,\n"
             "    \"description\": \"\\u00A77Generated with LordGonner's\\nTerritory Pack Generator\"\n"
             "  }\n"
             "}\n")
    fp.close()


# function to go through the input jsons and store necessary attributes in a Territory object array
def create_territories():
    global HQ
    valid = False

    # Receive and validate input of HQ territory
    while not valid:
        HQ = input("Input HQ Territory Name: ")
        for terr in terr_data:
            if terr == HQ:
                valid = True
                break
            else:
                valid = False

        if not valid:
            print("Invalid Territory Name...")

    # From here on this is really fucking inefficiently coded, but I got lazy, and it works...

    for terr in terr_data:
        owner = 'none'  # default owner to none
        acr = (''.join([s[0] for s in (terr.replace('-', ' ')).split()])).upper()  # generate acronyms

        # if the acronyms are too long, then manually replace for the following terrs
        if len(acr) > 4:
            if terr == 'Swamp Dark Forest Transition Upper':
                acr = 'SDTU'
            elif terr == 'Nesaak Plains Lower North West':
                acr = 'NPLN'
            elif terr == 'Path To Ozoth\'s Spire Lower':
                acr = 'POSL'
            elif terr == 'Nesaak Plains Upper North West':
                acr = 'NPUN'
            elif terr == 'Swamp Dark Forest Transition Mid':
                acr = 'SDTM'
            elif terr == 'Swamp Dark Forest Transition Lower':
                acr = 'SDTL'
            elif terr == 'Path To Ozoth\'s Spire Upper':
                acr = 'POSU'
            elif terr == 'Temple of the Lost East':
                acr = 'TOLE'
            elif terr == 'Cliff Side of the Lost':
                acr = 'CSOL'
            elif terr == 'Swamp Mountain Transition Mid-Upper':
                acr = 'SMMU'
            elif terr == 'Path To Ozoth\'s Spire Mid':
                acr = 'POSM'
            elif terr == 'Nesaak Plains Mid North West':
                acr = 'NPMN'

        # check and set production types, and if it is a city, manually replace the acronym
        if int(terr_data[terr]['resources']['emeralds']) > 9000:
            prod = 'city'
            if terr == 'Ahmsord':
                acr = 'AHMS'
            elif terr == 'Almuj City':
                acr = 'ALMJ'
            elif terr == 'Cinfras':
                acr = 'CINF'
            elif terr == 'City of Troms':
                acr = 'TRMS'
            elif terr == 'Corkus City':
                acr = 'CORK'
            elif terr == 'Detlas':
                acr = 'DTLS'
            elif terr == 'Gelibord':
                acr = 'GELI'
            elif terr == 'Kandon-Beda':
                acr = 'KB'
            elif terr == 'Llevigar':
                acr = 'LLEV'
            elif terr == 'Lusuco':
                acr = 'LSCO'
            elif terr == 'Lutho':
                acr = 'LTHO'
            elif terr == 'Nemract Town':
                acr = 'NEM'
            elif terr == 'Nesaak Village':
                acr = 'NSAK'
            elif terr == 'Olux':
                acr = 'OLUX'
            elif terr == 'Ragni':
                acr = 'RGNI'
            elif terr == 'Rodoroc':
                acr = 'RODO'
            elif terr == 'Selchar':
                acr = 'SELC'
            elif terr == 'Thanos':
                acr = 'THNS'
            elif terr == 'Thesead':
                acr = 'THSD'
        elif int(terr_data[terr]['resources']['ore']) == 3600:
            prod = 'ore'
        elif int(terr_data[terr]['resources']['crops']) == 3600:
            prod = 'crop'
        elif int(terr_data[terr]['resources']['fish']) == 3600:
            prod = 'fish'
        elif int(terr_data[terr]['resources']['wood']) == 3600:
            prod = 'wood'
        elif int(terr_data[terr]['resources']['ore']) == 7200:
            prod = 'ore'
            owner = 'double'  # set owner to double to tell generator to use double prod texture
        elif int(terr_data[terr]['resources']['crops']) == 7200:
            prod = 'crop'
            owner = 'double'  # set owner to double to tell generator to use double prod texture
        elif int(terr_data[terr]['resources']['fish']) == 7200:
            prod = 'fish'
            owner = 'double'  # set owner to double to tell generator to use double prod texture
        elif int(terr_data[terr]['resources']['wood']) == 7200:
            prod = 'wood'
            owner = 'double'  # set owner to double to tell generator to use double prod texture
        elif int(terr_data[terr]['resources']['emeralds']) == 1800:
            prod = 'rainbow'
        else:
            prod = 'na'  # if for some weird reason there is no prod then just use na texture

        conns = terr_data[terr]['Trading Routes']  # get the connections of the territory from terr_data

        # check if the HQ territory is a connection of the current territory, if it is then set owner to conn
        for conn in conns:
            if conn == HQ:
                owner = 'conn'

        # find the owner of the territory
        for territory in map_data['territories']:
            if territory == terr:
                if owner != 'conn' and owner != 'double':
                    if map_data['territories'][territory] is None:
                        owner = 'ffa'
                    elif map_data['territories'][territory] == guild_tag:
                        owner = 'claim'
                    else:
                        owner = 'ally'
                break

        # create and save a new Territory object with the found attributes in the array
        new_terr = Territory(terr, acr, prod, owner)
        terr_arr.append(new_terr)


# function to create the images, jsons, and properties files for each territory
def create_files():
    # create temporary variables for hq file locations
    hq_png = base_textures_dir + '/hq.png'
    hq_json = base_dir + '/hq.json'
    hq_properties = base_dir + '/hq.properties'

    # check for hq files and if they exist then copy to location in the pack
    if os.path.exists(hq_png):
        shutil.copy(hq_png, textures_dir)
        if os.path.exists(hq_json):
            shutil.copy(hq_json, models_dir)
        if os.path.exists(hq_properties):
            shutil.copy(hq_properties, cit_dir)

    # iterate through terr_arr and create the various files for each territory
    for terr in terr_arr:
        draw_normal(terr)
        draw_warn(terr)
        create_json(terr)
        create_json_warn(terr)
        create_properties(terr)
        create_properties_warn(terr)


# create the texture (and mcmeta file if needed) for territories in the normal state
def draw_normal(terr: Territory):
    fp_out = textures_dir + terr.get_file_name() + '.png'  # output file pointer
    img = Image.open(terr.get_base_file() + '.png')  # open base image
    img_size_x, img_size_y = img.size  # fetch image dimensions tuple
    size_x = len(terr.acronym) * 8  # calculate x size for the box around the text
    size_y = img_size_x  # individual frame size in case creating animated texture
    y_offset = -11  # y offset constant for height of the box around text

    rect = Image.new('RGBA', (img_size_x, img_size_y))

    imgdraw = ImageDraw.Draw(img)
    rectdraw = ImageDraw.Draw(rect)

    n = img_size_y/size_y  # determine if single frame or animated

    if n == 1:
        rectdraw.rectangle(((32 - size_x), 21, 32, 31), fill=(255, 255, 255, 77))
    else:
        while n > 0:
            rectdraw.rectangle(((img_size_x - size_x), (y_offset+(size_y*n)), img_size_x, ((size_y*n)-1)), fill=(255, 255, 255, 77))
            n = n-1

    img.alpha_composite(rect)

    n = img_size_y / 32  # determine if single frame or animated

    if n == 1:
        imgdraw.text((33, 32), terr.acronym, font=font, fill=(0, 0, 0), anchor="rb")
    else:
        while n > 0:
            imgdraw.text((img_size_x+1, (size_y*n)), terr.acronym, font=font, fill=(0, 0, 0), anchor="rb")
            n = n-1

        # create mcmeta file for any animated texture
        animation_file = open(fp_out + '.mcmeta', 'w')
        animation_file.write('{ \n'
                             '  "animation": { \n'
                             '    "frametime": 20, \n'
                             '    "interpolate": true \n'
                             '  } \n'
                             '}')

    img.save(fp_out)


# create the texture (and mcmeta file if needed) for territories in the alert state (I made a separate function bc I was lazy)
def draw_warn(terr: Territory):
    fp_out = textures_dir + terr.get_file_name() + '_warn.png'  # output file pointer
    img = Image.open(terr.get_base_file() + '.png')  # open base image
    img_size_x, img_size_y = img.size  # fetch image dimensions tuple
    size_x = len(terr.acronym) * 8  # calculate x size for the box around the text
    size_y = img_size_x  # individual frame size in case creating animated texture
    y_offset = -11  # y offset constant for height of the box around text

    rect = Image.new('RGBA', (img_size_x, img_size_y))

    imgdraw = ImageDraw.Draw(img)
    rectdraw = ImageDraw.Draw(rect)

    n = img_size_y/32  # determine if single frame or animated

    if n == 1:
        rectdraw.rectangle((1, 1, 3, 7), fill=(205, 51, 51, 255))
        rectdraw.rectangle((1, 10, 3, 12), fill=(205, 51, 51, 255))
        rectdraw.rectangle(((32 - size_x), 21, 32, 31), fill=(255, 255, 255, 77))
    else:
        while n > 0:
            rectdraw.rectangle((1, (-31 + size_y*n), 3, (-25 + size_y*n)), fill=(205, 51, 51, 255))
            rectdraw.rectangle((1, (-22 + size_y*n), 3, (-20 + size_y*n)), fill=(205, 51, 51, 255))
            rectdraw.rectangle(((img_size_x - size_x), (y_offset+(size_y*n)), img_size_x, ((size_y*n)-1)), fill=(255, 255, 255, 77))
            n = n-1

    img.alpha_composite(rect)

    n = img_size_y / 32  # determine if single frame or animated

    if n == 1:
        imgdraw.text((33, 32), terr.acronym, font=font, fill=(0, 0, 0), anchor="rb")
    else:
        while n > 0:
            imgdraw.text((img_size_x + 1, (size_y * n)), terr.acronym, font=font, fill=(0, 0, 0), anchor="rb")
            n = n - 1

        # create mcmeta file for any animated texture
        animation_file = open(fp_out + '.mcmeta', 'w')
        animation_file.write('{ \n'
                             '  "animation": { \n'
                             '    "frametime": 20, \n'
                             '    "interpolate": true \n'
                             '  } \n'
                             '}')

    img.save(fp_out)


# create json file for territories in the normal state
def create_json(terr: Territory):
    new_json = {
        "parent": "item/generated",
        "textures": {
            "layer0": "favorites/" + terr.get_file_name()
        }
    }

    json_path = models_dir + terr.get_file_name() + '.json'
    with open(json_path, 'w') as jsonFile:
        json.dump(new_json, jsonFile, indent=4)


# create json file for territories in the alert state (I made a separate function bc I was lazy)
def create_json_warn(terr: Territory):
    new_json = {
        "parent": "item/generated",
        "textures": {
            "layer0": "favorites/" + terr.get_file_name() + "_warn"
        }
    }

    json_path = models_dir + terr.get_file_name() + '_warn.json'
    with open(json_path, 'w') as jsonFile:
        json.dump(new_json, jsonFile, indent=4)


# create properties file for territories in the normal state
def create_properties(terr: Territory):
    # handle regex anomalies caused by certain territory names
    if terr.name == 'Thanos' or terr.name == 'Cinfras' or terr.name == 'Military Base':
        name = '(?<!Path To )' + terr.name
    elif terr.name == 'Jungle Upper' or terr.name == 'Jungle Mid' or terr.name == 'Jungle Lower':
        name = '(?<!Dernel )' + terr.name
    else:
        name = terr.name

    # create and save the properties file to the appropriate location
    fp = open(cit_dir + '/' + terr.get_file_name() + '.properties', 'w')
    fp.write("type=item\n"
             "items=minecraft:paper\n"
             "model=item/favorites/" + terr.get_file_name() + "\n"
             "nbt.display.Name=iregex:(\u00a7f.*)(" + name + ")\n"
             "nbt.display.*=iregex:.*(Click to Select|Left-Click).*\n")
    fp.close()


# create properties file for territories in the alert state (I made a separate function bc I was lazy)
def create_properties_warn(terr: Territory):
    # handle regex anomalies caused by certain territory names
    if terr.name == 'Thanos' or terr.name == 'Cinfras' or terr.name == 'Military Base':
        name = '(?<!Path To )' + terr.name
    elif terr.name == 'Jungle Upper' or terr.name == 'Jungle Mid' or terr.name == 'Jungle Lower':
        name = '(?<!Dernel )' + terr.name
    else:
        name = terr.name

    # create and save the properties file to the appropriate location
    fp = open(cit_dir + '/' + terr.get_file_name() + '_warn.properties', 'w')
    fp.write("type=item\n"
             "items=minecraft:diamond_axe\n"
             "model=item/favorites/" + terr.get_file_name() + "_warn\n"
             "nbt.display.Name=iregex:.*(" + name + ")\n"
             "nbt.display.Lore.11=iregex:.*(Alert).*\n")
    fp.close()


generate_empty_pack()
create_territories()
create_files()
