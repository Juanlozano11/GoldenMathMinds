## path : cd Desktop/Math/GoldenMathMinds/projects/video03
## run :  manim -pql gcdproof.py BezoutsIdentityProof


from manim import *

class BezoutsIdentityProof(Scene):
    def construct(self):
        

        title = Text("Proof using Bézout's Identity", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Displaying the problem statement
        statement = Tex(
            r"Let $a, b, c \in \mathbb{Z}$ such that $\gcd(a, b) = 1$. Then \\",
            r"\[(a \mid bc) \Rightarrow (a \mid c).\]"
        ).next_to(title, DOWN)
        self.play(Write(statement))
        
        # Step 1: Introduce Bézout's identity
        bezout_identity = Tex(
            r"Bézout's Identity: For $a, b \in \mathbb{Z}$, if $\gcd(a, b) = 1$, \\",
            r"then there exist $x, y \in \mathbb{Z}$ such that $ax + by = 1$."
        ).scale(0.8).next_to(statement, DOWN, buff=1)
        self.play(Write(bezout_identity))
        
        # Step 2: Start the proof
        proof_text = Tex("Proof: Assume ", "$a \\mid bc$", " so ", "$bc = ka$ for some $k \\in \\mathbb{Z}$.")
        proof_text[1].set_color(BLUE)
        proof_text.next_to(bezout_identity, DOWN, buff=1)
        self.play(Write(proof_text))
        
        # Step 3: Using Bézout's identity
        bezout_step = Tex(
            r"Since $\gcd(a, b) = 1$, Bézout's identity gives us $x, y \in \mathbb{Z}$ \\",
            r"such that $ax + by = 1$. Multiply both sides by $c$:"
        ).scale(0.8).next_to(proof_text, DOWN, buff=0.5)
        self.play(Write(bezout_step))
        
        # Step 4: Expanding with multiplication
        expansion = MathTex(
            "c = acx + bcy = a(cx + ky)"
        ).scale(0.9).next_to(bezout_step, DOWN, buff=0.5)
        self.play(Write(expansion))
        
        # Step 5: Conclusion
        conclusion = Tex(
            r"Since $cx + ky \in \mathbb{Z}$, we conclude that $a \mid c$ as required."
        ).next_to(expansion, DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        # Display box around the proof
        box = SurroundingRectangle(conclusion, color=WHITE, buff=0.3)
        self.play(Create(box))
        
        # End of proof
        qed = Tex(r"$\square$").next_to(conclusion, RIGHT, buff=0.2)
        self.play(Write(qed))
        
        # Pause to view final proof
        self.wait(2)
