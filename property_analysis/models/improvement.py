from traits.api import (
    HasStrictTraits, Str, Float, Int,
)


class Improvement(HasStrictTraits):

    prop_id = Int()


if __name__ == "__main__":
    imp = Improvement(prop_id=5)
    imp.print_traits()