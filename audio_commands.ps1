# Import the AudioDeviceCmdlets module
Import-Module AudioDeviceCmdlets

# List all audio devices
Get-AudioDevice

# Set the default audio playback device (replace with your device name)
Set-AudioDevice -Playback -Name "Your_Speakers_Name"

# Adjust the volume of the default audio playback device
Set-AudioDeviceVolume -Playback -Volume 50  # Set volume to 50%

# Mute the default audio playback device
Set-AudioDeviceMute -Playback -Mute $true

# Unmute the default audio playback device
Set-AudioDeviceMute -Playback -Mute $false
