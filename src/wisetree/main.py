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

returs: a tree
"""
#TODO what types are data and features?
#TODO what is a tree?
def wise_tree(data,features):
    #TODO tree is a data structure
    root = tree();
    #TODO .trivial() determines whether all data lies in the same class
    if (data.trivial()):
        #TODO leaf is a marker;
        #it avoids splitting;
        #also, it adds a label for the class
        #TODO .majority_class_label() choose the label with the majority data;
        #in this case all data must have that label
        root.leaf(data.majority_class_label());
        return root;
    #TODO empty determines if we have no features
    #TODO .Features() extracts al values on the given features
    #TODO .size() we need the ability to count our observations
    if (features.empty() || data.Features(features).size()==1):
        root.leaf(data.class_label(data.Features(features)));
        return root;
    #TODO .optimal_split_feat() determines the better feature to start splitting
    #TODO what is a feature?
    optimal_feature = features.optimal_split_feat();
    #TODO .feature() extracts the values of the given feature
    for observation in data.feature(optimal_feature):
        #TODO .where() selects the subset with the given value for the given feature
        data_observation = data.where(optimal_feature,observation);
        if (data_observation.size()==0):
            #TODO .add_leafs() adds a leaf to a tree
            branch = root.add_leaf(data.majority_class_label()); 
            return root;
        else:
            #TODO .pop() pops a feature
            branch = wise_tree(data_observation,features.pop(optimal_feature));
            #TODO .add_branch() pastes two trees
            root.add_branch(branch)
    
            
    
