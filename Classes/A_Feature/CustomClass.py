'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


class CustomClass(type):
    '''MetaClass
    Create custom classes to match features'''
    def __call__(cls, *args, **kwargs):
        '''Method
        Enable features from the features list
        
        :kwarg features: List of features to enable - list/tuple'''
        features_list = kwargs.get("features", [])
        if features_list ==  []:
            return super(CustomClass, cls).__call__(*args, **kwargs)
        
        features = tuple()
        import os
        user_features = list(features_list)
        this_folder = os.path.abspath(os.path.dirname(__file__))
        available_features = []
        for f in os.listdir(this_folder):
            if(f[0].isupper() and f.endswith('.py')):
                available_features.append(f.replace('.py',''))
        for feature in available_features:
            if(feature.lower() in user_features):
                featureClass = getattr(__import__(feature), feature)
                features += (featureClass,)

        features = (cls,) + features
        new_cls = type(cls.__name__, features, {'__base__':features})
        return super(CustomClass, new_cls).__call__(*args, **kwargs)
