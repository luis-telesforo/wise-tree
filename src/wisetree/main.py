"""
An implementation of the Decision Tree Learning algorithm
input : A collection of pairs (x,y) where x is an observation and y is the value to learn.
A collection of features; each x must have exactly those features.
output : A decision tree.
"""


"""
The main function.
data : pairs (x,y)
features : features of x

returns: a tree
"""
##TODO implement data and features with numpy
def wise_tree(data,features):
    #TODO the node data structure as a class
    root = node();
    ##TODO .trivial() determines whether all data lies in the same label
    ##implement trivial with numpy
    if (data.trivial()):
        #TODO leaf is a subclass of node
        #it avoids splitting;
        #also, it adds a label for the data
        ##TODO .majority_class_label() choose the label with the majority data;
        ##in this case all data must have that label
        ##implement with numpy
        root.leaf(data.majority_class_label());
        return root;
    ##TODO .empty determines if we have no features
    ##implement with numpy
    ##TODO .Features() extracts al values on the given features
    ##implement with numpy
    ##TODO .size() we need the ability to count our observations
    ##implement with numpy
    if (features.empty() || data.Features(features).size()==1):
        root.leaf(data.class_label(data.Features(features)));
        return root;
    #TODO .optimal_split_feat() determines the better feature to start splitting
    optimal_feature = features.optimal_split_feat();
    ##TODO data.optimal_feature as in Pandas
    ##implement with numpy
    for observation in data.optimal_feature:
        ##TODO .where() is a boolean mask
        ##implement with numpy
        data_observation = data.where(optimal_feature,observation);
        if (data_observation.size()==0):
            #TODO .add_leafs() adds a leaf to a tree
            branch = root.add_leaf(data.majority_class_label()); 
            return root;
        else:
            ##TODO .pop() pops a feature
            ##implement with numpy
            branch = wise_tree(data_observation,features.pop(optimal_feature));
            #TODO .add_branch() pastes two trees
            root.add_branch(branch)
    
            
    
