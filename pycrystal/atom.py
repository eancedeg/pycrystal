from .atom_data import chemical_symbols, atomic_names, NUM_TO_SYMBOL, ELEM_TO_NAME, NAME_TO_ELEM, ELEM_TO_NUM


class Element(object):
    def __init__(self, element):
        if isinstance(element, int):
            try:
                element = NUM_TO_SYMBOL[element]
            except KeyError:
                raise ValueError(f'Atomic number {element} not supported.')
        elif isinstance(element, Element):
            element = element.symbol

    def __str__(self):
        return f'{self.element}'

    def __repr__(self):
        return f'{self.element}'

    @property
    def symbol(self):
        return self.element


class Atom(Element):
    def __init__(self, element, coords):
        self.element = element
        self.cords = coords
        super(Atom, self).__init__(element)
