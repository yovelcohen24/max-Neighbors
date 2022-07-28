def check_mat(matr):#The function checks for each organ if it is really large from all its neighbors . the function prints the organs in a matrix that is really larger than its neighbors and returns their number.
   neighbor_lst=[]#A list containing the neighboring numbers of each of the matrix organ.
   count=0#A variable accumulates how many organs are larger than their neighbors in the matrix.
   flag=0#A flag varaible that says if there is a neighboring organ that larger than the one we are checking the flag is 1 else the flag is 0 .
   if len(matr[0])==1:#If the matrix is a single column matrix.
       for k in range(len(matr)):  
           if k==0:#If this is the first organ in the column.
               neighbor_lst.append(matr[k+1][0])#Adding a neighbor organ to the list of neighbors.
               if matr[k+1][0]>=matr[k][0]:#Checks if the neighboring organ is larger than the organ we are check.
                      flag=1 
           if k==len(matr)-1:#The last organ in the column.
               neighbor_lst.append(matr[len(matr)-2][0])#Adding a neighbor organ to the list of neighbors.
               if matr[len(matr)-2][0]>=matr[k][0]:#Checks if the neighboring organ is larger than the organ we are check.
                      flag=1 
           if k!=0 and k<len(matr)-1:#The organ located between the first and last organ in the column.
                neighbor_lst.append(matr[k+1][0])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[k-1][0])
                for i in range(len(neighbor_lst)):
                  if neighbor_lst[i]>=matr[k][0]:#Checks if the neighboring organ is larger than the organ we are check.
                          flag=1 
           if flag==0:#If the flag is 0 it means that the organ is larger than all its neighboring organs and we need to print and add to the counter +1.
               count+=1
               print(count,".","matr[",k,"][ 0 ]=",matr[k][0],"> (",end="")#Prints the organ that is larger than its neighbors and the organs themselves
               for k in range(len(neighbor_lst)):
                    print(neighbor_lst[k],end="")
                    if k!=len(neighbor_lst)-1:
                        print(",",end="")
               print(")")               
           neighbor_lst=[]
           flag=0
   else:               
    for i in range(len(matr)):
       if len(matr)==1:#If the matrix is a single row matrix.
            for k in range(len(matr[0])):
                if k==0:#The first organ in a the row.
                    neighbor_lst.append(matr[0][1])#Adding a neighbor organ to the list of neighbors.
                    if matr[0][1]>=matr[0][0]:#Checks if the neighboring organ is larger than the organ we are check.
                      flag=1 
                if k==len(matr[0])-1:#The last organ on the list.
                    neighbor_lst.append(matr[0][len(matr[0])-2])#Adding a neighbor organ to the list of neighbors.
                    if matr[0][len(matr[0])-2]>=matr[0][len(matr[0])-1]:#Checks if the neighboring organ is larger than the organ we are check.
                      flag=1 
                if k>0 and k<len(matr[0])-1:#The organ located between the first and last organ in the row.
                    neighbor_lst.append(matr[0][k-1])#Adding a neighbor organ to the list of neighbors.
                    neighbor_lst.append(matr[0][k+1])
                    for j in range(len(neighbor_lst)):
                      if neighbor_lst[j]>=matr[0][k]:#Checks if the neighboring organ is larger than the organ we are check.
                          flag=1 
                if flag==0:#If the flag is 0 it means that the organ is larger than all its neighboring organs and we need to print and add to the counter +1.
                  count+=1
                  print(count,".","matr[",i,"][",k,"]=",matr[0][k],"> (",end="")#Prints the organ that is larger than its neighbors and the organs themselves
                  for x in range(len(neighbor_lst)):
                    print(neighbor_lst[x],end="")
                    if x!=len(neighbor_lst)-1:
                      print(",",end="")
                  print(")") 
                flag=0
                neighbor_lst=[]
       else:#If the matrix is not a single row matrix or a single column matrix.
        for j in range(len(matr[0])):
            flag=0
            neighbor_lst=[]
            if i==0 and j==0:#The organ in the up left corner.
                neighbor_lst.append(matr[1][1])
                neighbor_lst.append(matr[1][0])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[0][1])
                for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1 
            if i==0 and j==len(matr[i])-1:#The organ in the up right corner.
                neighbor_lst.append(matr[0][len(matr[i])-2])
                neighbor_lst.append(matr[1][len(matr[i])-2])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[1][len(matr[i])-1])
                for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
            if i==len(matr)-1 and j==0:#The organ in the down left corner.
                neighbor_lst.append(matr[len(matr)-2][1])
                neighbor_lst.append(matr[len(matr)-2][0])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[len(matr)-1][1])
                for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
            if i==len(matr)-1 and j==len(matr[i])-1:#The organ in the down right corner.
                neighbor_lst.append(matr[len(matr)-2][len(matr[i])-2])
                neighbor_lst.append(matr[len(matr)-2][len(matr[i])-1])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[len(matr)-1][len(matr[i])-2])
                for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
            if  i==0  and j>0 and j<len(matr[i])-1:#The organ in the first row between the organ in the up left corner and the oregan in the up right corner.
                 neighbor_lst.append(matr[1][j-1])
                 neighbor_lst.append(matr[1][j])
                 neighbor_lst.append(matr[1][j+1])#Adding a neighbor organ to the list of neighbors.
                 neighbor_lst.append(matr[0][j-1])
                 neighbor_lst.append(matr[0][j+1])
                 for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
                 
            if  i==len(matr)-1  and j>0 and j<len(matr[i])-1:#The organ in the last row between the organ in the down left corner and the oregan in the down right corner.
                 neighbor_lst.append(matr[len(matr)-2][j-1])
                 neighbor_lst.append(matr[len(matr)-2][j])
                 neighbor_lst.append(matr[len(matr)-2][j+1])#Adding a neighbor organ to the list of neighbors.
                 neighbor_lst.append(matr[len(matr)-1][j-1])
                 neighbor_lst.append(matr[len(matr)-1][j+1]) 
                 for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
                 
            if  i>0 and i<len(matr)-1 and j==0:#The organ between the top first and the last row in the most left column.
                neighbor_lst.append(matr[i-1][0])
                neighbor_lst.append(matr[i-1][1])
                neighbor_lst.append(matr[i][1])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[i+1][0])
                neighbor_lst.append(matr[i+1][1])
                for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
                
            if i>0 and i<len(matr)-1 and j==len(matr[i])-1:#The organ between the top first and the last row in the most right  column.
                neighbor_lst.append(matr[i-1][len(matr[i])-1])
                neighbor_lst.append(matr[i-1][len(matr[i])-2])
                neighbor_lst.append(matr[i][len(matr[i])-2])#Adding a neighbor organ to the list of neighbors.
                neighbor_lst.append(matr[i+1][len(matr[i])-1])
                neighbor_lst.append(matr[i+1][len(matr[i])-2])
                for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
                                    
            if i!=0  and j!=0 and i!=len(matr)-1 and j!=len(matr[i])-1:#All the organs within the frame organs of the matrix.
               neighbor_lst.append(matr[i-1][j-1])
               neighbor_lst.append(matr[i-1][j])
               neighbor_lst.append(matr[i-1][j+1])
               neighbor_lst.append(matr[i][j-1])
               neighbor_lst.append(matr[i][j+1])#Adding a neighbor organ to the list of neighbors.
               neighbor_lst.append(matr[i+1][j-1])
               neighbor_lst.append(matr[i+1][j])
               neighbor_lst.append(matr[i+1][j+1])
               for k in range(len(neighbor_lst)):
                   if neighbor_lst[k]>=matr[i][j]:#Checks if the neighboring organ is larger than the organ we are check.
                     flag=1  
          
            if flag==0:#If the flag is 0 it means that the organ is larger than all its neighboring organs and we need to print and add to the counter +1.
                count+=1
                print(count,".","matr[",i,"][",j,"]=",matr[i][j],"> (",end="")#Prints the organ that is larger than its neighbors and the organs themselves
                for k in range(len(neighbor_lst)):
                    print(neighbor_lst[k],end="")
                    if k!=len(neighbor_lst)-1:
                      print(",",end="")
                print(")")       
  
   return count

def main():#The main function summons the check_mat function and prints how many organs are larger than their neighbors in the matrix
    matr=[[2,3,4,5,6],[6,5,7,4,3],[3,4,9,8,2],[5,4,8,7,6],[1,2,9,5,9]]#The matrix that we check.
    count=check_mat(matr)#gets from the check_mat function how many organs are larger than their neighbors in the matrix
    print()
    print("count=",count)
        
main()   
