Android SVG Asset Generator
----
Future proof your assets and save time! This tool allows you to create your image assets once and then let the generator do the hard work.
SVG images are scaled and put into appropriate folders for android and the 9 patch is applied.

Source Image Info
----
The document size on your SVG files should reflect the image size at 72dpi.

Ex: an app icon should be 27x27 px at 72dpi so that when scaled up to 240dpi (HDPI) it is 72x72 px.

To add a 9patch to generated images, add a hidden layer called 9patch see tag.svg for an example

Generating Images
----
	
	./process_assets ./assets ./
