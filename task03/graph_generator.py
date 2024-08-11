import networkx as nx
import random
import faker


def generate_fb_friends(main_account_name):
    fb_graph = nx.Graph()
    fake = faker.Faker()

    num_friends = 7
    # Add nodes with names
    fb_graph.add_node(main_account_name)

    friend_for_search = fake.name()
    fb_graph.add_node(friend_for_search)
    for i in range(1, num_friends):
        fb_graph.add_node(fake.name())

    # Randomly connect nodes
    friends = list(fb_graph.nodes)
    for i in range(len(friends)):
        if i != 0:
            weight = random.randint(1, 10)
            fb_graph.add_edge(friends[0], friends[i], weight=weight)
        for j in range(i + 1, len(friends)):
            if random.random() < 0.3:  # 30% chance of connection
                weight = random.randint(1, 10)
                fb_graph.add_edge(friends[i], friends[j], weight=weight)

    return fb_graph, friend_for_search
