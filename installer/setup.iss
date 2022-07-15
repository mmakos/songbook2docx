﻿; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{08D4F6FB-E6A8-4637-AC92-C8AA3DD017B6}
AppName=Songbook to docx
AppVersion=1.0
;AppVerName=Songbook to docx 1.0
AppPublisher=Michał Makoś
AppPublisherURL=https://spiewnik.mmakos.pl
AppSupportURL=https://spiewnik.mmakos.pl
AppUpdatesURL=https://spiewnik.mmakos.pl
DefaultDirName={autopf}\Songbook2docx
ChangesAssociations=yes
DefaultGroupName=Songbook to docx
DisableProgramGroupPage=yes
LicenseFile=C:\Users\mmakos\PycharmProjects\Songbook-Online\html2docx\licence.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\mmakos\PycharmProjects\Songbook-Online\html2docx\installer
OutputBaseFilename=Songbook2docx
SetupIconFile=C:\Users\mmakos\PycharmProjects\Songbook-Online\html2docx\smm.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "polish"; MessagesFile: "compiler:Languages\Polish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\mmakos\PycharmProjects\Songbook-Online\html2docx\dist\songbook2docx.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\mmakos\PycharmProjects\Songbook-Online\html2docx\dist\fonts"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\mmakos\PycharmProjects\Songbook-Online\html2docx\dist\conf.ini"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\.smm\OpenWithProgids"; ValueType: string; ValueName: "ŚpiewnikMichałaMakosia.smm"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\ŚpiewnikMichałaMakosia.smm"; ValueType: string; ValueName: ""; ValueData: "Śpiewnik Michała Makosia"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\ŚpiewnikMichałaMakosia.smm\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\songbook2docx.exe,0"
Root: HKA; Subkey: "Software\Classes\ŚpiewnikMichałaMakosia.smm\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\songbook2docx.exe"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\songbook2docx.exe\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{group}\Songbook to docx"; Filename: "{app}\songbook2docx.exe"
Name: "{autodesktop}\Songbook to docx"; Filename: "{app}\songbook2docx.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\songbook2docx.exe"; Description: "{cm:LaunchProgram,Songbook to docx}"; Flags: nowait postinstall skipifsilent

