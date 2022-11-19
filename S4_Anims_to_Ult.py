import os , sys
import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

print("Please select the original Sm4sh animation files, exported from Smash Forge in .smd or .anim format")

anims = filedialog.askopenfilenames(filetypes=[("Source Animation (.smd)", "*.smd"), ("Maya Anim (.anim)", "*.anim")])

if len(anims) == 0:
    quit()

has_LegC = input("Does your character contain a LegC bone? (Y/N): ")
while has_LegC.lower() not in ("y", "n"):
    print("Not a valid input.")
    has_LegC = input("Does your character contain a LegC bone? (Y/N): ")
has_LegC = has_LegC.lower() == "y"

has_ClavicleC = input("Does your character contain a ClavicleC bone? (Y/N): ")
while has_ClavicleC.lower() not in ("y", "n"):
    print("Not a valid input.")
    has_ClavicleC = input("Does your character contain a ClavicleC bone? (Y/N): ")
has_ClavicleC = has_ClavicleC.lower() == "y"

filename, extension = os.path.splitext(anims[0])

with open(anims[0], 'r') as anim1:
    animRead = anim1.read()

match extension:
    case '.smd':
        base_keyframe_data = re.findall("(ime.*\n[\S\s]*?)t", animRead)

        for anim in range(1, len(anims)):
            with open(anims[anim], 'r') as nextAnim:
                nextAnimRead = nextAnim.read()

            keyframe_data = re.findall("ime.*\n([\S\s]*?)t", nextAnimRead)
            for time in range(len(keyframe_data)):
                animRead = animRead.replace(base_keyframe_data[time], base_keyframe_data[time] + keyframe_data[time], 1)
                base_keyframe_data[time] += keyframe_data[time]
            nextAnim.close()
    case '.anim':
        empty_bone_data = re.findall("anim ([\S]*) 0 0 0;", animRead)
        for anim in range(1, len(anims)):
            with open(anims[anim], 'r') as nextAnim:
                nextAnimRead = nextAnim.read()

            keyframe_data = re.findall("(anim translate.translateX translateX ([\S]*?) 0 0 0;\n[\S\s]*?scaleZ[\S\s]*?\}\n\})", nextAnimRead)
            keyframe_dict = {}
            for ele in keyframe_data:
                keyframe_dict[ele[1]] = ele[0]
            for i in range(len(empty_bone_data)):
                if empty_bone_data[i] in keyframe_dict:
                    animRead = animRead.replace("anim " + empty_bone_data[i] + " 0 0 0;", keyframe_dict[empty_bone_data[i]], 1)
    


# Handle renaming bones to match Ultimate bonesets
# Trans, Rot, & Hip
if "TransN" in animRead:
    bone = "Trans"
    animRead = animRead.replace("TransN", bone) 

if "XRotN" in animRead:
    bone = "Rot"
    animRead = animRead.replace("RotN", bone)

if "RotN" in animRead:
    bone = "Rot"
    animRead = animRead.replace("RotN", bone)

if "HipN" in animRead:
    bone = "Hip"
    animRead = animRead.replace("HipN", bone)

if "HLP_HaraJb" in animRead:
    bone = "H_Waist"
    animRead = animRead.replace("HLP_HaraJb", bone)

if "ThrowN" in animRead:
    bone = "Throw"
    animRead = animRead.replace("ThrowN", bone)

#Left Leg
if "HLP_LLegJc" in animRead:
    bone = "LegL2"
    animRead = animRead.replace("HLP_LLegJc", bone)

if "HLP_RLegJc" in animRead:
    bone = "LegR2"
    animRead = animRead.replace("HLP_RLegJc", bone)

if "LLegJb" in animRead:
    bone = "H_LegL1"
    animRead = animRead.replace("LLegJb", bone)

if "RLegJb" in animRead:
    bone = "H_LegR1"
    animRead = animRead.replace("RLegJb", bone)

if "LLegJ" in animRead:
    bone = "LegL"
    animRead = animRead.replace("LLegJ", bone)

if "LKneeJ" in animRead:
    bone = "KneeL"
    animRead = animRead.replace("LKneeJ", bone)

if "LFootJ" in animRead:
    bone = "FootL"
    animRead = animRead.replace("LFootJ", bone)

if "LToeN" in animRead:
    bone = "ToeL"
    animRead = animRead.replace("LToeN", bone)

if "LToe1stN" in animRead:
    bone = "ToeL2"
    animRead = animRead.replace("LToe1stN", bone)

if "LToe2ndN" in animRead:
    bone = "ToeL3"
    animRead = animRead.replace("LToe2ndN", bone)

if "LToe3rdN" in animRead:
    bone = "ToeL4"
    animRead = animRead.replace("LToe3rdN", bone)

if "HLP_LComaneciJb" in animRead:
    bone = "H_LegL"
    animRead = animRead.replace("HLP_LComaneciJb", bone)

if "HLP_LKneeJb" in animRead:
    bone = "H_KneeL"
    animRead = animRead.replace("HLP_LKneeJb", bone)

# Right Leg
if "RLegJ" in animRead:
    bone = "LegR"
    animRead = animRead.replace("RLegJ", bone)

if "RKneeJ" in animRead:
    bone = "KneeR"
    animRead = animRead.replace("RKneeJ", bone)

