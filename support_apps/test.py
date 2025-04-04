import mermaid as md
from mermaid.graph import Graph

# Define the Mermaid diagram syntax
mermaid_syntax = """
pie title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15
"""

# Create a Graph object with the syntax
graph = Graph("piechart", mermaid_syntax)

# Generate the SVG content directly from the Graph object
md.Mermaid(graph).to_svg("./support_apps/image/mermaid_diagram.svg")
md.Mermaid(graph).to_png("./support_apps/image/mermaid_diagram.png")


print("Mermaid diagram saved as mermaid_diagram")
