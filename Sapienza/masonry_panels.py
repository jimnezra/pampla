from pyautocad import Autocad
import array


def stack(brick_length, brick_height, hor_bricks, ver_bricks):
    acad = Autocad(create_if_not_exists=True)
    acad.prompt('Hello, Autocad from Python\n')

    for ver_count in range(ver_bricks):
        for hor_count in range(hor_bricks):
            points = [
                hor_count*brick_length, ver_count*brick_height,
                hor_count*brick_length + brick_length, ver_count*brick_height,
                hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                hor_count*brick_length, ver_count*brick_height + brick_height,
                ]
            points = array.array("d", points)
            pline = acad.model.AddLightWeightPolyline(points)
            pline.Closed = True
    
    return None


def running(brick_length, brick_height, hor_bricks, ver_bricks):
    acad = Autocad(create_if_not_exists=True)
    acad.prompt('Hello, Autocad from Python\n')

    ver_count = 0
    while ver_count < ver_bricks:
        hor_count = 0
        while hor_count < hor_bricks:
            # Bottom course
            if ver_count == 0:
                points = [
                    hor_count*brick_length, 0,
                    hor_count*brick_length + brick_length, 0,
                    hor_count*brick_length + brick_length, brick_height,
                    hor_count*brick_length + brick_length/2, brick_height,
                    hor_count*brick_length, brick_height,
                    ]
                hor_count += 1
            # Top course
            elif ver_count == ver_bricks - 1:
                if ver_bricks % 2 == 0:
                    if hor_count == 0 or hor_count == hor_bricks - 0.5:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 0.5
                    else:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 1
                else:
                    points = [
                        hor_count*brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length/2, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                        hor_count*brick_length, ver_count*brick_height + brick_height,
                        ]
                    hor_count += 1
            # Rest of courses
            else:
                if ver_count != ver_bricks - 1 and (ver_count + 1) % 2 == 0:
                    if hor_count == 0 or hor_count == hor_bricks - 0.5:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 0.5
                    else:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 1
                else:
                    points = [
                        hor_count*brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length/2, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                        hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                        hor_count*brick_length, ver_count*brick_height + brick_height,
                        ]
                    hor_count += 1
                        
            points = array.array("d", points)
            pline = acad.model.AddLightWeightPolyline(points)
            pline.Closed = True
        
        ver_count += 1

    return None


def english(brick_length, brick_height, hor_bricks, ver_bricks):
    acad = Autocad(create_if_not_exists=True)
    acad.prompt('Hello, Autocad from Python\n')

    ver_count = 0
    while ver_count < ver_bricks:
        hor_count = 0
        hor_count2 = 1
        while hor_count < hor_bricks:
            # Bottom course
            if ver_count == 0:
                points = [
                    hor_count*brick_length, 0,
                    hor_count*brick_length + brick_length, 0,
                    hor_count*brick_length + brick_length, brick_height,
                    hor_count*brick_length + brick_length*3/4, brick_height,
                    hor_count*brick_length + brick_length*1/4, brick_height,
                    hor_count*brick_length, brick_height,
                    ]
                hor_count += 1
            # Top course
            elif ver_count == ver_bricks - 1:
                if ver_bricks % 2 == 0:
                    if hor_count == 0 or hor_count == hor_bricks - 0.25:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/4, ver_count*brick_height,
                            hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 0.25
                        hor_count2 += 1
                    else:
                        if hor_count2 % 2 == 0:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.5
                            hor_count2 += 1
                        else:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.5
                            hor_count2 += 1
                else:
                    points = [
                        hor_count*brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                        hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                        hor_count*brick_length, ver_count*brick_height + brick_height,
                        ]
                    hor_count += 1
            # Rest of courses
            else:
                if ver_count != ver_bricks - 1 and (ver_count + 1) % 2 == 0:
                    if hor_count == 0 or hor_count == hor_bricks - 0.25:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/4, ver_count*brick_height,
                            hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 0.25
                        hor_count2 += 1
                    else:
                        if hor_count2 % 2 == 0:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.5
                            hor_count2 += 1
                        else:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.5
                            hor_count2 += 1
                else:
                    points = [
                        hor_count*brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                        hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                        hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                        hor_count*brick_length + brick_length*1/4, ver_count*brick_height + brick_height,
                        hor_count*brick_length, ver_count*brick_height + brick_height,
                        ]
                    hor_count += 1
                        
            points = array.array("d", points)
            pline = acad.model.AddLightWeightPolyline(points)
            pline.Closed = True
        
        ver_count += 1

    return None


