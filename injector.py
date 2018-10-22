
from dependency_injector import containers, providers
import json
import collections

def inject():
    obj_pool = {}
    with open('config.json') as f:
        comp = json.load(f)

    for key in comp['components']:
        obj = providers.Factory(_import('components.' + comp['components'][key]))
        obj_pool.update({key: obj()})
        main_cls = obj_pool.get(comp['main'])
        main_cls.execute()
        
    
def _import(name):
    comps = name.split('.')
    length = len(comps)
    cls_name = comps[-1]
    mod = __import__('.'.join(comps[0:-1]), fromlist=[cls_name])
    klass = getattr(mod, cls_name)
    return klass


if __name__ == '__main__':
    # _import("components.main.Main")
    inject()
