# OpenRCT2 palette exporter plugin for GIMP

A small plugin for GIMP that links GIMP to the RCTPaletteMaker tool to easily create OpenRCT2 palettes directly from GIMP.

- Exports BMP's with the correct bitmap color info.
- Creates a DAT palette file with your preferred name.

Only GIMP 2.10 or higher is supported.

![(Image of the export plugin in GIMP)](https://github.com/Basssiiie/GIMP-RCT2PaletteExporter/raw/main/images/plugin.png)

## How to install

1. Download `GIMP-RCT2PaletteExporter.py` from this repository.
2. Paste it into the correct folder by following [this guide](https://thegimptutorials.com/how-to-install-gimp-plugins/).
3. Restart GIMP.
4. You can find the tool under `Export` -> `RCT2 Palette` menu item in the top bar of the program.

## How to use

1. Load a palette BMP into GIMP and edit it to your desires.
1. Press `Export` -> `RCT2 Palette` to open the exporter.
1. Fill in the following required fields:
   - **Output folder:** select a folder where the file(s) should be saved.
   - **File name:** select a name for your file.
     - If you want to create a palette DAT file as well, the filename cannot be longer than 8 characters.
   - **Create DAT file:**: select `yes` or `no` on whether you want to create the DAT file.
1. Fill in the following fields only if `Create DAT file` is set to `yes`:
   - **Ingame palette name:** select a name for your file.
   - **Path to RCTPALMAKER.exe:** select the `RCTPALMAKER.exe` file, which will be used for creating the DAT file.
1. Press `OK` to generate your palette file(s).
1. (Optional) Copy the DAT file to one of the following folders to have it show up ingame.
	- `/Documents/OpenRCT2/object/` (preferred)
	- `/RollerCoaster Tycoon 2/ObjData/`

## Development

This folder is set up according to [this guide](http://gimpchat.com/viewtopic.php?f=9&t=18606) to make VS Code's Python plugin work with GIMP libraries.

Things to note:
- Path to Python 2.7 is configured in `"python.defaultInterpreterPath"` in `.vscode/settings.json`. Note that this setting is the replacement for the now deprecated `"python.pythonPath"` property mentioned in the guide.
- The `"PYTHONPATH"` environment variable is updated in `.env` and should have the full path to the Python libraries in your GIMP installation, e.g. `/GIMP 2/lib/gimp/2.0/python`.

### Error log

You can see any load or runtime errors by launching GIMP from cmdline, for example with Powershell like:
1. Go to `/GIMP 2/bin/` in the GIMP installation folder.
1. Shift right-click inside the folder (but not on any file).
1. Click the `Open PowerShell window here` option.
1. Type `./gimp-2.##.exe --verbose` but replace the `##` with the version number present in the folder.

### Documentation

- [GIMP Python Documentation](https://www.gimp.org/docs/python/index.html)
- [GIMP Library Reference Manual](https://www.manpagez.com/html/libgimp/libgimp-2.10.16/)
- Procedure manual inside GIMP: `Filters -> Python-fu -> Console -> Browse...`