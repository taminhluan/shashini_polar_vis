
def read_data(filename):
    input_file = open(filename)

    count = 0
    result = []
    point = []
    header_line = True

    old_value = -1
    while True:
        line = input_file.readline()
        if not line:
            break
        
        line = line.replace('"Point(X = ', '').replace(' Y = ', '').replace(' Z = ', '').replace(')"', '').replace(',\n', '')
        if True:
        # try:
            arr = line.split(',')
            x = arr[0]
            y = arr[1]
            z = arr[2]
            radiation = float(arr[3])

            vertice = (float(x), float(y), float(z))
            
            if count % 9 == 0:
                if old_value != -1:
                    point.append(radiation)
                    result.append(point)
                    point = []
            point.append(vertice)
            old_value = 9
                
            # mod = count % 9
            # vertice = (float(x), float(y), float(z))
            # if mod == 0:
            #     point = [vertice]
            # elif mod == 2 or mod == 6:
            #     point.append(vertice)
            # elif mod == 8:
            #     point.append(vertice)
            #     point.append(float(radiation))
            #     result.append(point)
            count += 1
        # except:
        #     count += 1
        #     print('ERROR')
        #     print(line)
        #     continue
    return result
    
    

