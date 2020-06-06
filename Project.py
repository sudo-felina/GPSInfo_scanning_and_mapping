import os
from PIL import Image,ExifTags
import gmplot

img_folder = r"/path/to/Dataset"
img_contents = os.listdir(img_folder)
lat_list = []
long_list = []


def convert_to_degrees(value):
    d0= value[0][0]
    d1= value[0][1]
    d = float (d0) / float (d1)
    

    m0= value[1][0]
    m1 = value[1][1]
    m = float (m0)/ float (m1)

    s0= value[2][0]
    s1 = value[2][1]
    s = float (s0) / float (s1)

    return(d + (m/60.0) + (s/3600.0))


for image in img_contents:
    full_path = os.path.join(img_folder,image)
    img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k,v in img.getexif().items() if k in ExifTags.TAGS}
    
    gps_all = {}
    try:
        for key in exif["GPSInfo"].keys():
            decoded_value = ExifTags.GPSTAGS.get(key)
            gps_all[decoded_value] = exif["GPSInfo"][key]
        
        long_ref = gps_all.get('GPSLongitudeRef')
        lat_ref = gps_all.get("GPSLatitudeRef")
        
        
        longg = gps_all.get('GPSLongitude')
        lat = gps_all.get('GPSLatitude')
        
        
        
        if lat_ref == "S":
            lat_degre = -abs(convert_to_degrees(lat))
        else :
            lat_degre = convert_to_degrees(lat)
        if long_ref == "W":
            longg_degre = -abs(convert_to_degrees(longg))
        else:
            longg_degre = convert_to_degrees(longg)
        
        lat_list.append(lat_degre)
        long_list.append(longg_degre)


                    
    except:
        print("Image {} no gps".format(image))
        pass


gmap = gmplot.GoogleMapPlotter(56.4907,-4.2026,8)   #Defines the base map i.e the co-ordinates of the region where the photo was taken. 
gmap.heatmap(lat_list,long_list)
gmap.draw("/path/to/heat/map.html")