if "RFootJ" in animRead:
    bone = "FootR"
    animRead = animRead.replace("RFootJ", bone)

if "RToeN" in animRead:
    bone = "ToeR"
    animRead = animRead.replace("RToeN", bone)

if "RToe1stN" in animRead:
    bone = "ToeR2"
    animRead = animRead.replace("RToe1stN", bone)

if "RToe2ndN" in animRead:
    bone = "ToeR3"
    animRead = animRead.replace("RToe2ndN", bone)

if "RToe3rdN" in animRead:
    bone = "ToeR4"
    animRead = animRead.replace("RToe3rdN", bone)

if "HLP_RComaneciJb" in animRead:
    bone = "H_LegR"
    animRead = animRead.replace("HLP_RComaneciJb", bone)

if "HLP_RKneeJb" in animRead:
    bone = "H_KneeR"
    animRead = animRead.replace("HLP_RKneeJb", bone)

# Waist & Bust
if "WaistN" in animRead:
    bone = "Waist"
    animRead = animRead.replace("WaistN", bone)

if "BustN" in animRead:
    bone = "Bust"
    animRead = animRead.replace("BustN", bone)

# Left Arm
if "LShoulderN" in animRead:
    bone = "ClavicleL"
    animRead = animRead.replace("LShoulderN", bone)

if "LShoulderJ" in animRead:
    bone = "ShoulderL"
    animRead = animRead.replace("LShoulderJ", bone)

if "LArmJ" in animRead:
    bone = "ArmL"
    animRead = animRead.replace("LArmJ", bone)

if "LHandN" in animRead:
    bone = "HandL"
    animRead = animRead.replace("LHandN", bone)

if "HLP_LElbowJb" in animRead:
    bone = "H_ElbowL"
    animRead = animRead.replace("HLP_LElbowJb", bone)

if "HLP_LTekubiJb" in animRead:
    bone = "H_WristL"
    animRead = animRead.replace("HLP_LTekubiJb", bone)

if "HLP_LArmTwistjb" in animRead:
    bone = "H_ArmtwistL"
    animRead = animRead.replace("HLP_LArmTwistjb", bone)

if "HLP_LSholJb" in animRead:
    bone = "H_SholderL"
    animRead = animRead.replace("HLP_LSholJb", bone)

# Left Hand
if "LFingerBaseN" in animRead:
    bone = "FingerL10"
    animRead = animRead.replace("LFingerBaseN", bone)

if "LThumb1N" in animRead:
    bone = "FingerL51"
    animRead = animRead.replace("LThumb1N", bone)

if "LThumb2N" in animRead:
    bone = "FingerL52"
    animRead = animRead.replace("LThumb2N", bone)

if "LThumb3N" in animRead:
    bone = "FingerL53"
    animRead = animRead.replace("LThumb3N", bone)

# BRAWL -----------------------------------------------
if "LThumbNa" in animRead:
    bone = "FingerL51"
    animRead = animRead.replace("LThumbNa", bone)

if "LThumbNb" in animRead:
    bone = "FingerL52"
    animRead = animRead.replace("LThumbNb", bone)
# BRAWL -----------------------------------------------

if "LIndex1N" in animRead:
    bone = "FingerL11"
    animRead = animRead.replace("LIndex1N", bone)

if "LIndex2N" in animRead:
    bone = "FingerL12"
    animRead = animRead.replace("LIndex2N", bone)

if "LIndex3N" in animRead:
    bone = "FingerL13"
    animRead = animRead.replace("LIndex3N", bone)

# BRAWL -----------------------------------------------
if "L1stNa" in animRead:
    bone = "FingerL11"
    animRead = animRead.replace("L1stNa", bone)

if "L1stNb" in animRead:
    bone = "FingerL12"
    animRead = animRead.replace("L1stNb", bone)
# BRAWL -----------------------------------------------

if "LMiddleN" in animRead:
    bone = "FingerL20"
    animRead = animRead.replace("LMiddleN", bone)

if "LMiddle1N" in animRead:
    bone = "FingerL21"
    animRead = animRead.replace("LMiddle1N", bone)

if "LMiddle2N" in animRead:
    bone = "FingerL22"
    animRead = animRead.replace("LMiddle2N", bone)

if "LMiddle3N" in animRead:
    bone = "FingerL23"
    animRead = animRead.replace("LMiddle3N", bone)

# BRAWL -----------------------------------------------
if "L2ndNa" in animRead:
    bone = "FingerL21"
    animRead = animRead.replace("L2ndNa", bone)

if "L2ndNb" in animRead:
    bone = "FingerL22"
    animRead = animRead.replace("L2ndNb", bone)
# BRAWL -----------------------------------------------

if "LRingN" in animRead:
    bone = "FingerL30"
    animRead = animRead.replace("LRingN", bone)

if "LRing1N" in animRead:
    bone = "FingerL31"
    animRead = animRead.replace("LRing1N", bone)

if "LRing2N" in animRead:
    bone = "FingerL32"
    animRead = animRead.replace("LRing2N", bone)

if "LRing3N" in animRead:
    bone = "FingerL33"
    animRead = animRead.replace("LRing3N", bone)

# BRAWL -----------------------------------------------
if "L3rdNa" in animRead:
    bone = "FingerL31"
    animRead = animRead.replace("L3rdNa", bone)

if "L3rdNb" in animRead:
    bone = "FingerL32"
    animRead = animRead.replace("L3rdNb", bone)
# BRAWL -----------------------------------------------

if "LPinkyN" in animRead:
    bone = "FingerL40"
    animRead = animRead.replace("LPinkyN", bone)

if "LPinky1N" in animRead:
    bone = "FingerL41"
    animRead = animRead.replace("LPinky1N", bone)

if "LPinky2N" in animRead:
    bone = "FingerL42"
    animRead = animRead.replace("LPinky2N", bone)

if "LPinky3N" in animRead:
    bone = "FingerL43"
    animRead = animRead.replace("LPinky3N", bone)

# BRAWL -----------------------------------------------
if "L4thNa" in animRead:
    bone = "FingerL41"
    animRead = animRead.replace("L4thNa", bone)

if "L4thNb" in animRead:
    bone = "FingerL42"
    animRead = animRead.replace("L4thNb", bone)
# BRAWL -----------------------------------------------

# Right Arm
if "RShoulderN" in animRead:
    bone = "ClavicleR"
    animRead = animRead.replace("RShoulderN", bone)

if "RShoulderJ" in animRead:
    bone = "ShoulderR"
    animRead = animRead.replace("RShoulderJ", bone)

if "RArmJ" in animRead:
    bone = "ArmR"
    animRead = animRead.replace("RArmJ", bone)

if "RHandN" in animRead:
    bone = "HandR"
    animRead = animRead.replace("RHandN", bone)

if "HLP_RElbowJb" in animRead:
    bone = "H_ElbowR"
    animRead = animRead.replace("HLP_RElbowJb", bone)

if "HLP_RTekubiJb" in animRead:
    bone = "H_WristR"
    animRead = animRead.replace("HLP_RTekubiJb", bone)

if "HLP_RArmTwistJb" in animRead:
    bone = "H_ArmtwistR"
    animRead = animRead.replace("HLP_RArmTwistJb", bone)

if "HLP_RSholJb" in animRead:
    bone = "H_SholderR"
    animRead = animRead.replace("HLP_RSholJb", bone)

# Right Hand
if "RFingerBaseN" in animRead:
    bone = "FingerR10"
    animRead = animRead.replace("RFingerBaseN", bone)

if "RThumb1N" in animRead:
    bone = "FingerR51"
    animRead = animRead.replace("RThumb1N", bone)

if "RThumb2N" in animRead:
    bone = "FingerR52"
    animRead = animRead.replace("RThumb2N", bone)

if "RThumb3N" in animRead:
    bone = "FingerR53"
    animRead = animRead.replace("RThumb3N", bone)

# BRAWL -----------------------------------------------
if "RThumbNa" in animRead:
    bone = "FingerR51"
    animRead = animRead.replace("RThumbNa", bone)

if "RThumbNb" in animRead:
    bone = "FingerR52"
    animRead = animRead.replace("RThumbNb", bone)
# BRAWL -----------------------------------------------

if "RIndex1N" in animRead:
    bone = "FingerR11"
    animRead = animRead.replace("RIndex1N", bone)

if "RIndex2N" in animRead:
    bone = "FingerR12"
    animRead = animRead.replace("RIndex2N", bone)

if "RIndex3N" in animRead:
    bone = "FingerR13"
    animRead = animRead.replace("RIndex3N", bone)

# BRAWL -----------------------------------------------
if "R1stNa" in animRead:
    bone = "FingerR11"
    animRead = animRead.replace("R1stNa", bone)

if "R1stNb" in animRead:
    bone = "FingerR12"
    animRead = animRead.replace("R1stNb", bone)
# BRAWL -----------------------------------------------

if "RMiddleN" in animRead:
    bone = "FingerR20"
    animRead = animRead.replace("RMiddleN", bone)

if "RMiddle1N" in animRead:
    bone = "FingerR21"
    animRead = animRead.replace("RMiddle1N", bone)

if "RMiddle2N" in animRead:
    bone = "FingerR22"
    animRead = animRead.replace("RMiddle2N", bone)

if "RMiddle3N" in animRead:
    bone = "FingerR23"
    animRead = animRead.replace("RMiddle3N", bone)

# BRAWL -----------------------------------------------
if "R2ndNa" in animRead:
    bone = "FingerR21"
    animRead = animRead.replace("R2ndNa", bone)

if "R2ndNb" in animRead:
    bone = "FingerR22"
    animRead = animRead.replace("R2ndNb", bone)
# BRAWL -----------------------------------------------

if "RRingN" in animRead:
    bone = "FingerR30"
    animRead = animRead.replace("RRingN", bone)

if "RRing1N" in animRead:
    bone = "FingerR31"
    animRead = animRead.replace("RRing1N", bone)

if "RRing2N" in animRead:
    bone = "FingerR32"
    animRead = animRead.replace("RRing2N", bone)

if "RRing3N" in animRead:
    bone = "FingerR33"
    animRead = animRead.replace("RRing3N", bone)

# BRAWL -----------------------------------------------
if "R3rdNa" in animRead:
    bone = "FingerR31"
    animRead = animRead.replace("R3rdNa", bone)

if "R3rdNb" in animRead:
    bone = "FingerR32"
    animRead = animRead.replace("R3rdNb", bone)
