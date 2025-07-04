; Inno Setup Script for CAGED Trainer

[Setup]
AppName=CAGED Trainer
AppVersion=1.0.0
DefaultDirName={pf}\CAGED Trainer
DefaultGroupName=CAGED Trainer
OutputDir=..\build
OutputBaseFilename=CAGED_Trainer_Setup

[Files]
Source: "..\dist\CAGED Trainer\CAGED Trainer.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\CAGED Trainer\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\CAGED Trainer"; Filename: "{app}\CAGED Trainer.exe"
Name: "{commondesktop}\CAGED Trainer"; Filename: "{app}\CAGED Trainer.exe"; Tasks: desktopicon
Name: "{group}\Uninstall CAGED Trainer"; Filename: "{uninstallexe}"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked
