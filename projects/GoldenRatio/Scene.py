from manim import * 

class S1(Scene):
       
       def construct(self):
        for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=BLACK))

        l1 = Line(start=[(2/(1 + np.sqrt(5) )+ 1) / 2, -0.5, 0], end=[(2/(1 + np.sqrt(5) )+ 1) / 2, 0.5, 0])

        t_a  = Text("a").shift(LEFT * 2.70) 
        t_a2 = Text("a").shift(LEFT * 0.85 , DOWN * 1.85 ) 
        t_b  = Text("b").shift(RIGHT * 1.75 , DOWN * 1.85 )  
        t1   = Text("This is a Golden Ratio Rectangle").shift(DOWN * 3)
        t2   = Text("And this is a golden ratio line").shift(DOWN * 3)
        t3   = Text("But, what does this really mean? ")

        r1 = Polygon(
            np.array([ ((2 / (1 + np.sqrt (5))) + 1 )/ 2  ,  0.5, 0]),
            np.array([ ((2 / (1 + np.sqrt (5))) + 1 )/ 2  , -0.5, 0]),
            np.array([-((2 / (1 + np.sqrt (5))) + 1 )/ 2  , -0.5, 0]), 
            np.array([-((2 / (1 + np.sqrt (5))) + 1 )/ 2  ,  0.5, 0])
            )
        
        r2 = Polygon(
           np.array([ ((2 / (1 + np.sqrt (5))) + 1 )/ 2  , -0.5, 0]),
            np.array([-((2 / (1 + np.sqrt (5))) + 1 )/ 2  , -0.5, 0]))
        
        
        self.play (Create(r1))
    
       
        self.play(Transform( r1, r1.copy().scale(3) ))
        self.play(Transform( l1, l1.copy().scale(3) ))

        self.play (Create(t_a))
        self.play (Create(t_a2))
        self.play (Create(t_b))
        self.play (Create(t1))



        self.play(Transform( r1, r2.shift(DOWN).scale(3)) )
        self.play(Transform( t_a, t_a.copy().scale(0) ))
        self.play(Transform( l1, l1.copy().shift(DOWN * 1.5).scale(0.4) ))
        self.play (Transform(t1, t2))
        self.wait(3)
        self.play (Create(t3))


        
        self.wait(1)