# BRAWL -----------------------------------------------

if "RPinkyN" in animRead:
    bone = "FingerR40"
    animRead = animRead.replace("RPinkyN", bone)

if "RPinky1N" in animRead:
    bone = "FingerR41"
    animRead = animRead.replace("RPinky1N", bone)

if "RPinky2N" in animRead:
    bone = "FingerR42"
    animRead = animRead.replace("RPinky2N", bone)

if "RPinky3N" in animRead:
    bone = "FingerR43"
    animRead = animRead.replace("RPinky3N", bone)

# BRAWL -----------------------------------------------
if "R4thNa" in animRead:
    bone = "FingerR41"
    animRead = animRead.replace("R4thNa", bone)

if "R4thNb" in animRead:
    bone = "FingerR42"
    animRead = animRead.replace("R4thNb", bone)
# BRAWL -----------------------------------------------

# Face
if "FaceN" in animRead:
    bone = "Face"
    animRead = animRead.replace("FaceN", bone)

if "FaceLEyebrowInnerN" in animRead:
    bone = "BrowL1_offset"
    animRead = animRead.replace("FaceLEyebrowInnerN", bone)

if "FaceLEyebrowMidN" in animRead:
    bone = "BrowL2_offset"
    animRead = animRead.replace("FaceLEyebrowMidN", bone)

if "FaceLEyebrowOuterN" in animRead:
    bone = "BrowL3_offset"
    animRead = animRead.replace("FaceLEyebrowOuterN", bone)

if "FaceREyebrowInnerN" in animRead:
    bone = "BrowR1_offset"
    animRead = animRead.replace("FaceREyebrowInnerN", bone)

if "FaceREyebrowMidN" in animRead:
    bone = "BrowR2_offset"
    animRead = animRead.replace("FaceREyebrowMidN", bone)

if "FaceREyebrowOuterN" in animRead:
    bone = "BrowR3_offset"
    animRead = animRead.replace("FaceREyebrowOuterN", bone)

if "Mouth3N" in animRead:
    bone = "Mouth2"
    animRead = animRead.replace("Mouth3N", bone)

if "Mouth4N" in animRead:
    bone = "Mouth1"
    animRead = animRead.replace("Mouth4N", bone)

if "HairN" in animRead:
    bone = "Hair"
    animRead = animRead.replace("HairN", bone)

if "LHornN" in animRead:
    bone = "HornL"
    animRead = animRead.replace("LHornN", bone)

if "RHornN" in animRead:
    bone = "HornR"
    animRead = animRead.replace("RHornN", bone)

if "NoseN" in animRead:
    bone = "Snout"
    animRead = animRead.replace("NoseN", bone)

# Mouth Upper
if "FaceCLipUpperN" in animRead:
    bone = "UplipC_offset"
    animRead = animRead.replace("FaceCLipUpperN", bone)

if "FaceLLipUpperN" in animRead:
    bone = "UplipL1_offset"
    animRead = animRead.replace("FaceLLipUpperN", bone)

if "FaceLLipCornerN" in animRead:
    bone = "UplipL2_offset"
    animRead = animRead.replace("FaceLLipCornerN", bone)

if "FaceRLipUpperN" in animRead:
    bone = "UplipR1_offset"
    animRead = animRead.replace("FaceRLipUpperN", bone)

if "FaceRLipCornerN" in animRead:
    bone = "UplipR2_offset"
    animRead = animRead.replace("FaceRLipCornerN", bone)

# Mouth Lower
if "FaceJawN" in animRead:
    bone = "Jaw_offset"
    animRead = animRead.replace("FaceJawN", bone)

if "FaceCLipLowerN" in animRead:
    bone = "DownlipC_offset"
    animRead = animRead.replace("FaceCLipLowerN", bone)

if "FaceLLipLowerN" in animRead:
    bone = "DownlipL_offset"
    animRead = animRead.replace("FaceLLipLowerN", bone)

if "FaceRLipLowerN" in animRead:
    bone = "DownlipR_offset"
    animRead = animRead.replace("FaceRLipLowerN", bone)

if "FaceTongueN" in animRead:
    bone = "Tongue_offset"
    animRead = animRead.replace("FaceTongueN", bone)

# Other HLP
if "HLP_LSakotsuJb" in animRead:
    bone = "H_ClavicleL"
    animRead = animRead.replace("HLP_LSakotsuJb", bone)

if "HLP_RSakotsuJb" in animRead:
    bone = "H_ClavicleR"
    animRead = animRead.replace("HLP_RSakotsuJb", bone)

if "HLP_LComaneciJb" in animRead:
    bone = "H_LegL"
    animRead = animRead.replace("HLP_LComaneciJb", bone)

if "HLP_LComaneciJc" in animRead:
    bone = "H_LegL"
    animRead = animRead.replace("HLP_LComaneciJc", bone)

if "HLP_LComaneciJc1" in animRead:
    bone = "H_LegL2"
    animRead = animRead.replace("HLP_LComaneciJc1", bone)

if "HLP_RComaneciJb" in animRead:
    bone = "H_LegR"
    animRead = animRead.replace("HLP_RComaneciJb", bone)

if "HLP_RComaneciJc" in animRead:
    bone = "H_LegR"
    animRead = animRead.replace("HLP_RComaneciJc", bone)

