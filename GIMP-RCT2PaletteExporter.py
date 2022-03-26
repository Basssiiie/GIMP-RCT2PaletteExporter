#! /usr/bin/env python

from datetime import date
import os
import struct
import subprocess
import gimpfu
import gimp


# Strip bitmap color info (BMP v3)
#  Thanks to https://stackoverflow.com/a/30531080
#  and https://en.wikipedia.org/wiki/BMP_file_format#DIB_header_(bitmap_information_header)
def bmp_strip_extra_header_data(bmp_file_name):
	# Bitmap offsets
	FILE_SIZE_OFFSET = 2
	PIXEL_START_OFFSET = 10
	HEADER_OFFSET = 14
	# Required sizes for 'BITMAPINFOHEADER'
	REQUIRED_HEADER_SIZE = 40
	REQUIRED_PIXEL_OFFSET = 54

	# Open bitmap file
	with open(bmp_file_name, "rb+") as bitmap_file:
		data = bytearray(bitmap_file.read())
		header_size = struct.unpack("I", data[HEADER_OFFSET: HEADER_OFFSET + 4])[0]

		if header_size != REQUIRED_HEADER_SIZE:
			# Move pixel data to offset 54
			original_pixel_start = struct.unpack("I", data[PIXEL_START_OFFSET: PIXEL_START_OFFSET + 4])[0]
			data[REQUIRED_PIXEL_OFFSET:] = data[original_pixel_start:]

			# Update new header size, start of pixel data and file size
			data[HEADER_OFFSET: HEADER_OFFSET + 4] = struct.pack("I", REQUIRED_HEADER_SIZE)
			data[PIXEL_START_OFFSET: PIXEL_START_OFFSET + 4] = struct.pack("I", REQUIRED_PIXEL_OFFSET)
			data[FILE_SIZE_OFFSET: FILE_SIZE_OFFSET + 4] = struct.pack("I", len(data))

		# Write new bitmap file to disk
		bitmap_file.seek(0)
		bitmap_file.write(data)
		bitmap_file.truncate()


# Export the palette as the correct *.bmp and DAT files.
def export_palette(img, layer, output_folder, file_name, create_dat_file, palette_name, palette_maker_path):

	if (create_dat_file and len(file_name) > 8):
		gimp.message("Error: DAT file name cannot be longer than 8 characters!")
		return

	# DATs are always uppercase
	file_name = file_name.upper()

	# Get a copy of the image
	gimpfu.pdb.gimp_selection_all(img)
	gimpfu.pdb.gimp_edit_copy_visible(img)
	img_copy = gimpfu.pdb.gimp_edit_paste_as_new_image()

	# Remove the alpha layer
	gimpfu.pdb.gimp_layer_flatten(img_copy.layers[0])

	# Save to disk as *.bmp
	file_name_bmp = (file_name + ".bmp")
	save_path = os.path.join(output_folder, (file_name_bmp))
	gimpfu.pdb.gimp_file_save(img_copy, img_copy.layers[0], save_path, save_path)
	bmp_strip_extra_header_data(save_path)

	# Run PaletteMaker
	if (create_dat_file):
		subprocess.check_call([palette_maker_path, file_name, (file_name + ".DAT"), palette_name, file_name_bmp], cwd=output_folder)

	# Delete the image copy
	gimpfu.pdb.gimp_image_delete(img_copy)


# Register the export functionality
gimpfu.register("export-rct2-palette",
	"""
Export this image as a RCT2 compatible 24-bit *.bmp file and optionally converts it to a *.DAT palette with the RCT2 Palette Maker.

Please note:

 - RCT2 palettes are must have at least 326 pixels total. Something like 16x21 is recommended.

 - When exporting as *.DAT, the file name must be globally unique and not longer than 8 characters. Do not use a common name, because users cannot load your palette if they already have a RCT2 object installed with the same name.

 - To install the palette, place it into either '/Documents/OpenRCT2/object/' or '/RollerCoaster Tycoon 2/ObjData/'.
	""",
	"Exports this image as a RCT2 palette.",
	"Basssiiie", "Basssiiie", str(date.today().year),
	"<Image>/Export/RCT2 Palette",
	"*",
	[
		(gimpfu.PF_DIRNAME, "output-folder", "Output folder", None),
		(gimpfu.PF_STRING, "file-name", "File name", 'EXAMPLE'),
		(gimpfu.PF_BOOL, "create-dat-file", "Create DAT file", True),
		(gimpfu.PF_STRING, "palette-name", "Ingame palette name", 'Example name'),
		(gimpfu.PF_FILE, "palette-maker-path", "Path to RCTPALMAKER.exe", None),
	],
	[],
	export_palette) #, menu, domain, on_query, on_run)

gimpfu.main()