def arithmetic_arranger(problems, answers=False):

    if len(problems) > 5:
        
        return "Error: Too many problems."

    else:

        import re
        solutions = [[]] * len(problems)
        answer = [0, 0, 0, 0, 0]

        # break input down into smaller pieces
        for x in range(len(problems)):
            solutions[x] = [[]] * 3
            if answers == True:
                
                # remove all white space and split into numbers and sign
                problems[x].strip()

                #Error check for non-digit characters
                letters = ["", "", "", "", "", ""]
                letters[x] = re.findall("[a-zA-Z]", problems[x]) or "Clean"
               
                if letters[x] != "Clean":
                  return "Error: Numbers must only contain digits."

                solutions[x][0] = re.findall("\d+", problems[x])

                #error check for numbers > than 4
                if len(solutions[x][0][0]) > 4:
                    
                    return "Error: Numbers cannot be more than four digits."
                if len(solutions[x][0][1]) > 4:
          
                    return "Error: Numbers cannot be more than four digits."

                solutions[x][1] = str(re.findall("[+-]", problems[x]) or "Error")
                solutions[x][1] = solutions[x][1][2]

                #error check for non + or - operators
                if str(solutions[x][1]) == "r":
                    
                    return "Error: Operator must be '+' or '-'."

                #do math on the two values
                #if add
                
                if str(solutions[x][1]) == "+":
                  answer[x] = int(solutions[x][0][0]) + int(solutions[x][0][1])
              
                else:
                  answer[x] = int(solutions[x][0][0]) - int(solutions[x][0][1])
                  
              
                # find out larger of three numbers and create dashes
                # find out larger of two numbers and create dashes
                if int(solutions[x][0][0]) > int(solutions[x][0][1]):
                    solutions[x][2] = "-" * len(str(solutions[x][0][0]))
                    solutions[x][2] = solutions[x][2] + "--"
                else:
                    solutions[x][2] = "-" * len(str(solutions[x][0][1]))
                    solutions[x][2] = solutions[x][2] + "--"
            else:
                # remove all white space and split into numbers and sign
                problems[x].strip()


                #Error check for non-digit characters
                letters = ["", "", "", "", "", ""]
                letters[x] = re.findall("[a-zA-Z]", problems[x]) or "Clean"
               
                if letters[x] != "Clean":
                  
                  return "Error: Numbers must only contain digits."

                solutions[x][0] = re.findall("\d+", problems[x])

                #error check for numbers > than 4
                if len(solutions[x][0][0]) > 4:
                    
                    return "Error: Numbers cannot be more than four digits."
                if len(solutions[x][0][1]) > 4:
                    
                    return "Error: Numbers cannot be more than four digits."

                solutions[x][1] = str(re.findall("[+-]", problems[x]) or "Error")
                solutions[x][1] = solutions[x][1][2]

                
                if str(solutions[x][1]) == "r":
                    
                    return "Error: Operator must be '+' or '-'."
                
                # find out larger of two numbers and create dashes
                if int(solutions[x][0][0]) > int(solutions[x][0][1]):
                    solutions[x][2] = "-" * len(str(solutions[x][0][0]))
                    solutions[x][2] = solutions[x][2] + "--"
                else:
                    solutions[x][2] = "-" * len(str(solutions[x][0][1]))
                    solutions[x][2] = solutions[x][2] + "--"
                

        # print out the answer line by line
        if answers == True:
            line0 = ""
            line1 = ""
            line2 = ""
            line3 = ""

            for x in range(len(problems)):
                #go line by line and add numbers in from each problem

                #adding line0
                space0 = int(len(solutions[x][2])) - int(len(str(solutions[x][0][0])))
                line0 = line0 + (" " * int(space0))
                line0 = line0 + solutions[x][0][0]
                line0 = line0 + "    "

                #adding line1
                space1 = (int(len(solutions[x][2])) - int(len(solutions[x][0][1]))) - 1
                line1 = line1 + str(solutions[x][1])
                line1 = line1 + (" " * int(space1))
                line1 = line1 + solutions[x][0][1]
                line1 = line1 + "    "

                #adding line2
                line2 = line2 + str(solutions[x][2])
                line2 = line2 + "    "

                #adding line3
                space3 = int(len(solutions[x][2])) - int(len(str(answer[x])))
                line3 = line3 + (" " * int(space3))
                line3 = line3 + str(answer[x])
                line3 = line3 + "    "

            line0 = line0[:-4]
            line1 = line1[:-4]
            line2 = line2[:-4]
            line3 = line3[:-4]
            
            finishedProduct = F"{line0}\n{line1}\n{line2}\n{line3}"
            return finishedProduct

        else:
            line0 = ""
            line1 = ""
            line2 = ""

            for x in range(len(problems)):
                #go line by line and add numbers in from each problem

                #adding line0
                space0 = int(len(solutions[x][2])) - int(
                    len(str(solutions[x][0][0])))
                line0 = line0 + (" " * int(space0))
                line0 = line0 + solutions[x][0][0]
                line0 = line0 + "    "

                #adding line1
                space1 = (int(len(solutions[x][2])) -
                          int(len(solutions[x][0][1]))) - 1
                line1 = line1 + str(solutions[x][1])
                line1 = line1 + (" " * int(space1))
                line1 = line1 + solutions[x][0][1]
                line1 = line1 + "    "

                #adding line2
                line2 = line2 + str(solutions[x][2])
                line2 = line2 + "    "
            
            
            line0 = line0[:-4]
            line1 = line1[:-4]
            line2 = line2[:-4]
            finishedProduct = F"{line0}\n{line1}\n{line2}"
            return finishedProduct



