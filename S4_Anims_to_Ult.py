import os , sys
import tkinter as tk
from tkinter import filedialog
import re

root = tk.Tk()
root.withdraw()

print("Please select the original Sm4sh animation file, exported from Smash Forge in .smd format")

file_orig = filedialog.askopenfilename(filetypes=[("Source Animation (.smd)", "*.smd")])

has_LegC = input("Does your character contain a LegC bone? (Y/N): ")
while has_LegC.lower() not in ("y", "n"):
    print("Not a valid input.")
    has_LegC = input("Does your character contain a LegC bone? (Y/N): ")

has_ClavicleC = input("Does your character contain a ClavicleC bone? (Y/N): ")
while has_ClavicleC.lower() not in ("y", "n"):
    print("Not a valid input.")
    has_ClavicleC = input("Does your character contain a ClavicleC bone? (Y/N): ")

filename, extension = os.path.splitext(file_orig)

with open(file_orig, 'r') as fileOrig:
    fileOrigRead = fileOrig.read()

# Trans, Rot, & Hip
if "TransN" in fileOrigRead:
    bone = "Trans"
    fileOrigRead = fileOrigRead.replace("TransN", bone) 

if "XRotN" in fileOrigRead:
    bone = "Rot"
    fileOrigRead = fileOrigRead.replace("RotN", bone)

if "RotN" in fileOrigRead:
    bone = "Rot"
    fileOrigRead = fileOrigRead.replace("RotN", bone)

if "HipN" in fileOrigRead:
    bone = "Hip"
    fileOrigRead = fileOrigRead.replace("HipN", bone)

if "HLP_HaraJb" in fileOrigRead:
    bone = "H_Waist"
    fileOrigRead = fileOrigRead.replace("HLP_HaraJb", bone)

if "ThrowN" in fileOrigRead:
    bone = "Throw"
    fileOrigRead = fileOrigRead.replace("ThrowN", bone)

#Left Leg
if "HLP_LLegJc" in fileOrigRead:
    bone = "LegL2"
    fileOrigRead = fileOrigRead.replace("HLP_LLegJc", bone)

if "HLP_RLegJc" in fileOrigRead:
    bone = "LegR2"
    fileOrigRead = fileOrigRead.replace("HLP_RLegJc", bone)

if "LLegJb" in fileOrigRead:
    bone = "H_LegL1"
    fileOrigRead = fileOrigRead.replace("LLegJb", bone)

if "RLegJb" in fileOrigRead:
    bone = "H_LegR1"
    fileOrigRead = fileOrigRead.replace("RLegJb", bone)

if "LLegJ" in fileOrigRead:
    bone = "LegL"
    fileOrigRead = fileOrigRead.replace("LLegJ", bone)

if "LKneeJ" in fileOrigRead:
    bone = "KneeL"
    fileOrigRead = fileOrigRead.replace("LKneeJ", bone)

if "LFootJ" in fileOrigRead:
    bone = "FootL"
    fileOrigRead = fileOrigRead.replace("LFootJ", bone)

if "LToeN" in fileOrigRead:
    bone = "ToeL"
    fileOrigRead = fileOrigRead.replace("LToeN", bone)

if "LToe1stN" in fileOrigRead:
    bone = "ToeL2"
    fileOrigRead = fileOrigRead.replace("LToe1stN", bone)

if "LToe2ndN" in fileOrigRead:
    bone = "ToeL3"
    fileOrigRead = fileOrigRead.replace("LToe2ndN", bone)

if "LToe3rdN" in fileOrigRead:
    bone = "ToeL4"
    fileOrigRead = fileOrigRead.replace("LToe3rdN", bone)

if "HLP_LComaneciJb" in fileOrigRead:
    bone = "H_LegL"
    fileOrigRead = fileOrigRead.replace("HLP_LComaneciJb", bone)

if "HLP_LKneeJb" in fileOrigRead:
    bone = "H_KneeL"
    fileOrigRead = fileOrigRead.replace("HLP_LKneeJb", bone)

# Right Leg
if "RLegJ" in fileOrigRead:
    bone = "LegR"
    fileOrigRead = fileOrigRead.replace("RLegJ", bone)

if "RKneeJ" in fileOrigRead:
    bone = "KneeR"
    fileOrigRead = fileOrigRead.replace("RKneeJ", bone)

if "RFootJ" in fileOrigRead:
    bone = "FootR"
    fileOrigRead = fileOrigRead.replace("RFootJ", bone)

if "RToeN" in fileOrigRead:
    bone = "ToeR"
    fileOrigRead = fileOrigRead.replace("RToeN", bone)

if "RToe1stN" in fileOrigRead:
    bone = "ToeR2"
    fileOrigRead = fileOrigRead.replace("RToe1stN", bone)

if "RToe2ndN" in fileOrigRead:
    bone = "ToeR3"
    fileOrigRead = fileOrigRead.replace("RToe2ndN", bone)

if "RToe3rdN" in fileOrigRead:
    bone = "ToeR4"
    fileOrigRead = fileOrigRead.replace("RToe3rdN", bone)

if "HLP_RComaneciJb" in fileOrigRead:
    bone = "H_LegR"
    fileOrigRead = fileOrigRead.replace("HLP_RComaneciJb", bone)

if "HLP_RKneeJb" in fileOrigRead:
    bone = "H_KneeR"
    fileOrigRead = fileOrigRead.replace("HLP_RKneeJb", bone)

# Waist & Bust
if "WaistN" in fileOrigRead:
    bone = "Waist"
    fileOrigRead = fileOrigRead.replace("WaistN", bone)

if "BustN" in fileOrigRead:
    bone = "Bust"
    fileOrigRead = fileOrigRead.replace("BustN", bone)

# Left Arm
if "LShoulderN" in fileOrigRead:
    bone = "ClavicleL"
    fileOrigRead = fileOrigRead.replace("LShoulderN", bone)

if "LShoulderJ" in fileOrigRead:
    bone = "ShoulderL"
    fileOrigRead = fileOrigRead.replace("LShoulderJ", bone)

