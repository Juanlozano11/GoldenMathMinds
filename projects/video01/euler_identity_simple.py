## Path: cd Desktop/Math/GoldenMathMinds/projects/video01
## run: manim -pql euler_identity_simple.py EulerIdentityExplanation

from manim import *

class EulerIdentityExplanationEnhanced(Scene):
    def construct(self):
        # Display the main equation in the center
        euler_identity = MathTex(r"e^{i \pi} + 1 = 0")
        euler_identity.set_color_by_gradient(BLUE, PURPLE, ORANGE)
        euler_identity.scale(2)
        euler_identity.to_edge(UP, buff=1.5)  # Move equation closer to the top

        # Step 1: Show the equation with a write effect
        self.play(Write(euler_identity))
        self.wait(1.5)

        # Step 2: Breakdown and explain each part with animations
        explanations = [
            ("e", "Euler's Number", BLUE),
            ("i", "Imaginary Unit", GREEN),
            (r"\pi", "Pi", ORANGE),
            ("1", "One", YELLOW),
            ("0", "Zero", RED)
        ]

        # Animate each explanation
        for symbol_str, explanation_text, color in explanations:
            # Create a MathTex object for the symbol with the correct color
            symbol = MathTex(symbol_str).set_color(color)
            symbol.scale(2)

            # Duplicate the part of the equation for the symbol
            symbol_copy = symbol.copy().move_to(euler_identity.get_part_by_tex(symbol_str).get_center())

            # Explanation text setup
            explanation = Text(explanation_text, font_size=36).set_color(color)
            explanation.next_to(symbol, DOWN, buff=0.5)

            # Animate symbol moving from the equation, text writing, and return of the symbol
            self.play(TransformFromCopy(euler_identity.get_part_by_tex(symbol_str), symbol))
            self.play(Write(explanation))
            self.wait(1.5)
            self.play(FadeOut(explanation), Transform(symbol, symbol_copy))
            self.remove(symbol)

        # Step 3: Display summary text below the equation with adjusted positioning
        summary_text = Text(
            "Euler’s Identity connects 5 fundamental constants in one beautiful equation!",
            font_size=30, color=WHITE
        )
        summary_text.next_to(euler_identity, DOWN, buff=1)  # Position summary text below the equation
        self.play(Write(summary_text))
        self.wait(3)
        self.play(FadeOut(summary_text))

        # Step 4: Show the equation again with the final statement
        final_equation = MathTex(r"e^{i \pi} + 1 = 0")
        final_equation.set_color_by_gradient(BLUE, PURPLE, ORANGE)
        final_equation.scale(2.5)
        final_equation.move_to(UP * 0.5)  # Adjust position to fit in the frame

        final_statement = Text(
            "The most beautiful equation in mathematics!",
            font_size=32, color=WHITE
        )
        final_statement.next_to(final_equation, DOWN, buff=0.5)  # Position below the equation

        self.play(FadeIn(final_equation), Write(final_statement))
        self.wait(3)
        self.play(FadeOut(final_equation), FadeOut(final_statement))
