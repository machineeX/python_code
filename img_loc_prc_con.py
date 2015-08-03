from PIL import Image


def main():
#{

        #img= Image.open("img1.png")            # creating a cropped immage
        #box = 100,100,1200,600                 # range : 0,0  to  1232,674
        #img.crop(box).save("img2.png","PNG")   # cropped image is img7

        f1 = raw_input("enter main file name :")
        f2 = raw_input("enter croped file name :")
        img_o = Image.open(f1)             #original file
        img_c = Image.open(f2)             #cropped file
        img_o=img_o.convert("RGB")
        img_c=img_c.convert("RGB")
        size_o= ox,oy=img_o.size
        size_c= cx,cy=img_c.size
        o_x=-1   #initialize
        o_y=0    #initialize
        zer=0,0  #initialize
        

        
        dr=cx*cy
        nr=dr
        bx=0
        by=0
        val=0.0

        for x in list(img_o.getdata()):                        # wandering in main image
            o_x += 1                        #increment
            if(o_x>=ox):                    #increment
                o_x=o_x-ox                  #increment
                o_y += 1                    #increment
            o_cor=o_x,o_y                   #initialize
            if (img_o.getpixel(o_cor) == img_c.getpixel(zer)):  # match 1st pts
                c_x=-1                      #initialize
                c_y=0                       #initialize
                nr=0.0                        #initialize
                for y in list(img_c.getdata()):                  # wandering in suspected part of main image
                    
                    c_x += 1                #increment
                    if(c_x>=cx):            #increment
                        c_x=c_x-cx          #increment
                        c_y += 1            #increment
                    o_cor=(o_x+c_x),(o_y+c_y)#initialize
                    c_cor=c_x,c_y           #initialize
                    
                    try:                                          # if right bounds are reached
                        if(img_o.getpixel(o_cor) != img_c.getpixel(c_cor)):   # checking wrong suspition
                            nr += 1
                            #break
                    except:
                         nr += 1
                         #break

            if (nr==0):
                print "yup 2nd img is totally present in 1st"
                for a in range(o_x,o_x+cx,1):
                        img_o.putpixel((a,o_y),(0,0,0,0))
                        img_o.putpixel((a,o_y+cy),(0,0,0,0))
                for b in range(o_y,o_y+cy,1):
                        img_o.putpixel((o_x,b),(0,0,0,0))
                        img_o.putpixel((o_x+cx,b),(0,0,0,0))
                img_o.show()
                break
            elif(val<(1.0-(nr/dr)) and (1.0-(nr/dr))>0.8):
                val=(1.0-(nr/dr))
                bx=o_x
                by=o_y
                    
            

        if(nr!=0 and val<0.8):
            print "2nd img not found in first"
            print "\n % match is:"+str(val*100)
        elif(nr!=0 and val>=0.8):
                print "yup 2nd img is present in 1st"
                for a in range(bx,bx+cx,1):
                        img_o.putpixel((a,by),(0,0,0,0))
                        img_o.putpixel((a,by+cy),(0,0,0,0))
                for b in range(by,by+cy,1):
                        img_o.putpixel((bx,b),(0,0,0,0))
                        img_o.putpixel((bx+cx,b),(0,0,0,0))
                img_o.show()
                print "\n % match is:"+str(val*100)
                

        raw_input(" ")
        print "\a"
#}

    
if (__name__=="__main__"):       #python interpreter is running this module as the main program so it sets the special __name__ variable to have a value "__main__"
#{                                thus no one can import this
        main()

#}
