import sys
import tqdm
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from networkx.drawing.nx_agraph import graphviz_layout

# def return_colour(aNum):
#     colours = ["#006816","#8d34e4","#c9a738","#0163d0","#ee5700", "#00937e", "#ff4284", "#4b5400", "#ea80ff","#9f0040"]
#     assert aNum < len(colours)
#     return colours[aNum], aNum+1

# def return_legend(legend):
#     legends = [Line2D([0], [0], marker='o', color='w', label='Party Leader', markerfacecolor='r', markersize=10), Line2D([0], [0], marker='o', color='w', label='Retweet', markerfacecolor='#79BFD3', markersize=10)]
#     legend = sorted(legend, key=lambda tup: tup[1])
#     for color, cluster_num in legend:
#         legends.append(Line2D([0], [0], marker='o', color='w', label='Topic {}'.format(cluster_num), markerfacecolor=color, markersize=10))
#     return legends

class Graph(object):
    '''
    Initiates the networkx graph, houses visualization, as well as some quick/dirty analysis.
    Parameters
    ----------
    :param usernames: A list of strings, corresponding to the twitter usernames stored in `/data`
    
    :param n: An int, corresponding to the number of tweets to map.
    '''
    def __init__(self, usernames, n=None):
        self.num_retweeters = 0
        self.num_tweets = 0
        self.num_retweets = 0
        self.G = nx.Graph()
        self.title = ""
        for username in usernames:
            self.title += "{}_".format(username)
            user_graph = self.build_graph(username, n)
            self.G = nx.compose(self.G, user_graph)
        print("--- {} tweets, {} retweeters, {} retweets ---".format(self.num_tweets,self.num_retweeters, self.num_retweets))

    def draw_graph(self, G=None, save=False, file_type='png',use_pos=False):
        """
        Handles rendering and drawing the network.
        Parameters
        ----------
        :param G: `optional` 
        
        a networkx graph. If present draws this graph instead of the one built in the constructor.
        :param save: `optional` 
        
        A boolean. If true saves an image of the graph to `/visualizations` otherwise renders the graph.
        
        :param file_type: `optional` 
        
        A string. If save flag is true it saves graph with this file extension.
        
        :param use_pos: `optional` 
        
        A boolean. If true renders the graph using default positions of the entire graph. Otherwise calculates positions based on data used.
        """
        if not G:
            G = self.G
        print("--- Adding colours and labels ---")
        colors = []
        legend = set()
        labels = {}
        pbar = tqdm.tqdm(total=len(G.nodes()))
        for node in G.nodes():
            attributes = G.nodes[node]
            assert 'type' in attributes, "Type is a required attribute for any vertex in this graph."
            if attributes['type'] == 'retweet':
                colors.append('#79BFD3')
            elif attributes['type'] == 'tweet':
                cluster = self.__return_colour(attributes["lda_cluster"])
                legend.add(cluster)
                colors.append(cluster[0])
            elif attributes['type'] == 'user':
                labels[node] = node
                colors.append('red')
            pbar.update(1)
        pbar.close()
        plt.figure(figsize=(30, 30))
        pos = graphviz_layout(self.G, prog="sfdp") if use_pos else graphviz_layout(G, prog="sfdp")
        _xlim = None
        _ylim = None
        if use_pos: #To use the same positioning for two subgraphs we need to make sure the x/y limits are the same for the plot
            nx.draw(self.G,pos)
            _xlim = plt.gca().get_xlim() # grab the xlims
            _ylim = plt.gca().get_ylim() # grab the ylims
            # Clear the figure.
            plt.clf()
        print("--- Drawing {} nodes and {} edges ---".format(len(G.nodes()), G.number_of_edges()))
        nx.draw(G, pos,
                node_color=colors,
                with_labels=False,
                alpha=0.75,
                node_size=20,
                width=0.2,
                arrows=False
                )
        if use_pos: plt.axis( [ _xlim[0], _xlim[1], _ylim[0], _ylim[1] ] )
        nx.draw_networkx_labels(G, pos, labels, font_size=16, font_color='r')
        plt.legend(handles=self.__return_legend(legend), loc="best")
        topics_used = '_'.join(str(l[1]) for l in sorted(legend, key=lambda tup: tup[1]))
        plt.savefig("../visualizations/{}graph_{}_tweets_{}_retweeters_{}_retweets_topics{}.{}".format(self.title,self.num_tweets, self.num_retweeters, self.num_retweets,topics_used, file_type)) if save else plt.show()

    def __return_legend(self, legend):
        return return_legend(legend)

    def build_graph(self, username, n=None):
        twitter_df = pd.read_csv(f"topic_centrality/data/{username}/{username}_data.csv")
        if n:
            twitter_df = twitter_df.sample(n=min(n, len(twitter_df)),random_state=1)
        # twitter_df = twitter_df.set_index('id')
        retweet_df = pd.read_csv(f"topic_centrality/data/{username}/{username}_retweets.csv")
        # if we're only taking 20 tweets find all the retweets for those 20
        retweet_df = retweet_df[retweet_df['original_tweet_id'].isin(
            twitter_df['id'])]
        # Instantiate a new Graph (there could potentially be multiple edges between a pair of nodes)
        G = nx.Graph()
        G.add_node(username, type='user')
        # add tweet nodes
        nodes = twitter_df.drop_duplicates(subset="id").set_index('id').to_dict('index').items()
        G.add_nodes_from(nodes)
        print("--- adding edges ---")
        pbar = tqdm.tqdm(total=len(twitter_df)+len(retweet_df))
        for _, row in twitter_df.iterrows():
            pbar.update(1)
            G.add_edge(username, row['id'])
        # add retweet user nodes (those who retweeted the original tweets) multipl
        user_nodes = retweet_df.drop_duplicates(subset="original_author")
        user_nodes = user_nodes.set_index('original_author').to_dict('index').items()
        G.add_nodes_from(user_nodes)
        for _, row in retweet_df.iterrows():
            pbar.update(1)
            G.add_edge(row['original_tweet_id'], row['original_author'])
        pbar.close()
        self.num_retweeters += len(user_nodes)
        self.num_tweets += len(twitter_df)
        self.num_retweets += len(retweet_df)
        return G

    # def get_density(self):
    #     density = nx.density(self.G)
    #     print("The percentage of edges/possible edges is {0:.4f}%: ".format(density*100))
    #     return density

    def map_topics(self, topics):
        '''
        Rebuilds the graph with only certain tweet topics
        Parameters
        ----------
        :param topics: A list of ints between 0-k, where k is the number of topics-1, corresponding with the topics to isolate for
        '''
        mapped_graph = self.G.copy()
        remove = [node for node in mapped_graph.nodes() if "lda_cluster" in mapped_graph.nodes[node] and not mapped_graph.nodes[node]["lda_cluster"] in topics]
        mapped_graph.remove_nodes_from(remove)
        remove = [node for node in mapped_graph.nodes() if "type" in mapped_graph.nodes[node] and mapped_graph.nodes[node]["type"] == "retweet" and mapped_graph.degree(node) == 0]
        mapped_graph.remove_nodes_from(remove)        
        assert not any(node in remove for node in mapped_graph.nodes)
        return mapped_graph

    # def __return_colour(self, aNum):
    #     return return_colour(aNum)
        
    # def diameter(self,G=None):
    #     if not G:
    #         G = self.G
    #     d = nx.diameter(G)
    #     print("Diameter: {}".format(d))
    #     return d

    # def retweet_histogram(self):
    #     degree_sequence = [d for n, d in self.G.degree() if self.G.nodes[n]["type"] == "retweet"]
    #     return np.histogram(degree_sequence, bins=len(degree_sequence)//2)

    def __len__(self):
        return len(self.G)

if __name__ == '__main__':
    # Read in CSV file for that twitter user (these are the original tweets)
    usernames = [politicians[0],politicians[1]]
    topics = range(0,8)
    G = Graph(usernames,100)