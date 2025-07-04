; Inno Setup Script for CAGED Trainer

[Setup]
AppName=CAGED Trainer
AppVersion=1.0.0
DefaultDirName={pf}\CAGED Trainer
DefaultGroupName=CAGED Trainer
OutputDir=build
OutputBaseFilename=CAGED_Trainer_Setup

[Files]
Source: "dist\CAGED Trainer\CAGED Trainer.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\CAGED Trainer"; Filename: "{app}\CAGED Trainer.exe"