# Swing Bones
if "SWG_Scarf0__swing" in animRead:
    bone = "S_Scarf1"
    animRead = animRead.replace("SWG_Scarf0__swing", bone)

if "SWG_Scarf1__swing" in animRead:
    bone = "S_Scarf2"
    animRead = animRead.replace("SWG_Scarf1__swing", bone)

if "SWG_Scarf2__swing" in animRead:
    bone = "S_Scarf3"
    animRead = animRead.replace("SWG_Scarf2__swing", bone)

if "SWG_cap1__swing" in animRead:
    bone = "S_Hat1"
    animRead = animRead.replace("SWG_cap1__swing", bone)

if "SWG_cap2__swing" in animRead:
    bone = "S_Hat2"
    animRead = animRead.replace("SWG_cap2__swing", bone)

if "SWG_sodeLa01__swing" in animRead:
    bone = "S_SleeveFL1"
    animRead = animRead.replace("SWG_sodeLa01__swing", bone)

if "SWG_sodeRa01__swing" in animRead:
    bone = "S_SleeveFR1"
    animRead = animRead.replace("SWG_sodeRa01__swing", bone)

if "SWG_BHem0__swing" in animRead:
    bone = "S_ShirttailB1"
    animRead = animRead.replace("SWG_BHem0__swing", bone)

if "SWG_FHem1__swing" in animRead:
    bone = "S_ShirttailF1"
    animRead = animRead.replace("SWG_FHem1__swing", bone)

if "SWG_LBHem0__swing" in animRead:
    bone = "S_ShirttailBL1"
    animRead = animRead.replace("SWG_LBHem0__swing", bone)

if "SWG_LFHem1__swing" in animRead:
    bone = "S_ShirttailFL1"
    animRead = animRead.replace("SWG_LFHem1__swing", bone)

if "SWG_LSHem1__swing" in animRead:
    bone = "S_ShirttailL1"
    animRead = animRead.replace("SWG_LSHem1__swing", bone)

if "SWG_RBHem0__swing" in animRead:
    bone = "S_ShirttailBR1"
    animRead = animRead.replace("SWG_RBHem0__swing", bone)

if "SWG_RFHem1__swing" in animRead:
    bone = "S_ShirttailFR1"
    animRead = animRead.replace("SWG_RFHem1__swing", bone)

if "SWG_RSHem1__swing" in animRead:
    bone = "S_ShirttailR1"
    animRead = animRead.replace("SWG_RSHem1__swing", bone)

if "SWG_LFinN__swing" in animRead:
    bone = "S_FinL1"
    animRead = animRead.replace("SWG_LFinN__swing", bone)

if "SWG_RFinN__swing" in animRead:
    bone = "S_FinR1"
    animRead = animRead.replace("SWG_RFinN__swing", bone)

if "SWG_TailN__swing" in animRead:
    bone = "S_Tail1"
    animRead = animRead.replace("SWG_TailN__swing", bone)

if "SWG_LBStingNa__swing" in animRead:
    bone = "StingL1"
    animRead = animRead.replace("SWG_LBStingNa__swing", bone)

if "SWG_LBStingNb_swing" in animRead:
    bone = "StingL2"
    animRead = animRead.replace("SWG_LBStingNb__swing", bone)

if "SWG_RBStingNa__swing" in animRead:
    bone = "StingR1"
    animRead = animRead.replace("SWG_RBStingNa__swing", bone)

if "SWG_RBStingNb_swing" in animRead:
    bone = "StingR2"
    animRead = animRead.replace("SWG_RBStingNb__swing", bone)

if "SWG_DStingNa__swing" in animRead:
    bone = "S_StingD1"
    animRead = animRead.replace("SWG_DStingNa__swing", bone)

if "SWG_DStingNb_swing" in animRead:
    bone = "S_StingD2"
    animRead = animRead.replace("SWG_DStingNb__swing", bone)

if "SWG_UStingNa__swing" in animRead:
    bone = "S_StingU1"
    animRead = animRead.replace("SWG_UStingNa__swing", bone)

if "SWG_UStingNb_swing" in animRead:
    bone = "S_StingU2"
    animRead = animRead.replace("SWG_UStingNb__swing", bone)

if "SWG_UStingNc__swing" in animRead:
    bone = "S_StingU3"
    animRead = animRead.replace("SWG_UStingNc__swing", bone)

if "SWG_LAStingNa__swing" in animRead:
    bone = "S_StingBL1"
    animRead = animRead.replace("SWG_LAStingNa__swing", bone)

if "SWG_LAStingNb__swing" in animRead:
    bone = "S_StingBL2"
    animRead = animRead.replace("SWG_LAStingNb__swing", bone)

if "SWG_RAStingNa__swing" in animRead:
    bone = "S_StingBR1"
    animRead = animRead.replace("SWG_RAStingNa__swing", bone)

if "SWG_RAStingNb__swing" in animRead:
    bone = "S_StingBR2"
    animRead = animRead.replace("SWG_RAStingNb__swing", bone)

if "SWG_HairA1__swing" in animRead:
    bone = "S_HairF1"
    animRead = animRead.replace("SWG_HairA1__swing", bone)

