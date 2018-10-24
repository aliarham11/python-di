# python-di
## Dependency injection wrapper for python (uncompleted)
Actually this is a playground for python newbie, so feel free to contribute newbiers XD.
I Will try to implement wrapper for dependency injection in python. 
For further implementation, i plan to implement some concept and ideas on this repo (for research purpose) : 

- Decorator
- Annotator
- Extendable Plugin
- Benchmarking the Performance with merapi (DI wrapper on Javascript)


# how to run ?
Specify components that you want to register for injection in config.json like this : 
```
{
    "components": {
        "main": {
            "path": "main.Main",
            "dependencies": [
                "first_component"
            ]
        },
        "first_component": {
            "path": "first_component.FirstComponent",
            "dependencies": []
        }
    },
    "main": "main"
}
```

Main component will be executed first.  If you want to set a component to main component, you must implement method `execute` in the component.

If all set, run with `python injector.py`