if "LArmJ" in fileOrigRead:
    bone = "ArmL"
    fileOrigRead = fileOrigRead.replace("LArmJ", bone)

if "LHandN" in fileOrigRead:
    bone = "HandL"
    fileOrigRead = fileOrigRead.replace("LHandN", bone)

if "HLP_LElbowJb" in fileOrigRead:
    bone = "H_ElbowL"
    fileOrigRead = fileOrigRead.replace("HLP_LElbowJb", bone)

if "HLP_LTekubiJb" in fileOrigRead:
    bone = "H_WristL"
    fileOrigRead = fileOrigRead.replace("HLP_LTekubiJb", bone)

if "HLP_LArmTwistjb" in fileOrigRead:
    bone = "H_ArmtwistL"
    fileOrigRead = fileOrigRead.replace("HLP_LArmTwistjb", bone)

if "HLP_LSholJb" in fileOrigRead:
    bone = "H_SholderL"
    fileOrigRead = fileOrigRead.replace("HLP_LSholJb", bone)

# Left Hand
if "LFingerBaseN" in fileOrigRead:
    bone = "FingerL10"
    fileOrigRead = fileOrigRead.replace("LFingerBaseN", bone)

if "LThumb1N" in fileOrigRead:
    bone = "FingerL51"
    fileOrigRead = fileOrigRead.replace("LThumb1N", bone)

if "LThumb2N" in fileOrigRead:
    bone = "FingerL52"
    fileOrigRead = fileOrigRead.replace("LThumb2N", bone)

if "LThumb3N" in fileOrigRead:
    bone = "FingerL53"
    fileOrigRead = fileOrigRead.replace("LThumb3N", bone)

# BRAWL -----------------------------------------------
if "LThumbNa" in fileOrigRead:
    bone = "FingerL51"
    fileOrigRead = fileOrigRead.replace("LThumbNa", bone)

if "LThumbNb" in fileOrigRead:
    bone = "FingerL52"
    fileOrigRead = fileOrigRead.replace("LThumbNb", bone)
# BRAWL -----------------------------------------------

if "LIndex1N" in fileOrigRead:
    bone = "FingerL11"
    fileOrigRead = fileOrigRead.replace("LIndex1N", bone)

if "LIndex2N" in fileOrigRead:
    bone = "FingerL12"
    fileOrigRead = fileOrigRead.replace("LIndex2N", bone)

if "LIndex3N" in fileOrigRead:
    bone = "FingerL13"
    fileOrigRead = fileOrigRead.replace("LIndex3N", bone)

# BRAWL -----------------------------------------------
if "L1stNa" in fileOrigRead:
    bone = "FingerL11"
    fileOrigRead = fileOrigRead.replace("L1stNa", bone)

if "L1stNb" in fileOrigRead:
    bone = "FingerL12"
    fileOrigRead = fileOrigRead.replace("L1stNb", bone)
# BRAWL -----------------------------------------------

if "LMiddleN" in fileOrigRead:
    bone = "FingerL20"
    fileOrigRead = fileOrigRead.replace("LMiddleN", bone)

if "LMiddle1N" in fileOrigRead:
    bone = "FingerL21"
    fileOrigRead = fileOrigRead.replace("LMiddle1N", bone)

if "LMiddle2N" in fileOrigRead:
    bone = "FingerL22"
    fileOrigRead = fileOrigRead.replace("LMiddle2N", bone)

if "LMiddle3N" in fileOrigRead:
    bone = "FingerL23"
    fileOrigRead = fileOrigRead.replace("LMiddle3N", bone)

# BRAWL -----------------------------------------------
if "L2ndNa" in fileOrigRead:
    bone = "FingerL21"
    fileOrigRead = fileOrigRead.replace("L2ndNa", bone)

if "L2ndNb" in fileOrigRead:
    bone = "FingerL22"
    fileOrigRead = fileOrigRead.replace("L2ndNb", bone)
# BRAWL -----------------------------------------------

if "LRingN" in fileOrigRead:
    bone = "FingerL30"
    fileOrigRead = fileOrigRead.replace("LRingN", bone)

if "LRing1N" in fileOrigRead:
    bone = "FingerL31"
    fileOrigRead = fileOrigRead.replace("LRing1N", bone)

if "LRing2N" in fileOrigRead:
    bone = "FingerL32"
    fileOrigRead = fileOrigRead.replace("LRing2N", bone)

if "LRing3N" in fileOrigRead:
    bone = "FingerL33"
    fileOrigRead = fileOrigRead.replace("LRing3N", bone)

# BRAWL -----------------------------------------------
if "L3rdNa" in fileOrigRead:
    bone = "FingerL31"
    fileOrigRead = fileOrigRead.replace("L3rdNa", bone)

if "L3rdNb" in fileOrigRead:
    bone = "FingerL32"
    fileOrigRead = fileOrigRead.replace("L3rdNb", bone)
# BRAWL -----------------------------------------------

if "LPinkyN" in fileOrigRead:
    bone = "FingerL40"
    fileOrigRead = fileOrigRead.replace("LPinkyN", bone)

if "LPinky1N" in fileOrigRead:
    bone = "FingerL41"
    fileOrigRead = fileOrigRead.replace("LPinky1N", bone)

if "LPinky2N" in fileOrigRead:
    bone = "FingerL42"
    fileOrigRead = fileOrigRead.replace("LPinky2N", bone)

if "LPinky3N" in fileOrigRead:
    bone = "FingerL43"
    fileOrigRead = fileOrigRead.replace("LPinky3N", bone)

# BRAWL -----------------------------------------------
if "L4thNa" in fileOrigRead:
    bone = "FingerL41"
    fileOrigRead = fileOrigRead.replace("L4thNa", bone)

if "L4thNb" in fileOrigRead:
    bone = "FingerL42"
    fileOrigRead = fileOrigRead.replace("L4thNb", bone)
# BRAWL -----------------------------------------------

