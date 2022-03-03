#!/usr/bin/env python
# coding: utf-8

# In[2]:


LEN = int(input("enter the size of NxN matrix:"))
matrix = []

def show():
    #to create a matrix containg "W"
    for i in range(LEN):
        empt_mat =[]
        for j in range(LEN):
            k = str("W")
            empt_mat.append(k)
        matrix.append(empt_mat)
    
    #to make the inside matrix empty    
    for i in range(1,LEN-1):
        for j in range(1,LEN-1):
            matrix[int(i)][int(j)]=str(" ")
            
    #to make ground and a ball        
    for i in range(LEN-1,LEN):
        for j in range(1,LEN-1):
            matrix[int(i)][int(j)]=str("G")
    matrix[int(LEN-1)][int((LEN-1)/2)]=str("o")
    
    #to input brick values and number of balls
    ans = "Y"
    while(ans!="N"):
        i,j,new_val = input("Enter the brick's position and the brick type :").split()
        if ((new_val)=="1" or (new_val)=="2" or (new_val)=="3"):
            matrix[int(i)][int(j)]=int(new_val)
        else:
            matrix[int(i)][int(j)]=new_val

        ans = input("Do you want to continue(Y or N)?")
    balls = int(input("enter ball count: "))
   
    #to print the final matrix        
    for i in range(LEN):
        for j in range(LEN):
             print(matrix[i][j], end=" ")
        print()
    print("Ball count is ",balls)
    
    def traverse_show():
        rep=1
        while(rep!=0):
            #traversing the ball
            trav = input("Enter the direction in which the ball need to traverse :")
            nonlocal balls
            if(trav=="ST"):
                balls =balls-1
                for i in range(LEN-1,0,-1):
                    j=(LEN-1)/2
                    if matrix[int(i)][int(j)]==str(" "):
                        pass
                    if matrix[int(i)][int(j)]==1 or matrix[int(i)][int(j)]==2 or matrix[int(i)][int(j)]==3:
                        matrix[int(i)][int(j)]=int(matrix[int(i)][int(j)]-1)
                        if matrix[int(i)][int(j)]==0:
                            matrix[int(i)][int(j)]=str(" ")
                            break
                    elif matrix[int(i)][int(j)]==("DE"):
                        for j in range(1,LEN-1):
                            matrix[i][j]=str(" ")
                        break
                    elif matrix[int(i)][int(j)]=="B":
                        matrix[int(i)][int(j)]=str(" ")
                        balls=balls+1
                        break
                 
            elif(trav=="LD"):
                balls =balls-1
                matrix[int(LEN-1)][int((((LEN-1)/2)-1))]=str("o")
                matrix[int(LEN-1)][int((LEN-1)/2)]=str("W")
                for i in range(LEN-1,0,-1):
                    j=((LEN-1)/2)-1
                    if matrix[int(i)][int(j)]==str(" "):
                        pass
                    elif matrix[int(i)][int(j)]==1 or matrix[int(i)][int(j)]==2 or matrix[int(i)][int(j)]==3:
                        matrix[int(i)][int(j)]=matrix[int(i)][int(j)]-1
                        if matrix[int(i)][int(j)]==0:
                            matrix[int(i)][int(j)]=str(" ")
                        break
                    elif matrix[int(i)][int(j)]=="DE":
                        for j in range(1,LEN-1):
                            matrix[i][j]=str(" ")
                        break
                    elif matrix[int(i)][int(j)]=="B":
                        matrix[int(i)][int(j)]=str(" ")
                        balls=balls+1
                        break
                                        
            elif(trav=="RD"):
                balls =balls-1
                matrix[int(LEN-1)][int((((LEN-1)/2)+1))]=str("o")
                matrix[int(LEN-1)][int((LEN-1)/2)]=str("W")
                for i in range(LEN-1,0,-1):
                    j=((LEN-1)/2)+1
                    if matrix[int(i)][int(j)]==str(" "):
                        pass
                    elif matrix[int(i)][int(j)]==1 or matrix[int(i)][int(j)]==2 or matrix[int(i)][int(j)]==3:
                        matrix[int(i)][int(j)]=matrix[int(i)][int(j)]-1
                        if matrix[int(i)][int(j)]==0:
                            matrix[int(i)][int(j)]=str(" ")
                        break
                    elif matrix[int(i)][int(j)]=="DE":
                        for j in range(1,LEN-1):
                            matrix[i][j]=str(" ")
                        break
                    elif matrix[int(i)][int(j)]=="B":
                        matrix[int(i)][int(j)]=str(" ")
                        balls=balls+1
                        break
             #to print the final matrix        
            for i in range(LEN):
                for j in range(LEN):
                    print(matrix[i][j], end=" ")
                print()
            print("Ball count is ",balls)
            if balls==0:
                print("your game is over")
                rep =0
        
    traverse_show()
show()


# In[ ]:




