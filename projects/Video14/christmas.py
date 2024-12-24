## Path: cd Desktop/Math/GoldenMathMinds/projects/video14
## run: manim -pql christmas.py MerryChristmas


from manim import *

class MerryChristmas(Scene):
    def construct(self):
        # Initial equation
        equation = MathTex(r"y =", r"\frac{\log_e\left(\frac{x}{m} - sa\right)}{r^2}")
        self.play(Write(equation))
        self.wait(2)

        # Step 1: Multiply by r^2 (move r^2 to the left-hand side)
        updated_eq1 = MathTex(r"yr^2 =", r"\log_e\left(\frac{x}{m} - sa\right)").move_to(equation)
        self.play(TransformMatchingTex(equation, updated_eq1))
        self.wait(2)

        # Step 2: Exponentiation (apply e^ to both sides)
        updated_eq2 = MathTex(r"e^{yr^2} =", r"\frac{x}{m} - sa").move_to(updated_eq1)
        self.play(TransformMatchingTex(updated_eq1, updated_eq2))
        self.wait(2)

        # Step 3: Multiply by m (simplify the fraction)
        updated_eq3 = MathTex(r"me^{yr^2} =", r"x - msa").move_to(updated_eq2)
        self.play(TransformMatchingTex(updated_eq2, updated_eq3))
        self.wait(2)

        # Step 4: Simplify to "merry = x - mas"
        updated_eq4 = MathTex(r"merry =", r"x - mas").move_to(updated_eq3)
        self.play(TransformMatchingTex(updated_eq3, updated_eq4))
        self.wait(2)

        # Final festive message
        final_message = Text("Merry Christmas!").scale(1.2).set_color_by_gradient(RED, GREEN)
        self.play(FadeOut(updated_eq4), Write(final_message))
        self.wait(3)

# To render this animation, save it as a .py file and run:
# manim -pql your_file_name.py MerryChristmas