# Right Arm
if "RShoulderN" in fileOrigRead:
    bone = "ClavicleR"
    fileOrigRead = fileOrigRead.replace("RShoulderN", bone)

if "RShoulderJ" in fileOrigRead:
    bone = "ShoulderR"
    fileOrigRead = fileOrigRead.replace("RShoulderJ", bone)

if "RArmJ" in fileOrigRead:
    bone = "ArmR"
    fileOrigRead = fileOrigRead.replace("RArmJ", bone)

if "RHandN" in fileOrigRead:
    bone = "HandR"
    fileOrigRead = fileOrigRead.replace("RHandN", bone)

if "HLP_RElbowJb" in fileOrigRead:
    bone = "H_ElbowR"
    fileOrigRead = fileOrigRead.replace("HLP_RElbowJb", bone)

if "HLP_RTekubiJb" in fileOrigRead:
    bone = "H_WristR"
    fileOrigRead = fileOrigRead.replace("HLP_RTekubiJb", bone)

if "HLP_RArmTwistJb" in fileOrigRead:
    bone = "H_ArmtwistR"
    fileOrigRead = fileOrigRead.replace("HLP_RArmTwistJb", bone)

if "HLP_RSholJb" in fileOrigRead:
    bone = "H_SholderR"
    fileOrigRead = fileOrigRead.replace("HLP_RSholJb", bone)

# Right Hand
if "RFingerBaseN" in fileOrigRead:
    bone = "FingerR10"
    fileOrigRead = fileOrigRead.replace("RFingerBaseN", bone)

if "RThumb1N" in fileOrigRead:
    bone = "FingerR51"
    fileOrigRead = fileOrigRead.replace("RThumb1N", bone)

if "RThumb2N" in fileOrigRead:
    bone = "FingerR52"
    fileOrigRead = fileOrigRead.replace("RThumb2N", bone)

if "RThumb3N" in fileOrigRead:
    bone = "FingerR53"
    fileOrigRead = fileOrigRead.replace("RThumb3N", bone)

# BRAWL -----------------------------------------------
if "RThumbNa" in fileOrigRead:
    bone = "FingerR51"
    fileOrigRead = fileOrigRead.replace("RThumbNa", bone)

if "RThumbNb" in fileOrigRead:
    bone = "FingerR52"
    fileOrigRead = fileOrigRead.replace("RThumbNb", bone)
# BRAWL -----------------------------------------------

if "RIndex1N" in fileOrigRead:
    bone = "FingerR11"
    fileOrigRead = fileOrigRead.replace("RIndex1N", bone)

if "RIndex2N" in fileOrigRead:
    bone = "FingerR12"
    fileOrigRead = fileOrigRead.replace("RIndex2N", bone)

if "RIndex3N" in fileOrigRead:
    bone = "FingerR13"
    fileOrigRead = fileOrigRead.replace("RIndex3N", bone)

# BRAWL -----------------------------------------------
if "R1stNa" in fileOrigRead:
    bone = "FingerR11"
    fileOrigRead = fileOrigRead.replace("R1stNa", bone)

if "R1stNb" in fileOrigRead:
    bone = "FingerR12"
    fileOrigRead = fileOrigRead.replace("R1stNb", bone)
# BRAWL -----------------------------------------------

if "RMiddleN" in fileOrigRead:
    bone = "FingerR20"
    fileOrigRead = fileOrigRead.replace("RMiddleN", bone)

if "RMiddle1N" in fileOrigRead:
    bone = "FingerR21"
    fileOrigRead = fileOrigRead.replace("RMiddle1N", bone)

if "RMiddle2N" in fileOrigRead:
    bone = "FingerR22"
    fileOrigRead = fileOrigRead.replace("RMiddle2N", bone)

if "RMiddle3N" in fileOrigRead:
    bone = "FingerR23"
    fileOrigRead = fileOrigRead.replace("RMiddle3N", bone)

# BRAWL -----------------------------------------------
if "R2ndNa" in fileOrigRead:
    bone = "FingerR21"
    fileOrigRead = fileOrigRead.replace("R2ndNa", bone)

if "R2ndNb" in fileOrigRead:
    bone = "FingerR22"
    fileOrigRead = fileOrigRead.replace("R2ndNb", bone)
# BRAWL -----------------------------------------------

if "RRingN" in fileOrigRead:
    bone = "FingerR30"
    fileOrigRead = fileOrigRead.replace("RRingN", bone)

if "RRing1N" in fileOrigRead:
    bone = "FingerR31"
    fileOrigRead = fileOrigRead.replace("RRing1N", bone)

if "RRing2N" in fileOrigRead:
    bone = "FingerR32"
    fileOrigRead = fileOrigRead.replace("RRing2N", bone)

if "RRing3N" in fileOrigRead:
    bone = "FingerR33"
    fileOrigRead = fileOrigRead.replace("RRing3N", bone)

# BRAWL -----------------------------------------------
if "R3rdNa" in fileOrigRead:
    bone = "FingerR31"
    fileOrigRead = fileOrigRead.replace("R3rdNa", bone)

if "R3rdNb" in fileOrigRead:
    bone = "FingerR32"
    fileOrigRead = fileOrigRead.replace("R3rdNb", bone)
# BRAWL -----------------------------------------------

if "RPinkyN" in fileOrigRead:
    bone = "FingerR40"
    fileOrigRead = fileOrigRead.replace("RPinkyN", bone)

if "RPinky1N" in fileOrigRead:
    bone = "FingerR41"
    fileOrigRead = fileOrigRead.replace("RPinky1N", bone)

if "RPinky2N" in fileOrigRead:
    bone = "FingerR42"
    fileOrigRead = fileOrigRead.replace("RPinky2N", bone)

if "RPinky3N" in fileOrigRead:
    bone = "FingerR43"
    fileOrigRead = fileOrigRead.replace("RPinky3N", bone)

# BRAWL -----------------------------------------------
if "R4thNa" in fileOrigRead:
    bone = "FingerR41"
    fileOrigRead = fileOrigRead.replace("R4thNa", bone)

