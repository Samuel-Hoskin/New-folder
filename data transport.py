from pyvis.network import Network
import pandas as pd

data = pd.read_csv("relationship.csv")
got_net = Network(height='750px', width='100%', directed=True)

# Create the dataframe

data2 = data.melt(id_vars = "name", var_name="relation")

for index, row in data.iterrows():
    name = row[0]
    got_net.add_node(name, title=name)

for index, row in data2.iterrows():
    name = row[0]
    relation = row[1]
    weight = row[2]

    if weight > 0:
        got_net.add_edge(name, relation, value=weight)

got_net.barnes_hut(gravity=-80000, central_gravity=0.3, spring_length=250, spring_strength=0.001, damping=0.09, overlap=0)
got_net.show_buttons()
got_net.show('TeamChart.html')