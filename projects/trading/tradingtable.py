## path : cd Desktop/Math/GoldenMathMinds/projects/trading
## run :  manim -pql tradingtable.py TraderComparison

from manim import *

class TraderComparison(Scene):
    def construct(self):
        # Titles for Trader A and Trader B
        trader_a_title = Text("Trader A")
        trader_b_title = Text("Trader B")

        # Position titles for each trader
        trader_a_title.to_edge(UP).shift(LEFT * 3)
        trader_b_title.to_edge(UP).shift(RIGHT * 3)

        # Trades for Trader A
        trader_a_trades = VGroup(
            Text("+ $300").set_color(GREEN),
            Text("- $100").set_color(RED),
            Text("- $200").set_color(RED),
            Text("+ $400").set_color(GREEN),
            Text("+ $200").set_color(GREEN),
            Text("- $200").set_color(RED),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(trader_a_title, DOWN, buff=0.5)
        
        # Total and trade count for Trader A
        trader_a_total = Text("+ $400", color=GREEN).scale(1.2).next_to(trader_a_trades, DOWN, buff=0.7)
        trader_a_trades_count = Text("[6 trades]").next_to(trader_a_total, DOWN, buff=0.3)

        # Add horizontal line above Trader A's total to indicate it is the sum
        line_a = Line(
            trader_a_total.get_left() + LEFT * 0.1, 
            trader_a_total.get_right() + RIGHT * 0.1
        ).next_to(trader_a_total, UP, buff=0.1)

        # Trades for Trader B
        trader_b_trades = VGroup(
            Text("+ $300").set_color(GREEN),
            Text("- $100").set_color(RED),
            Text("no trade").set_color(WHITE),
            Text("no trade").set_color(WHITE),
            Text("+ $200").set_color(GREEN),
            Text("no trade").set_color(WHITE),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(trader_b_title, DOWN, buff=0.5)
        
        # Add yellow background rectangles for "no trade" entries
        #for i in [2, 3, 5]:  # Indices of "no trade" entries
        #    rect = SurroundingRectangle(trader_b_trades[i], color=YELLOW, fill_opacity=0.3, buff=0.1)
        #    self.add(rect)

        # Total and trade count for Trader B
        trader_b_total = Text("+ $400", color=GREEN).scale(1.2).next_to(trader_b_trades, DOWN, buff=0.7)
        trader_b_trades_count = Text("[3 trades]").next_to(trader_b_total, DOWN, buff=0.3)

        # Add horizontal line above Trader B's total to indicate it is the sum
        line_b = Line(
            trader_b_total.get_left() + LEFT * 0.1, 
            trader_b_total.get_right() + RIGHT * 0.1
        ).next_to(trader_b_total, UP, buff=0.1)

        # Group Trader A and Trader B elements for easier positioning
        trader_a_group = VGroup(trader_a_title, trader_a_trades, trader_a_total, trader_a_trades_count, line_a)
        trader_b_group = VGroup(trader_b_title, trader_b_trades, trader_b_total, trader_b_trades_count, line_b)

        # Shift Trader A and Trader B groups to opposite sides
        trader_a_group.shift(LEFT * 2.5)
        trader_b_group.shift(RIGHT * 2.5)

        # Create a vertical dividing line and center it between Trader A and Trader B groups
        dividing_line = Line(
            trader_a_group.get_right() + RIGHT * 0.25 + UP * 0.1,
            trader_b_group.get_left() + LEFT * 0.25 + UP * 0.1,
        ).set_color(GRAY).rotate(PI / 2)  # Rotate by 90 degrees to make it vertical

        # Group everything together for scaling and centering
        full_layout = VGroup(trader_a_group, trader_b_group, dividing_line)
        full_layout.center().scale(0.8)  # Center and scale down to fit the frame

        # Play animations for entry
        self.play(
            Write(trader_a_title),
            Write(trader_b_title),
            Write(trader_a_trades),
            Write(trader_b_trades),
            Write(trader_a_total),
            Write(trader_b_total),
            Write(trader_a_trades_count),
            Write(trader_b_trades_count),
            Create(line_a),
            Create(line_b),
            Create(dividing_line)
        )
        self.wait(2)
