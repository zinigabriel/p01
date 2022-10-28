def contorno( t, matric ):
    t.penup()
    ss = t.screensize()
    t.sety( -(ss[1] // 2) )
    t.pendown()
    pensz = t.pensize()
    spd = t.speed()
    t.speed( 0 )
    t.pencolor('red')
    t.pensize( 2 )
    t.left( 90 )
    t.forward( 12 )
    
    while matric > 0:
        d = matric % 10
        matric = matric // 10
        t.forward( 16 )
        if d % 2 == 0:
            t.right( 90 )
            if d > 0:
                t.forward( d*10+12 )
            t.left( 90 )
            t.forward( 20+4 )
            t.left( 90 )
            if d > 0:
                t.forward( d*10+12 )
            t.right( 90 )
        else:
            t.left( 90 )
            if d > 0:
                t.forward( d*10+12 )
            t.right( 90 )
            t.forward( 20+4 )
            t.right( 90 )
            if d > 0:
                t.forward( d*10+12 )
            t.left( 90 )

    t.pencolor('blue')
    t.pensize( 20 )
    t.penup()
    t.home()
    t.sety( -(ss[1] // 2) )
    t.pendown()
    t.left( 90 )
    t.speed( spd )
