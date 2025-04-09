import mermaid as md
from mermaid.graph import Graph

# Define the Mermaid diagram syntax
mermaid_syntax = """
flowchart LR
    A[Monitoring] --> B[Alerts/ Dashboards]
    A[Monitoring] --> C[Threshold Checks]
    D[Observability] --> B[Alerts/ Dashboards]
    D[Observability] --> C[Threshold Checks]
    D[Observability] --> E[Deep Investigation & Unknown Unknowns]
"""

# Create a Graph object with the syntax
graph = Graph("flowchart", mermaid_syntax)

# Generate the SVG content directly from the Graph object
md.Mermaid(graph).to_svg("./support_apps/image/mermaid_diagram.svg")
md.Mermaid(graph).to_png("./support_apps/image/mermaid_diagram.png")


print("Mermaid diagram saved as mermaid_diagram")
