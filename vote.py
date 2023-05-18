import datetime



def vote(usrcheck, topcheck,poscheck, form, usrSesport):   
    postID = form.submit
    if form.check == True:
        poscheck = poscheck +1;
        usrSesport = usrSesport + "</vote" + postID + "check" + " " + datetime.date() + "  />" 

    if form.bait == True:
        check = check + 1;
        usrcheck = usrcheck + 1;
        usrSesport = usrSesport + "</vote" + postID + "bait" + " " + datetime.date() + "  />" 

    if form.hype == True:
        check = check + 1;
        topcheck = topcheck + 1;
        usrSesport = usrSesport + "</vote" + postID + "hype" + " " + datetime.date() + "  />" 

    # insert SQL Eventflag Timestamp
    return file2Str("voteclosing.html").format(**locals()), usrSesport