if "R4thNb" in fileOrigRead:
    bone = "FingerR42"
    fileOrigRead = fileOrigRead.replace("R4thNb", bone)
# BRAWL -----------------------------------------------

# Face
if "FaceN" in fileOrigRead:
    bone = "Face"
    fileOrigRead = fileOrigRead.replace("FaceN", bone)

if "FaceLEyebrowInnerN" in fileOrigRead:
    bone = "BrowL1_offset"
    fileOrigRead = fileOrigRead.replace("FaceLEyebrowInnerN", bone)

if "FaceLEyebrowMidN" in fileOrigRead:
    bone = "BrowL2_offset"
    fileOrigRead = fileOrigRead.replace("FaceLEyebrowMidN", bone)

if "FaceLEyebrowOuterN" in fileOrigRead:
    bone = "BrowL3_offset"
    fileOrigRead = fileOrigRead.replace("FaceLEyebrowOuterN", bone)

if "FaceREyebrowInnerN" in fileOrigRead:
    bone = "BrowR1_offset"
    fileOrigRead = fileOrigRead.replace("FaceREyebrowInnerN", bone)

if "FaceREyebrowMidN" in fileOrigRead:
    bone = "BrowR2_offset"
    fileOrigRead = fileOrigRead.replace("FaceREyebrowMidN", bone)

if "FaceREyebrowOuterN" in fileOrigRead:
    bone = "BrowR3_offset"
    fileOrigRead = fileOrigRead.replace("FaceREyebrowOuterN", bone)

if "Mouth3N" in fileOrigRead:
    bone = "Mouth2"
    fileOrigRead = fileOrigRead.replace("Mouth3N", bone)

if "Mouth4N" in fileOrigRead:
    bone = "Mouth1"
    fileOrigRead = fileOrigRead.replace("Mouth4N", bone)

if "HairN" in fileOrigRead:
    bone = "Hair"
    fileOrigRead = fileOrigRead.replace("HairN", bone)

if "LHornN" in fileOrigRead:
    bone = "HornL"
    fileOrigRead = fileOrigRead.replace("LHornN", bone)

if "RHornN" in fileOrigRead:
    bone = "HornR"
    fileOrigRead = fileOrigRead.replace("RHornN", bone)

if "NoseN" in fileOrigRead:
    bone = "Snout"
    fileOrigRead = fileOrigRead.replace("NoseN", bone)

# Mouth Upper
if "FaceCLipUpperN" in fileOrigRead:
    bone = "UplipC_offset"
    fileOrigRead = fileOrigRead.replace("FaceCLipUpperN", bone)

if "FaceLLipUpperN" in fileOrigRead:
    bone = "UplipL1_offset"
    fileOrigRead = fileOrigRead.replace("FaceLLipUpperN", bone)

if "FaceLLipCornerN" in fileOrigRead:
    bone = "UplipL2_offset"
    fileOrigRead = fileOrigRead.replace("FaceLLipCornerN", bone)

if "FaceRLipUpperN" in fileOrigRead:
    bone = "UplipR1_offset"
    fileOrigRead = fileOrigRead.replace("FaceRLipUpperN", bone)

if "FaceRLipCornerN" in fileOrigRead:
    bone = "UplipR2_offset"
    fileOrigRead = fileOrigRead.replace("FaceRLipCornerN", bone)

# Mouth Lower
if "FaceJawN" in fileOrigRead:
    bone = "Jaw_offset"
    fileOrigRead = fileOrigRead.replace("FaceJawN", bone)

if "FaceCLipLowerN" in fileOrigRead:
    bone = "DownlipC_offset"
    fileOrigRead = fileOrigRead.replace("FaceCLipLowerN", bone)

if "FaceLLipLowerN" in fileOrigRead:
    bone = "DownlipL_offset"
    fileOrigRead = fileOrigRead.replace("FaceLLipLowerN", bone)

if "FaceRLipLowerN" in fileOrigRead:
    bone = "DownlipR_offset"
    fileOrigRead = fileOrigRead.replace("FaceRLipLowerN", bone)

if "FaceTongueN" in fileOrigRead:
    bone = "Tongue_offset"
    fileOrigRead = fileOrigRead.replace("FaceTongueN", bone)

# Other HLP
if "HLP_LSakotsuJb" in fileOrigRead:
    bone = "H_ClavicleL"
    fileOrigRead = fileOrigRead.replace("HLP_LSakotsuJb", bone)

if "HLP_RSakotsuJb" in fileOrigRead:
    bone = "H_ClavicleR"
    fileOrigRead = fileOrigRead.replace("HLP_RSakotsuJb", bone)

if "HLP_LComaneciJb" in fileOrigRead:
    bone = "H_LegL"
    fileOrigRead = fileOrigRead.replace("HLP_LComaneciJb", bone)

if "HLP_LComaneciJc" in fileOrigRead:
    bone = "H_LegL"
    fileOrigRead = fileOrigRead.replace("HLP_LComaneciJc", bone)

if "HLP_LComaneciJc1" in fileOrigRead:
    bone = "H_LegL2"
    fileOrigRead = fileOrigRead.replace("HLP_LComaneciJc1", bone)

if "HLP_RComaneciJb" in fileOrigRead:
    bone = "H_LegR"
    fileOrigRead = fileOrigRead.replace("HLP_RComaneciJb", bone)

if "HLP_RComaneciJc" in fileOrigRead:
    bone = "H_LegR"
    fileOrigRead = fileOrigRead.replace("HLP_RComaneciJc", bone)

# Swing Bones
if "SWG_Scarf0__swing" in fileOrigRead:
    bone = "S_Scarf1"
    fileOrigRead = fileOrigRead.replace("SWG_Scarf0__swing", bone)

if "SWG_Scarf1__swing" in fileOrigRead:
    bone = "S_Scarf2"
    fileOrigRead = fileOrigRead.replace("SWG_Scarf1__swing", bone)

if "SWG_Scarf2__swing" in fileOrigRead:
    bone = "S_Scarf3"
    fileOrigRead = fileOrigRead.replace("SWG_Scarf2__swing", bone)

