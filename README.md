# S4-Anims-to-Ult

This is a simple script to convert Smash 4 animation files (exported as either .smd or .anim) into Ultimate-compatible format.

Note: this may not work with some characters, if their boneset has been fundamentally changed between Smash 4 and Ultimate (barring the addition of LegC or ClavicleC bones).

## Usage
### Exporting Smash 4 animation files
#### Sm4sh Explorer
Use Sm4sh Explorer, found [here](https://github.com/Deinonychus71/Sm4shExplorer), and a dump of Smash 4 to extract the model/boneset/animation data of the character whose animation you want to port. It's best to extract a character's entire folder found in `data/fighter`.

#### Smash Forge
Use Smash Forge, found [here](https://github.com/jam1garner/Smash-Forge), to view a character's model/boneset/animation data, by going to `File -> Open -> Open Character` and selecting the character's folder which you extracted.  
 
Locate the .pac files in the Animations List. These contain all animation data. There will be mutliple .pac files, such as main.pac, lhand.pac, rhand.pac, and usually a few others as well.
 
Starting with the first .pac in the list, expand it, and navigate to the .omo for the animation which you are porting (they will be named similarly to Ultimate's animations). Right click the corresponding .omo and export the animation either as .smd or .anim.
 
>.smd files take up less space and are a bit easier to read, but do not contain scaling data for animations. .anim files do contain scaling data, so if your character's animations typically utilize squashing and stretching (e.g. Kirby, Yoshi), you should export as .anim.

Do the same for each .pac in the list. You should end up with multiple .smd/.anim files for the same animation. **Store them in the same location.**
>Some of your character's .pac files may not contain data for certain animations, so if you don't see a corresponding .omo for an animation in one or two .pac files, don't worry. The pose data is just null for that .pac.

>Stick to **one** filetype (.smd/.anim) per animation. Do not mix and match when exporting.

### Using the script
#### Prep
Determine whether your character's **Ultimate** boneset contains a ClavicleC and/or LegC bone. Do this by going into StudioSB, loading up your character's model, and viewing their bone tree. Most characters do.

#### Running the script
Run `S4_Anims_to_Ult.py`. In the pop-up window, navigate to the location where all of your .smd or .anim files are stored. *This script is meant to process one animation at a time.*

Select **all** of the files at once and submit.

Input whether or not your character has a LegC bone.

Input whether or not your character has a ClavicleC bone.

The script will now process the files and create an output file in either .smd or .anim format, depending on the input type. An `export` directory will be created at the input files' location and the output file will be written there, named `anim_conv`.

### Creating a .nuanmb
#### StudioSB
Open up StudioSB and load in your character's model.

Go to `File -> Import -> Animation into Scene` and navigate to your exported `anim_conv` file. Select it and submit.

Play the animation back to verify everything has ported correctly.

Go to `File -> Export -> Animation to File` and export the animation in .nuanmb format. Use the default export settings.

Your ported animation should now be ready for usage ingame!
