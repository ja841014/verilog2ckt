import re
# def translator(src,dst):
if __name__ == "__main__":
    fin = open('verilog.v', 'r')
    f = open('f_input.txt', 'w')
    f_output = open('f_output.txt', 'w')
    f_wire = open('f_wire.txt', 'w')
    f_gate = open('gate_.txt', 'w')
    # read all verilog file in list
    f_content = fin.readlines()
    

    # seperate the file #
    # read content line by line
    for i in range(len(f_content)):
        # create a file only contain input output and wire information
        if f_content[i].find("Input") == 0:
            f.write(f_content[i])
        elif f_content[i].find("Output") == 0:
            f_output.write(f_content[i])
            # print(f_content[i])
        elif f_content[i].find("Wire") == 0:
            f_wire.write(f_content[i])
        # create a file only contain gate information
        elif f_content[i].find("Module") == -1 and f_content[i].find("Endmodule") == -1 and f_content[i] not in ['\n','\r\n']: 
            f_gate.write(f_content[i])
            # print(f_content[i])
    fin.close()
    f_gate.close()
    f.close()
    f_output.close()
    f_wire.close()

    # create a map #
    input_arr = []
    output_arr = []
    wire_arr = []

    #############
    # input_arr #
    #############
    f_r_in = open("f_input.txt", "r", encoding='UTF-8')
    # print("a",f_r_in_out_wire)
    flist_in= list(f_r_in)
    # print("qq",flist_in_out_wire)
    count = 0
    inarr_num = 0
    # print line by line
    for i in range(len(flist_in)):
        sepe_arr = flist_in[i].split()
        if sepe_arr[0].find('Input[') == 0:
            # print("here?")
            # print word by word
            count = 0
            for j in sepe_arr:
                # eliminate the the first one input[8:0] and extract its number
                if count == 0:
                    inarr_num = int(j[6])
                    # print(inarr_num)
                    count += 1
                else:
                    # using th number we acquire from above and input the input array 
                    for k in range(inarr_num + 1):
                        input_arr.append(j.strip(',;') +'['+ str(k) + ']')
        else:
            count = 0
            # print word by word
            # input the single input
            for j in sepe_arr:
                if count != 0:
                    input_arr.append(j.strip(',;'))
                count += 1
    print('input_arr',input_arr)
    f_r_in.close()

    ##############
    # output_arr #
    ##############

    f_r_out = open("f_output.txt", "r", encoding='UTF-8')
    # print("a",f_r_in_out_wire)
    flist_out= list(f_r_out)
    # print("qq",flist_in_out_wire)
    count = 0
    outarr_num = 0
    # print line by line
    for i in range(len(flist_out)):
        sepe_arr = flist_out[i].split()
        if sepe_arr[0].find('Output[') == 0:
            # print("here?")
            # print word by word
            count = 0
            for j in sepe_arr:
                # eliminate the the first one output[8:0] and extract its number
                if count == 0:
                    outarr_num = int(j[7])
                    # print(inarr_num)
                    count += 1
                else:
                    # using th number we acquire from above and input the input array 
                    for k in range(outarr_num + 1):
                        output_arr.append(j.strip(',;') +'['+ str(k) + ']')
        else:
            count = 0
            # print word by word
            # input the single input
            for j in sepe_arr:
                if count != 0:
                    output_arr.append(j.strip(',;'))
                count += 1
    print('output_arr',output_arr)
    f_r_out.close()

    ############
    # wire_arr #
    ############

    f_r_wire = open("f_wire.txt", "r", encoding='UTF-8')
    # print("a",f_r_in_out_wire)
    flist_wire= list(f_r_wire)
    # print("qq",flist_in_out_wire)
    count = 0
    wirearr_num = 0
    # print line by line
    for i in range(len(flist_wire)):
        sepe_arr = flist_wire[i].split()
        if sepe_arr[0].find('Wire[') == 0:
            # print("here?")
            # print word by word
            count = 0
            for j in sepe_arr:
                # eliminate the the first one wire[8:0] and extract its number
                if count == 0:
                    wirearr_num = int(j[5])
                    # print(inarr_num)
                    count += 1
                else:
                    # using th number we acquire from above and input the input array 
                    for k in range(wirearr_num + 1):
                        wire_arr.append(j.strip(',;') +'['+ str(k) + ']')
        else:
            count = 0
            # print word by word
            # input the single input
            for j in sepe_arr:
                if count != 0:
                    wire_arr.append(j.strip(',;'))
                count += 1
    print('wire_arr',wire_arr)
    f_r_wire.close()

    ##################
    #gate information#
    ##################

    f_r_gate = open("gate_.txt", "r", encoding='UTF-8')
    # print("a",f_r_in_out_wire)
    flist_gate= list(f_r_gate)
    # print("qq",flist_in_out_wire)
    count = 0
    wirearr_num = 0
    gate_freq = {}
    wire_gate_relation = {}
    # print line by line
    for i in range(len(flist_gate)):
        count = 0
        sepe_arr = flist_gate[i].split()
        # print(sepe_arr)
        wire_gate_relation[sepe_arr[2].strip('(),;')] = sepe_arr[0].strip('(),;')
        # print word by word
        for j in sepe_arr:
            # if not found in dictionary 
            if gate_freq. __contains__(j.strip('(),;')) == False and count >= 3:
                # print("not found", j.strip('(),;'))
                gate_freq[j.strip('(),;')] = 1
            # if found in dictionary
            elif gate_freq. __contains__(j.strip('(),;')) == True and count >= 3:
                # print("found")
                gate_freq[j.strip('(),;')] += 1
            count += 1

    ## input to gate wire
    gate_input_num = {}
    
    for i in range(len(flist_gate)):
        count = 0
        sepe_arr = flist_gate[i].split()
        input_to_gate = []
        pre_gate = ""
        for j in sepe_arr:
            # key
            if count == 2:
                gate_input_num[j.strip('(),;')] = input_to_gate
                pre_gate = j.strip('(),;')
            # value
            if count >= 3:
                gate_input_num.get(pre_gate).append(j.strip('(),;'))
            count += 1
    print("gate_input_num", gate_input_num)
    # print("gate_input_num.get(N10): ", len(gate_input_num.get("N10")))
    # print("gate_input_num.get(N10)[0]: ", gate_input_num.get("N10")[0])
    print('gate_freq: ',gate_freq)
    print("wire_gate_relation: ",wire_gate_relation)
    f_r_gate.close()
    
    #################
    #Build up column#
    #################
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []

    ## column 1 ##

    ## deal with input(1) and its branch(2)
    for i in range(len(input_arr)):
        # print(i)
        column1.append(1)
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            for j in range(int(gate_freq.get(input_arr[i]))):
                column1.append(2)
    ## deal with wire(inner gate output)(0) and its branch(2)
    for i in range(len(wire_arr)):
        column1.append(0)
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column1.append(2)
    ## deal with output gate(3)
    for i in range(len(output_arr)):
        column1.append(3)

    print(column1)

    ## column 2 ##
    count = 1
    map_id = {}
    ## deal with input and its branch
    for i in range(len(input_arr)):
        # print(i)
        column2.append(count)
        map_id[input_arr[i]] = count
        count += 1
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            for j in range(int(gate_freq.get(input_arr[i]))):
                column2.append(count)
                count += 1
    ##deal with inner gate output and its branch
    for i in range(len(wire_arr)):
        column2.append(count)
        map_id[wire_arr[i]] = count
        count += 1
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column2.append(count)
                count += 1
    ## deal with output gate 
    for i in range(len(output_arr)):
        column2.append(count)
        map_id[output_arr[i]] = count
        count += 1

    print(column2)
    ## column 3 ##
    ## deal with input and its branch
    for i in range(len(input_arr)):
        # print(i)
        column3.append(0)
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            for j in range(int(gate_freq.get(input_arr[i]))):
                column3.append(1)
    ## deal with inner gate
    for i in range(len(wire_arr)):
        if wire_gate_relation.get(wire_arr[i]) == 'xor':
            column3.append(2)
        elif wire_gate_relation.get(wire_arr[i]) == 'or':
            column3.append(3)
        elif wire_gate_relation.get(wire_arr[i]) == 'nor':
            column3.append(4)
        elif wire_gate_relation.get(wire_arr[i]) == 'not':
            column3.append(5)
        elif wire_gate_relation.get(wire_arr[i]) == 'Nand':
            column3.append(6)
        elif wire_gate_relation.get(wire_arr[i]) == 'and':
            column3.append(7)
        elif wire_gate_relation.get(wire_arr[i]) == 'xnor':
            column3.append(8)

        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column3.append(1)
    ## deal with ouput gate
    for i in range(len(output_arr)):
        if wire_gate_relation.get(output_arr[i]) == 'xor':
            column3.append(2)
        elif wire_gate_relation.get(output_arr[i]) == 'or':
            column3.append(3)
        elif wire_gate_relation.get(output_arr[i]) == 'nor':
            column3.append(4)
        elif wire_gate_relation.get(output_arr[i]) == 'not':
            column3.append(5)
        elif wire_gate_relation.get(output_arr[i]) == 'Nand':
            column3.append(6)
        elif wire_gate_relation.get(output_arr[i]) == 'and':
            column3.append(7)
        elif wire_gate_relation.get(output_arr[i]) == 'xnor':
            column3.append(8)
    print(column3)

    ## column 4 ##
    count = -1
    nonstopcount = -1
    ## deal with input and its branch
    for i in range(len(input_arr)):
        # print(i)
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            column4.append(gate_freq.get(input_arr[i]))
            count += 1
            nonstopcount += 1
            # print("gate>=2:",count)
            for j in range(int(gate_freq.get(input_arr[i]))):
                column4.append(column2[count])
                nonstopcount += 1
            count = nonstopcount
        elif gate_freq.get(input_arr[i]) != None:
            column4.append(gate_freq.get(input_arr[i]))
            count += 1
            nonstopcount += 1
            # print("gate=1:",count)
    # print(count)
    ## deal with inner gate and its branch
    for i in range(len(wire_arr)):
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            column4.append(gate_freq.get(wire_arr[i]))
            count += 1
            nonstopcount += 1
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column4.append(column2[count])
                nonstopcount += 1
            count = nonstopcount
        elif gate_freq.get(wire_arr[i]) != None:
            column4.append(gate_freq.get(wire_arr[i]))
            count += 1
            nonstopcount += 1
    ## deal with output gate
    for i in range(len(output_arr)):
        column4.append(0)
        # count += 1
        # nonstopcount += 1
    print(column4)

    ## column 5 ##
    ## NOTE: not sure column5.append(' ') or column5.append('')
    ## deal with input(0) and its branch(empty)
    for i in range(len(input_arr)):
        # print(i)
        column5.append(0)
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            for j in range(int(gate_freq.get(input_arr[i]))):
                column5.append(' ')
    # ftest = open("testblank.txt", 'w')
    # for i in range(len(column5)):
    #     ftest.write(str(column5[i]))

    ##deal with inner gate output and its branch
    for i in range(len(wire_arr)):
        column5.append(2)
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column5.append(' ')
    ## deal with output gate 
    for i in range(len(output_arr)):
        column5.append(2)
    print(column5)
    
    ## column 6 ##
    print('map_id: ',map_id)
    gate_input_id = {}
    used = []
    # process what is the line id input to the inner gate 
    count = 1
    for i in range(len(wire_arr)):
        if wire_arr[i] not in gate_input_id:
            gate_input_id[map_id.get(wire_arr[i])] = []
            for j in range(len(gate_input_num.get(wire_arr[i]))):
                if gate_freq.get( gate_input_num.get(wire_arr[i])[j] ) >= 2:
                    # print("sss", map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count in used)
                    while map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count in used:
                        count += 1
                        # print("count", count)
                    gate_input_id.get(map_id.get(wire_arr[i])).append(map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count)
                    used.append(map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count)
                    
                elif gate_freq.get( gate_input_num.get(wire_arr[i])[j] ) == 1:
                    gate_input_id.get(map_id.get(wire_arr[i])).append(map_id.get( gate_input_num.get(wire_arr[i])[j] ))
            count = 1
    # process what is the line id input to the output gate 
    count = 1
    for i in range(len(output_arr)):
        if output_arr[i] not in gate_input_id:
            gate_input_id[map_id.get(output_arr[i])] = []
            for j in range(len(gate_input_num.get(output_arr[i]))):
                if gate_freq.get( gate_input_num.get(output_arr[i])[j] ) >= 2:
                    # print("sss", map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count in used)
                    while map_id.get( gate_input_num.get(output_arr[i])[j] ) + count in used:
                        count += 1
                        # print("count", count)
                    gate_input_id.get(map_id.get(output_arr[i])).append(map_id.get( gate_input_num.get(output_arr[i])[j] ) + count)
                    used.append(map_id.get( gate_input_num.get(output_arr[i])[j] ) + count)
                    
                elif gate_freq.get( gate_input_num.get(output_arr[i])[j] ) == 1:
                    gate_input_id.get(map_id.get(output_arr[i])).append(map_id.get( gate_input_num.get(output_arr[i])[j] ))
            count = 1

    # print('used', used)
    print('gate_input_id',gate_input_id)

    ######################
    ## print out result ##
    ######################
    # print(gate_input_id.get(16)[0])
    f_result = open('result.txt', 'w')
    for i in range(len(column1)):
        f_result.writelines([str(column1[i]), ' ', str(column2[i]), ' ', str(column3[i]), ' ', str(column4[i]), ' ', str(column5[i]),' '])
        if i+1 in gate_input_id:
            for j in range(len(gate_input_id.get(i+1))):
                f_result.writelines([str(gate_input_id.get(i+1)[j]), ' '])
        f_result.writelines(['\n'])

    f_result.close()