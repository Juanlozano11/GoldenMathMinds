## Path: cd Desktop/Math/GoldenMathMinds/projects/logo
## run: manim -pql logo.py GoldenMathMindsLogo

from manim import *

class GoldenMathMindsCompact(Scene):
    def construct(self):
        # Golden Ratio Spiral (one quick rotation)
        spiral = ParametricFunction(
            lambda t: np.array([np.cos(t) * (1.618 ** (t / (2 * np.pi))),
                                np.sin(t) * (1.618 ** (t / (2 * np.pi))),
                                0]),
            t_range=[0, 2 * PI],
            color=GOLD
        ).scale(0.5).shift(LEFT)
        
        # Dot that traces part of the spiral and stops midway
        trace_dot = Dot(color=RED).move_to(spiral.get_start())
        halfway_point = spiral.point_from_proportion(0.5)  # Get halfway position along the spiral
        
        # Euler's Identity
        euler_identity = MathTex("e^{i\\pi} + 1 = 0", color=WHITE).scale(1.2).next_to(trace_dot, 3*DOWN, buff=0.2)

        # Golden Math Minds text with adjusted position
        logo_text = Text("Golden Math Minds", font_size=42, color=YELLOW).next_to(euler_identity, 2.7*DOWN, buff=0.3)

        # Animations
        self.play(Create(spiral), MoveAlongPath(trace_dot, spiral, rate_func=linear), run_time=2)
        self.play(trace_dot.animate.move_to(halfway_point), run_time=1)  # Stop the dot halfway
        self.play(Write(euler_identity), run_time=1)
        self.wait(0.5)
        self.play(Write(logo_text))
        self.wait(1.3)

        # Final cool ending animation
        self.play(
            FadeOut(logo_text),                     # Fade out the logo text
            FadeOut(euler_identity),                # Fade out Euler's identity
            spiral.animate.scale(0.1).move_to(ORIGIN),  # Spiral shrinks to center
            trace_dot.animate.scale(0.1).move_to(ORIGIN), # Dot shrinks to center
            run_time=2
        )

        # Hold for a moment after transition
        self.wait(0.8)
