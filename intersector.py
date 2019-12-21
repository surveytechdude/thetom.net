from collections import defaultdict

def line_intersection(line1, line2):
    try:
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        #if div == 0:

        #raise Exception('lines do not intersect')


        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y
    except:
        pass

dict_gridline_northing = defaultdict(list)
dict_gridline_easting = defaultdict(list)
dict_gridline_xy_intersections = {}


userinput_linedata_fn = input("line data filename: ").rstrip(".txt")
userinput_pointdata_fn = input("Point data filename: ").rstrip(".txt")

userinput_linedata_fn += ".txt"
userinput_pointdata_fn += ".txt"
linedata_file = open(userinput_linedata_fn,'r+')

intersect_file_readlines = linedata_file.readlines()
print(intersect_file_readlines)

pointdata_file = open(userinput_pointdata_fn,'r+')
pointdata_file_readlines = pointdata_file.readlines()
print(pointdata_file_readlines)

for i in intersect_file_readlines:
    print("\n--------------------------------")
    intersect_file_currentline = (str(i).rstrip('\n'))
    print("intersect_file_currentline: " + str(intersect_file_currentline))
    intersect_file_currentline_split = intersect_file_currentline.split(",")
    print("intersect_file_currentline_split: " + str(intersect_file_currentline_split))
    currentline_number = intersect_file_currentline_split[0]
    currentline_northing = intersect_file_currentline_split[1]
    currentline_easting = intersect_file_currentline_split[2]
    currentline_elevation = intersect_file_currentline_split[3]
    currentline_description = intersect_file_currentline_split[4]
    currentline_gridline1 = currentline_description
    print("currentline_number: " + str(currentline_number))
    print("currentline_northing: " + str(currentline_northing))
    print("currentline_easting: " + str(currentline_easting))
    print("currentline_elevation: " + str(currentline_elevation))
    print("currentline_description: " + str(currentline_description))
    print("currentline_gridline1: " + str(currentline_gridline1))
    #print("currentline_gridline2: " + str(currentline_gridline2))

    dict_gridline_northing[currentline_gridline1].append(currentline_northing)

    dict_gridline_easting[currentline_gridline1].append(currentline_easting)

print("dict_gridline_northing: " + str(dict_gridline_northing))
print("dict_gridline_easting: " + str(dict_gridline_easting))



dict_gridlines = defaultdict(list)
print("\n---------------------------------------------")
for i in dict_gridline_easting:
    print("\n---------------------------------------------")
    print("i in dict_gridline_easting: " + str(i))
    gridline_northing_out = dict_gridline_northing.get(i)
    gridline_easting_out = dict_gridline_easting.get(i)
    print("gridline_northing_out: " + str(gridline_northing_out))
    print("gridline_easting_out: " + str(gridline_easting_out))

    if len(gridline_northing_out) > 1:
        print("*****************************")
        gridline_northing1 = gridline_northing_out[0]
        gridline_northing2 = gridline_northing_out[1]
        gridline_easting1 = gridline_easting_out[0]
        gridline_easting2 = gridline_easting_out[1]
        print("gridline_northing1: " + str(gridline_northing1))
        print("gridline_northing2: " + str(gridline_northing2))
        print("gridline_easting1: " + str(gridline_northing1))
        print("gridline_easting2: " + str(gridline_northing2))
        dict_gridlines[i].append(gridline_easting1)
        dict_gridlines[i].append(gridline_northing1)
        dict_gridlines[i].append(gridline_easting2)
        dict_gridlines[i].append(gridline_northing2)
        print("*****************************")

print("\n---------------------------------------------")
print("dict_gridlines: " + str(dict_gridlines))