if "SWG_cap1__swing" in fileOrigRead:
    bone = "S_Hat1"
    fileOrigRead = fileOrigRead.replace("SWG_cap1__swing", bone)

if "SWG_cap2__swing" in fileOrigRead:
    bone = "S_Hat2"
    fileOrigRead = fileOrigRead.replace("SWG_cap2__swing", bone)

if "SWG_sodeLa01__swing" in fileOrigRead:
    bone = "S_SleeveFL1"
    fileOrigRead = fileOrigRead.replace("SWG_sodeLa01__swing", bone)

if "SWG_sodeRa01__swing" in fileOrigRead:
    bone = "S_SleeveFR1"
    fileOrigRead = fileOrigRead.replace("SWG_sodeRa01__swing", bone)

if "SWG_BHem0__swing" in fileOrigRead:
    bone = "S_ShirttailB1"
    fileOrigRead = fileOrigRead.replace("SWG_BHem0__swing", bone)

if "SWG_FHem1__swing" in fileOrigRead:
    bone = "S_ShirttailF1"
    fileOrigRead = fileOrigRead.replace("SWG_FHem1__swing", bone)

if "SWG_LBHem0__swing" in fileOrigRead:
    bone = "S_ShirttailBL1"
    fileOrigRead = fileOrigRead.replace("SWG_LBHem0__swing", bone)

if "SWG_LFHem1__swing" in fileOrigRead:
    bone = "S_ShirttailFL1"
    fileOrigRead = fileOrigRead.replace("SWG_LFHem1__swing", bone)

if "SWG_LSHem1__swing" in fileOrigRead:
    bone = "S_ShirttailL1"
    fileOrigRead = fileOrigRead.replace("SWG_LSHem1__swing", bone)

if "SWG_RBHem0__swing" in fileOrigRead:
    bone = "S_ShirttailBR1"
    fileOrigRead = fileOrigRead.replace("SWG_RBHem0__swing", bone)

if "SWG_RFHem1__swing" in fileOrigRead:
    bone = "S_ShirttailFR1"
    fileOrigRead = fileOrigRead.replace("SWG_RFHem1__swing", bone)

if "SWG_RSHem1__swing" in fileOrigRead:
    bone = "S_ShirttailR1"
    fileOrigRead = fileOrigRead.replace("SWG_RSHem1__swing", bone)

if "SWG_LFinN__swing" in fileOrigRead:
    bone = "S_FinL1"
    fileOrigRead = fileOrigRead.replace("SWG_LFinN__swing", bone)

if "SWG_RFinN__swing" in fileOrigRead:
    bone = "S_FinR1"
    fileOrigRead = fileOrigRead.replace("SWG_RFinN__swing", bone)

if "SWG_TailN__swing" in fileOrigRead:
    bone = "S_Tail1"
    fileOrigRead = fileOrigRead.replace("SWG_TailN__swing", bone)

if "SWG_LBStingNa__swing" in fileOrigRead:
    bone = "StingL1"
    fileOrigRead = fileOrigRead.replace("SWG_LBStingNa__swing", bone)

if "SWG_LBStingNb_swing" in fileOrigRead:
    bone = "StingL2"
    fileOrigRead = fileOrigRead.replace("SWG_LBStingNb__swing", bone)

if "SWG_RBStingNa__swing" in fileOrigRead:
    bone = "StingR1"
    fileOrigRead = fileOrigRead.replace("SWG_RBStingNa__swing", bone)

if "SWG_RBStingNb_swing" in fileOrigRead:
    bone = "StingR2"
    fileOrigRead = fileOrigRead.replace("SWG_RBStingNb__swing", bone)

if "SWG_DStingNa__swing" in fileOrigRead:
    bone = "S_StingD1"
    fileOrigRead = fileOrigRead.replace("SWG_DStingNa__swing", bone)

if "SWG_DStingNb_swing" in fileOrigRead:
    bone = "S_StingD2"
    fileOrigRead = fileOrigRead.replace("SWG_DStingNb__swing", bone)

if "SWG_UStingNa__swing" in fileOrigRead:
    bone = "S_StingU1"
    fileOrigRead = fileOrigRead.replace("SWG_UStingNa__swing", bone)

if "SWG_UStingNb_swing" in fileOrigRead:
    bone = "S_StingU2"
    fileOrigRead = fileOrigRead.replace("SWG_UStingNb__swing", bone)

if "SWG_UStingNc__swing" in fileOrigRead:
    bone = "S_StingU3"
    fileOrigRead = fileOrigRead.replace("SWG_UStingNc__swing", bone)

if "SWG_LAStingNa__swing" in fileOrigRead:
    bone = "S_StingBL1"
    fileOrigRead = fileOrigRead.replace("SWG_LAStingNa__swing", bone)

if "SWG_LAStingNb__swing" in fileOrigRead:
    bone = "S_StingBL2"
    fileOrigRead = fileOrigRead.replace("SWG_LAStingNb__swing", bone)

if "SWG_RAStingNa__swing" in fileOrigRead:
    bone = "S_StingBR1"
    fileOrigRead = fileOrigRead.replace("SWG_RAStingNa__swing", bone)

if "SWG_RAStingNb__swing" in fileOrigRead:
    bone = "S_StingBR2"
    fileOrigRead = fileOrigRead.replace("SWG_RAStingNb__swing", bone)

if "SWG_HairA1__swing" in fileOrigRead:
    bone = "S_HairF1"
    fileOrigRead = fileOrigRead.replace("SWG_HairA1__swing", bone)

if "SWG_HairB1__swing" in fileOrigRead:
    bone = "S_HairFR1"
    fileOrigRead = fileOrigRead.replace("SWG_HairB1__swing", bone)

if "SWG_HairC1__swing" in fileOrigRead:
    bone = "S_HairFL1"
    fileOrigRead = fileOrigRead.replace("SWG_HairC1__swing", bone)

if "SWG_HairD1__swing" in fileOrigRead:
    bone = "S_HairBR1"
    fileOrigRead = fileOrigRead.replace("SWG_HairD1__swing", bone)

