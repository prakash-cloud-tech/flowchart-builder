# flowchart-builder
A python script to create a simple flowchart from data in a yml file

📊 YAML Flowchart Generator (Graphviz)

A lightweight Python utility that converts a simple YAML-defined workflow into a visual flowchart using Graphviz.

## It generates:
- 🖼️ A PNG flowchart image
- 🌐 A simple HTML viewer to display the diagram

## 🚀 Features
- Define workflows in simple YAML format
- Supports:
  - Linear steps
  - Decision nodes (yes/no)
  - Automatically generates flowcharts using Graphviz
- Outputs:
- flowchart.png
- viewer.html (static page to display diagram)
- Minimal setup, no web framework required

## 📦 Requirements
- Python dependencies
- pip install pyyaml graphviz
- System dependency (required)

## Graphviz must be installed on your system:

### Ubuntu / WSL
- sudo apt install graphviz

### Mac (Homebrew)
- brew install graphviz

### Windows
Download installer:
https://graphviz.org/download/

Add Graphviz bin folder to PATH.

## 📁 Project Structure
.
├── flow.yml
├── generate.py
├── flowchart.png   (auto-generated)
└── viewer.html     (static viewer)

## 🧾 YAML Format

Define your workflow like this:

start: Start
steps:
  - id: step1
    text: Load data
    next: step2

  - id: step2
    text: Validate data
    decision: true
    yes: step3
    no: step4

  - id: step3
    text: Process data
    next: step5

  - id: step4
    text: Reject data
    next: end

  - id: step5
    text: Save results
    next: end

end: End

## ▶️ Usage

Run the generator:

```
python script.py
```

This will generate:

```
flowchart.png

````
## 🌐 View Flowchart

Open the HTML file in your browser:
```
open viewer.html   # Mac
start viewer.html  # Windows
xdg-open viewer.html # Linux
```

## 🧠 How it works
- YAML is parsed into a structured workflow
- Graph nodes are created using Graphviz
- Edges are generated based on:
  - next
  - yes / no (for decisions)
- Output is rendered as a PNG image
- HTML file simply embeds the image

## 📌 Example Output
Start
  ↓
Load Data
  ↓
Validate Data
   ↙        ↘
Reject     Process
   ↓          ↓
  End        Save
               ↓
              End

## ⚡ Why this tool?
- No UI framework required
- No complex diagramming tools

## Ideal for:
- Documentation
- Workflow visualization
- LMS / training content
- Architecture drafts
- Quick prototyping

## 🔧 Future Improvements
- SVG output support (sharper diagrams)
- Interactive HTML flowcharts
- Swimlane support
- Auto layout optimization
- CLI wrapper (flowgen generate flow.yml)

## 📄 License

MIT — feel free to use and modify.