print("\n---------------------------------------------")
for i in dict_gridlines:
    print("\n---------------------------------------------")
    print("i in dict_gridlines: " + str(i))
    gridline_linepoints = dict_gridlines.get(i)
    print("gridline_linepoints: " + str(gridline_linepoints))

    for j in dict_gridlines:
        print("*****************************")
        print("Gridline " + str(i) + " compared to gridline " + str(j))
        gridline_linepoint_intersecting = dict_gridlines.get(j)
        print("gridline_linepoints: " + str(gridline_linepoints))
        print("gridline_linepoint_intersecting: " + str(gridline_linepoint_intersecting))
        print("*****************************")


        A = (float(gridline_linepoints[1]),float(gridline_linepoints[0]))
        B = (float(gridline_linepoints[3]),float(gridline_linepoints[2]))
        C = (float(gridline_linepoint_intersecting[1]),float(gridline_linepoint_intersecting[0]))
        D = (float(gridline_linepoint_intersecting[3]),float(gridline_linepoint_intersecting[2]))
        print("A: " + str(A))
        print("B: " + str(B))
        print("C: " + str(C))
        print("D: " + str(D))
        line1 = (A,B)
        line2 = (C,D)
        print("*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$")
        currentline_intersection_label = str(i) + "/" + str(j)
        currentline_intersection_label_inverted = str(j) + "/" + str(i)
        xy_intersection = line_intersection(line1,line2)
        print("currentline_intersection_label: " + str(currentline_intersection_label))
        print("xy_intersection: " + str(xy_intersection))


        #check if inverse label is not already in the dictionary
        inversioncheck = dict_gridline_xy_intersections.get(currentline_intersection_label_inverted)
        print("*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$")
        if xy_intersection != None and inversioncheck == None:
            dict_gridline_xy_intersections[currentline_intersection_label] = xy_intersection

    print("dict_gridline_xy_intersections: " + str(dict_gridline_xy_intersections))

print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
output_labeledpoints_txt = open('labeledpoints.txt','w+')
for i in pointdata_file_readlines:
    print("\n--------------------------------")
    pointdata_file_currentline = (str(i).rstrip('\n'))
    print("pointdata_file_currentline: " + str(pointdata_file_currentline))
    pointdata_file_currentline_split = pointdata_file_currentline.split(",")
    pointdata_currentline_number = pointdata_file_currentline_split[0]
    pointdata_currentline_northing = pointdata_file_currentline_split[1]
    pointdata_currentline_easting = pointdata_file_currentline_split[2]
    pointdata_currentline_elevation = pointdata_file_currentline_split[3]
    pointdata_currentline_description = pointdata_file_currentline_split[4]
    print("pointdata_currentline_number: " + str(pointdata_currentline_number))
    print("pointdata_currentline_northing: " + str(pointdata_currentline_northing))
    print("pointdata_currentline_easting: " + str(pointdata_currentline_easting))
    print("pointdata_currentline_elevation: " + str(pointdata_currentline_elevation))
    print("pointdata_currentline_description: " + str(pointdata_currentline_description))
    print("*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$")
    list_total_diff_xy = []
    list_labels_for_totaldiffxy = []
    for j in dict_gridline_xy_intersections:

        compared_intersection_tuple = dict_gridline_xy_intersections.get(j)
        print("compared_intersection_tuple " + str(j) + ": " + str(compared_intersection_tuple))
        diff_x_point_intersection = float(pointdata_currentline_easting) - float(compared_intersection_tuple[1])
        diff_y_point_intersection = float(pointdata_currentline_northing) - float(compared_intersection_tuple[0])
        print("diff_x_point_intersection: " + str(diff_x_point_intersection))
        print("diff_y_point_intersection: " + str(diff_y_point_intersection))
        total_diff_xy = abs(diff_x_point_intersection) + abs(diff_y_point_intersection)
        print("total_diff_xy: " + str(total_diff_xy))

        list_labels_for_totaldiffxy.append(j)
        list_total_diff_xy.append(total_diff_xy)

    minimum_total_diff_xy = min(list_total_diff_xy)

    index_for_minimum_total_diff_xy = list_total_diff_xy.index(minimum_total_diff_xy)
    label_for_minimum_total_diff_xy = list_labels_for_totaldiffxy[index_for_minimum_total_diff_xy]

    print("index_for_minimum_total_diff_xy: " + str(index_for_minimum_total_diff_xy))
    print("label_for_minimum_total_diff_xy:" + str(label_for_minimum_total_diff_xy))
    print("minimum_total_diff_xy: " + str(minimum_total_diff_xy))

    output_labeledpoints_txt.write(pointdata_currentline_number)
    output_labeledpoints_txt.write(",")
    output_labeledpoints_txt.write(pointdata_currentline_northing)
    output_labeledpoints_txt.write(",")
    output_labeledpoints_txt.write(pointdata_currentline_easting)
    output_labeledpoints_txt.write(",")
    output_labeledpoints_txt.write(pointdata_currentline_elevation)
    output_labeledpoints_txt.write(",")
    output_labeledpoints_txt.write(label_for_minimum_total_diff_xy)
    output_labeledpoints_txt.write("\n")