if "SWG_HairE1__swing" in fileOrigRead:
    bone = "S_HairBL1"
    fileOrigRead = fileOrigRead.replace("SWG_HairE1__swing", bone)

if "SWG_LMant0__swing" in fileOrigRead:
    bone = "S_MantleL1"
    # fileOrigRead = fileOrigRead.replace("SWG_LMant0__swing", bone)

if "SWG_LMant1__swing" in fileOrigRead:
    bone = "S_MantleL2"
    fileOrigRead = fileOrigRead.replace("SWG_LMant1__swing", bone)

if "SWG_LMant2__swing" in fileOrigRead:
    bone = "S_MantleL3"
    fileOrigRead = fileOrigRead.replace("SWG_LMant2__swing", bone)

if "SWG_LMant3__swing" in fileOrigRead:
    bone = "S_MantleL4"
    fileOrigRead = fileOrigRead.replace("SWG_LMant3__swing", bone)

if "SWG_RMant0__swing" in fileOrigRead:
    bone = "S_MantleR1"
    # fileOrigRead = fileOrigRead.replace("SWG_RMant0__swing", bone)

if "SWG_RMant1__swing" in fileOrigRead:
    bone = "S_MantleR2"
    fileOrigRead = fileOrigRead.replace("SWG_RMant1__swing", bone)

if "SWG_RMant2__swing" in fileOrigRead:
    bone = "S_MantleR3"
    fileOrigRead = fileOrigRead.replace("SWG_RMant2__swing", bone)

if "SWG_RMant3__swing" in fileOrigRead:
    bone = "S_MantleR4"
    fileOrigRead = fileOrigRead.replace("SWG_RMant3__swing", bone)

if "SWG_CMant0__swing" in fileOrigRead:
    bone = "S_MantleC1"
    fileOrigRead = fileOrigRead.replace("SWG_CMant0__swing", bone)

if "SWG_CMant1__swing" in fileOrigRead:
    bone = "S_MantleC2"
    fileOrigRead = fileOrigRead.replace("SWG_CMant1__swing", bone)

if "SWG_CMant2__swing" in fileOrigRead:
    bone = "S_MantleC3"
    fileOrigRead = fileOrigRead.replace("SWG_CMant2__swing", bone)

if "SWG_CMant3__swing" in fileOrigRead:
    bone = "S_MantleC4"
    fileOrigRead = fileOrigRead.replace("SWG_CMant3__swing", bone)

if "SWG_LFLeg0__swing" in fileOrigRead:
    bone = "S_ShirttailFL1"
    fileOrigRead = fileOrigRead.replace("SWG_LFLeg0__swing", bone)

if "SWG_LFLeg1__swing" in fileOrigRead:
    bone = "S_ShirttailFL2"
    fileOrigRead = fileOrigRead.replace("SWG_LFLeg1__swing", bone)

if "SWG_LFLeg2__swing" in fileOrigRead:
    bone = "S_ShirttailFL3"
    fileOrigRead = fileOrigRead.replace("SWG_LFLeg2__swing", bone)

if "SWG_RFLeg0__swing" in fileOrigRead:
    bone = "S_ShirttailFR1"
    fileOrigRead = fileOrigRead.replace("SWG_RFLeg0__swing", bone)

if "SWG_RFLeg1__swing" in fileOrigRead:
    bone = "S_ShirttailFR2"
    fileOrigRead = fileOrigRead.replace("SWG_RFLeg1__swing", bone)

if "SWG_RFLeg2__swing" in fileOrigRead:
    bone = "S_ShirttailFR3"
    fileOrigRead = fileOrigRead.replace("SWG_RFLeg2__swing", bone)

if "SWG_RBHip0__swing" in fileOrigRead:
    bone = "S_ShirttailBR1"
    fileOrigRead = fileOrigRead.replace("SWG_RBHip0__swing", bone)

if "SWG_RBHip1__swing" in fileOrigRead:
    bone = "S_ShirttailBR2"
    fileOrigRead = fileOrigRead.replace("SWG_RBHip1__swing", bone)

if "SWG_LBHip0__swing" in fileOrigRead:
    bone = "S_ShirttailBL1"
    fileOrigRead = fileOrigRead.replace("SWG_LBHip0__swing", bone)

if "SWG_LBHip1__swing" in fileOrigRead:
    bone = "S_ShirttailBL2"
    fileOrigRead = fileOrigRead.replace("SWG_LBHip1__swing", bone)


# Accessory
for match in ("KenJ", "SwordN"):
    if match in fileOrigRead:
        bone = "Sword1"
        fileOrigRead = fileOrigRead.replace(match, bone)

for match in ("KenModelN", "SwordHeadN"):
    if match in fileOrigRead:
        bone = "Sword2"
        fileOrigRead = fileOrigRead.replace(match, bone)

for match in ("SayaN", "Saya01N"):
    if match in fileOrigRead:
        bone = "Scabbard"
        fileOrigRead = fileOrigRead.replace(match, bone)

if "SayaTateN" in fileOrigRead:
    bone = "ShieldB"
    fileOrigRead = fileOrigRead.replace("SayaTateN", bone)

for match in ("SayaTukaN", "TsukaN"):
    if match in fileOrigRead:
        bone = "Hilt"
        fileOrigRead = fileOrigRead.replace(match, bone)

if "SWG_BagA0__swing" in fileOrigRead:
    bone = "queiver"
    fileOrigRead = fileOrigRead.replace("SWG_BagA0__swing", bone)

if "TateN" in fileOrigRead:
    bone = "Shield"
    fileOrigRead = fileOrigRead.replace("TateN", bone)

if "SphereN" in fileOrigRead:
    bone = "Sphere"
    fileOrigRead = fileOrigRead.replace("SphereN", bone)

if "HatN" in fileOrigRead:
    bone = "Hat"
    fileOrigRead = fileOrigRead.replace("HatN", bone)