if "SWG_HairB1__swing" in animRead:
    bone = "S_HairFR1"
    animRead = animRead.replace("SWG_HairB1__swing", bone)

if "SWG_HairC1__swing" in animRead:
    bone = "S_HairFL1"
    animRead = animRead.replace("SWG_HairC1__swing", bone)

if "SWG_HairD1__swing" in animRead:
    bone = "S_HairBR1"
    animRead = animRead.replace("SWG_HairD1__swing", bone)

if "SWG_HairE1__swing" in animRead:
    bone = "S_HairBL1"
    animRead = animRead.replace("SWG_HairE1__swing", bone)

if "SWG_LMant0__swing" in animRead:
    bone = "S_MantleL1"
    # animRead = animRead.replace("SWG_LMant0__swing", bone)

if "SWG_LMant1__swing" in animRead:
    bone = "S_MantleL2"
    animRead = animRead.replace("SWG_LMant1__swing", bone)

if "SWG_LMant2__swing" in animRead:
    bone = "S_MantleL3"
    animRead = animRead.replace("SWG_LMant2__swing", bone)

if "SWG_LMant3__swing" in animRead:
    bone = "S_MantleL4"
    animRead = animRead.replace("SWG_LMant3__swing", bone)

if "SWG_RMant0__swing" in animRead:
    bone = "S_MantleR1"
    # animRead = animRead.replace("SWG_RMant0__swing", bone)

if "SWG_RMant1__swing" in animRead:
    bone = "S_MantleR2"
    animRead = animRead.replace("SWG_RMant1__swing", bone)

if "SWG_RMant2__swing" in animRead:
    bone = "S_MantleR3"
    animRead = animRead.replace("SWG_RMant2__swing", bone)

if "SWG_RMant3__swing" in animRead:
    bone = "S_MantleR4"
    animRead = animRead.replace("SWG_RMant3__swing", bone)

if "SWG_CMant0__swing" in animRead:
    bone = "S_MantleC1"
    animRead = animRead.replace("SWG_CMant0__swing", bone)

if "SWG_CMant1__swing" in animRead:
    bone = "S_MantleC2"
    animRead = animRead.replace("SWG_CMant1__swing", bone)

if "SWG_CMant2__swing" in animRead:
    bone = "S_MantleC3"
    animRead = animRead.replace("SWG_CMant2__swing", bone)

if "SWG_CMant3__swing" in animRead:
    bone = "S_MantleC4"
    animRead = animRead.replace("SWG_CMant3__swing", bone)

if "SWG_LFLeg0__swing" in animRead:
    bone = "S_ShirttailFL1"
    animRead = animRead.replace("SWG_LFLeg0__swing", bone)

if "SWG_LFLeg1__swing" in animRead:
    bone = "S_ShirttailFL2"
    animRead = animRead.replace("SWG_LFLeg1__swing", bone)

if "SWG_LFLeg2__swing" in animRead:
    bone = "S_ShirttailFL3"
    animRead = animRead.replace("SWG_LFLeg2__swing", bone)

if "SWG_RFLeg0__swing" in animRead:
    bone = "S_ShirttailFR1"
    animRead = animRead.replace("SWG_RFLeg0__swing", bone)

if "SWG_RFLeg1__swing" in animRead:
    bone = "S_ShirttailFR2"
    animRead = animRead.replace("SWG_RFLeg1__swing", bone)

if "SWG_RFLeg2__swing" in animRead:
    bone = "S_ShirttailFR3"
    animRead = animRead.replace("SWG_RFLeg2__swing", bone)

if "SWG_RBHip0__swing" in animRead:
    bone = "S_ShirttailBR1"
    animRead = animRead.replace("SWG_RBHip0__swing", bone)

if "SWG_RBHip1__swing" in animRead:
    bone = "S_ShirttailBR2"
    animRead = animRead.replace("SWG_RBHip1__swing", bone)

if "SWG_LBHip0__swing" in animRead:
    bone = "S_ShirttailBL1"
    animRead = animRead.replace("SWG_LBHip0__swing", bone)

if "SWG_LBHip1__swing" in animRead:
    bone = "S_ShirttailBL2"
    animRead = animRead.replace("SWG_LBHip1__swing", bone)


# Accessory
for match in ("KenJ", "SwordN"):
    if match in animRead:
        bone = "Sword1"
        animRead = animRead.replace(match, bone)

for match in ("KenModelN", "SwordHeadN"):
    if match in animRead:
        bone = "Sword2"
        animRead = animRead.replace(match, bone)

for match in ("SayaN", "Saya01N"):
    if match in animRead:
        bone = "Scabbard"
        animRead = animRead.replace(match, bone)

if "SayaTateN" in animRead:
    bone = "ShieldB"
    animRead = animRead.replace("SayaTateN", bone)

for match in ("SayaTukaN", "TsukaN"):
    if match in animRead:
        bone = "Hilt"
        animRead = animRead.replace(match, bone)

if "SWG_BagA0__swing" in animRead:
    bone = "queiver"
    animRead = animRead.replace("SWG_BagA0__swing", bone)

if "TateN" in animRead:
    bone = "Shield"
    animRead = animRead.replace("TateN", bone)

if "SphereN" in animRead:
    bone = "Sphere"
    animRead = animRead.replace("SphereN", bone)

