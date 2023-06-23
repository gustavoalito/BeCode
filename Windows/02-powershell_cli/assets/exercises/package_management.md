# Powershell Package Management

It's time to start installing software and keep them updated. We will see how to use Chocolatey and how to use Windows Updates.

* Instructions

- Get Windows updates
    - Install the `PSWindowsUpdate` module

`Install-Module -Name PSWindowsUpdate`
=> In order to run the command Get-WindowsUpdate (below), we need to enable PowerShell scripts to run. For that, we need to run the command `Set-ExecutionPolicy RemoteSigned` and Type "A" to accept all. 

![image](https://github.com/gustavoalito/BeCode/assets/133368766/030d6b17-8979-4c73-be6c-4f49075d40c8)

    - Type `Get-WindowsUpdate` to check for updates
    - Type `Install-WindowsUpdate` to install updates

- Manage Packages

Chocolatey or Choco as it is sometimes referred to, is a free, open-source package manager for Windows that is very similar to Apt or DNF in the Linux realm. In other words, this is a program used for installing software via the Windows command line. It downloads a program, installs it, then will check for updates, and installs those updates automatically if needed. Those who use Linux are quite familiar with the package management systems like this.

    - Install `Chocolatey`

From https://chocolatey.org/install, you need to run the following script: `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/44b0eec5-bc02-4d8a-83db-c2cb1fca0219)

    - Install `VLC` from `Chocolatey`
`choco install vlc`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/c8f5e4a2-e63c-4563-b609-b6a32a2a0da7)

    - Upgrade `VLC` to the latest version (it should already be but it's your first use)

`choco upgrade vlc`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/0bddacbc-4b07-4fc2-a12a-b5c346a2bf26)

    - Remove the `VLC` package using `Chocolatey`

`choco uninstall vlc`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/301fd65d-8d86-41c9-a78b-9e8474644703)

    - Could you use `Chocolatey` on already installed software? How?
Chocolatey works in a similar manner to how you would do things if you downloaded and installed things yourself. Its design and infrastructure are built that way on purpose. It takes the pain of manually doing it yourself away.
Now, Chocolatey can take over existing installs and be able to handle uninstalls in most cases. Can is very dependent on the packaging and the underlying software installer that is used for the installation (installer packages are the context here).
So when a package takes over the existing install, if the registry snapshot doesn't differ, it won't be able to automatically uninstall it (if you have autoUninstaller turned on). If there is no chocolateyUninstall.ps1 that would uninstall the software, choco won't be able to uninstall it. At some point, it will though, as choco continues to get better at things. And at some point in the near future it will contain a check to do nothing for an install if a registry key exists (and record that for later uninstall).
Ref.: https://docs.chocolatey.org/en-us/why#can-i-use-chocolatey-with-existing-software

- Manage Windows Features
    - Get installed Windows features with the command `Get-WindowsFeature`

This command is not available on Win10 Enterprise. Only on Server versions.

    - Install a new feature such as hyper-v with `Install-WindowsFeature`

Use this command: `Get-WindowsOptionalFeature -Online`

![image](https://github.com/gustavoalito/BeCode/assets/133368766/20552443-13e9-44f9-aea5-ea3c7bf7cc12)

  - Install a new feature such as hyper-v with Install-WindowsFeature

 It actually needs to be enabled, as you can see in the screenshot above.
`Enable-WindowsOptionalFeature -FeatureName Microsoft-Hyper-V-All -Online`
After Enabling this, the computer will need a restart.
       
**WARNING**: This exercise **will only work on Windows** since it's specific to the way Windows manages packages.