if "ShellNb" in fileOrigRead:
    bone = "Shell2"
    fileOrigRead = fileOrigRead.replace("ShellNb", bone)

if "ShellN" in fileOrigRead:
    bone = "Shell1"
    fileOrigRead = fileOrigRead.replace("ShellN", bone)

if "ShellCenterN" in fileOrigRead:
    bone = "Shell"
    fileOrigRead = fileOrigRead.replace("ShellCenterN", bone)

# Other
if "TailNa" in fileOrigRead:
    bone = "Tail1"
    fileOrigRead = fileOrigRead.replace("TailNa", bone)

if "TailNb" in fileOrigRead:
    bone = "Tail2"
    fileOrigRead = fileOrigRead.replace("TailNb", bone)

if "TailNc" in fileOrigRead:
    bone = "Tail3"
    fileOrigRead = fileOrigRead.replace("TailNc", bone)

if "TailNd" in fileOrigRead:
    bone = "Tail4"
    fileOrigRead = fileOrigRead.replace("TailNd", bone)

if "TailN" in fileOrigRead:
    bone = "Tail1"
    fileOrigRead = fileOrigRead.replace("TailN", bone)

if "Tail1N" in fileOrigRead:
    bone = "Tail2"
    fileOrigRead = fileOrigRead.replace("Tail1N", bone)

if "Tail2N" in fileOrigRead:
    bone = "Tail3"
    fileOrigRead = fileOrigRead.replace("Tail2N", bone)

if "HLP_NeckJb" in fileOrigRead:
    bone = "H_Neck"
    fileOrigRead = fileOrigRead.replace("HLP_NeckJb", bone)

if "NeckN" in fileOrigRead:
    bone = "Neck"
    fileOrigRead = fileOrigRead.replace("NeckN", bone)

if "HeadN" in fileOrigRead:
    bone = "Head"
    fileOrigRead = fileOrigRead.replace("HeadN", bone)

if "RHaveN" in fileOrigRead:
    bone = "HaveR"
    fileOrigRead = fileOrigRead.replace("RHaveN", bone)

if "LHaveN" in fileOrigRead:
    bone = "HaveL"
    fileOrigRead = fileOrigRead.replace("LHaveN", bone)

if "SpineN" in fileOrigRead:
    bone = "Spine"
    fileOrigRead = fileOrigRead.replace("SpineN", bone)

if "HanaN" in fileOrigRead:
    bone = "Snout"
    fileOrigRead = fileOrigRead.replace("HanaN", bone)

if "ChinNa" in fileOrigRead:
    bone = "Mouth2"
    fileOrigRead = fileOrigRead.replace("ChinNa", bone)

if "ChinN" in fileOrigRead:
    bone = "Mouth1"
    fileOrigRead = fileOrigRead.replace("ChinN", bone)

if "CheekN" in fileOrigRead:
    bone = "Cheek"
    fileOrigRead = fileOrigRead.replace("CheekN", bone)

if "TamagoN" in fileOrigRead:
    bone = "Egg"
    fileOrigRead = fileOrigRead.replace("TamagoN", bone)

if "HLP_KneeLb" in fileOrigRead:
    bone = "H_KneeL"
    fileOrigRead = fileOrigRead.replace("HLP_KneeLb", bone)

if "HLP_KneeRb" in fileOrigRead:
    bone = "H_KneeR"
    fileOrigRead = fileOrigRead.replace("HLP_KneeRb", bone)

if "HLP_LUpArmTwistjb" in fileOrigRead:
    bone = "H_UparmtwistL"
    fileOrigRead = fileOrigRead.replace("HLP_LUpArmTwistjb", bone)

if "HLP_RUpArmTwistjb" in fileOrigRead:
    bone = "H_UparmtwistR"
    fileOrigRead = fileOrigRead.replace("HLP_RUpArmTwistjb", bone)

if "HLP_LTekubiJb" in fileOrigRead:
    bone = "H_WristL"
    fileOrigRead = fileOrigRead.replace("HLP_LTekubiJb", bone)

if "HLP_RTekubiJb" in fileOrigRead:
    bone = "H_WristR"
    fileOrigRead = fileOrigRead.replace("HLP_RTekubiJb", bone)

if "SWG_SHair1N__swing" in fileOrigRead:
    bone = "S_HairF1"
    fileOrigRead = fileOrigRead.replace("SWG_SHair1N__swing", bone)

if "SWG_SHair2N__swing" in fileOrigRead:
    bone = "S_HairB1"
    fileOrigRead = fileOrigRead.replace("SWG_SHair2N__swing", bone)

if "HLP_CShellJb" in fileOrigRead:
    bone = "H_ShellC"
    fileOrigRead = fileOrigRead.replace("HLP_CShellJb", bone)

if "HLP_LShellJb" in fileOrigRead:
    bone = "H_ShellL"
    fileOrigRead = fileOrigRead.replace("HLP_LShellJb", bone)

if "HLP_RShellJb" in fileOrigRead:
    bone = "H_ShellR"
    fileOrigRead = fileOrigRead.replace("HLP_RShellJb", bone)

if "JawN" in fileOrigRead:
    bone = "Jaw"
    fileOrigRead = fileOrigRead.replace("JawN", bone)

if "HaveN" in fileOrigRead:
    bone = "Have"
    fileOrigRead = fileOrigRead.replace("HaveN", bone)

if "PipeJA" in fileOrigRead:
    bone = "Pipe1"
    fileOrigRead = fileOrigRead.replace("PipeJA", bone)

if "PipeJB" in fileOrigRead:
    bone = "Pipe2"
    fileOrigRead = fileOrigRead.replace("PipeJB", bone)

if "PipeJC" in fileOrigRead:
    bone = "Pipe3"
    fileOrigRead = fileOrigRead.replace("PipeJC", bone)

if "PipeJD" in fileOrigRead:
    bone = "Pipe4"
    fileOrigRead = fileOrigRead.replace("PipeJD", bone)

if "PipeJE" in fileOrigRead:
    bone = "Pipe5"
    fileOrigRead = fileOrigRead.replace("PipeJE", bone)

