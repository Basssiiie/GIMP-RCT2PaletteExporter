# OpenRCT2 palette exporter plugin for GIMP

A small plugin for GIMP that links GIMP to the RCTPaletteMaker tool to easily create OpenRCT2 palettes directly from GIMP.

- Exports BMP's with the correct bitmap color info.
- Creates a DAT palette file with your preferred name.

![(Image of the export plugin in GIMP)](https://raw.githubusercontent.com/Basssiiie/GIMP-RCT2PaletteExporter/main/images/plugin.png)

## How to install

1. Download `GIMP-RCT2PaletteExporter.py` from this repository.
2. Paste it into the correct folder by following [this guide](https://thegimptutorials.com/how-to-install-gimp-plugins/).
3. Restart GIMP.
4. You can find the tool under `Export` -> `RCT2 Palette` menu item in the top bar of the program.

## How to use

1. Load a palette BMP into GIMP and edit it to your desires.
2. Press `Export` -> `RCT2 Palette` to open the exporter.
3. Fill in the following fields:
   - **Output folder:** select a folder where the file(s) should be saved.
   - **File name:** select a name for your file.
     - If you want to create a palette DAT file as well, the filename cannot be longer than 8 characters.
   - **Create DAT file:**: select `yes` or `no` on whether you want to create the DAT file.
   - **Path to RCTPALMAKER.exe:** select the `RCTPALMAKER.exe` file, which will be used for creating the DAT file.
     - If `Create DAT file` is set to `no`, this option can be left empty to export the BMP only.
4. Press `OK` to generate your palette file(s).