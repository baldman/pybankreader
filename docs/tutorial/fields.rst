Fields
======

As said earlier, fields are the most atomic part of the library. They are the
building blocks for inidividual records.

Using Fields
------------
A Field serves two purposes:

  * validation of data
  * automatic coercion to type

Validation is based on the type of field, so for instance while ``123`` is an
acceptable value for :py:class:`pybankreader.fields.IntegerField`, ``ABC`` is
not.

You will use fields when creating a record (more on that later). To illustrate
with an example::

    class MyRecord(Record):

        my_field = fields.IntegerField(required=True, length=10)


Notice that there are two parameters: ``required`` and ``length``. Both are
mandatory, since it's more expressive. Particularly ``IntegerField`` does not
have any other parameters, but for instance
:py:class:`pybankreader.fields.RegexField` has another one (``regex``)

A field has one attribute called ``value``, where the validated and already
coerced value resides.

.. warning:: The automatic coercion and validation has implications. For
    instance, a string with whitespaces (like ``\t``) is trimmed. Therefore,
    if you have separator fields defined like this:
    ``my_field = fields.CharField(length=1, required=True)``
    the load will fail, since empty string is coerced to None and therefore is
    treated like failing the ``required`` flag. For separators, always use
    ``required=False``.


Fields available in the library:

* :py:class:`pybankreader.fields.CharField`
* :py:class:`pybankreader.fields.RegexField`
* :py:class:`pybankreader.fields.IntegerField`
* :py:class:`pybankreader.fields.DecimalField`
* :py:class:`pybankreader.fields.TimestampField`


Custom Fields
-------------

Creating a custom field is very easy. You extend from the abstract base class
:py:class:`pybankreader.fields.Field`, where you would ordinarily override
the ``__init__`` and `_set_value` methods.

To have an example, let's implement a field that takes just hexa-decimal
numbers. Since this is basically just a regular expression, we use the
``RegexField`` for this particular situation, even though we could do it
ourselves::


    class HexField(RegexField):

        def __init__(*args, **kwargs):
            super(HexField, self).__init__(
                "^#[0-9a-f]{6}$", *args, **kwargs
            )

        def _set_value(self, value):
            try:
                super(HexField, self)._set_value(value)
            except ValidationError:
                # Make the ValidationError more specific
                msg = u"Value '{}' is not a hex number".format(
                    value, self._regex
                )
                raise ValidationError(self._field_name, msg)

            # If this is not a required field, we don't have to continue. Value
            # None is already set
            if self._value is None:
                return

            # We coerce the value to something, like this imaginary class. We
            # don't have to of course.
            self._value = MyHexRepresentationClass(value)


As you can see, it's basically all about those two methods. In ``__init__``,
we just pass the regex to the superclass. And in ``_set_value``, we're wrapping
the ValidationError and coercing the data to some type we want the value to be.