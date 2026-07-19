import graphviz

def generate_level_0():
    # Create Level 0 DFD
    dot = graphviz.Digraph('Level_0', filename='DFD_Level_0_Context', format='png')
    dot.attr(rankdir='LR', dpi='300') # High resolution
    dot.attr('node', fontname='Helvetica', fontsize='12')
    dot.attr('edge', fontname='Helvetica', fontsize='10')

    # Define Nodes (Box for Entity, Circle for Process)
    dot.node('Student', 'Student', shape='box', style='filled', fillcolor='#E0F7FA', penwidth='2')
    dot.node('System', '0.0\nSmart Career Guidance &\nSkill Recommendation', shape='circle', style='filled', fillcolor='#FFF3E0', penwidth='2')

    # Define Data Flows
    dot.edge('Student', 'System', label=' Assessment Inputs (CGPA, Logic, etc.) ')
    dot.edge('System', 'Student', label=' Career Prediction & Roadmap ')

    dot.render(cleanup=True)
    print("Level 0 DFD generated successfully as DFD_Level_0_Context.png")

def generate_level_1():
    # Create Level 1 DFD
    dot = graphviz.Digraph('Level_1', filename='DFD_Level_1_Main', format='png')
    dot.attr(rankdir='TD', dpi='300')
    dot.attr('node', fontname='Helvetica', fontsize='12')
    dot.attr('edge', fontname='Helvetica', fontsize='10')

    # External Entity
    dot.node('Student', 'Student', shape='box', style='filled', fillcolor='#E0F7FA', penwidth='2')

    # Processes (Circles)
    dot.node('P1', '1.0\nUser Management', shape='circle', style='filled', fillcolor='#E8F5E9', penwidth='2')
    dot.node('P2', '2.0\nAssessment Processing', shape='circle', style='filled', fillcolor='#E8F5E9', penwidth='2')
    dot.node('P3', '3.0\nPrediction Engine', shape='circle', style='filled', fillcolor='#E8F5E9', penwidth='2')
    dot.node('P4', '4.0\nRoadmap Curation', shape='circle', style='filled', fillcolor='#E8F5E9', penwidth='2')

    # Data Stores (Cylinders)
    dot.node('D1', 'D1: Users DB', shape='cylinder', style='filled', fillcolor='#EDE7F6', penwidth='2')
    dot.node('D2', 'D2: Roadmaps DB', shape='cylinder', style='filled', fillcolor='#EDE7F6', penwidth='2')

    # Flows
    dot.edge('Student', 'P1', label=' Login / Register Data')
    dot.edge('P1', 'D1', label=' Auth Check / Save')
    dot.edge('Student', 'P2', label=' Raw Scores')
    dot.edge('P2', 'P3', label=' Normalized Array')
    dot.edge('P3', 'P4', label=' Predicted Role')
    dot.edge('P4', 'D2', label=' Fetch Matches')
    dot.edge('D2', 'P4', label=' Course Links')
    dot.edge('P4', 'Student', label=' Final JSON Dashboard')

    dot.render(cleanup=True)
    print("Level 1 DFD generated successfully as DFD_Level_1_Main.png")

def generate_level_2():
    # Create Level 2 DFD (Zoomed into Prediction Engine)
    dot = graphviz.Digraph('Level_2', filename='DFD_Level_2_Prediction', format='png')
    dot.attr(rankdir='LR', dpi='300')
    dot.attr('node', fontname='Helvetica', fontsize='12')
    dot.attr('edge', fontname='Helvetica', fontsize='10')

    # Inputs / Outputs (Plain text/boxes)
    dot.node('In', 'Raw Feature Vector\n(From Process 2.0)', shape='plaintext')
    dot.node('Out1', 'Predicted Role String\n(To Process 4.0)', shape='plaintext')
    dot.node('Out2', 'Confidence %\n(To Process 4.0)', shape='plaintext')

    # Processes
    dot.node('P31', '3.1\nNormalization Node', shape='circle', style='filled', fillcolor='#E8F5E9', penwidth='2')
    dot.node('P32', '3.2\nDecision Tree Model', shape='circle', style='filled', fillcolor='#E8F5E9', penwidth='2')

    # Data Store (The ML Model file)
    dot.node('D3', 'D3: Serialized\n.pkl Model', shape='cylinder', style='filled', fillcolor='#EDE7F6', penwidth='2')

    # Flows
    dot.edge('In', 'P31')
    dot.edge('P31', 'P32', label=' Scaled Array')
    dot.edge('D3', 'P32', label=' Load Tree Weights')
    dot.edge('P32', 'Out1')
    dot.edge('P32', 'Out2')

    dot.render(cleanup=True)
    print("Level 2 DFD generated successfully as DFD_Level_2_Prediction.png")

# Run the functions
if __name__ == '__main__':
    print("Generating DFDs...")
    generate_level_0()
    generate_level_1()
    generate_level_2()
    print("All done! Check your folder for the image files.")