# QAFrame

---
With easing the work of automation in mind, I'm creating this software to not have to create a script every time I want to check something.

## Technologies used

---
The project is created with:

- Python 3.6 or above
- Selenium

## Routine file

---
The `routine.json` file specifies how the program will proceed, and what actions to do.

The following is a sample of the structure and is followed by an explanation:

```
 {
    "verbose": 1 for verbose, 0 for no verbose - if no value, default will be 0
    "headless": 1 for headless, 0 for visible - if no value, default will be 1
    "on_error_proceed": 0 for stopping when a step fails and 1 to proceed - if no value is provided, default is 0,
    "routine": [
        {
            "time_load": time, in seconds, to wait until executing the action - if no value provided, default is 2,
            "wait":  time, in seconds, to wait to proceed to the next step - if no value provided, default is 0,
            "url": URL to execute the action - obligatory,
            "element": the XPath of the element to perform the action on - obligatory,
            "action": action to be performed, it can be one of the specified next - obligatory,
        }
    ]
 }
```

### Action
|         Action         |                                             Description                                              |                                                                                                       Options                                                                                                        | 
|:----------------------:|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|  `"action": "click"`   |            With this type of action, there will be an action performed in the `element`.             |                                                                                     `"element"` - element that will be clicked.                                                                                      |
|   `"action": "read"`   | This type of action will read a value and verify if it is the same, else it will result on an error. | `"element"` - element for the value to be read;<br/>`"value_to_verify"` - value to be verified against;<br/>`"on_error_proceed"` - if 0, stops here and will print the step on which it stopped, else will continue. |

### URL
To use the page from the previous routine, set `"url": "prev"`.