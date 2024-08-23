# WAP TO SHOW THE FINE STATUS OF THE STUDENT ACCORDING TO ATTENDENCE
#CONDITIONS ATTENDENCE IN % --->
# if attendenc > 90 (NO FINE)
# if attendenc (85 > 90 (500rs /-)
# if attendenc (80 > 85 )(1000rs /-)

attendec = int(input("ENTER STUDENT ATTENDENCE IN '%' "))
if(attendec < 0 or attendec > 100):
    print("INVALID INPUT! attendence must be between '0' and '100' !")
elif(attendec >= 90):
    print("NO FINE ! ")
elif( 85 <= attendec  < 90):
    print("500rs/- fine will be awarded ! ")
elif(  80 <= attendec < 85):
    print("1000rs/- fine will be awarded ! ")
else:
    print("NOT DECIDED YET! PLEASE CONTACT TO YOUR CO-ORDINATIOR ! ")