if "HatN" in animRead:
    bone = "Hat"
    animRead = animRead.replace("HatN", bone)


if "ShellNb" in animRead:
    bone = "Shell2"
    animRead = animRead.replace("ShellNb", bone)

if "ShellN" in animRead:
    bone = "Shell1"
    animRead = animRead.replace("ShellN", bone)

if "ShellCenterN" in animRead:
    bone = "Shell"
    animRead = animRead.replace("ShellCenterN", bone)

# Other
if "TailNa" in animRead:
    bone = "Tail1"
    animRead = animRead.replace("TailNa", bone)

if "TailNb" in animRead:
    bone = "Tail2"
    animRead = animRead.replace("TailNb", bone)

if "TailNc" in animRead:
    bone = "Tail3"
    animRead = animRead.replace("TailNc", bone)

if "TailNd" in animRead:
    bone = "Tail4"
    animRead = animRead.replace("TailNd", bone)

if "TailN" in animRead:
    bone = "Tail1"
    animRead = animRead.replace("TailN", bone)

if "Tail1N" in animRead:
    bone = "Tail2"
    animRead = animRead.replace("Tail1N", bone)

if "Tail2N" in animRead:
    bone = "Tail3"
    animRead = animRead.replace("Tail2N", bone)

if "HLP_NeckJb" in animRead:
    bone = "H_Neck"
    animRead = animRead.replace("HLP_NeckJb", bone)

if "NeckN" in animRead:
    bone = "Neck"
    animRead = animRead.replace("NeckN", bone)

if "HeadN" in animRead:
    bone = "Head"
    animRead = animRead.replace("HeadN", bone)

if "RHaveN" in animRead:
    bone = "HaveR"
    animRead = animRead.replace("RHaveN", bone)

if "LHaveN" in animRead:
    bone = "HaveL"
    animRead = animRead.replace("LHaveN", bone)

if "SpineN" in animRead:
    bone = "Spine"
    animRead = animRead.replace("SpineN", bone)

if "HanaN" in animRead:
    bone = "Snout"
    animRead = animRead.replace("HanaN", bone)

if "ChinNa" in animRead:
    bone = "Mouth2"
    animRead = animRead.replace("ChinNa", bone)

if "ChinN" in animRead:
    bone = "Mouth1"
    animRead = animRead.replace("ChinN", bone)

if "CheekN" in animRead:
    bone = "Cheek"
    animRead = animRead.replace("CheekN", bone)

if "TamagoN" in animRead:
    bone = "Egg"
    animRead = animRead.replace("TamagoN", bone)

if "HLP_KneeLb" in animRead:
    bone = "H_KneeL"
    animRead = animRead.replace("HLP_KneeLb", bone)

if "HLP_KneeRb" in animRead:
    bone = "H_KneeR"
    animRead = animRead.replace("HLP_KneeRb", bone)

if "HLP_LUpArmTwistjb" in animRead:
    bone = "H_UparmtwistL"
    animRead = animRead.replace("HLP_LUpArmTwistjb", bone)

if "HLP_RUpArmTwistjb" in animRead:
    bone = "H_UparmtwistR"
    animRead = animRead.replace("HLP_RUpArmTwistjb", bone)

if "HLP_LTekubiJb" in animRead:
    bone = "H_WristL"
    animRead = animRead.replace("HLP_LTekubiJb", bone)

if "HLP_RTekubiJb" in animRead:
    bone = "H_WristR"
    animRead = animRead.replace("HLP_RTekubiJb", bone)

if "SWG_SHair1N__swing" in animRead:
    bone = "S_HairF1"
    animRead = animRead.replace("SWG_SHair1N__swing", bone)

if "SWG_SHair2N__swing" in animRead:
    bone = "S_HairB1"
    animRead = animRead.replace("SWG_SHair2N__swing", bone)

if "HLP_CShellJb" in animRead:
    bone = "H_ShellC"
    animRead = animRead.replace("HLP_CShellJb", bone)

if "HLP_LShellJb" in animRead:
    bone = "H_ShellL"
    animRead = animRead.replace("HLP_LShellJb", bone)

if "HLP_RShellJb" in animRead:
    bone = "H_ShellR"
    animRead = animRead.replace("HLP_RShellJb", bone)

if "JawN" in animRead:
    bone = "Jaw"
    animRead = animRead.replace("JawN", bone)

if "HaveN" in animRead:
    bone = "Have"
    animRead = animRead.replace("HaveN", bone)

if "PipeJA" in animRead:
    bone = "Pipe1"
    animRead = animRead.replace("PipeJA", bone)

if "PipeJB" in animRead:
    bone = "Pipe2"
    animRead = animRead.replace("PipeJB", bone)

if "PipeJC" in animRead:
    bone = "Pipe3"
    animRead = animRead.replace("PipeJC", bone)

if "PipeJD" in animRead:
    bone = "Pipe4"
    animRead = animRead.replace("PipeJD", bone)

if "PipeJE" in animRead:
    bone = "Pipe5"
    animRead = animRead.replace("PipeJE", bone)

if "SWG_TaiNa__swing" in animRead:
    bone = "S_Tail1"
    animRead = animRead.replace("SWG_TaiNa__swing", bone)

if "SWG_TaiNb__swing" in animRead:
    bone = "S_Tail2"
    animRead = animRead.replace("SWG_TaiNb__swing", bone)

if "SWG_TaiNc__swing" in animRead:
    bone = "S_Tail3"
    animRead = animRead.replace("SWG_TaiNc__swing", bone)

if "SWG_TaiNd__swing" in animRead:
    bone = "S_Tail4"
    animRead = animRead.replace("SWG_TaiNd__swing", bone)

if "SWG_TaiNe__swing" in animRead:
    bone = "S_Tail5"
    animRead = animRead.replace("SWG_TaiNe__swing", bone)

if "SWG_TaiNf__swing" in animRead:
    bone = "S_Tail6"
    animRead = animRead.replace("SWG_TaiNf__swing", bone)

if "SWG_TaiNg__swing" in animRead:
    bone = "S_Tail7"
    animRead = animRead.replace("SWG_TaiNg__swing", bone)

if "LMimiNb" in animRead:
    bone = "EarL2"
    animRead = animRead.replace("LMimiNb", bone)

if "RMimiNb" in animRead:
    bone = "EarR2"
    animRead = animRead.replace("RMimiNb", bone)

if "LMimiN" in animRead:
    bone = "EarL1"
    animRead = animRead.replace("LMimiN", bone)

if "RMimiN" in animRead:
    bone = "EarR1"
    animRead = animRead.replace("RMimiN", bone)

if "Sippo1N" in animRead:
    bone = "S_Tail1"
    animRead = animRead.replace("Sippo1N", bone)

if "Sippo2N" in animRead:
    bone = "S_Tail2"
    animRead = animRead.replace("Sippo2N", bone)

if "Sippo3N" in animRead:
    bone = "S_Tail3"
    animRead = animRead.replace("Sippo3N", bone)

if "Sipoo4N" in animRead:
    bone = "S_Tail4"
    animRead = animRead.replace("Sipoo4N", bone)

if "Sipoo5N" in animRead:
    bone = "S_Tail5"
    animRead = animRead.replace("Sipoo5N", bone)

if "Sippo6N" in animRead:
    bone = "S_Tail6"
    animRead = animRead.replace("Sippo6N", bone)

if "Sippo7N" in animRead:
    bone = "S_Tail7"
    animRead = animRead.replace("Sippo7N", bone)

if "Sipoo8N" in animRead:
    bone = "S_Tail8"
    animRead = animRead.replace("Sipoo8N", bone)

if "Sippo9N" in animRead:
    bone = "S_Tail9"
    animRead = animRead.replace("Sippo9N", bone)

if "AgoN" in animRead:
    bone = "Mouth"
    animRead = animRead.replace("AgoN", bone)

if "JikuN" in animRead:
    bone = "Shaft"
    animRead = animRead.replace("JikuN", bone)

if "LKataSinN" in animRead:
    bone = "ShoulderpadL"
    animRead = animRead.replace("LKataSinN", bone)

if "RKataSinN" in animRead:
    bone = "ShoulderpadR"
    animRead = animRead.replace("RKataSinN", bone)


# Handle ClavicleC/LegC bone addition
match extension:
    case '.smd':
        if has_ClavicleC:
            bone_count = int(re.findall("(\d+).*\nend\nskeleton", animRead)[0])
            bust_index = int(re.findall("(\d+).*Bust", animRead)[0])
            clavicleC_index = bone_count + 1
            animRead = re.sub("(\"ClavicleR\") \d+", "\\1" + " " + str(clavicleC_index), animRead, 1)
            animRead = re.sub("(\"ClavicleL\") \d+", "\\1" + " " + str(clavicleC_index), animRead, 1)
            animRead = re.sub("(\d+.*)\n(end\nskeleton)", "\\1" + "\n" + str(clavicleC_index) + " \"ClavicleC\" " + str(bust_index) + "\n" + "\\2", animRead, 1)
            animRead = re.sub("(\d+)\ntime", "\\1" + "\n" + str(clavicleC_index) + " 0 0 0 0 0 0\ntime", animRead)

        if has_LegC:
            bone_count = int(re.findall("(\d+).*\nend\nskeleton", animRead)[0])
            hip_index = int(re.findall("(\d+).*Hip", animRead)[0])
            legC_index = bone_count + 1
            animRead = re.sub("(\"LegR\") \d+", "\\1" + " " + str(legC_index), animRead, 1)
            animRead = re.sub("(\"LegL\") \d+", "\\1" + " " + str(legC_index), animRead, 1)
            animRead = re.sub("(\d+.*)\n(end\nskeleton)", "\\1" + "\n" + str(legC_index) + " \"LegC\" " + str(hip_index) + "\n" + "\\2", animRead, 1)
            animRead = re.sub("(\d+)\ntime", "\\1" + "\n" + str(legC_index) + " 0 0 0 0 0 0\ntime", animRead)

# Delete last frame of animation
match extension:
    case '.smd':
        animRead = re.sub("time " + str(len(keyframe_data)) + "\n[\S\s]*?end", "end", animRead, 1)

if not os.path.exists(os.path.dirname(anims[0]) + '/export'):
    os.makedirs(os.path.dirname(anims[0]) + '/export')

with open(os.path.dirname(anims[0]) + '/export/anim_conv' + extension, 'w') as animConv:
    animConv.write(animRead)

anim1.close()
animConv.close()
