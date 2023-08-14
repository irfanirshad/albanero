# DATA CLASS WIZARD 

Minimal setup required. In most cases, all you need is a dataclass that sub-classes from JSONWizard.



## Features of DataClass-Wizard

Supported Features::

1. JSON/YAML (de-serialization) :: marshal dataclasses to/from JSON, YAML and Python dict objects..

2. Field properties: support for suing properties with default values in dataclass instances..

3. JSON to DataClass generation: construct a dataclass schema with a JSON file or string input


## Wizard Mixins

1. JSONListWizard: Extends JSONWizard to return Container(like a list object but not exactly)(can be used to prettify, to_json, to_json_file)

2. JSONFileWizard: Makes it easier to convert dataclass instances from/to JSON files on a local drive

3. YAMLWizard: Provides support to convert dataclass instances to/from YAML, using default PyYAML parser...