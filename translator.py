import re
# def translator(src,dst):
if __name__ == "__main__":
    fin = open('C432A.txt', 'r')
    f = open('f_input.txt', 'w')
    f_output = open('f_output.txt', 'w')
    f_wire = open('f_wire.txt', 'w')
    f_gate = open('gate_.txt', 'w')
    # read all verilog file in list
    f_content = fin.readlines()
    print("title", (f_content[0].split())[1])
    ckt_title = (f_content[0].split())[1]

    # seperate the file #
    # read content line by line
    for i in range(len(f_content)):
        # create a file only contain input output and wire information
        if f_content[i].find("input") == 0:
            f.write(f_content[i])
        elif f_content[i].find("output") == 0:
            f_output.write(f_content[i])
            # print(f_content[i])
        elif f_content[i].find("wire") == 0:
            f_wire.write(f_content[i])
        # create a file only contain gate information
        elif f_content[i].find("module") == -1 and f_content[i].find("endmodule") == -1 and f_content[i] not in ['\n','\r\n']: 
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
    record_index1 = 0
    record_index2 = 0

    # print line by line
    for i in range(len(flist_in)):
        sepe_arr = flist_in[i].split()
        if sepe_arr[0].find('input[') == 0:
            # print("here?")
            # print word by word
            count = 0
            for j in sepe_arr:
                # eliminate the the first one input[0:8] and extract its number
                if count == 0:
                    for k in range(len(j)):
                        if j[k] == ':':
                            record_index1 = k+1
                        if j[k] == ']':
                            record_index2 = k
                    inarr_num = int(j[record_index1:record_index2])
                    # print('inarr_num: ',inarr_num)
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
    print('input_arr\n',input_arr)
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
    record_index1 = 0
    record_index2 = 0
    # print line by line
    for i in range(len(flist_out)):
        sepe_arr = flist_out[i].split()
        if sepe_arr[0].find('output[') == 0:
            # print word by word
            count = 0
            for j in sepe_arr:
                # eliminate the the first one output[0:8] and extract its number
                if count == 0:
                    for k in range(len(j)):
                        if j[k] == ':':
                            record_index1 = k+1
                        if j[k] == ']':
                            record_index2 = k     
                    outarr_num = int(j[record_index1:record_index2])
                    # outarr_num = int(j[9])
                    # print(outarr_num)
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
    print('output_arr\n',output_arr)
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
    record_index1 = 0
    record_index2 = 0
    # print line by line
    for i in range(len(flist_wire)):
        sepe_arr = flist_wire[i].split()
        if sepe_arr[0].find('wire[') == 0:
            # print("here?")
            # print word by word
            count = 0
            for j in sepe_arr:
                # eliminate the the first one wire[0:8] and extract its number
                if count == 0:
                    for k in range(len(j)):
                        if j[k] == ':':
                            record_index1 = k+1
                            print(record_index1)
                        if j[k] == ']':
                            record_index2 = k
                    # record_index1 = record_index1 + record_index2 
                    # print(record_index1)     
                    wirearr_num = int(j[record_index1:record_index2])
                    # print(wirearr_num)
                    # wirearr_num = int(j[7])
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
    print('wire_arr\n',wire_arr)
    f_r_wire.close()

    ##################
    #gate information#
    ##################

    f_r_gate = open("gate_.txt", "r", encoding='UTF-8')
    # print("a",f_r_in_out_wire)
    flist_gate= list(f_r_gate)

    # print("qq",len(flist_gate))
    
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
    print("gate_input_num\n", gate_input_num)
    # print("gate_input_num.get(N10): ", len(gate_input_num.get("N10")))
    # print("gate_input_num.get(N10)[0]: ", gate_input_num.get("N10")[0])
    print('gate_freq: \n',gate_freq)
    print("wire_gate_relation: \n",wire_gate_relation)
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
        
        column1.append( input_arr[i]+ "_" + str(1)) # char format
        # column1.append(1) # number format
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            for j in range(int(gate_freq.get(input_arr[i]))):
                column1.append(input_arr[i]+ "_"  + str(2))
                # column1.append(2) # number format
    ## deal with wire(inner gate output)(0) and its branch(2)
    for i in range(len(wire_arr)):
        column1.append(wire_arr[i]+ "_" + str(0))
        # column1.append(0) # number format
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column1.append(wire_arr[i]+ "_" + str(2))
                # column1.append(2) # number format
    ## deal with output gate(3)
    for i in range(len(output_arr)):
        column1.append(output_arr[i]+ "_" + str(3))
        # column1.append(3) # number format

    print("column1: \n", column1)

    ## column 2 ##
    count = 1
    # put input_arr wire_arr and output_arr
    map_id = {} 
    ## deal with input and its branch
    for i in range(len(input_arr)):
        # print(i)
        column2.append(ckt_title + "_" + str(count))
        # column2.append(count)
        # map_id[input_arr[i]] = ckt_title + "_" + str(count) # character format
        map_id[input_arr[i]] = count # number format
        count += 1
        if gate_freq.get(input_arr[i]) != None and gate_freq.get(input_arr[i]) >= 2:
            for j in range(int(gate_freq.get(input_arr[i]))):
                column2.append(ckt_title + "_" + str(count))
                # column2.append(count)
                count += 1
    ##deal with inner gate output and its branch
    for i in range(len(wire_arr)):
        column2.append(ckt_title + "_" + str(count))
        # column2.append(count)
        # map_id[wire_arr[i]] = ckt_title + "_" + str(count) # character format
        map_id[wire_arr[i]] = count # number format
        count += 1
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column2.append(ckt_title + "_" + str(count))
                # column2.append(count)
                count += 1
    ## deal with output gate 
    for i in range(len(output_arr)):
        column2.append(ckt_title + "_" + str(count))
        # column2.append(count)
        # map_id[output_arr[i]] = ckt_title + "_" + str(count) # character format
        map_id[output_arr[i]] = count # number format
        count += 1

    print("column2: \n",column2)

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
        elif wire_gate_relation.get(wire_arr[i]) == 'nand':
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
        elif wire_gate_relation.get(output_arr[i]) == 'nand':
            column3.append(6)
        elif wire_gate_relation.get(output_arr[i]) == 'and':
            column3.append(7)
        elif wire_gate_relation.get(output_arr[i]) == 'xnor':
            column3.append(8)
    print("column3: \n", column3)

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
    print("column4: \n", column4)

    ##############
    ## column 5 ##
    ##############

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
        column5.append(len(gate_input_num.get(wire_arr[i])) )
        if gate_freq.get(wire_arr[i]) != None and gate_freq.get(wire_arr[i]) >= 2:
            for j in range(int(gate_freq.get(wire_arr[i]))):
                column5.append(' ')
    ## deal with output gate 
    for i in range(len(output_arr)):
        column5.append(len(gate_input_num.get(output_arr[i])))
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
                    gate_input_id.get(map_id.get(wire_arr[i])).append( ckt_title + "_" + str(map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count)) # char format
                    # gate_input_id.get(map_id.get(wire_arr[i])).append( map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count ) # number format
                    used.append(map_id.get( gate_input_num.get(wire_arr[i])[j] ) + count)
                    
                elif gate_freq.get( gate_input_num.get(wire_arr[i])[j] ) == 1:
                    gate_input_id.get(map_id.get(wire_arr[i])).append( ckt_title + "_"  + str(map_id.get( gate_input_num.get(wire_arr[i])[j] ))  ) # char format
                    # gate_input_id.get(map_id.get(wire_arr[i])).append( map_id.get( gate_input_num.get(wire_arr[i])[j] ))   # number format 
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
                    gate_input_id.get(map_id.get(output_arr[i])).append(  ckt_title + "_" + str(map_id.get( gate_input_num.get(output_arr[i])[j] ) + count) ) # char format
                    # gate_input_id.get(map_id.get(output_arr[i])).append( map_id.get( gate_input_num.get(output_arr[i])[j] ) + count  ) # number format
                    used.append(map_id.get( gate_input_num.get(output_arr[i])[j] ) + count)
                    
                elif gate_freq.get( gate_input_num.get(output_arr[i])[j] ) == 1:
                    gate_input_id.get(map_id.get(output_arr[i])).append(  ckt_title + "_"  + str(map_id.get( gate_input_num.get(output_arr[i])[j] )) ) # char format
                    # gate_input_id.get(map_id.get(output_arr[i])).append(  map_id.get( gate_input_num.get(output_arr[i])[j] )) # number format
            count = 1

    # print('used', used)
    print('gate_input_id: \n',gate_input_id)


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

    # class Node():
    #     def __init__(self, name, type1, id1, gtype, outline, inline, inputid):
    #         self.name = name
    #         self.type = type1
    #         self.id = id1
    #         self.gtype = gtype
    #         self.outline = outline
    #         self.inline = inline
    #         self.inputid = inputid

    # nodes.append(Node(column1, ..)) 

    
    # for i in range(len(column1)):
    #     f_result.writelines([str(column1[i]), ' ', str(column2[i]), ' ', str(column3[i]), ' ', str(column4[i]), ' ', str(column5[i]),' '])
    #     if i+1 in gate_input_id:
    #         for j in range(len(gate_input_id.get(i+1))):
    #             f_result.writelines([str(gate_input_id.get(i+1)[j]), ' '])
    #     f_result.writelines(['\n'])

    # def __str__(self):
	# 	return str(self.name)+'\t'+str(self.type)+'\t'+str(self.id)+'\t'+str(self.gtype)+'\t'+str(self.outline)+'\t'+str(self.inline)+'\t'+str(self.inputid)
	# def __repr__(self):
	# 	return str(self.name)+'\t'+str(self.type)+'\t'+str(self.id)+'\t'+str(self.gtype)+'\t'+str(self.outline)+'\t'+str(self.inline)+'\t'+str(self.inputid)
