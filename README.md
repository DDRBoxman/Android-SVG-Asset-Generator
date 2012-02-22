Android SVG Asset Generator
----
Future proof your assets and save time! 

This tool allows you to use SVG files for your Android apps resources. 

This means that you only have to create art once or find SVG files online.

SVG images are scaled and put into appropriate folders for android and the 9 patch is applied.

Iconograpy for apps can be quickly generated from content from sites like those below:
http://www.fileformat.info/info/unicode/char/search.htm

Generating Images
----
Example:

	./process_assets ./assets/ ./
	
The asset generator code can be kept in a sub folder and called from there. This makes it really easy to include in your project as a git submodule.

	./asset_generator/process_assets ./source_images/ ./AndroidProjectFolder/

Source Image Info
----
The document size on your SVG files should reflect the image size at 72dpi.

Ex: an app icon should be 27x27 px at 72dpi so that when scaled up to 240dpi (HDPI) it is 72x72 px.

To add a 9patch to generated images, add a hidden layer called 9patch see tag.svg for an example

Requirements
----
* Linux, OS X, (Cygwin? requires inkscape to be on your path.)
* Inkscape
* Python
* PIL