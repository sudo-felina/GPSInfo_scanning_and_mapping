# Mapping of geotagged images
This python script traverses through all the images in the sepcified directory and gives us a **heat map** using the gps location present in those images metadata.Since EXIF metadata are present only in .jpeg files, so this will work only for jpeg/jpg images.
Along with giving us the heat map, it can also print out the metadata of each image which sometimes proves extremely useful during an investigation.

**Pillow library** was used for getting the exif metadata and **Gmplot** was used for plotting of the heat map.Gmplot provides us with many different options for plotting of those points and you can read about it more at https://pypi.org/project/gmplot/.

Data-set used here was take from the following link https://www.kaggle.com/jbakerdstl/geolocated-imagery-dataset-scotland.

![output](GPSInfo_scanning_and_mapping/Output.png)
Format: ![Alt Text](url)
