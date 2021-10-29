import json
from src.read_roid import Roi
import os
import cv2 as cv



head = '{"_via_settings":{"ui":{"annotation_editor_height":25,"annotation_editor_fontsize":0.8,"leftsidebar_width":18,"image_grid":{"img_height":80,"rshape_fill":"none","rshape_fill_opacity":0.3,"rshape_stroke":"yellow","rshape_stroke_width":2,"show_region_shape":true,"show_image_policy":"all"},"image":{"region_label":"__via_region_id__","region_color":"__via_default_region_color__","region_label_font":"10px Sans","on_image_annotation_editor_placement":"NEAR_REGION"}},"core":{"buffer_size":18,"filepath":{},"default_filepath":""},"project":{"name":"via_project_1Sep2021_16h14m"}},"_via_img_metadata":{'

for i in range(4):
    imagen = str(i)
    try:
        roi = Roi('datasets/roi/'+imagen + ".roi")
        contorno = roi.get_contorno()
        print (contorno)
        img = cv.imread('datasets/label/'+imagen + ".png")
        # x, y = zip(*contorno)
        # d = '"' + imagen + '.png2006417":{"filename":"' + imagen + '.png","size":2006417,"regions":[{"shape_attributes":{"name":"polyline","all_points_x":' + str(
        #     list(x)) + ',"all_points_y":' + str(list(y)) + '},"region_attributes":{}}],"file_attributes":{}}'
        # head = head + d
        # head = head + ','

    except:
        print("imagen no encontrada: ", i)

cadena = head[:-1] + '},"_via_attributes":{"region":{},"file":{}}}'

data = json.loads(cadena)

# with open('via_project_1Sep2021_16h14m.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)