import yaml
from graphviz import Digraph

def create_flowchart(yaml_file, output_file="flowchart"):
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    dot = Digraph(
    format="png",
    graph_attr={
        "rankdir": "TB",
        "nodesep": "0.5",
        "ranksep": "0.6"
        }
    )

    # Add start and end
    dot.node("start", data.get("start", "Start"), shape="oval")
    dot.node("end", data.get("end", "End"), shape="oval")

    steps = {step["id"]: step for step in data["steps"]}

    # Create nodes
    for step in steps.values():
        shape = "diamond" if step.get("decision") else "box"
        dot.node(step["id"], step["text"], shape=shape)

    # Connect start to first step
    first_step = data["steps"][0]["id"]
    dot.edge("start", first_step)

    # Create edges
    for step in steps.values():
        if step.get("decision"):
            if "yes" in step:
                dot.edge(step["id"], step["yes"], label="Yes")
            if "no" in step:
                dot.edge(step["id"], step["no"], label="No")
        else:
            if "next" in step:
                dot.edge(step["id"], step["next"])

    # Render
    dot.render(output_file)
    print(f"Flowchart generated: {output_file}.png")


if __name__ == "__main__":
    create_flowchart("flow.yml")