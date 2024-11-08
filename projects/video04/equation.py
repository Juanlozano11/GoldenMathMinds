## path : cd Desktop/Math/GoldenMathMinds/projects/video04
## run :  manim -pql equation.py SimpleMathProblem


from manim import *

class SimpleMathProblem(Scene):
    def construct(self):
        # Title text: "Can you solve this?"
        title = Text("Can you solve this?", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Display a simple equation: (2^3) + 3! - Σ (1+2)
        problem = MathTex(r"2^3 + 3! + \sum_{n=1}^{6} (0!)  - \sum_{n=1}^{2} (1 + n)", font_size=48)
        self.play(Write(problem))
        self.wait(2)

        # Display the answer after a pause
        #answer = MathTex(r"= 8 + 6 - (1 + 2 + 2 + 3) = 7", font_size=48, color=GREEN)
        #self.play(Transform(problem, answer))
        #self.wait(2)

# The equation is designed to be simple:
# 2^3 = 8
# 3! = 6
# Σ(1 + n) for n=1 to 2 -> (1+1) + (1+2) = 2 + 3 = 5
# So, 8 + 6 - 5 = 7
