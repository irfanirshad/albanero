# Useful validation techniques and options in Marshmallow:

## Validators: 
In addition to using the validate decorator, you can also define custom validation methods within your schema class. These methods should start with the prefix validate_ followed by the field name. For example, if you have a field named age, you can define a method named validate_age to perform validation specific to that field.

## Custom Validation Error Messages: 
You can provide custom error messages for validation failures. Instead of relying on the default error messages, you can define your own messages to provide more informative feedback to the user.

## Required Fields: 
Use the required parameter when defining fields to indicate whether a field is required. For example, fields.Int(required=True) specifies that the field must be provided in the input data.

## Validating Nested Schemas: 
When you use Nested fields to represent nested objects or lists of objects, you can apply validation to those nested schemas as well. This allows you to ensure the validity of complex data structures.

## Custom Validation Functions: 
You can define custom validation functions that take the entire data object as input. This is useful when you need to validate the relationship between multiple fields or perform cross-field validation.

## Pre- and Post-Load Hooks: 
Marshmallow provides pre_load and post_load hooks that allow you to execute custom code before and after the data is loaded into the schema. This can be useful for performing additional validation checks or data manipulation.

## Error Handling: 
When validation fails, Marshmallow raises a ValidationError with detailed error messages. You can catch and handle this exception to provide a user-friendly response or take specific actions based on the validation failure.

## Custom Validations in Nested Schemas: 

When you're using nested schemas, you can define custom validation methods within the nested schema to handle specific validation logic for that schema.



# Rough area

### Field Validators as Methods


It is sometimes convenient to write validators as methods. Use the validates decorator to register field validator methods.

```

from marshmallow import fields, Schema, validates, ValidationError

class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates("quantity")
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if value > 30:
            raise ValidationError("Quantity must not be greater than 30.")

```