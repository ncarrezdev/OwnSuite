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
        import os

        features_list = kwargs.get("features", [])
        if features_list ==  []:
            return super(CustomClass, cls).__call__(*args, **kwargs)
        
        features = tuple()
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

    def __repr__(cls):
        '''Representation operator'''
        res = ''
        res += cls.__name__ + '(' 
        for attribute, value in CustomClass.__get_attributes__(cls):
            res += str(attribute) 
            res += ':'
            if(type(value) != str):
                res += str(value) 
            if(type(value) == str):
                res += '\'' + str(value) + '\''
            res += "; "
        if(res != cls.__name__ + '('):
            res = res[:-2]
        res += ')'
        return res

    def __get_attributes__(cls):
        '''Private Method
        Returns the list of attributes and associated values.
        
        :return: A tuple of tuple ((name, value),)'''
        res = tuple()
        for attribute in dir(cls):
            if (not ('__' in attribute) and not callable(getattr(cls, attribute))):
                res += ((attribute, getattr(cls, attribute)),)
        return res