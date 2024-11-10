## path : cd Desktop/Math/GoldenMathMinds/projects/video05
## run :  manim -pql gcdproof.py BezoutsIdentityProof


from manim import *

class BezoutsIdentityProof(Scene):
    def construct(self):
        # Title
        title = Text("Proof using Bézout's Identity", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Introduction to the goal
        goal = Tex(
            r"Goal: Show that if $a, b, c \in \mathbb{Z}$ with $\gcd(a, b) = 1$, then \\",
            r"$(a \mid bc) \Rightarrow (a \mid c).$"
        ).scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(Write(goal))
        self.wait(1)

        # Introduction to Bézout's Identity (we'll uncreate these after displaying)
        bezout_intro = Tex(
            r"Bézout's Identity: For $a, b \in \mathbb{Z}$, if $\gcd(a, b) = 1$, \\",
            r"then there exist $x, y \in \mathbb{Z}$ such that $ax + by = 1$."
        ).scale(0.7).next_to(goal, DOWN, buff=0.5)
        self.play(Write(bezout_intro))
        self.wait(2)

        # Clearing space by fading out goal and Bézout's identity
        self.play(FadeOut(goal), FadeOut(bezout_intro))

        # Step 1: Assume the hypothesis
        hypothesis = Tex("Let's start by assuming the hypothesis: ", "$a \\mid bc$")
        hypothesis[1].set_color(BLUE)
        hypothesis.scale(0.8).next_to(title, DOWN, buff=0.5)
        self.play(Write(hypothesis))

        # Step 2: Write what this assumption means
        assumption_expansion = Tex(
            "This means that ", "$bc = ka$", " for some integer ", "$k \\in \\mathbb{Z}$."
        )
        assumption_expansion[1].set_color(BLUE)
        assumption_expansion.scale(0.8).next_to(hypothesis, DOWN, buff=0.5)
        self.play(Write(assumption_expansion))
        self.wait(2)

        # Clearing space by fading out the hypothesis text
        self.play(FadeOut(hypothesis), FadeOut(assumption_expansion))

        # Step 3: Use Bézout's identity in the proof
        bezout_step = Tex(
            r"Since $\gcd(a, b) = 1$, Bézout's identity gives $x, y \in \mathbb{Z}$ \\",
            r"such that $ax + by = 1$. We now multiply both sides by $c$:"
        ).scale(0.7).next_to(title, DOWN, buff=0.5)
        self.play(Write(bezout_step))
        self.wait(2)

        # Step 4: Expanding with multiplication
        expansion = MathTex(
            "c = acx + bcy = a(cx + ky)"
        ).scale(0.8).next_to(bezout_step, DOWN, buff=0.5)
        self.play(Write(expansion))
        self.wait(2)

          # Step 5: Conclude the proof with enhanced visual effects
        conclusion = Tex(
            r"Since $cx + ky \in \mathbb{Z}$, we conclude that $a \mid c$ as required."
        ).scale(0.8).next_to(expansion, DOWN, buff=0.5)
        
        # Apply gradient color to the conclusion text
        conclusion.set_color_by_gradient(BLUE, GREEN)
        self.play(Write(conclusion))

        # Display box around the conclusion with gradient color effect and adjust position
        box = SurroundingRectangle(conclusion, color=WHITE, buff=0.3)
        self.play(Create(box))

        # Scaling effect for emphasis
        self.play(box.animate.scale(1.1).shift(DOWN * 0.2), conclusion.animate.scale(1.1).shift(DOWN * 0.2))

        # Final celebratory QED symbol with adjusted placement
        qed = Tex(r"$\blacksquare$").set_color(YELLOW).scale(1.2).next_to(conclusion, DOWN, buff=0.2)
        qed.to_corner(DR, buff=0.5)
        self.play(Write(qed))

        # Clear everything else for a clean, focused final view
        self.play(FadeOut(title), FadeOut(expansion), FadeOut(bezout_step))
        self.play(FadeOut(box), FadeOut(conclusion), FadeOut(qed))

        # Pause to enjoy the final clean scene
        self.wait(0.3)


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
