@echo off

REM mklink /J (Junction) OR /H (Hardlink) OR /D (Symbolic link) + "link-to" "link-from"

mklink /H "E:\Minecraft\All-the-Mods-6-v1.6.4_remix\overrides\config\crossroads-server.toml" "E:\Minecraft\All-the-Mods-6-v1.6.4_remix\.remix-patch\config\crossroads-server.toml"
mklink /H "E:\Minecraft\All-the-Mods-6-v1.6.4_remix\overrides\config\alexsmobs.toml" "E:\Minecraft\All-the-Mods-6-v1.6.4_remix\.remix-patch\config\alexsmobs.toml"

pause