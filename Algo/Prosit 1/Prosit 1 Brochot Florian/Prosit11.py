import matplotlib.pyplot as plt
import networkx as nx 
import numpy as np 
import time
head_zone_A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
Adj_zone_A = [["B", "J"], ["A", "C"], ["B", "D"], ["C", "E", "I", "G"], ["D", "F"], ["E", "G"],
               ["D", "F", "H", "I"], ["G", "I"], ["D", "G", "J","H"], ["A", "I"]]
adj_matrix = np.zeros((len(head_zone_A), len(head_zone_A)), dtype=int)

# Remplir la matrice d'adjacence en fonction de la liste des successeurs
for i, succ_list in enumerate(Adj_zone_A):
    for succ_node in succ_list:
        j = head_zone_A.index(succ_node)
        adj_matrix[i, j] = 1

print(adj_matrix)
###Degrée
def degreSommetGrapheMatrice(matrice, sommet):
    degre = []
    for i in range(len(adj_matrix)):
        degre.append(sum(adj_matrix[i]))
    return degre
print("### Degré des sommets du graphe de la Zone A ###")
for sommet in range(len(adj_matrix)):
    degreSommetGrapheMatrice(adj_matrix, sommet)
print(str(degreSommetGrapheMatrice(adj_matrix, sommet)))    

print("\n### Voisins des sommets du graphe de la Zone A ###")

#####Y'a til un cycle eulerieen #####
def existeCycleEulerien(matrice):
    a=0
    for sommet in range(len(matrice)):
        if int(sum(adj_matrix[sommet])) % 2 == 0:
            pass
        else : 
            a+=1
    if a == 0:
         return True
    else: 
        return False  
if (existeCycleEulerien(adj_matrix)):
    print ("Le graphe de la Zone A est eulérien")
else:
    print ("Le graphe de la Zone A n'est pas eulérien")
print()

G = nx.Graph()

# Ajout des arêtes
for i, succ_list in enumerate(Adj_zone_A): ##Parcour matrice adjacence
    for succ_node in succ_list:   #Liste les successeurs
        G.add_edge(head_zone_A[i], succ_node) ###pour graphe, ajoute une arrete entre les deux

# Vérification de l'existence d'un cycle eulérien
if nx.is_eulerian(G):
    # Recherche d'un cycle eulérien
    eulerian_cycle = list(nx.eulerian_circuit(G)) #génere les arretes du cycle eulerien en liste 
    print("Cycle eulérien trouvé :", eulerian_cycle)
    #pos = nx.spring_layout(G)  # Positionnement des nœuds
    #nx.draw(G, pos, with_labels=True, font_weight='bold')  # Dessiner le graphe
    #nx.draw_networkx_edges(G, pos, edgelist=eulerian_cycle, edge_color='r', width=2)  # Mettre en évidence le cycle
    #plt.show()
    
else:
    print("Le graphe de la Zone A n'est pas eulérien.")
print(f"{time.process_time()} seconde")