if "SWG_TaiNa__swing" in fileOrigRead:
    bone = "S_Tail1"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNa__swing", bone)

if "SWG_TaiNb__swing" in fileOrigRead:
    bone = "S_Tail2"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNb__swing", bone)

if "SWG_TaiNc__swing" in fileOrigRead:
    bone = "S_Tail3"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNc__swing", bone)

if "SWG_TaiNd__swing" in fileOrigRead:
    bone = "S_Tail4"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNd__swing", bone)

if "SWG_TaiNe__swing" in fileOrigRead:
    bone = "S_Tail5"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNe__swing", bone)

if "SWG_TaiNf__swing" in fileOrigRead:
    bone = "S_Tail6"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNf__swing", bone)

if "SWG_TaiNg__swing" in fileOrigRead:
    bone = "S_Tail7"
    fileOrigRead = fileOrigRead.replace("SWG_TaiNg__swing", bone)

if "LMimiNb" in fileOrigRead:
    bone = "EarL2"
    fileOrigRead = fileOrigRead.replace("LMimiNb", bone)

if "RMimiNb" in fileOrigRead:
    bone = "EarR2"
    fileOrigRead = fileOrigRead.replace("RMimiNb", bone)

if "LMimiN" in fileOrigRead:
    bone = "EarL1"
    fileOrigRead = fileOrigRead.replace("LMimiN", bone)

if "RMimiN" in fileOrigRead:
    bone = "EarR1"
    fileOrigRead = fileOrigRead.replace("RMimiN", bone)

if "Sippo1N" in fileOrigRead:
    bone = "S_Tail1"
    fileOrigRead = fileOrigRead.replace("Sippo1N", bone)

if "Sippo2N" in fileOrigRead:
    bone = "S_Tail2"
    fileOrigRead = fileOrigRead.replace("Sippo2N", bone)

if "Sippo3N" in fileOrigRead:
    bone = "S_Tail3"
    fileOrigRead = fileOrigRead.replace("Sippo3N", bone)

if "Sipoo4N" in fileOrigRead:
    bone = "S_Tail4"
    fileOrigRead = fileOrigRead.replace("Sipoo4N", bone)

if "Sipoo5N" in fileOrigRead:
    bone = "S_Tail5"
    fileOrigRead = fileOrigRead.replace("Sipoo5N", bone)

if "Sippo6N" in fileOrigRead:
    bone = "S_Tail6"
    fileOrigRead = fileOrigRead.replace("Sippo6N", bone)

if "Sippo7N" in fileOrigRead:
    bone = "S_Tail7"
    fileOrigRead = fileOrigRead.replace("Sippo7N", bone)

if "Sipoo8N" in fileOrigRead:
    bone = "S_Tail8"
    fileOrigRead = fileOrigRead.replace("Sipoo8N", bone)

if "Sippo9N" in fileOrigRead:
    bone = "S_Tail9"
    fileOrigRead = fileOrigRead.replace("Sippo9N", bone)

if "AgoN" in fileOrigRead:
    bone = "Mouth"
    fileOrigRead = fileOrigRead.replace("AgoN", bone)

if "JikuN" in fileOrigRead:
    bone = "Shaft"
    fileOrigRead = fileOrigRead.replace("JikuN", bone)

if "LKataSinN" in fileOrigRead:
    bone = "ShoulderpadL"
    fileOrigRead = fileOrigRead.replace("LKataSinN", bone)

if "RKataSinN" in fileOrigRead:
    bone = "ShoulderpadR"
    fileOrigRead = fileOrigRead.replace("RKataSinN", bone)


# Handle ClavicleC/LegC bone addition

if has_ClavicleC.lower() == "y":
    bone_count = int(re.findall("(\d+).*\nend\nskeleton", fileOrigRead)[0])
    bust_index = int(re.findall("(\d+).*Bust", fileOrigRead)[0])
    clavicleC_index = bone_count + 1
    fileOrigRead = re.sub("(\"ClavicleR\") \d+", "\\1" + " " + str(clavicleC_index), fileOrigRead, 1)
    fileOrigRead = re.sub("(\"ClavicleL\") \d+", "\\1" + " " + str(clavicleC_index), fileOrigRead, 1)
    fileOrigRead = re.sub("(\d+.*)\n(end\nskeleton)", "\\1" + "\n" + str(clavicleC_index) + " \"ClavicleC\" " + str(bust_index) + "\n" + "\\2", fileOrigRead, 1)
    fileOrigRead = re.sub("(\d+)\ntime", "\\1" + "\n" + str(clavicleC_index) + " 0 0 0 0 0 0\ntime", fileOrigRead)
    fileOrigRead = re.sub("end\n\Z", str(clavicleC_index) + " 0 0 0 0 0 0\nend\n", fileOrigRead)

if has_LegC.lower() == "y":
    bone_count = int(re.findall("(\d+).*\nend\nskeleton", fileOrigRead)[0])
    hip_index = int(re.findall("(\d+).*Hip", fileOrigRead)[0])
    legC_index = bone_count + 1
    fileOrigRead = re.sub("(\"LegR\") \d+", "\\1" + " " + str(legC_index), fileOrigRead, 1)
    fileOrigRead = re.sub("(\"LegL\") \d+", "\\1" + " " + str(legC_index), fileOrigRead, 1)
    fileOrigRead = re.sub("(\d+.*)\n(end\nskeleton)", "\\1" + "\n" + str(legC_index) + " \"LegC\" " + str(hip_index) + "\n" + "\\2", fileOrigRead, 1)
    fileOrigRead = re.sub("(\d+)\ntime", "\\1" + "\n" + str(legC_index) + " 0 0 0 0 0 0\ntime", fileOrigRead)
    fileOrigRead = re.sub("end\n\Z", str(legC_index) + " 0 0 0 0 0 0\nend\n", fileOrigRead)

with open(filename + '_conv' + extension, 'w') as fileConv:
    fileConv.write(fileOrigRead)

fileOrig.close()
fileConv.close()
