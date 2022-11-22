#pip install comtypes
#pip install pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

#devices = AudioUtilities.GetSpeakers()
#interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#volume = cast(interface, POINTER(IAudioEndpointVolume))

#FOR MASTER VOLUME
#volume.SetMasterVolumeLevel(-65.0, None)
#changing 1 to 0 will bypass the mute
#volume.SetMute(1, None)

#ADD LEVEL TO MASTER VOLUME
#current = volume.GetMasterVolumeLevel()
#volume.SetMasterVolumeLevel(current + 6.0, None)

#VOLUME CONTROL FOR INDIVIDUAL PROGRAM
#sessions = AudioUtilities.GetAllSessions()
#for session in sessions:
#    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
#    if session.Process and session.Process.name() == "program.exe":
#        volume.SetMasterVolume(0.5, None) 
#THIS WILL CHANGE THE PROGRAM'S VOLUME TO HALF IT'S ORIGINAL VOLUME