def flemish(brick_length, brick_height, hor_bricks, ver_bricks):
    acad = Autocad(create_if_not_exists=True)
    acad.prompt('Hello, Autocad from Python\n')

    ver_count = 0
    while ver_count < ver_bricks:
        hor_count = 0
        hor_count2 = 1
        if (ver_count + 1) % 2 == 0:
            hor_count3 = hor_bricks + 1
            if hor_bricks % 2 != 0:
                hor_count3 +=1
        else:
            hor_count3 = hor_bricks
        while hor_count2 <= hor_count3:
            # Bottom course
            if ver_count == 0:
                if hor_count2 % 2 == 0:
                    points = [
                        hor_count*brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length/2, ver_count*brick_height,
                        hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                        hor_count*brick_length, ver_count*brick_height + brick_height,
                        ]
                    hor_count += 0.5
                    hor_count2 += 1
                else:
                    points = [
                        hor_count*brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height,
                        hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                        hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                        hor_count*brick_length + brick_length*1/4, ver_count*brick_height + brick_height,
                        hor_count*brick_length, ver_count*brick_height + brick_height,
                        ]
                    hor_count += 1
                    hor_count2 += 1
            # Top course
            elif ver_count == ver_bricks - 1:
                if ver_bricks % 2 == 0:
                    if hor_bricks % 2 == 0:
                        if hor_count == 0:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.25
                            hor_count2 += 1
                        elif hor_count2 == hor_bricks + 1:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.75
                            hor_count2 += 1
                        else:
                            if hor_count2 % 2 == 0:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 0.5
                                hor_count2 += 1
                            else:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 1
                                hor_count2 += 1
                    else:
                        if hor_count == 0 or hor_count2 == (hor_bricks + 2):
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.25
                            hor_count2 += 1
                        else:
                            if hor_count2 % 2 == 0:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 0.5
                                hor_count2 += 1
                            else:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 1
                                hor_count2 += 1
                else:
                    if hor_count2 % 2 == 0:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 0.5
                        hor_count2 += 1
                    else:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                            hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 1
                        hor_count2 += 1
            # Rest of courses
            else:
                if ver_count != ver_bricks - 1 and (ver_count + 1) % 2 == 0:
                    if hor_bricks % 2 == 0:
                        if hor_count == 0:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.25
                            hor_count2 += 1
                        elif hor_count2 == hor_bricks + 1:
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.75
                            hor_count2 += 1
                        else:
                            if hor_count2 % 2 == 0:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 0.5
                                hor_count2 += 1
                            else:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                                    hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                                    hor_count*brick_length + brick_length*1/4, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 1
                                hor_count2 += 1
                    else:
                        if hor_count == 0 or hor_count2 == (hor_bricks + 2):
                            points = [
                                hor_count*brick_length, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height,
                                hor_count*brick_length + brick_length/4, ver_count*brick_height + brick_height,
                                hor_count*brick_length, ver_count*brick_height + brick_height,
                                ]
                            hor_count += 0.25
                            hor_count2 += 1
                        else:
                            if hor_count2 % 2 == 0:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height,
                                    hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 0.5
                                hor_count2 += 1
                            else:
                                points = [
                                    hor_count*brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height,
                                    hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                                    hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                                    hor_count*brick_length + brick_length*1/4, ver_count*brick_height + brick_height,
                                    hor_count*brick_length, ver_count*brick_height + brick_height,
                                    ]
                                hor_count += 1
                                hor_count2 += 1
                else:
                    if hor_count2 % 2 == 0:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height,
                            hor_count*brick_length + brick_length/2, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 0.5
                        hor_count2 += 1
                    else:
                        points = [
                            hor_count*brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length*1/4, ver_count*brick_height,
                            hor_count*brick_length + brick_length*3/4, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height,
                            hor_count*brick_length + brick_length, ver_count*brick_height + brick_height,
                            hor_count*brick_length + brick_length*3/4, ver_count*brick_height + brick_height,
                            hor_count*brick_length + brick_length*1/4, ver_count*brick_height + brick_height,
                            hor_count*brick_length, ver_count*brick_height + brick_height,
                            ]
                        hor_count += 1
                        hor_count2 += 1
                
            points = array.array("d", points)
            pline = acad.model.AddLightWeightPolyline(points)
            pline.Closed = True
        
        ver_count += 1

    return None
