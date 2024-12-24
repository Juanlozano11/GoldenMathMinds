## Path: cd Desktop/Math/GoldenMathMinds/projects/video14
## run: manim -pql christmas.py MerryChristmas

from manim import *

class MerryChristmas(Scene):
    def construct(self):
        # Initial equation
        equation = MathTex(r"y =", r"\frac{\log_e\left(\frac{x}{m} - sa\right)}{r^2}")
        self.play(Write(equation))
        

        # Step 1: Multiply by r^2 (move r^2 to the left-hand side)
        self.play(equation[1].animate.set_color(YELLOW))  # Highlight the changing part
        updated_eq1 = MathTex(r"yr^2 =", r"\log_e\left(\frac{x}{m} - sa\right)").move_to(equation)
        self.play(
            TransformMatchingTex(equation, updated_eq1, path_arc=90, run_time=1),
            FadeOut(equation, shift=UP, scale=0.8, run_time=1)
        )
        self.play(updated_eq1[0].animate.set_color(WHITE))  # Reset color
        

        # Step 2: Exponentiation (apply e^ to both sides)
        updated_eq2 = MathTex(r"e^{yr^2} =", r"\frac{x}{m} - sa").move_to(updated_eq1)
        self.play(Indicate(updated_eq1[0], color=BLUE, scale_factor=1.2))  # Indicate the changing term
        self.play(
            TransformMatchingTex(updated_eq1, updated_eq2, path_arc=90, run_time=1.2),
            FadeOut(updated_eq1, shift=UP, scale=0.8, run_time=1.2)
        )
        

        # Step 3: Multiply by m (simplify the fraction)
        updated_eq3 = MathTex(r"me^{yr^2} =", r"x - msa").move_to(updated_eq2)
        self.play(ApplyWave(updated_eq2[1], amplitude=0.2))  # Add a wave effect to focus
        self.play(
            TransformMatchingTex(updated_eq2, updated_eq3, run_time=1.2),
            FadeOut(updated_eq2, shift=UP, scale=0.8, run_time=1.2)
        )
        

        # Step 4: Simplify to "merry = x - mas"
        updated_eq4 = MathTex(r"me^{rry} =", r"x - mas").move_to(updated_eq3)
        self.play(FadeToColor(updated_eq3[0], RED))  # Highlight changing term in red
        self.play(
            TransformMatchingTex(updated_eq3, updated_eq4, path_arc=-90, run_time=1.2),
            FadeOut(updated_eq3, shift=UP, scale=0.8, run_time=1.2)
        )
        self.play(FadeToColor(updated_eq4, WHITE))  # Reset color
        

        # Final festive message
        final_message = Text("Merry Christmas!").scale(1.2).set_color_by_gradient(RED, GREEN)
        self.play(
            FadeOut(updated_eq4, shift=UP, scale=0.5, run_time=1.2),
            GrowFromCenter(final_message, run_time=1.5)
        )

        self.play(FadeOut(final_message))

        # Golden Ratio Spiral (one smooth rotation)
        spiral = ParametricFunction(
            lambda t: np.array([np.cos(t) * (1.618 ** (t / (2 * np.pi))),
                                np.sin(t) * (1.618 ** (t / (2 * np.pi))),
                                0]),
            t_range=[0, 2 * PI],
            color=TEAL_A
        ).scale(0.5).shift(LEFT)
        
        # Dot tracing part of the spiral, stopping midway
        trace_dot = Dot(color=MAROON_A).move_to(spiral.get_start())
        halfway_point = spiral.point_from_proportion(0.5)
        
        # Euler's Identity with elegant text
        euler_identity = MathTex("e^{i\\pi} + 1 = 0", color=WHITE).scale(1.3).next_to(trace_dot, 3 * DOWN, buff=0.3)

        # "Golden Math Minds" with gradient effect
        logo_text = Text("Golden Math Minds", font_size=44, gradient=(YELLOW, ORANGE, GOLD))
        logo_text.next_to(euler_identity, 2.5 * DOWN, buff=0.3)

        # Animations
        self.play(Create(spiral), MoveAlongPath(trace_dot, spiral, rate_func=linear), run_time=2.5)
        self.play(trace_dot.animate.move_to(halfway_point), run_time=1)
        self.play(Write(euler_identity), run_time=1.2)
        self.wait(0.5)
        self.play(Write(logo_text))
        self.wait(1.5)

        # Final cool ending animation
        self.play(
            FadeOut(logo_text),
            FadeOut(euler_identity),
            spiral.animate.scale(0.1).move_to(ORIGIN),
            trace_dot.animate.scale(0.1).move_to(ORIGIN),
            run_time=2
        )

        # Hold briefly
        self.wait(0.8)

        
